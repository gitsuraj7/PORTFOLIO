import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY

def draw_pure_glass_background(canvas, doc):
    """
    Renders an ethereal, ultra-smooth ice-blue & porcelain white glass background:
    - Base canvas: Pure clean porcelain white (#ffffff)
    - Subtle frosted ambient soft blue glow (#f0f7ff / #e0f0fe / #dbeafe)
      radiating smoothly across the background corners.
    - Minimalist footer page indicators.
    """
    canvas.saveState()
    width, height = letter
    
    # 1. Base clean white canvas
    canvas.setFillColor(colors.HexColor("#ffffff"))
    canvas.rect(0, 0, width, height, fill=1, stroke=0)
    
    # 2. Ultra-smooth monochromatic sky/ice blue glow
    canvas.setFillColor(colors.HexColor("#f4f9ff"))
    canvas.circle(width - 20, height - 20, 260, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#e6f2fe"))
    canvas.circle(width - 10, height - 10, 160, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#d8ecfe"))
    canvas.circle(width, height, 90, fill=1, stroke=0)

    canvas.setFillColor(colors.HexColor("#f6faff"))
    canvas.circle(20, 40, 240, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#eaf4fe"))
    canvas.circle(0, 0, 140, fill=1, stroke=0)
    
    # 3. Clean editorial footer
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#94a3b8"))
    page_num = canvas.getPageNumber()
    canvas.drawString(28, 20, "SURAJ DAS  •  COMPREHENSIVE ENGINEERING DOSSIER")
    canvas.drawRightString(width - 28, 20, f"PAGE {page_num} OF 4")
    
    canvas.restoreState()

def generate_super_dossier(output_paths=None):
    if output_paths is None:
        output_paths = [
            "e:/keep EXP/portfolio/Suraj_Das_Comprehensive_Engineering_Dossier.pdf",
            os.path.join(os.environ['USERPROFILE'], 'Downloads', 'Suraj_Das_Comprehensive_Engineering_Dossier.pdf'),
            os.path.join(os.environ['USERPROFILE'], 'Downloads', 'dossier.pdf')
        ]

    # Monochromatic White & Bluish Glass Palette
    PRIMARY = colors.HexColor("#0f172a")          # Slate 900
    SECONDARY = colors.HexColor("#334155")        # Slate 700
    MUTED = colors.HexColor("#64748b")            # Slate 500
    
    ACCENT_BLUE = colors.HexColor("#0284c7")      # Pure Sky Blue
    DARK_BLUE = colors.HexColor("#0369a1")        # Deep Sky
    
    GLASS_CARD_BG = colors.HexColor("#fcfdff")    # Pure Frosted White Surface
    GLASS_BORDER = colors.HexColor("#dbeafe")     # Soft Sky/Ice border sheen
    HEADER_BG = colors.HexColor("#f0f7ff")        # Subtle Ice-blue header pill
    
    styles = getSampleStyleSheet()
    FULL_W = 556

    # Typography Hierarchy
    hero_name_style = ParagraphStyle(
        'HeroName', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=24, leading=26, textColor=PRIMARY
    )
    role_badge_style = ParagraphStyle(
        'HeroBadge', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=ACCENT_BLUE
    )
    sub_summary_style = ParagraphStyle(
        'HeroSub', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=12, textColor=MUTED
    )
    contact_style = ParagraphStyle(
        'ContactPill', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=12.5, textColor=SECONDARY, alignment=TA_RIGHT
    )
    section_title_style = ParagraphStyle(
        'SectionTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=DARK_BLUE
    )
    card_title_style = ParagraphStyle(
        'CardTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=PRIMARY
    )
    card_tag_style = ParagraphStyle(
        'CardTag', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8, leading=10.5, textColor=ACCENT_BLUE
    )
    card_date_style = ParagraphStyle(
        'CardDate', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8, leading=10.5, textColor=MUTED, alignment=TA_RIGHT
    )
    body_style = ParagraphStyle(
        'GlassBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=12.5, textColor=SECONDARY
    )
    bullet_style = ParagraphStyle(
        'GlassBullet', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.2, leading=12, textColor=SECONDARY, leftIndent=10, firstLineIndent=-10
    )
    pill_label_style = ParagraphStyle(
        'PillLabel', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=PRIMARY
    )

    story = []

    def make_section_banner(title):
        p_title = Paragraph(f"<b>{title.upper()}</b>", section_title_style)
        t = Table([[p_title]], colWidths=[FULL_W])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), HEADER_BG),
            ('BOX', (0,0), (-1,-1), 0.8, GLASS_BORDER),
            ('LINELEFT', (0,0), (-1,-1), 3.5, ACCENT_BLUE),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('TOPPADDING', (0,0), (-1,-1), 3.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ]))
        return t

    # =============================================================
    # PAGE 1: HERO, ACADEMICS & TECHNICAL COMPETENCIES
    # =============================================================
    
    # 1. Hero Header
    hero_left = [
        Paragraph("<b>SURAJ DAS</b>", hero_name_style),
        Spacer(1, 3),
        Paragraph("FULL-STACK SYSTEMS ENGINEER & AI PROTOTYPER", role_badge_style),
        Spacer(1, 2),
        Paragraph("100% English Medium &bull; Class 10 Math Topper (89%) &bull; Class 12 Science (75%)", sub_summary_style)
    ]
    hero_right = [
        Paragraph("📍 West Bengal, India &nbsp;|&nbsp; 🌐 <i>Open to Relocation (Japan / Global)</i>", contact_style),
        Spacer(1, 2),
        Paragraph('📧 <a href="mailto:itzzsuraj7@gmail.com" color="#0284c7"><b>itzzsuraj7@gmail.com</b></a> &nbsp;|&nbsp; 🔗 <a href="https://linkedin.com/in/suraj-das-5801793aa" color="#0284c7"><b>LinkedIn</b></a>', contact_style),
        Spacer(1, 2),
        Paragraph('💻 <a href="https://github.com/gitsuraj7" color="#0284c7"><b>GitHub</b></a> &nbsp;|&nbsp; 🚀 <b>Portfolio:</b> <a href="https://portfolio-phi-nine-m7qu98woxl.vercel.app" color="#0369a1"><b>portfolio-phi-nine-m7qu98woxl.vercel.app</b></a>', contact_style)
    ]
    hero_table = Table([[hero_left, hero_right]], colWidths=[296, 260])
    hero_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 1.2, GLASS_BORDER),
        ('LINELEFT', (0,0), (-1,-1), 4, ACCENT_BLUE),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 9),
    ]))
    story.append(hero_table)
    story.append(Spacer(1, 8))

    # 2. Executive Systems Biography
    story.append(make_section_banner("Executive Systems Biography & Technical Philosophy"))
    story.append(Spacer(1, 5))
    bio_text = (
        "<b>Autonomous Systems Builder & Applied Computer Scientist</b> specializing in mathematically rigorous full-stack "
        "applications, real-time deterministic physics simulation engines, multi-agent AI blueprint orchestration, and high-frequency "
        "browser rendering. Characterized by an insatiable curiosity for how complex machines function at the core level—from tearing down "
        "salvaged PC hardware to developing zero-dependency vector physics engines in pure JavaScript. Combines top-tier analytical ability "
        "(Class 10 Board Examination Subject Topper in Mathematics) with AI-augmented prototyping velocity. Actively targeting specialized "
        "higher education and research labs in Information Processing and Computer Science in Japan (MEXT Scholarship candidate)."
    )
    bio_card = Table([[Paragraph(bio_text, body_style)]], colWidths=[FULL_W])
    bio_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(bio_card)
    story.append(Spacer(1, 8))

    # 3. Academic Background
    story.append(make_section_banner("Academic Background & Mathematical Excellence (100% English Medium)"))
    story.append(Spacer(1, 5))

    hs_header = [
        Paragraph("<b>Serampore Vivekananda Academy</b> &nbsp;<font color='#64748b'>| Higher Secondary & Secondary (Class 9–12)</font>", card_title_style),
        Paragraph("2022 – 2026", card_date_style)
    ]
    hs_t = Table([hs_header], colWidths=[430, 110])
    hs_t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    hs_bullets = [
        hs_t,
        Spacer(1, 3),
        Paragraph("• &nbsp;<b>Class 12 Higher Secondary (Science Stream):</b> <b>75% Aggregate</b> &bull; Complete English Medium instruction across Physics, Chemistry, Advanced Mathematics, Biology, English, and Physical Education.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Class 10 Secondary Board Examination:</b> <b>89% Aggregate &bull; <font color='#0284c7'>Class Subject Topper in Mathematics</font></b> (Demonstrated exceptional quantitative logic, Euclidean geometry, and algebra).", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Computational Mathematics Self-Study:</b> Discrete mathematics, graph algorithms, linear algebra for vector graphics, and agentic state-machine workflows.", bullet_style)
    ]
    hs_card = Table([[hs_bullets]], colWidths=[FULL_W])
    hs_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LINELEFT', (0,0), (-1,-1), 3, ACCENT_BLUE),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(hs_card)
    story.append(Spacer(1, 5))

    sec_header = [
        Paragraph("<b>Sacred Heart School</b> &nbsp;<font color='#64748b'>| Primary & Lower Secondary (Class 1–8, English Medium, Baidyabati)</font>", card_title_style),
        Paragraph("2014 – 2022", card_date_style)
    ]
    sec_t = Table([sec_header], colWidths=[430, 110])
    sec_t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    sec_bullets = [
        sec_t,
        Spacer(1, 3),
        Paragraph("• &nbsp;<b>Foundational English Medium Curriculum:</b> Rigorous schooling establishing early excellence in mathematics, physical sciences, and computer literacy.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Practical Mathematics Application:</b> Translated coordinate geometry and trigonometry directly into game logic and trajectory calculators.", bullet_style)
    ]
    sec_card = Table([[sec_bullets]], colWidths=[FULL_W])
    sec_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(sec_card)
    story.append(Spacer(1, 8))

    # 4. Technical Competencies Matrix
    story.append(make_section_banner("Technical Competencies & System Toolchains"))
    story.append(Spacer(1, 5))

    skills_data = [
        [Paragraph("<b>Frontend & UI</b>", pill_label_style), Paragraph("React 18+, TypeScript, JavaScript (ES6+), Tailwind CSS, Vite, HTML5 Canvas API, Responsive UI/UX, CSS Grid/Flexbox, Lucide Icons", body_style)],
        [Paragraph("<b>Backend & Cloud</b>", pill_label_style), Paragraph("Node.js, Express, RESTful API Architecture, Firebase (Auth, Firestore, Hosting, Cloud Functions), Vercel CI/CD, JSON Database Schemas", body_style)],
        [Paragraph("<b>Physics & Math</b>", pill_label_style), Paragraph("2D Canvas Physics (Elastic Collisions, Velocity Decay, Friction, Vector Kinematics, Sub-stepping), Game Loops, FIDE Chess Validation", body_style)],
        [Paragraph("<b>AI Systems & Agents</b>", pill_label_style), Paragraph("Multi-Agent Blueprint Design, Automated Pipeline Orchestration, LLM Prompt Engineering, Antigravity IDE, Browser Automation Tools", body_style)],
        [Paragraph("<b>3D & Creative Tech</b>", pill_label_style), Paragraph("Blender 4.2 (Procedural Environment Modeling, EEVEE/Cycles Rendering, Python Scripting), Web Audio API Sound Synthesis", body_style)],
        [Paragraph("<b>Engineering Practices</b>", pill_label_style), Paragraph("Git, GitHub Version Control, Deterministic State Management, Rapid Prototyping Velocity, Code Refactoring, Automated Test Setup", body_style)],
    ]
    skills_table = Table(skills_data, colWidths=[125, 415])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#f0f7ff")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(skills_table)

    # PAGE BREAK TO PAGE 2
    story.append(PageBreak())

    # =============================================================
    # PAGE 2: DEEP DIVE INTO FLAGSHIP WEB APPLICATIONS
    # =============================================================
    story.append(make_section_banner("Flagship Software Architecture & Production Web Platforms"))
    story.append(Spacer(1, 5))

    # Project 1: OfferIntel
    p1_head = Table([[
        Paragraph("<b>1. OfferIntel — AI-Assisted Compensation Decision Platform</b> &nbsp;[<a href='https://offerintel-7fcf6.web.app' color='#0284c7'>Live Production</a>]", card_title_style),
        Paragraph("Production Web App", card_date_style)
    ]], colWidths=[430, 110])
    p1_head.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    p1_content = [
        p1_head,
        Spacer(1, 2),
        Paragraph("<font color='#0284c7'><b>Stack:</b> React • TypeScript • Tailwind CSS • Firebase Authentication • Firestore • Vercel / Firebase Hosting</font>", card_tag_style),
        Spacer(1, 3),
        Paragraph("• &nbsp;<b>Core Problem & Innovation:</b> Traditional compensation calculators compare only base salary numbers. OfferIntel implements an advanced multi-variable decision model that factors in equity vesting cliffs, bonus liquidity, health/retirement benefit monetary valuations, localized tax liabilities, and long-term career growth velocity.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Mathematical Scoring Algorithm:</b> Formulated a proprietary weighted scoring index that normalizes disparate financial and qualitative offer variables into unified, comparable metrics.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Dynamic Visual Analytics:</b> Built real-time reactive trade-off matrices and comparative charts enabling job candidates to run instant sensitivity analysis across competing job offers.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Cloud & State Architecture:</b> Integrated Firebase Authentication with seamless client-side state persistence and responsive UI flows optimized for both mobile and desktop viewports.", bullet_style)
    ]
    p1_card = Table([[p1_content]], colWidths=[FULL_W])
    p1_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LINELEFT', (0,0), (-1,-1), 3.5, ACCENT_BLUE),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p1_card)
    story.append(Spacer(1, 7))

    # Project 2: FreeStack
    p2_head = Table([[
        Paragraph("<b>2. FreeStack — Open-Source Developer Stack & Library Catalog</b> &nbsp;[<a href='https://freestack-sigma.vercel.app' color='#0284c7'>Live Platform</a>]", card_title_style),
        Paragraph("Open Source", card_date_style)
    ]], colWidths=[430, 110])
    p2_head.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    p2_content = [
        p2_head,
        Spacer(1, 2),
        Paragraph("<font color='#0284c7'><b>Stack:</b> React • TypeScript • Tailwind CSS • Vite • Dynamic Routing • Structured JSON Schema Database</font>", card_tag_style),
        Spacer(1, 3),
        Paragraph("• &nbsp;<b>Core Problem & Value:</b> Aspiring engineers and student developers waste hundreds of hours vetting broken starter kits, bloated dependencies, and outdated tutorials. FreeStack solves this by curating production-grade, zero-bloat templates and roadmap architectures.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Sub-Millisecond Client-Side Filtering:</b> Engineered high-performance client-side indexing and instant multi-tag filtering algorithms that search through hundreds of development resources with zero server round-trips.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Modular Routing Architecture:</b> Implemented dynamic subpath routing (<font name='Helvetica-Oblique'>/library</font>, <font name='Helvetica-Oblique'>/about</font>) with client-side state caching and responsive drawer navigation.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Community Impact:</b> 100% free and open-access platform lowering the barrier to entry for self-taught software developers worldwide.", bullet_style)
    ]
    p2_card = Table([[p2_content]], colWidths=[FULL_W])
    p2_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p2_card)
    story.append(Spacer(1, 7))

    # Project 3: Scentscape Luxury Storefront
    p3_head = Table([[
        Paragraph("<b>3. Scentscape — Luxury Ambient E-Commerce Storefront</b> &nbsp;[<a href='https://frontend-itzzsurajzz-9476s-projects.vercel.app/' color='#0284c7'>Live Demo</a>]", card_title_style),
        Paragraph("E-Commerce Architecture", card_date_style)
    ]], colWidths=[430, 110])
    p3_head.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    p3_content = [
        p3_head,
        Spacer(1, 2),
        Paragraph("<font color='#0284c7'><b>Stack:</b> React • Tailwind CSS • Reactive Cart Architecture • Micro-Interactions • Vercel CI/CD</font>", card_tag_style),
        Spacer(1, 3),
        Paragraph("• &nbsp;<b>Luxury Dark-Mode Aesthetic:</b> Designed an ambient, high-conversion visual retail experience with glassmorphic cards, luminous gradients, and smooth layout transitions.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Reactive Cart State Engine:</b> Built a zero-friction shopping cart state architecture handling real-time item addition, quantity recalculation, and persistent local storage synchronization.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Performance Optimization:</b> Zero Cumulative Layout Shift (CLS) with optimized image lazy-loading and fluid CSS grid adaptations.", bullet_style)
    ]
    p3_card = Table([[p3_content]], colWidths=[FULL_W])
    p3_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p3_card)

    # PAGE BREAK TO PAGE 3
    story.append(PageBreak())

    # =============================================================
    # PAGE 3: PURE PHYSICS ENGINES, GAMES & AI AGENTS
    # =============================================================
    story.append(make_section_banner("Zero-Dependency Physics Engines, Interactive Games & AI Agents"))
    story.append(Spacer(1, 5))

    # Project 4: 2D Custom Canvas Physics Engine & Tank Shooter
    p4_head = Table([[
        Paragraph("<b>4. Tank Shooter — 2D Custom Canvas Physics Engine & Arcade Game</b> &nbsp;[<a href='https://tank-pied.vercel.app' color='#0284c7'>Live Game</a>]", card_title_style),
        Paragraph("Custom Physics Engine", card_date_style)
    ]], colWidths=[430, 110])
    p4_head.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    p4_content = [
        p4_head,
        Spacer(1, 2),
        Paragraph("<font color='#0284c7'><b>Stack:</b> HTML5 Canvas API • Vanilla JavaScript • Vector Math • Sub-Stepping Loop • Web Audio API</font>", card_tag_style),
        Spacer(1, 3),
        Paragraph("• &nbsp;<b>Zero-Dependency Physics Architecture:</b> Programmed an entire 2D physics and collision resolution engine completely from scratch in pure JavaScript—no third-party frameworks like Phaser or Matter.js, ensuring instant load time and lightweight execution.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Mathematical Kinematics:</b> Implemented continuous vector calculations for acceleration, velocity decay, dynamic surface friction, and realistic obstacle boundary bounces.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Particle Systems & Juiciness:</b> Engineered a custom particle explosion emitter and screen-shake camera offsets tied to impact kinetic energy.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Performance & Web Audio:</b> Maintained rock-solid 60 FPS using optimized <font name='Helvetica-Oblique'>requestAnimationFrame</font> loops with procedural audio sound effect synthesis.", bullet_style)
    ]
    p4_card = Table([[p4_content]], colWidths=[FULL_W])
    p4_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LINELEFT', (0,0), (-1,-1), 3.5, ACCENT_BLUE),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p4_card)
    story.append(Spacer(1, 7))

    # Project 5: Carrom Football Pro
    p5_head = Table([[
        Paragraph("<b>5. Carrom Football Pro — Elastic Impulse & Table Physics Simulator</b> &nbsp;[<a href='https://carrom-football-pro.vercel.app/' color='#0284c7'>Live Game</a>]", card_title_style),
        Paragraph("Elastic Physics Game", card_date_style)
    ]], colWidths=[430, 110])
    p5_head.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    p5_content = [
        p5_head,
        Spacer(1, 2),
        Paragraph("<font color='#0284c7'><b>Stack:</b> HTML5 Canvas API • Vanilla JavaScript • Elastic Collision Resolution • Vector Physics</font>", card_tag_style),
        Spacer(1, 3),
        Paragraph("• &nbsp;<b>Mechanics Hybrid:</b> Combines Indian table carrom striker mechanics with competitive football penalty dynamics.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Circle-to-Circle Elastic Impulse Collision:</b> Mathematically calculated 2D elastic collision impulses, resolving normal vectors, tangential friction, and mass momentum transfers between the striker and pucks.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Frictional Drag Models:</b> Programmed realistic non-linear kinetic deceleration modeling physical carrom board friction.", bullet_style)
    ]
    p5_card = Table([[p5_content]], colWidths=[FULL_W])
    p5_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p5_card)
    story.append(Spacer(1, 7))

    # Project 6: Autonomous Developer Agent Ecosystem & Web Terminal
    p6_head = Table([[
        Paragraph("<b>6. Autonomous Developer Agent Ecosystem & Web Terminal Simulator</b> &nbsp;[<a href='https://portfolio-phi-nine-m7qu98woxl.vercel.app' color='#0284c7'>Live Console</a>]", card_title_style),
        Paragraph("AI Multi-Agent System", card_date_style)
    ]], colWidths=[430, 110])
    p6_head.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    p6_content = [
        p6_head,
        Spacer(1, 2),
        Paragraph("<font color='#0284c7'><b>Stack:</b> React • TypeScript • Tailwind CSS • Multi-Agent Blueprints • In-Browser Terminal Emulator</font>", card_tag_style),
        Spacer(1, 3),
        Paragraph("• &nbsp;<b>20 Autonomous Persona Blueprints:</b> Cataloged 20 specialized AI software engineer personas across Architecture (Code Archaeologist, Database Architect), Testing (Debugger, QA Automation), DevOps, Security, and Frontend development.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Interactive Web Terminal:</b> Engineered an in-browser developer shell (<font name='Helvetica-Oblique'>developer-console.sh</font>) with custom command execution, log streaming, and real-time agent dispatch simulation.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Advanced UI Interactions:</b> Created custom text scramblers, gooey text morphing transitions, and high-density modal drawers in pure TypeScript/CSS.", bullet_style)
    ]
    p6_card = Table([[p6_content]], colWidths=[FULL_W])
    p6_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LINELEFT', (0,0), (-1,-1), 3.5, ACCENT_BLUE),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p6_card)

    # PAGE BREAK TO PAGE 4
    story.append(PageBreak())

    # =============================================================
    # PAGE 4: CHESS ENGINE, 3D BLENDER, HARDWARE BUILDS & METHODOLOGY
    # =============================================================
    story.append(make_section_banner("Interactive Chess Engine, 3D Environments & Hardware Systems"))
    story.append(Spacer(1, 5))

    # Project 7: Chess Simulator
    p7_head = Table([[
        Paragraph("<b>7. Interactive Web Chess Simulator & State Validation Engine</b> &nbsp;[<a href='https://chess-zeta-henna.vercel.app/' color='#0284c7'>Live Simulation</a>]", card_title_style),
        Paragraph("FIDE Rule Engine", card_date_style)
    ]], colWidths=[430, 110])
    p7_head.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    p7_content = [
        p7_head,
        Spacer(1, 2),
        Paragraph("<font color='#0284c7'><b>Stack:</b> React • CSS Grid • State Validation Engine • Board History Traversal</font>", card_tag_style),
        Spacer(1, 3),
        Paragraph("• &nbsp;<b>Modular Move Validation:</b> Architected a custom piece-movement rule engine enforcing standard FIDE chess rules, legal move generation, pin detection, check, checkmate, and en passant in real-time.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Board State & History:</b> Engineered deterministic board state management with responsive turn visualizers and undo history traversal.", bullet_style)
    ]
    p7_card = Table([[p7_content]], colWidths=[FULL_W])
    p7_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(p7_card)
    story.append(Spacer(1, 6))

    # 3D Blender Systems & Creative Technology
    story.append(make_section_banner("Creative Technology & 3D Environment Design (Blender)"))
    story.append(Spacer(1, 5))

    b_content = [
        Paragraph("<b>Procedural 3D Environment Modeling & Lighting:</b> Developed atmospheric 3D scenes (Ancient Ruins & Sacred Cavern series) in Blender 4.2 utilizing procedural texturing, volumetric fog, EEVEE Next and Cycles rendering passes.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Technical Lighting & Asset Pipelines:</b> Optimized asset geometry, PBR material nodes, and camera depth-of-field setups for real-time web visualization and high-fidelity rendering.", bullet_style)
    ]
    b_card = Table([[b_content]], colWidths=[FULL_W])
    b_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(b_card)
    story.append(Spacer(1, 6))

    # Extracurricular Engineering & Hardware Teardowns
    story.append(make_section_banner("Extracurricular Hardware Systems & Junkyard Diagnostics"))
    story.append(Spacer(1, 5))

    hw_content = [
        Paragraph("• &nbsp;<b>Junkyard Hardware Teardowns & Diagnostics:</b> Salvaged and rebuilt legacy desktop towers from local junkyards; taught himself CPU/GPU thermal paste optimization, power supply diagnostics, and motherboard capacitor testing to become the neighborhood go-to IT technician.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Physical-Digital Systems Synergy:</b> Inspired by his father (an electrical technician), bridges physical electrical troubleshooting with digital software logic to build resilient computer systems.", bullet_style),
        Spacer(1, 2),
        Paragraph("• &nbsp;<b>Global Academic Preparation:</b> Actively preparing for specialized training and undergraduate studies in Information Processing and Computer Science in Japan (MEXT Scholarship).", bullet_style)
    ]
    hw_card = Table([[hw_content]], colWidths=[FULL_W])
    hw_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('LINELEFT', (0,0), (-1,-1), 3.5, ACCENT_BLUE),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(hw_card)
    story.append(Spacer(1, 6))

    # Global Team Readiness
    story.append(make_section_banner("Global Team Readiness & Work Methodology"))
    story.append(Spacer(1, 5))

    methods_data = [
        [Paragraph("<b>Rapid Prototyping Velocity:</b>", pill_label_style), Paragraph("Transforms complex system specifications into fully functioning, testable MVPs in days rather than weeks with high code modularity.", body_style)],
        [Paragraph("<b>AI-Augmented Engineering:</b>", pill_label_style), Paragraph("Leverages agentic AI IDEs (Google Antigravity) to multiply developer velocity, automate test suites, and refactor architectures.", body_style)],
        [Paragraph("<b>International Team Alignment:</b>", pill_label_style), Paragraph("100% English Medium educational background with fluent technical communication, agile timezone flexibility, and complete readiness for worldwide relocation.", body_style)],
    ]
    methods_table = Table(methods_data, colWidths=[140, 400])
    methods_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BACKGROUND', (0,0), (-1,-1), GLASS_CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.9, GLASS_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor("#f0f7ff")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(methods_table)

    # Build primary PDF with ultra-smooth pure glass canvas callback
    primary_path = output_paths[0]
    doc_inst = SimpleDocTemplate(
        primary_path,
        pagesize=letter,
        leftMargin=28,
        rightMargin=28,
        topMargin=24,
        bottomMargin=24
    )
    doc_inst.build(
        story,
        onFirstPage=draw_pure_glass_background,
        onLaterPages=draw_pure_glass_background
    )
    print(f"Generated Super Dossier: {primary_path}")

    # Copy cleanly to Downloads & other paths
    for target in output_paths[1:]:
        shutil.copyfile(primary_path, target)
        print(f"Synced to: {target}")

if __name__ == "__main__":
    generate_super_dossier()
