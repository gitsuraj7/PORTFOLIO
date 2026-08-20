import React, { useState, useEffect, useRef } from "react"
import { Terminal, CornerDownLeft } from "lucide-react"
import agentsData from "../../agents-data.json"

interface LogEntry {
  type: "input" | "output" | "error" | "system" | "success"
  text: string
}

const PROJECTS_LIST = [
  { name: "OfferIntel", desc: "AI-assisted job offer comparison tool", url: "https://offerintel-7fcf6.web.app" },
  { name: "FreeStack", desc: "Open developer directory & resource stack", url: "https://freestack-sigma.vercel.app" },
  { name: "Scentscape", desc: "E-commerce platform for ambient scents", url: "https://frontend-itzzsurajzz-9476s-projects.vercel.app/" },
  { name: "Tank Shooter", desc: "2D HTML5 canvas action shooter", url: "https://tank-pied.vercel.app" },
  { name: "Chess", desc: "Interactive multiplayer chess application", url: "https://chess-zeta-henna.vercel.app/" },
  { name: "Carrom Football Pro", desc: "2D physics carrom football hybrid game", url: "https://carrom-football-pro.vercel.app/" }
]

export function TerminalConsole() {
  const [history, setHistory] = useState<LogEntry[]>([
    { type: "system", text: "Initializing Developer Terminal v1.4.2..." },
    { type: "system", text: "Systems online. Type 'help' to see available commands." }
  ])
  const [input, setInput] = useState("")
  const [cmdHistory, setCmdHistory] = useState<string[]>([])
  const [historyIndex, setHistoryIndex] = useState(-1)
  const [isSimulating, setIsSimulating] = useState(false)
  
  const terminalEndRef = useRef<HTMLDivElement>(null)
  const inputRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    // Auto scroll to bottom when history changes
    terminalEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [history])

  const focusInput = () => {
    inputRef.current?.focus()
  }

  // Focus terminal input on mount
  useEffect(() => {
    focusInput()
  }, [])

  const handleCommand = async (fullCommand: string) => {
    const trimmed = fullCommand.trim()
    if (!trimmed) return

    // Add command to terminal log history
    setHistory(prev => [...prev, { type: "input", text: trimmed }])
    
    // Add command to arrow history
    const newCmdHistory = [trimmed, ...cmdHistory.filter(h => h !== trimmed)].slice(0, 50)
    setCmdHistory(newCmdHistory)
    setHistoryIndex(-1)
    setInput("")

    const parts = trimmed.split(" ")
    const cmd = parts[0].toLowerCase()
    const args = parts.slice(1)

    if (isSimulating) {
      setHistory(prev => [...prev, { type: "error", text: "Please wait. Agent pipeline execution in progress..." }])
      return
    }

    switch (cmd) {
      case "help":
        setHistory(prev => [
          ...prev,
          { type: "output", text: "Available commands:" },
          { type: "output", text: "  help        - Display this menu" },
          { type: "output", text: "  about       - Details about Suraj Das (background & application)" },
          { type: "output", text: "  education   - Academic performance & faculty recommendations" },
          { type: "output", text: "  projects    - List independent projects with links" },
          { type: "output", text: "  agents      - List autonomous developer agents and their roles" },
          { type: "output", text: "  open <name> - Open agent drawer by name (e.g. 'open seo-specialist')" },
          { type: "output", text: "  orchestrate <prompt> - Simulate the agents collaborating on a task" },
          { type: "output", text: "  clear       - Clear screen history" }
        ])
        break

      case "education":
      case "academics":
        setHistory(prev => [
          ...prev,
          { type: "output", text: "EDUCATION & ACADEMIC PERFORMANCE:" },
          { type: "output", text: "  • Class 11–12 (Senior Secondary): 75% Aggregate (Science Stream) | Serampore Vivekananda Academy" },
          { type: "output", text: "  • Class 9–10  (Secondary): 89% Overall Aggregate | Subject Topper in Mathematics" },
          { type: "output", text: "  • Class 1–8   (Primary & Middle): 100% English Medium | Baidyabati Sacred Heart" },
          { type: "output", text: "FACULTY RECOMMENDATIONS & REFERENCES:" },
          { type: "output", text: "  • Mr. Sarbajit (Mathematics) - +91 98318 85664" },
          { type: "output", text: "  • Mr. Sadashiv (Physics)     - +91 80134 36054" },
          { type: "output", text: "  • Mrs. Ananna  (Chemistry)   - +91 80170 87317" },
          { type: "output", text: "  • Mr. Jisu     (English)     - +91 80171 96649" }
        ])
        break

      case "about":
        setHistory(prev => [
          ...prev,
          { type: "output", text: "NAME: Suraj Das" },
          { type: "output", text: "ROLE: Class 12 Student | Self-Taught Software Builder" },
          { type: "output", text: "FOCUS: MEXT Information Processing Candidate, Web Development, Game Dev" },
          { type: "output", text: "BIO: Most of my skills come from hands-on experimentation, building tools that solve real problems, and studying code. I prefer working prototypes over dry theory." }
        ])
        break

      case "projects":
        setHistory(prev => [
          ...prev,
          { type: "output", text: "Featured Projects (type 'open [project]' or click to view):" },
          ...PROJECTS_LIST.flatMap((proj, idx) => [
            { type: "output" as const, text: `  [${idx + 1}] ${proj.name} - ${proj.desc}` },
            { type: "success" as const, text: `      Link: ${proj.url}` }
          ])
        ])
        break

      case "agents":
        setHistory(prev => [
          ...prev,
          { type: "output", text: "Local Agent Repository (20 autonomous blueprints compiled):" },
          ...agentsData.map(agent => ({
            type: "output" as const,
            text: `  • ${agent.id.padEnd(25)} | Model: ${agent.model.padEnd(10)} | ${agent.description.slice(0, 60)}...`
          })),
          { type: "system", text: "Tip: Use 'open <agent-id>' to read their complete system prompt in the drawer." }
        ])
        break

      case "open":
        if (args.length === 0) {
          setHistory(prev => [...prev, { type: "error", text: "Error: Please specify a project index/name or an agent ID. Usage: 'open seo-specialist' or 'open offerintel'" }])
          break
        }
        
        const target = args.join("-").toLowerCase()
        
        // Check if index matches a project
        const projectIndex = parseInt(target) - 1
        if (!isNaN(projectIndex) && PROJECTS_LIST[projectIndex]) {
          window.open(PROJECTS_LIST[projectIndex].url, "_blank")
          setHistory(prev => [...prev, { type: "success", text: `Opening ${PROJECTS_LIST[projectIndex].name} in a new tab...` }])
          break
        }

        // Check if project name matches
        const matchedProj = PROJECTS_LIST.find(p => p.name.toLowerCase() === target)
        if (matchedProj) {
          window.open(matchedProj.url, "_blank")
          setHistory(prev => [...prev, { type: "success", text: `Opening ${matchedProj.name} in a new tab...` }])
          break
        }

        // Check if agent name matches
        const matchedAgent = agentsData.find(a => a.id.toLowerCase() === target || a.name.toLowerCase() === target)
        if (matchedAgent) {
          window.location.hash = `#/agent/${matchedAgent.id}`
          setHistory(prev => [...prev, { type: "success", text: `Opening drawer for agent '${matchedAgent.id}'...` }])
        } else {
          setHistory(prev => [...prev, { type: "error", text: `Error: Target '${args.join(" ")}' not found in projects or agent roster.` }])
        }
        break

      case "clear":
        setHistory([])
        break

      case "orchestrate":
        if (args.length === 0) {
          setHistory(prev => [...prev, { type: "error", text: "Error: Please provide a prompt. Usage: 'orchestrate compile a React calculator'" }])
          break
        }
        const promptText = args.join(" ")
        runOrchestration(promptText)
        break

      default:
        setHistory(prev => [
          ...prev,
          { type: "error", text: `Command not found: '${cmd}'. Type 'help' for valid inputs.` }
        ])
        break
    }
  }

  const runOrchestration = (prompt: string) => {
    setIsSimulating(true)
    
    // Choose 4 suitable agents for a realistic pipeline simulation
    const pipeline = [
      { agent: "Orchestrator", msg: `Received task: "${prompt}". Analyzing codebase structure...`, delay: 1000 },
      { agent: "Project Planner", msg: "Drafting execution plan. Creating components mapping...", delay: 2200 },
      { agent: "Frontend Specialist", msg: "Writing Tailwind UI layers. Integrating custom Framer Motion dynamics...", delay: 3500 },
      { agent: "Test Engineer", msg: "Creating integration test suites. Validating accessibility rules...", delay: 4800 },
      { agent: "SEO Specialist", msg: "Optimizing index viewport configurations and schema attributes...", delay: 6000 },
      { agent: "Orchestrator", msg: `Task "${prompt}" completed successfully. Build bundle: 14.2kB. All checks passed.`, delay: 7200 }
    ]

    setHistory(prev => [
      ...prev,
      { type: "system", text: `Spinning up multi-agent pipeline for task: "${prompt}"...` }
    ])

    pipeline.forEach(step => {
      setTimeout(() => {
        setHistory(prev => [
          ...prev,
          { 
            type: step.agent === "Orchestrator" && step.msg.includes("completed") ? "success" : "output",
            text: `[${step.agent}] ${step.msg}`
          }
        ])
        if (step.delay === 7200) {
          setIsSimulating(false)
        }
      }, step.delay)
    })
  }

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleCommand(input)
    } else if (e.key === "ArrowUp") {
      e.preventDefault()
      if (cmdHistory.length === 0) return
      
      const nextIndex = historyIndex + 1
      if (nextIndex < cmdHistory.length) {
        setHistoryIndex(nextIndex)
        setInput(cmdHistory[nextIndex])
      }
    } else if (e.key === "ArrowDown") {
      e.preventDefault()
      const nextIndex = historyIndex - 1
      if (nextIndex >= 0) {
        setHistoryIndex(nextIndex)
        setInput(cmdHistory[nextIndex])
      } else {
        setHistoryIndex(-1)
        setInput("")
      }
    }
  }

  return (
    <div 
      className="w-full bg-[#0f1012] border border-white/5 rounded-xl overflow-hidden font-code text-sm shadow-2xl flex flex-col h-[400px] hover:border-primary/20 transition-colors duration-300"
      onClick={focusInput}
    >
      {/* Title Bar */}
      <div className="flex items-center justify-between px-4 py-3 bg-[#151619] border-b border-white/5 select-none">
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-full bg-red-500/80" />
          <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
          <div className="w-3 h-3 rounded-full bg-green-500/80" />
          <span className="text-xs text-muted-foreground ml-2 flex items-center gap-1.5 font-semibold">
            <Terminal className="h-3.5 w-3.5 text-primary" /> developer-console.sh
          </span>
        </div>
        <div className="text-[10px] text-muted-foreground/60">
          guest@suraj-das
        </div>
      </div>

      {/* Console History Panel */}
      <div className="flex-1 p-4 overflow-y-auto space-y-2 select-text">
        {history.map((log, idx) => {
          let colorClass = "text-muted-foreground"
          let prefix = ""

          if (log.type === "input") {
            colorClass = "text-foreground font-semibold"
            prefix = "guest@suraj-das:~$ "
          } else if (log.type === "error") {
            colorClass = "text-rose-400 font-semibold"
          } else if (log.type === "success") {
            colorClass = "text-emerald-400 font-semibold"
          } else if (log.type === "system") {
            colorClass = "text-primary/70 font-semibold"
          }

          return (
            <div key={idx} className={`${colorClass} leading-relaxed break-all whitespace-pre-wrap`}>
              {prefix}{log.text}
            </div>
          )
        })}
        {isSimulating && (
          <div className="text-primary animate-pulse flex items-center gap-1">
            <span>⚡ Running pipeline orchestration</span>
            <span className="dot-animation">...</span>
          </div>
        )}
        <div ref={terminalEndRef} />
      </div>

      {/* Input Form Panel */}
      <div className="flex items-center bg-[#151619]/50 border-t border-white/5 px-4 py-2">
        <span className="text-primary font-semibold mr-2 select-none">guest@suraj-das:~$</span>
        <input
          ref={inputRef}
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          className="flex-1 bg-transparent border-0 outline-none text-foreground caret-primary py-1 w-full"
          autoComplete="off"
          autoCorrect="off"
          autoCapitalize="off"
          spellCheck="false"
          disabled={isSimulating}
          placeholder={isSimulating ? "Please wait..." : "Type command..."}
        />
        <CornerDownLeft className="h-3.5 w-3.5 text-muted-foreground/40 ml-2" />
      </div>
    </div>
  )
}
