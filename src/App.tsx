import { useState, useRef } from "react"
import { 
  Terminal as TerminalIcon, 
  ExternalLink, 
  Search, 
  Cpu, 
  MapPin, 
  Code, 
  Layers, 
  CheckCircle2, 
  ShieldAlert, 
  Sparkles,
  ArrowRight,
  ArrowUp,
  Info,
  Volume2,
  VolumeX,
  GraduationCap,
  Award,
  BookOpen,
  Phone,
  UserCheck
} from "lucide-react"

import { GooeyText } from "@/components/ui/gooey-text-morphing"
import { TextScramble } from "@/components/ui/TextScramble"
import { TerminalConsole } from "@/components/ui/TerminalConsole"
import { AgentDrawer } from "@/components/ui/AgentDrawer"
import agentsData from "./agents-data.json"

interface Agent {
  id: string
  name: string
  description: string
  tools: string[]
  model: string
  skills: string[]
  body: string
}

const CATEGORY_MAP: Record<string, string> = {
  "backend-specialist": "development",
  "frontend-specialist": "development",
  "mobile-developer": "development",
  "game-developer": "development",
  "explorer-agent": "development",
  "code-archaeologist": "architecture",
  "database-architect": "architecture",
  "orchestrator": "architecture",
  "project-planner": "architecture",
  "debugger": "testing",
  "test-engineer": "testing",
  "qa-automation-engineer": "testing",
  "devops-engineer": "devops-security",
  "penetration-tester": "devops-security",
  "security-auditor": "devops-security",
  "documentation-writer": "product-seo",
  "product-manager": "product-seo",
  "product-owner": "product-seo",
  "seo-specialist": "product-seo",
}

const CATEGORIES = [
  { id: "all", label: "All Agents" },
  { id: "development", label: "Dev" },
  { id: "architecture", label: "Architecture" },
  { id: "testing", label: "Testing" },
  { id: "devops-security", label: "Security & DevOps" },
  { id: "product-seo", label: "Product & SEO" }
]

const PROJECTS = [
  {
    id: "offerintel",
    title: "OfferIntel",
    desc: "AI-assisted Job Offer Comparison Tool. Helps users evaluate and compare job offers beyond basic salary by factoring in growth potential, role value, and long-term career perspective.",
    url: "https://offerintel-7fcf6.web.app",
    tags: ["React", "TypeScript", "Tailwind CSS", "Firebase Auth", "Product Design"],
    stats: "Live Tool • Interactive Flow"
  },
  {
    id: "freestack",
    title: "FreeStack",
    desc: "An open-source developer resource stack. Built as a comprehensive library for discovering learning materials, coding templates, and stack assets. Includes dynamic routing for the library and about pathways.",
    url: "https://freestack-sigma.vercel.app",
    sublinks: [
      { name: "Main Site", url: "https://freestack-sigma.vercel.app" },
      { name: "Library Catalog", url: "https://freestack-sigma.vercel.app/library" },
      { name: "Mission / About", url: "https://freestack-sigma.vercel.app/about" }
    ],
    tags: ["React", "TypeScript", "Tailwind CSS", "Vite", "JSON Database"],
    stats: "Curated Directory • Subpaths"
  },
  {
    id: "scentscape",
    title: "Scentscape",
    desc: "A premium e-commerce storefront showcasing olfactory products and room-ambient scents. Designed with a luxury dark mode theme, emphasizing visual micro-interactions and smooth shopping cart transitions.",
    url: "https://frontend-itzzsurajzz-9476s-projects.vercel.app/",
    tags: ["React", "Tailwind CSS", "Premium UI", "State Management", "Vercel"],
    stats: "E-Commerce Mockup"
  },
  {
    id: "tank-shooter",
    title: "Tank Shooter",
    desc: "A 2D HTML5 canvas arcade action game. Features dynamic velocity and friction calculations, keyboard action controls, obstacle collisions, explosion particle effects, and screen-shake feedback.",
    url: "https://tank-pied.vercel.app",
    tags: ["HTML5 Canvas", "JavaScript", "Physics Engine", "Game Loop", "Web Audio"],
    stats: "Indie Game • Full Physics"
  },
  {
    id: "chess",
    title: "Chess",
    desc: "An interactive web chess app. Supports standard chess moves validation, visual turn indicators, board state management, and an clean, distraction-free board visualization.",
    url: "https://chess-zeta-henna.vercel.app/",
    tags: ["React", "CSS Grid", "State Validation", "Interactive Board"],
    stats: "Board Game Sim"
  },
  {
    id: "carrom-football-pro",
    title: "Carrom Football Pro",
    desc: "A 2D canvas physics arcade game merging table carrom mechanics with football goals. Built from scratch with circle-to-circle collision impulses, elastic rebounds, and frictional decelerations.",
    url: "https://carrom-football-pro.vercel.app/",
    tags: ["HTML5 Canvas", "Physics Rebounds", "Vector Math", "Game Loop"],
    stats: "Arcade Physics Game"
  }
]

