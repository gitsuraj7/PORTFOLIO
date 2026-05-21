import * as React from "react"
import { cn } from "@/lib/utils"

interface TextScrambleProps {
  text: string
  className?: string
  as?: React.ElementType
}

export function TextScramble({ text, className, as: Component = "span" }: TextScrambleProps) {
  const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#%&*"
  const [displayText, setDisplayText] = React.useState(text)
  const [activeIndices, setActiveIndices] = React.useState<number[]>([])
  const isHovering = React.useRef(false)
  const isScrambling = React.useRef(false)
  const timerRef = React.useRef<number | null>(null)
  const frameRef = React.useRef(0)

  const startScramble = React.useCallback(() => {
    if (isScrambling.current) return
    isScrambling.current = true
    frameRef.current = 0
    const duration = Math.max(30, text.length * 3)

    if (timerRef.current) clearInterval(timerRef.current)

    timerRef.current = window.setInterval(() => {
      frameRef.current++
      const progress = frameRef.current / duration
      const revealedLength = Math.floor(progress * text.length)

      let currentText = ""
      const currentActiveIndices: number[] = []

      for (let i = 0; i < text.length; i++) {
        const char = text[i]
        if (char === " " || char === "." || char === "/" || char === "\\") {
          currentText += char
          continue
        }

        if (i < revealedLength) {
          currentText += char
        } else {
          currentText += chars[Math.floor(Math.random() * chars.length)]
          currentActiveIndices.push(i)
        }
      }

      setDisplayText(currentText)
      setActiveIndices(currentActiveIndices)

      if (frameRef.current >= duration) {
        if (timerRef.current) clearInterval(timerRef.current)
        isScrambling.current = false
        setDisplayText(text)
        setActiveIndices([])

        if (isHovering.current) {
          setTimeout(() => {
            if (isHovering.current) startScramble()
          }, 1200)
        }
      }
    }, 30)
  }, [text])

  const handleMouseEnter = () => {
    isHovering.current = true
    startScramble()
  }

  const handleMouseLeave = () => {
    isHovering.current = false
  }

  React.useEffect(() => {
    setDisplayText(text)
    return () => {
      if (timerRef.current) clearInterval(timerRef.current)
    }
  }, [text])

  return (
    <Component
      className={cn("text-scramble", className)}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      {displayText.split("").map((char, i) => (
        <span
          key={i}
          className={cn(
            "scramble-char",
            activeIndices.includes(i) && "active"
          )}
        >
          {char === " " ? "\u00A0" : char}
        </span>
      ))}
    </Component>
  )
}
