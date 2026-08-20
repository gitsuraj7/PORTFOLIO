import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY

def generate_cv_pdf(output_path="Suraj_Das_Software_Engineer_CV.pdf"):
    # Margins: 0.45 inch to make it a crisp, high-density, perfectly formatted 1-2 page document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=32,
        rightMargin=32,
        topMargin=30,
        bottomMargin=30
    )
    
    # Palette
    PRIMARY = colors.HexColor("#0f172a")     # Deep slate / near black
    ACCENT = colors.HexColor("#0284c7")      # Vibrant ocean cyan / blue
    SECONDARY = colors.HexColor("#334155")   # Slate text
    MUTED = colors.HexColor("#64748b")       # Muted gray text
    LINE_COLOR = colors.HexColor("#cbd5e1")  # Clean divider line
    BG_PILL = colors.HexColor("#f1f5f9")     # Pill background
    LINK_COLOR = colors.HexColor("#0369a1")  # Clickable link blue

    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'NameTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=PRIMARY
    )
    
    subtitle_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=ACCENT
    )
    
    contact_style = ParagraphStyle(
        'ContactBar',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=SECONDARY,
        alignment=TA_RIGHT
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=PRIMARY,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=SECONDARY,
        alignment=TA_LEFT
    )
    
    summary_style = ParagraphStyle(
        'SummaryText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=SECONDARY,
        alignment=TA_JUSTIFY
    )

    item_title_style = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=PRIMARY
    )
    
    item_date_style = ParagraphStyle(
        'ItemDate',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=13,
        textColor=ACCENT,
        alignment=TA_RIGHT
    )

    bullet_style = ParagraphStyle(
        'BulletPoint',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=SECONDARY,
        leftIndent=10,
        firstLineIndent=-10
    )

    skill_category_style = ParagraphStyle(
        'SkillCategory',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=PRIMARY
    )

    skill_desc_style = ParagraphStyle(
        'SkillDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=SECONDARY
    )

    story = []

    # 1. Header (Name + Contact info in two columns)
    header_left = [
        Paragraph("<b>SURAJ DAS</b>", title_style),
        Spacer(1, 2),
        Paragraph("Full-Stack Software Engineer & AI-Augmented Systems Builder", subtitle_style),
    ]
    
    header_right = [
        Paragraph("📍 West Bengal, India &nbsp;|&nbsp; 🌐 <i>Open to Worldwide Relocation / Remote</i>", contact_style),
        Spacer(1, 2),
        Paragraph('📧 <a href="mailto:itzzsuraj7@gmail.com" color="' + LINK_COLOR.hexval() + '">itzzsuraj7@gmail.com</a> &nbsp;|&nbsp; 🔗 <a href="https://linkedin.com/in/suraj-das-5801793aa" color="' + LINK_COLOR.hexval() + '">linkedin.com/in/suraj-das</a>', contact_style),
        Spacer(1, 2),
        Paragraph('💻 <a href="https://github.com/gitsuraj7" color="' + LINK_COLOR.hexval() + '">github.com/gitsuraj7</a> &nbsp;|&nbsp; 🚀 <a href="https://gitsuraj7.github.io/PORTFOLIO" color="' + LINK_COLOR.hexval() + '">Portfolio: gitsuraj7.github.io</a>', contact_style),
    ]

    header_table = Table([[header_left, header_right]], colWidths=[310, 238])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceBefore=2, spaceAfter=8))

    # Helper function for section headers
    def add_section_header(title_text):
        story.append(Paragraph(f"<b>{title_text.upper()}</b>", section_heading))
        story.append(HRFlowable(width="100%", thickness=0.6, color=LINE_COLOR, spaceBefore=1, spaceAfter=6))

    # 2. Executive Summary / Value Proposition
    add_section_header("Executive Summary")
    summary_p = (
        "<b>Results-driven Software Engineer and Product Builder</b> specialized in building high-performance modern web applications, "
        "interactive physics/simulation engines, and multi-agent AI automation workflows. Proven track record of shipping end-to-end production-grade "
        "applications independently—from intuitive UI/UX architectures (React, TypeScript, Tailwind) to robust backend integrations and client-side "
        "simulation engines. Highly adept at leveraging cutting-edge AI-assisted toolchains to rapidly build, test, and iterate on complex software. "
        "Passionate about international engineering environments, scalable web systems, and high-impact software."
    )
    story.append(Paragraph(summary_p, summary_style))
    story.append(Spacer(1, 8))

    # 3. Core Technical Competencies
    add_section_header("Technical Competencies")
    skills_data = [
        [
            Paragraph("<b>Frontend & UI:</b>", skill_category_style),
            Paragraph("React, TypeScript, JavaScript (ES6+), Tailwind CSS, Vite, HTML5 Canvas, Responsive UI/UX, CSS Grid/Flexbox", skill_desc_style)
        ],
        [
            Paragraph("<b>Backend & Cloud:</b>", skill_category_style),
            Paragraph("Node.js, RESTful API Design, Firebase (Auth, Firestore, Hosting), Vercel Deployment & CI/CD", skill_desc_style)
        ],
        [
            Paragraph("<b>Architecture & Simulation:</b>", skill_category_style),
            Paragraph("2D Physics Engines (Vector Math, Collisions, Impulse Dynamics), Game Loop Architecture, State Machines", skill_desc_style)
        ],
        [
            Paragraph("<b>AI Tooling & Automation:</b>", skill_category_style),
            Paragraph("Multi-Agent AI Workflows, LLM Agent Blueprints, Automated Prompt Pipelines, Antigravity/Cursor/Claude toolchains", skill_desc_style)
        ],
        [
            Paragraph("<b>Tools & Practices:</b>", skill_category_style),
            Paragraph("Git, GitHub, Automated QA & Testing principles, Agile Rapid Prototyping, Performance Optimization", skill_desc_style)
        ],
    ]
    skills_table = Table(skills_data, colWidths=[130, 418])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 8))

    # 4. Featured Software Engineering Projects
    add_section_header("Featured Engineering Projects")

    projects = [
        {
            "title": "OfferIntel — AI-Assisted Career & Compensation Intelligence Platform",
            "link": "https://offerintel-7fcf6.web.app",
            "date": "Live Production",
            "stack": "React • TypeScript • Tailwind CSS • Firebase Auth • Analytics",
            "bullets": [
                "Architected and deployed a multi-dimensional job offer comparison platform that quantifies role value, equity potential, career growth trajectories, and comprehensive benefits.",
                "Engineered a reactive assessment engine providing visual trade-off breakdowns and personalized decision matrices.",
                "Integrated Firebase Authentication and secured state management, enabling zero-friction onboarding."
            ]
        },
        {
            "title": "Autonomous Developer Agent Ecosystem & Interactive Shell",
            "link": "https://gitsuraj7.github.io/PORTFOLIO",
            "date": "Open Source",
            "stack": "React • TypeScript • Tailwind CSS • Vite • Agent Blueprints",
            "bullets": [
                "Designed and cataloged 20 specialized autonomous AI software engineering agent blueprints spanning Architecture, DevOps, Security, QA, and Frontend development.",
                "Built an interactive in-browser developer terminal (<font name='Helvetica-Oblique'>developer-console.sh</font>) supporting asynchronous multi-agent pipeline orchestration simulations.",
                "Crafted custom dynamic UI components including ScrambleText, GooeyMorph, and high-density responsive drawers."
            ]
        },
        {
            "title": "FreeStack — Curated Developer Resource & Knowledge Stack",
            "link": "https://freestack-sigma.vercel.app",
            "date": "Open Source",
            "stack": "React • TypeScript • Tailwind CSS • Vite • Dynamic Routing",
            "bullets": [
                "Built a structured developer discovery portal housing hundreds of categorized development templates, tutorials, and tech stack resources.",
                "Implemented dynamic client-side filtering, fuzzy keyword search, and modular categorical routing to deliver instant sub-millisecond search experiences."
            ]
        },
        {
            "title": "2D Custom Physics & Canvas Game Engine Series (Tank Shooter & Carrom Football Pro)",
            "link": "https://tank-pied.vercel.app",
            "date": "Live Games",
            "stack": "HTML5 Canvas • Vanilla JavaScript • Vector Mathematics • Web Audio API",
            "bullets": [
                "Engineered lightweight 2D canvas physics simulation loops from scratch featuring circle-to-circle elastic collision impulses, friction deceleration, and particle shockwaves.",
                "Achieved stable 60 FPS performance across desktop and mobile browsers with optimized rendering loops and custom state machines."
            ]
        },
        {
            "title": "Scentscape — Luxury Ambient Commerce Experience",
            "link": "https://frontend-itzzsurajzz-9476s-projects.vercel.app/",
            "date": "E-Commerce",
            "stack": "React • Tailwind CSS • State Architecture • Micro-Interactions",
            "bullets": [
                "Created a sleek dark-mode e-commerce application focusing on micro-interactions, responsive cart workflows, and high-conversion aesthetic polish."
            ]
        }
    ]

    for proj in projects:
        p_header = [
            Paragraph(f'<b>{proj["title"]}</b> &nbsp;[<a href="{proj["link"]}" color="{LINK_COLOR.hexval()}">Live Demo</a>]', item_title_style),
            Paragraph(proj["date"], item_date_style)
        ]
        p_table = Table([p_header], colWidths=[420, 128])
        p_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 1),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        story.append(p_table)
        story.append(Paragraph(f"<font color='{ACCENT.hexval()}'><b>Tech Stack:</b></font> {proj['stack']}", ParagraphStyle('StackStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=MUTED)))
        story.append(Spacer(1, 2))
        
        for bullet in proj["bullets"]:
            story.append(Paragraph(f"• &nbsp;{bullet}", bullet_style))
            story.append(Spacer(1, 1.5))
        story.append(Spacer(1, 4))

    # 5. Professional Philosophy & Working Methodology
    add_section_header("Work Methodology & Global Readiness")
    method_data = [
        [
            Paragraph("<b>Rapid Prototyping:</b>", skill_category_style),
            Paragraph("Fast iteration cycles from conceptualization to functional MVP with production-level code hygiene.", skill_desc_style)
        ],
        [
            Paragraph("<b>AI-Augmented Velocity:</b>", skill_category_style),
            Paragraph("Leverages state-of-the-art AI development tools to boost engineering throughput, debugging speed, and test coverage.", skill_desc_style)
        ],
        [
            Paragraph("<b>Global Mobility:</b>", skill_category_style),
            Paragraph("Fully adaptable to international team workflows, English communication, and remote / relocation opportunities.", skill_desc_style)
        ]
    ]
    method_table = Table(method_data, colWidths=[130, 418])
    method_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(method_table)
    story.append(Spacer(1, 8))

    # 6. Education & Academic Pursuits
    add_section_header("Education & Continuous Learning")
    edu_header = [
        Paragraph("<b>High School Education (Science & Mathematics)</b> &nbsp;|&nbsp; West Bengal, India", item_title_style),
        Paragraph("2024 – Present", item_date_style)
    ]
    edu_table = Table([edu_header], colWidths=[420, 128])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(edu_table)
    story.append(Paragraph("• &nbsp;<b>Focus:</b> Advanced Mathematics, Physics, and Computer Science fundamentals.", bullet_style))
    story.append(Paragraph("• &nbsp;<b>Independent Study:</b> Data Structures, Algorithms, Web Application Architecture, Multi-Agent AI systems.", bullet_style))
    story.append(Paragraph("• &nbsp;<b>International Academic Aspirations:</b> Pursuing global university undergraduate degree programs in Computer Science & Information Systems.", bullet_style))

    # Build document
    doc.build(story)
    print(f"Successfully generated CV at: {output_path}")

if __name__ == "__main__":
    generate_cv_pdf("e:/keep EXP/portfolio/Suraj_Das_Software_Engineer_CV.pdf")
