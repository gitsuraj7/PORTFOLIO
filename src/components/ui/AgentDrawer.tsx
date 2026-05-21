import * as React from "react"
import { X, Check } from "lucide-react"

interface Agent {
  name: string
  description: string
  tools: string[]
  model: string
  skills: string[]
  body: string
}

interface AgentDrawerProps {
  agents: Agent[]
  categoryMap: Record<string, string>
  formatName: (name: string) => string
}

export function AgentDrawer({ agents, categoryMap, formatName }: AgentDrawerProps) {
  const [open, setOpen] = React.useState(false)
  const [activeAgent, setActiveAgent] = React.useState<Agent | null>(null)
  const [copiedAnchor, setCopiedAnchor] = React.useState<string | null>(null)
  const drawerContentRef = React.useRef<HTMLDivElement>(null)

  // Parse markdown to HTML (Ported from app.js)
  const compileMarkdown = React.useCallback((markdown: string, agentName: string) => {
    let html = markdown
    
    // 1. Escape scripts
    html = html.replace(/<script[^>]*>([\s\S]*?)<\/script>/gi, "")

    // 2. Pre block codes (```language code block```)
    const codeBlocks: string[] = []
    html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (_match, _lang, code) => {
      const id = `__CODE_BLOCK_${codeBlocks.length}__`
      codeBlocks.push(`<pre class="bg-black/50 p-5 rounded-lg overflow-x-auto mb-6 border border-white/5 font-code text-sm"><code class="text-foreground">${escapeHTML(code.trim())}</code></pre>`)
      return id
    })

    // 3. Inline codes (`code`)
    html = html.replace(/`([^`]+)`/g, '<code class="bg-white/5 font-code text-xs px-1.5 py-0.5 rounded text-primary">$1</code>')

    // 4. Tables parsing
    const lines = html.split("\n")
    let inTable = false
    let tableHTML = ""
    
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim()
      if (line.startsWith("|")) {
        if (!inTable) {
          inTable = true;
          tableHTML = '<div class="overflow-x-auto mb-6"><table class="w-full border-collapse text-sm"><thead>'
        }
        
        if (line.includes("---")) {
          tableHTML = tableHTML.replace("<thead>", "").replace("</thead>", "") + "<tbody>"
          continue
        }
        
        const cols = line.split("|").slice(1, -1).map(c => c.trim())
        const tag = tableHTML.includes("<tbody>") ? "td" : "th"
        
        tableHTML += "<tr>"
        cols.forEach(col => {
          const classes = tag === "th" 
            ? 'p-3 text-left border-b border-white/5 font-code font-semibold text-primary' 
            : 'p-3 text-left border-b border-white/5'
          tableHTML += `<${tag} class="${classes}">${col}</${tag}>`
        })
        tableHTML += "</tr>"
        
        if (tag === "th") {
          tableHTML += "</thead>"
        }
        lines[i] = ""
      } else {
        if (inTable) {
          inTable = false
          tableHTML += "</tbody></table></div>"
          let prevIdx = i - 1
          while (prevIdx >= 0 && lines[prevIdx] === "") prevIdx--
          lines[prevIdx] = tableHTML + "\n"
          tableHTML = ""
        }
      }
    }
    if (inTable) {
      tableHTML += "</tbody></table></div>"
      lines[lines.length - 1] = tableHTML
    }
    html = lines.join("\n")

    // 5. Headings with anchors
    html = html.replace(/^## (.*?)$/gm, (_match, content) => {
      const id = cleanHeadingId(content)
      const anchor = `#/agent/${agentName}#${id}`
      return `<h2 id="${id}" class="text-xl font-display font-bold text-foreground mt-8 mb-4 border-b border-white/5 pb-2 flex justify-between items-center group">${content}<a href="${anchor}" data-anchor="${id}" class="heading-anchor font-code text-sm text-muted-foreground ml-3 no-underline opacity-0 group-hover:opacity-100 transition-opacity hover:text-primary" title="Copy Direct Link">#</a></h2>`
    })
    html = html.replace(/^### (.*?)$/gm, (_match, content) => {
      const id = cleanHeadingId(content)
      const anchor = `#/agent/${agentName}#${id}`
      return `<h3 id="${id}" class="text-lg font-display font-semibold text-foreground mt-6 mb-3 flex items-center group">${content}<a href="${anchor}" data-anchor="${id}" class="heading-anchor font-code text-sm text-muted-foreground ml-3 no-underline opacity-0 group-hover:opacity-100 transition-opacity hover:text-primary" title="Copy Direct Link">#</a></h3>`
    })
    html = html.replace(/^# (.*?)$/gm, '<h1 class="text-2xl font-display font-extrabold text-foreground mt-10 mb-5">$1</h1>')

    // 6. Blockquotes
    html = html.replace(/^> (.*?)$/gm, '<blockquote class="border-l-2 border-primary pl-4 mb-6 italic text-foreground">$1</blockquote>')

    // 7. Lists
    html = html.replace(/^\s*-\s+(.*?)$/gm, '<li class="mb-2">$1</li>')
    html = html.replace(/(<li class="mb-2">.*<\/li>)/gs, '<ul class="list-disc pl-5 mb-6">$1<\/ul>')
    html = html.replace(/<\/ul>\s*<ul class="list-disc pl-5 mb-6">/g, "")

    // 8. Bold text (**text**)
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong class="font-semibold text-foreground">$1</strong>')

    // 9. Paragraph breaks
    html = html.replace(/\n\n/g, "<br>")

    // Restore Code Blocks
    codeBlocks.forEach((block, idx) => {
      html = html.replace(`__CODE_BLOCK_${idx}__`, block)
    })

    return html
  }, [])

  const escapeHTML = (str: string) => {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;")
  }

  const cleanHeadingId = (text: string) => {
    return text.toLowerCase()
      .replace(/🛑|⛔|🏺|📅|🕸|⚠️|🛠|🤝|/g, "")
      .replace(/[^\w\s-]/g, "")
      .trim()
      .replace(/\s+/g, "-")
  }

  // Handle URL hash changes for routing
  React.useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash
      if (hash.startsWith("#/agent/")) {
        const parts = hash.substring(8).split("#")
        const agentName = parts[0]
        const anchorId = parts[1]

        const foundAgent = agents.find(a => a.name === agentName)
        if (foundAgent) {
          setActiveAgent(foundAgent)
          setOpen(true)
          document.body.style.overflow = "hidden" // lock body scroll

          // Handle scrolling to anchor inside drawer
          if (anchorId) {
            setTimeout(() => {
              const target = document.getElementById(anchorId)
              if (target) {
                target.scrollIntoView({ behavior: "smooth" })
                target.classList.add("text-primary")
                setTimeout(() => {
                  target.classList.remove("text-primary")
                }, 2000)
              }
            }, 400)
          }
        }
      } else {
        setOpen(false)
        document.body.style.overflow = "" // restore body scroll
      }
    }

    // Run on mount
    handleHashChange()

    window.addEventListener("hashchange", handleHashChange)
    return () => {
      window.removeEventListener("hashchange", handleHashChange)
      document.body.style.overflow = ""
    }
  }, [agents])

  const handleClose = () => {
    window.location.hash = ""
  }

  // Handle click events on heading anchors inside the compiled HTML
  const handleDrawerClick = (e: React.MouseEvent<HTMLDivElement>) => {
    const target = e.target as HTMLElement
    const anchor = target.closest(".heading-anchor")
    if (anchor) {
      e.preventDefault()
      const href = anchor.getAttribute("href")
      const anchorId = anchor.getAttribute("data-anchor")
      
      if (href && anchorId) {
        const fullLink = window.location.origin + window.location.pathname + href
        navigator.clipboard.writeText(fullLink).then(() => {
          setCopiedAnchor(anchorId)
          setTimeout(() => setCopiedAnchor(null), 1500)
        })
      }
    }
  }

  if (!open || !activeAgent) return null

  const category = categoryMap[activeAgent.name] || "development"

  return (
    <div 
      className="fixed inset-0 bg-black/60 backdrop-blur-sm z-[200] transition-opacity duration-300"
      onClick={handleClose}
    >
      <div 
        ref={drawerContentRef}
        className="fixed top-0 right-0 h-full w-full max-w-[680px] bg-[#0f1012] z-[210] shadow-2xl flex flex-col transition-transform duration-500 ease-out border-l border-white/5"
        style={{ transform: open ? "translateX(0)" : "translateX(100%)" }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Close Button */}
        <button 
          onClick={handleClose}
          className="absolute top-6 right-6 p-2 rounded-lg bg-white/5 hover:bg-white/10 text-muted-foreground hover:text-foreground transition-all duration-200"
          aria-label="Close panel"
        >
          <X className="h-5 w-5" />
        </button>

        {/* Content Body */}
        <div 
          className="flex-1 overflow-y-auto px-6 md:px-12 py-16 scroll-smooth"
          onClick={handleDrawerClick}
        >
          {/* Header Metadata */}
          <div className="border-b border-white/5 pb-6 mb-8">
            <span className="inline-block font-code text-xs text-primary bg-primary/5 px-2.5 py-1 rounded border border-primary/10 mb-4 uppercase tracking-wider">
              {category}
            </span>
            <h1 className="text-3xl font-display font-extrabold tracking-tight text-foreground mb-3">
              {formatName(activeAgent.name)}
            </h1>
            <div className="flex flex-wrap gap-2 text-xs">
              <span className="bg-white/5 text-muted-foreground px-2 py-0.5 rounded border border-white/5">
                Model: {activeAgent.model}
              </span>
              {activeAgent.tools.map((tool, idx) => (
                <span key={idx} className="bg-white/5 text-muted-foreground px-2 py-0.5 rounded border border-white/5">
                  {tool}
                </span>
              ))}
            </div>
          </div>

          {/* Compiled Markdown Body */}
          <div 
            className="drawer-body text-muted-foreground text-sm leading-relaxed space-y-4 font-body"
            dangerouslySetInnerHTML={{ __html: compileMarkdown(activeAgent.body, activeAgent.name) }}
          />

          {/* Copy Toast Alert inside headers if copied */}
          {copiedAnchor && (
            <div className="fixed bottom-6 right-6 bg-emerald-500 text-black font-code text-xs px-3 py-2 rounded-md shadow-lg flex items-center gap-2 z-[250] animate-bounce">
              <Check className="h-3.5 w-3.5" />
              <span>Link copied to clipboard!</span>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