export function App() {
  const [searchTerm, setSearchTerm] = useState("")
  const [activeCategory, setActiveCategory] = useState("all")
  const [isPlaying, setIsPlaying] = useState(false)
  const audioRef = useRef<HTMLAudioElement | null>(null)

  const toggleAudio = () => {
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause()
      } else {
        audioRef.current.play().catch(e => console.error("Audio playback failed:", e))
      }
      setIsPlaying(!isPlaying)
    }
  }

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" })
  }

  // Format ID to clean display name
  const formatAgentName = (id: string) => {
    return id.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ")
  }

  // Filter agents
  const filteredAgents = (agentsData as Agent[]).filter(agent => {
    const category = CATEGORY_MAP[agent.id] || "development"
    const matchesCategory = activeCategory === "all" || category === activeCategory
    const searchString = searchTerm.toLowerCase()
    const matchesSearch = 
      agent.name.toLowerCase().includes(searchString) ||
      agent.id.toLowerCase().includes(searchString) ||
      agent.description.toLowerCase().includes(searchString) ||
      agent.tools.some(t => t.toLowerCase().includes(searchString)) ||
      agent.skills.some(s => s.toLowerCase().includes(searchString))
    
    return matchesCategory && matchesSearch
  })

  const getCategoryIcon = (category: string) => {
    switch (category) {
      case "development": return <Code className="h-4.5 w-4.5 text-primary/80" />
      case "architecture": return <Layers className="h-4.5 w-4.5 text-primary/80" />
      case "testing": return <CheckCircle2 className="h-4.5 w-4.5 text-primary/80" />
      case "devops-security": return <ShieldAlert className="h-4.5 w-4.5 text-primary/80" />
      case "product-seo": return <Sparkles className="h-4.5 w-4.5 text-primary/80" />
      default: return <Cpu className="h-4.5 w-4.5 text-primary/80" />
    }
  }

  return (
    <div className="min-h-screen bg-[#0b0c0e] text-[#f0f2f5] relative overflow-hidden font-body selection:bg-primary selection:text-background pb-12">
      {/* Background Ambient Glows */}
      <div className="ambient-glow glow-1" />
      <div className="ambient-glow glow-2" />

      {/* Navigation Header */}
      <header className="sticky top-0 z-50 bg-[#0b0c0e]/85 backdrop-blur-md border-b border-white/5 py-4 px-6 md:px-12">
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <a href="#" className="flex items-center gap-2 group">
            <span className="w-2.5 h-2.5 rounded-full bg-primary animate-pulse" />
            <TextScramble 
              text="SURAJ DAS" 
              className="font-display font-extrabold text-lg tracking-wider text-foreground hover:text-primary transition-colors"
            />
          </a>
          <nav className="hidden sm:flex items-center gap-8 text-sm font-code">
            <a href="#about" className="text-muted-foreground hover:text-primary transition-colors py-1">/about</a>
            <a href="#education" className="text-muted-foreground hover:text-primary transition-colors py-1">/education</a>
            <a href="#projects" className="text-muted-foreground hover:text-primary transition-colors py-1">/projects</a>
            <a href="#team" className="text-muted-foreground hover:text-primary transition-colors py-1">/agents-team</a>
            <a href="#terminal" className="text-muted-foreground hover:text-primary transition-colors py-1">/developer-shell</a>
          </nav>
          <div className="flex items-center gap-3">
            <audio ref={audioRef} src="/bg-music.mp3" loop />
            <button 
              onClick={toggleAudio}
              className="p-2 rounded-lg bg-white/5 hover:bg-white/10 text-primary transition-all duration-200"
              aria-label="Toggle Background Music"
            >
              {isPlaying ? <Volume2 className="h-4 w-4" /> : <VolumeX className="h-4 w-4 text-muted-foreground" />}
            </button>
            <a 
              href="https://github.com/gitsuraj7" 
              target="_blank" 
              rel="noreferrer"
              className="p-2 rounded-lg bg-white/5 hover:bg-white/10 text-muted-foreground hover:text-foreground transition-all duration-200"
              aria-label="GitHub Profile"
            >
              <svg className="h-4 w-4 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
              </svg>
            </a>
            <a 
              href="https://www.linkedin.com/in/suraj-das-5801793aa" 
              target="_blank" 
              rel="noreferrer"
              className="p-2 rounded-lg bg-white/5 hover:bg-white/10 text-muted-foreground hover:text-foreground transition-all duration-200"
              aria-label="LinkedIn Profile"
            >
              <svg className="h-4 w-4 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
              </svg>
            </a>
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-6 md:px-12 py-12 space-y-24 relative z-10">
        
        {/* Typographic Asymmetric Hero Layout */}
        <section id="about" className="hero-layout pt-4 md:pt-10 scroll-mt-24">
          <div className="space-y-6">
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-md bg-[#151619] border border-white/5 text-xs text-muted-foreground font-code">
              <MapPin className="h-3.5 w-3.5 text-primary" /> West Bengal, India
            </div>
            
            <h1 className="text-4xl md:text-6xl font-display font-extrabold tracking-tight leading-[1.1] text-foreground">
              Exploring Ideas.
              <br />
              Prototyping Software.
            </h1>

            {/* GooeyText morpher wrapper */}
            <div className="h-[75px] md:h-[95px] flex items-center justify-start py-2">
              <GooeyText 
                texts={["Self-Taught Student", "MEXT Applicant", "Curious Learner", "Idea Prototyper"]}
                morphTime={1.2}
                cooldownTime={0.8}
                className="justify-start text-left w-full"
                textClassName="text-3xl md:text-[34pt] font-display font-extrabold text-primary font-bold text-left justify-start absolute left-0"
              />
            </div>

            <p className="text-muted-foreground text-base md:text-lg max-w-lg leading-relaxed font-body">
              I am an 18-year-old student using modern AI-assisted workflows to explore software development and turn practical ideas into working prototypes. By experimenting with real code, I'm actively learning how to build and iterate on digital projects before starting my formal university education.
            </p>

            <div className="flex flex-wrap gap-4 pt-4">
              <a 
                href="#terminal" 
                className="inline-flex items-center gap-2 bg-primary hover:bg-[#b89123] text-background font-semibold text-sm px-5 py-3 rounded-lg transition-all duration-300 shadow-lg shadow-primary/10 select-none cursor-pointer"
              >
                <TerminalIcon className="h-4 w-4" /> Open Developer Shell
              </a>
              <a 
                href="#projects" 
                className="inline-flex items-center gap-2 bg-[#151619] hover:bg-[#1e1f24] text-foreground font-semibold text-sm px-5 py-3 rounded-lg border border-white/5 transition-all duration-300 hover:border-primary/20 select-none cursor-pointer"
              >
                View Projects <ArrowRight className="h-4 w-4 text-primary" />
              </a>
            </div>
          </div>

          {/* Asymmetric Side Panel (About Card) */}
          <div className="bg-[#151619] rounded-xl p-8 border border-white/5 space-y-6 relative overflow-hidden group hover:border-primary/15 transition-all duration-500 shadow-xl">
            <div className="absolute top-0 right-0 w-32 h-32 bg-primary/5 rounded-bl-full filter blur-xl group-hover:bg-primary/10 transition-colors duration-500" />
            <h2 className="font-display font-bold text-lg text-foreground flex items-center gap-2.5">
              <span className="w-1.5 h-5 bg-primary rounded-full" /> Personal Profile
            </h2>
            <div className="space-y-4 font-body text-sm leading-relaxed text-muted-foreground">
              <p>
                <strong className="text-foreground">Self-Driven Learning:</strong> I learn by building and prototyping ideas. Using modern AI tools as an accelerator, I experiment with code, tackle real bugs, and figure out how to put applications together through active iteration.
              </p>
              <p>
                <strong className="text-foreground">MEXT Scholarship Goal:</strong> While I enjoy exploring independently, I want to deeply understand the fundamentals of computer science and system design through structured, formal education in Japan to unlock my true potential.
              </p>
              <p>
                <strong className="text-foreground">Current Explorations:</strong> Experimenting with React interfaces, basic browser canvas logic, web layouts, and integrating developer agents into my problem-solving workflow.
              </p>
            </div>
          </div>
        </section>

        {/* Education & Academic Performance Section */}
        <section id="education" className="space-y-12 scroll-mt-24">
          <div className="space-y-2">
            <span className="font-code text-xs text-primary uppercase tracking-widest">// academic record & learning approach</span>
            <h2 className="text-2xl md:text-3xl font-display font-extrabold tracking-tight text-foreground">
              Education & Academic Performance
            </h2>
            <p className="text-muted-foreground text-sm max-w-xl">
              Schooling history, academic milestones, practical learning workflow, and verified faculty recommendations.
            </p>
          </div>

          {/* Education Timeline / Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-[#151619] rounded-xl p-6 border border-white/5 space-y-4 hover:border-primary/20 transition-all duration-300 relative group shadow-lg">
              <div className="flex items-center justify-between">
                <span className="text-[10px] font-code text-primary bg-primary/10 px-2 py-0.5 rounded border border-primary/20">
                  2024 – 2026
                </span>
                <GraduationCap className="h-5 w-5 text-primary/80" />
              </div>
              <div>
                <h3 className="font-display font-bold text-base text-foreground group-hover:text-primary transition-colors">
                  Senior Secondary (Class 11–12)
                </h3>
                <p className="text-xs text-muted-foreground font-code mt-0.5">
                  Serampore Vivekananda Academy
                </p>
              </div>
              <div className="space-y-2 text-xs text-muted-foreground font-body pt-2 border-t border-white/5">
                <p>
                  <strong className="text-foreground">Science Stream:</strong> Mathematics, Physics, Chemistry, Biology, English, Physical Education.
                </p>
                <p className="text-primary font-semibold font-code bg-primary/5 p-2 rounded border border-primary/10">
                  Academic Score: Achieved 75% Aggregate Score in Higher Secondary Class 12 Boards.
                </p>
              </div>
            </div>

            <div className="bg-[#151619] rounded-xl p-6 border border-white/5 space-y-4 hover:border-primary/20 transition-all duration-300 relative group shadow-lg">
              <div className="flex items-center justify-between">
                <span className="text-[10px] font-code text-primary bg-primary/10 px-2 py-0.5 rounded border border-primary/20">
                  2022 – 2024
                </span>
                <Award className="h-5 w-5 text-primary/80" />
              </div>
              <div>
                <h3 className="font-display font-bold text-base text-foreground group-hover:text-primary transition-colors">
                  Secondary (Class 9–10)
                </h3>
                <p className="text-xs text-muted-foreground font-code mt-0.5">
                  Serampore Vivekananda Academy
                </p>
              </div>
              <div className="space-y-2 text-xs text-muted-foreground font-body pt-2 border-t border-white/5">
                <p className="text-primary font-semibold font-code bg-primary/5 p-2 rounded border border-primary/10">
                  Academic Score: Achieved 89% Overall Aggregate on Class 10 Board Examinations.
                </p>
                <p className="text-foreground font-medium flex items-center gap-1.5 pt-1">
                  <Sparkles className="h-3.5 w-3.5 text-primary shrink-0" />
                  <strong>Mathematics Award:</strong> Recognized as Class Subject Topper in Mathematics.
                </p>
              </div>
            </div>

            <div className="bg-[#151619] rounded-xl p-6 border border-white/5 space-y-4 hover:border-primary/20 transition-all duration-300 relative group shadow-lg">
              <div className="flex items-center justify-between">
                <span className="text-[10px] font-code text-primary bg-primary/10 px-2 py-0.5 rounded border border-primary/20">
                  2014 – 2022
                </span>
                <BookOpen className="h-5 w-5 text-primary/80" />
              </div>
              <div>
                <h3 className="font-display font-bold text-base text-foreground group-hover:text-primary transition-colors">
                  Primary & Middle School (Class 1–8)
                </h3>
                <p className="text-xs text-muted-foreground font-code mt-0.5">
                  Baidyabati Sacred Heart
                </p>
              </div>
              <div className="space-y-2 text-xs text-muted-foreground font-body pt-2 border-t border-white/5">
                <p>
                  <strong className="text-foreground">Medium of Instruction:</strong> 100% English Medium schooling completed continuously from Class 1 through Class 12.
                </p>
              </div>
            </div>
          </div>

          {/* Practical Workflow & Learning Approach */}
          <div className="bg-[#151619] rounded-xl p-8 border border-white/5 space-y-6">
            <h3 className="font-display font-bold text-lg text-foreground flex items-center gap-2.5">
              <span className="w-1.5 h-5 bg-primary rounded-full" />
              Practical Workflow & Learning Approach
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="p-4 rounded-lg bg-[#0b0c0e]/60 border border-white/5 space-y-2">
                <div className="text-primary font-code text-xs font-semibold flex items-center gap-1.5">
                  <Cpu className="h-4 w-4" /> AI-Assisted Building
                </div>
                <p className="text-xs text-muted-foreground leading-relaxed">
                  Use modern AI tools (Cursor, Claude, ChatGPT) to generate starter code, structure web layouts, debug errors, and turn ideas into working applications quickly.
                </p>
              </div>
              <div className="p-4 rounded-lg bg-[#0b0c0e]/60 border border-white/5 space-y-2">
                <div className="text-primary font-code text-xs font-semibold flex items-center gap-1.5">
                  <Code className="h-4 w-4" /> Applied Physics & Math
                </div>
                <p className="text-xs text-muted-foreground leading-relaxed">
                  Apply classroom geometry, trigonometry, and vector principles to build interactive 2D graphics, game loops, bounce angles, and surface friction models.
                </p>
              </div>
              <div className="p-4 rounded-lg bg-[#0b0c0e]/60 border border-white/5 space-y-2">
                <div className="text-primary font-code text-xs font-semibold flex items-center gap-1.5">
                  <ExternalLink className="h-4 w-4" /> Web Hosting & Deployment
                </div>
                <p className="text-xs text-muted-foreground leading-relaxed">
                  Deploy self-built projects live on the internet using hosting services like Vercel and Firebase so they can be viewed online.
                </p>
              </div>
              <div className="p-4 rounded-lg bg-[#0b0c0e]/60 border border-white/5 space-y-2">
                <div className="text-primary font-code text-xs font-semibold flex items-center gap-1.5">
                  <Layers className="h-4 w-4" /> Code Tracking
                </div>
                <p className="text-xs text-muted-foreground leading-relaxed">
                  Organize, update, and publish project source code publicly on GitHub to track version history and build a transparent portfolio.
                </p>
              </div>
            </div>
          </div>

          {/* Academic References & Recommendations */}
          <div className="space-y-4">
            <h3 className="font-display font-bold text-lg text-foreground flex items-center gap-2.5">
              <UserCheck className="h-5 w-5 text-primary" />
              Academic References & Recommendations
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {[
                { name: "Mr. Sarbajit", dept: "Mathematics Faculty", phone: "+91 98318 85664" },
                { name: "Mr. Sadashiv", dept: "Physics Faculty", phone: "+91 80134 36054" },
                { name: "Mrs. Ananna", dept: "Chemistry Faculty", phone: "+91 80170 87317" },
                { name: "Mr. Jisu", dept: "English Faculty", phone: "+91 80171 96649" }
              ].map((ref, idx) => (
                <div key={idx} className="bg-[#151619] rounded-xl p-5 border border-white/5 hover:border-primary/20 transition-all space-y-3">
                  <div>
                    <h4 className="font-display font-bold text-sm text-foreground">{ref.name}</h4>
                    <p className="text-xs text-primary font-code">{ref.dept}</p>
                  </div>
                  <div className="pt-2 border-t border-white/5 flex items-center justify-between text-xs text-muted-foreground font-code">
                    <span className="flex items-center gap-1.5">
                      <Phone className="h-3.5 w-3.5 text-primary/80" /> {ref.phone}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Featured Projects Grid */}
        <section id="projects" className="space-y-8 scroll-mt-24">
          <div className="space-y-2">
            <span className="font-code text-xs text-primary uppercase tracking-widest">// built prototypes</span>
            <h2 className="text-2xl md:text-3xl font-display font-extrabold tracking-tight text-foreground">
              Featured Projects
            </h2>
            <p className="text-muted-foreground text-sm max-w-xl">
              A curated catalog of interactive tools, games, and web layouts. Hover for active details.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {PROJECTS.map(project => (
              <div 
                key={project.id}
                className="bg-[#151619] rounded-xl p-6 border border-white/5 flex flex-col justify-between hover:border-primary/12 transition-all duration-300 group relative hover:translate-y-[-2px] shadow-lg"
              >
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-code text-primary/80 bg-primary/5 px-2 py-0.5 rounded border border-primary/10">
                      {project.stats}
                    </span>
                    {project.url && !project.sublinks && (
                      <a 
                        href={project.url} 
                        target="_blank" 
                        rel="noreferrer"
                        className="text-muted-foreground hover:text-primary transition-colors p-1"
                        title="View Live Site"
                      >
                        <ExternalLink className="h-4 w-4" />
                      </a>
                    )}
                  </div>

                  <h3 className="text-lg font-display font-bold text-foreground group-hover:text-primary transition-colors">
                    {project.title}
                  </h3>

                  <p className="text-muted-foreground text-xs leading-relaxed font-body">
                    {project.desc}
                  </p>
                </div>

                <div className="mt-6 pt-4 border-t border-white/5 space-y-3.5">
                  {/* Handle FreeStack Sublinks */}
                  {project.sublinks ? (
                    <div className="flex flex-wrap gap-2 text-[10px] font-code">
                      {project.sublinks.map((link, lidx) => (
                        <a 
                          key={lidx} 
                          href={link.url}
                          target="_blank"
                          rel="noreferrer"
                          className="flex items-center gap-1 bg-white/5 hover:bg-primary/10 text-muted-foreground hover:text-primary px-2 py-1 rounded transition-colors border border-white/5"
                        >
                          {link.name} <ExternalLink className="h-2.5 w-2.5" />
                        </a>
                      ))}
                    </div>
                  ) : (
                    <div className="flex flex-wrap gap-1.5">
                      {project.tags.map((tag, idx) => (
                        <span 
                          key={idx} 
                          className="text-[10px] font-code text-muted-foreground/90 bg-white/5 px-2 py-0.5 rounded border border-white/5"
                        >
                          {tag}
                        </span>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Autonomous Agent Team Showcase */}
        <section id="team" className="space-y-8 scroll-mt-24">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
            <div className="space-y-2">
              <span className="font-code text-xs text-primary uppercase tracking-widest">// system capabilities</span>
              <h2 className="text-2xl md:text-3xl font-display font-extrabold tracking-tight text-foreground">
                Autonomous Agents Team
              </h2>
              <p className="text-muted-foreground text-sm max-w-xl">
                A roster of 20 simulated developer agents representing automated engineering layers. Filter or click to view their full markdown blueprints.
              </p>
            </div>
            
            {/* Search Input */}
            <div className="relative w-full md:w-80">
              <Search className="absolute left-3.5 top-1/2 transform -translate-y-1/2 h-4 w-4 text-muted-foreground/60" />
              <input 
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Search tools, skills, or names..."
                className="w-full bg-[#151619] border border-white/5 rounded-lg py-2.5 pl-10 pr-4 text-sm text-foreground placeholder-muted-foreground focus:outline-none focus:border-primary/40 focus:ring-1 focus:ring-primary/20 transition-all font-body"
              />
            </div>
          </div>

          {/* Category Filters */}
          <div className="flex flex-wrap gap-2 pb-2">
            {CATEGORIES.map(category => (
              <button
                key={category.id}
                onClick={() => setActiveCategory(category.id)}
                className={`text-xs font-code px-3.5 py-2 rounded-lg border transition-all duration-200 select-none ${
                  activeCategory === category.id 
                    ? "bg-primary border-primary text-background font-semibold" 
                    : "bg-[#151619] border-white/5 text-muted-foreground hover:text-foreground hover:border-white/10"
                }`}
              >
                {category.label}
              </button>
            ))}
          </div>

          {/* Agents Roster Cards Grid */}
          {filteredAgents.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
              {filteredAgents.map(agent => {
                const category = CATEGORY_MAP[agent.id] || "development"
                return (
                  <a
                    key={agent.id}
                    href={`#/agent/${agent.id}`}
                    className="bg-[#151619] rounded-xl p-5 border border-white/5 flex flex-col justify-between hover:border-primary/12 transition-all duration-300 group hover:translate-y-[-2px] relative cursor-pointer"
                  >
                    <div className="space-y-3">
                      <div className="flex items-center justify-between text-xs">
                        <span className="bg-white/5 text-muted-foreground/80 px-2 py-0.5 rounded border border-white/5 flex items-center gap-1.5 uppercase font-code tracking-wider text-[9px]">
                          {getCategoryIcon(category)} {category.replace("-", " ")}
                        </span>
                        <span className="text-[10px] font-code text-muted-foreground/40">
                          {agent.model}
                        </span>
                      </div>
                      
                      <h3 className="font-display font-bold text-foreground group-hover:text-primary transition-colors text-base">
                        {formatAgentName(agent.id)}
                      </h3>
                      
                      <p className="text-muted-foreground text-xs leading-relaxed line-clamp-3 font-body">
                        {agent.description}
                      </p>
                    </div>

                    <div className="mt-4 pt-3 border-t border-white/5 flex items-center justify-between text-[10px] font-code text-muted-foreground/70">
                      <span>Tools: {agent.tools.length}</span>
                      <span className="text-primary/70 group-hover:text-primary flex items-center gap-1 transition-colors">
                        View Prompt <ArrowRight className="h-3 w-3" />
                      </span>
                    </div>
                  </a>
                )
              })}
            </div>
          ) : (
            <div className="bg-[#151619] rounded-xl p-12 border border-white/5 text-center space-y-3 max-w-md mx-auto">
              <Info className="h-8 w-8 text-primary/70 mx-auto" />
              <h3 className="font-display font-bold text-foreground">No agents found</h3>
              <p className="text-muted-foreground text-xs">
                We couldn't find any agents matching "{searchTerm}" in the "{activeCategory}" filter category. Try refining your keywords.
              </p>
            </div>
          )}
        </section>

        {/* Developer Simulated Terminal Console Section */}
        <section id="terminal" className="space-y-8 scroll-mt-24">
          <div className="space-y-2">
            <span className="font-code text-xs text-primary uppercase tracking-widest">// interactive terminal simulator</span>
            <h2 className="text-2xl md:text-3xl font-display font-extrabold tracking-tight text-foreground">
              Developer Shell console
            </h2>
            <p className="text-muted-foreground text-sm max-w-xl">
              Execute commands directly inside the mock shell environment below. Try commands like <code className="text-primary font-code font-semibold px-1 rounded bg-white/5 text-xs">help</code>, <code className="text-primary font-code font-semibold px-1 rounded bg-white/5 text-xs">about</code>, <code className="text-primary font-code font-semibold px-1 rounded bg-white/5 text-xs">projects</code>, or try typing <code className="text-primary font-code font-semibold px-1 rounded bg-white/5 text-xs">orchestrate assemble a web app</code> to simulate autonomous agent execution.
            </p>
          </div>

          <TerminalConsole />

          <div className="flex justify-center pt-8">
            <button 
              onClick={scrollToTop}
              className="inline-flex items-center gap-2 bg-[#151619] hover:bg-primary/20 text-muted-foreground hover:text-primary font-code text-xs px-5 py-2.5 rounded-full border border-white/5 transition-all duration-300 group"
            >
              <ArrowUp className="h-4 w-4 group-hover:-translate-y-1 transition-transform" /> Back to top
            </button>
          </div>
        </section>

      </main>

      {/* Floating Agent Details Drawer */}
      <AgentDrawer 
        agents={agentsData as Agent[]} 
        categoryMap={CATEGORY_MAP}
        formatName={formatAgentName}
      />

      {/* Footer Section */}
      <footer className="max-w-6xl mx-auto px-6 md:px-12 mt-16 pt-8 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-code text-muted-foreground select-none">
        <div>
          © {new Date().getFullYear()} Suraj Das. All rights reserved.
        </div>
        <div className="flex items-center gap-6">
          <a href="https://github.com/gitsuraj7" target="_blank" rel="noreferrer" className="hover:text-primary transition-colors">GitHub</a>
          <a href="https://www.linkedin.com/in/suraj-das-5801793aa" target="_blank" rel="noreferrer" className="hover:text-primary transition-colors">LinkedIn</a>
          <a href="mailto:itzzs.business@gmail.com" className="hover:text-primary transition-colors">Contact / Email</a>
        </div>
      </footer>
    </div>
  )
}

export default App
