import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_JUSTIFY

def generate_compact_1page_cv(output_path="Suraj_Das_CV_1Page.pdf"):
    # 0.35 in margin (approx 25pt) to fit cleanly on 1 page
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=26,
        rightMargin=26,
        topMargin=22,
        bottomMargin=22
    )
    
    PRIMARY = colors.HexColor("#0f172a")     # Slate 900
    ACCENT = colors.HexColor("#0284c7")      # Sky 600
    SECONDARY = colors.HexColor("#334155")   # Slate 700
    MUTED = colors.HexColor("#64748b")       # Slate 500
    LINE_COLOR = colors.HexColor("#cbd5e1")  # Slate 300
    LINK_COLOR = colors.HexColor("#0369a1")

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'NameTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=20,
        textColor=PRIMARY
    )
    
    subtitle_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=ACCENT
    )
    
    contact_style = ParagraphStyle(
        'ContactBar',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=SECONDARY,
        alignment=TA_RIGHT
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=11,
        textColor=PRIMARY,
        spaceAfter=1
    )
    
    summary_style = ParagraphStyle(
        'SummaryText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=SECONDARY,
        alignment=TA_JUSTIFY
    )

    item_title_style = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=PRIMARY
    )
    
    item_date_style = ParagraphStyle(
        'ItemDate',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=ACCENT,
        alignment=TA_RIGHT
    )

    bullet_style = ParagraphStyle(
        'BulletPoint',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=SECONDARY,
        leftIndent=8,
        firstLineIndent=-8
    )

    skill_category_style = ParagraphStyle(
        'SkillCategory',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=PRIMARY
    )

    skill_desc_style = ParagraphStyle(
        'SkillDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=SECONDARY
    )

    story = []

    # 1. Header
    header_left = [
        Paragraph("<b>SURAJ DAS</b>", title_style),
        Spacer(1, 1),
        Paragraph("Full-Stack Software Engineer & AI Systems Prototyper", subtitle_style),
    ]
    
    header_right = [
        Paragraph("📍 West Bengal, India &nbsp;|&nbsp; 🌐 <i>Open to International Relocation & Remote</i>", contact_style),
        Paragraph('📧 <a href="mailto:itzzsuraj7@gmail.com" color="' + LINK_COLOR.hexval() + '">itzzsuraj7@gmail.com</a> &nbsp;|&nbsp; 🔗 <a href="https://linkedin.com/in/suraj-das-5801793aa" color="' + LINK_COLOR.hexval() + '">LinkedIn</a> &nbsp;|&nbsp; 💻 <a href="https://github.com/gitsuraj7" color="' + LINK_COLOR.hexval() + '">GitHub</a>', contact_style),
        Paragraph('🚀 <b>Portfolio:</b> <a href="https://gitsuraj7.github.io/PORTFOLIO" color="' + LINK_COLOR.hexval() + '">gitsuraj7.github.io/PORTFOLIO</a>', contact_style),
    ]

    header_table = Table([[header_left, header_right]], colWidths=[310, 250])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=1, spaceAfter=4))

    def add_section(title):
        story.append(Paragraph(f"<b>{title.upper()}</b>", section_heading))
        story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=0.5, spaceAfter=3))

    # Executive Summary
    add_section("Executive Summary")
    summary_text = (
        "<b>High-initiative Software Engineer and Systems Builder</b> specializing in full-stack web applications, "
        "custom physics simulation engines, and autonomous AI developer workflows. Proven track record of independently architecting, "
        "building, and shipping production applications with polished UX, reactive architectures (React, TypeScript, Tailwind), and cloud integrations. "
        "Demonstrates exceptional rapid-prototyping velocity through AI-augmented workflows. Seeking high-impact global opportunities, "
        "internships, or academic research collaborations in software engineering and computer science."
    )
    story.append(Paragraph(summary_text, summary_style))
    story.append(Spacer(1, 4))

    # Technical Skills
    add_section("Technical Competencies")
    skills_data = [
        [Paragraph("<b>Frontend & UI:</b>", skill_category_style), Paragraph("React, TypeScript, JavaScript (ES6+), Tailwind CSS, Vite, HTML5 Canvas, Responsive UI/UX", skill_desc_style)],
        [Paragraph("<b>Backend & Cloud:</b>", skill_category_style), Paragraph("Node.js, REST APIs, Firebase (Auth, Firestore, Hosting), Vercel CI/CD & Deployments", skill_desc_style)],
        [Paragraph("<b>Physics & Simulation:</b>", skill_category_style), Paragraph("2D Canvas Physics Engines (Collision Impulses, Friction, Vector Math, Game Loops)", skill_desc_style)],
        [Paragraph("<b>AI Systems & Tooling:</b>", skill_category_style), Paragraph("Multi-Agent Architecture, LLM Agent Blueprints, Automated Engineering Workflows, Git", skill_desc_style)],
    ]
    skills_table = Table(skills_data, colWidths=[115, 445])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 4))

    # Projects
    add_section("Featured Engineering Projects")
    projects = [
        {
            "title": "OfferIntel — AI Job Offer Evaluation & Analytics Platform",
            "link": "https://offerintel-7fcf6.web.app",
            "tag": "React • TypeScript • Tailwind • Firebase Auth",
            "bullets": [
                "Engineered a multi-dimensional offer comparison tool that quantifies role value, equity potential, and growth upside beyond base salary.",
                "Integrated Firebase Auth and structured interactive decision matrix workflows with zero onboarding friction."
            ]
        },
        {
            "title": "Autonomous Developer Agent Ecosystem & Web Terminal",
            "link": "https://gitsuraj7.github.io/PORTFOLIO",
            "tag": "React • TypeScript • Tailwind • Multi-Agent Blueprints",
            "bullets": [
                "Constructed 20 autonomous AI agent blueprints spanning Architecture, DevOps, Security, QA, and Frontend development.",
                "Built an interactive in-browser developer console (<font name='Helvetica-Oblique'>developer-console.sh</font>) simulating multi-agent collaborative task execution."
            ]
        },
        {
            "title": "FreeStack — Open-Source Developer Resource Library",
            "link": "https://freestack-sigma.vercel.app",
            "tag": "React • TypeScript • Tailwind • Vite • Dynamic Routing",
            "bullets": [
                "Developed a curated discovery portal for development templates and learning roadmaps with instant sub-millisecond client-side filtering."
            ]
        },
        {
            "title": "2D Custom Physics & Canvas Game Engine (Tank Shooter & Carrom Pro)",
            "link": "https://tank-pied.vercel.app",
            "tag": "HTML5 Canvas • Vanilla JavaScript • Vector Math • 60 FPS",
            "bullets": [
                "Built custom lightweight physics engines from scratch handling elastic collision impulses, friction deceleration, and particle shockwaves."
            ]
        },
        {
            "title": "Scentscape — Ambient Luxury E-Commerce Experience",
            "link": "https://frontend-itzzsurajzz-9476s-projects.vercel.app/",
            "tag": "React • Tailwind CSS • Micro-Interactions • State Architecture",
            "bullets": [
                "Crafted high-conversion dark-mode e-commerce storefront with reactive state management and micro-interactions."
            ]
        }
    ]

    for proj in projects:
        p_table = Table([[
            Paragraph(f'<b>{proj["title"]}</b> &nbsp;[<a href="{proj["link"]}" color="{LINK_COLOR.hexval()}">Live Demo</a>]', item_title_style),
            Paragraph(proj["tag"], item_date_style)
        ]], colWidths=[330, 230])
        p_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(p_table)
        for bullet in proj["bullets"]:
            story.append(Paragraph(f"• &nbsp;{bullet}", bullet_style))
        story.append(Spacer(1, 2.5))

    story.append(Spacer(1, 2))

    # Work Methodology & International Value
    add_section("Global Team Readiness & Work Methodology")
    methods = [
        [Paragraph("<b>Fast Iteration Cycles:</b>", skill_category_style), Paragraph("Rapid prototype delivery from concept to functional MVP with high code cleanliness.", skill_desc_style)],
        [Paragraph("<b>AI Toolchain Mastery:</b>", skill_category_style), Paragraph("Harnesses next-gen AI engineering toolchains to maximize output velocity and debugging precision.", skill_desc_style)],
        [Paragraph("<b>Cross-Border Collaboration:</b>", skill_category_style), Paragraph("Fluent technical English, cross-timezone availability, open to global relocation and remote positions.", skill_desc_style)]
    ]
    m_table = Table(methods, colWidths=[130, 430])
    m_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
    ]))
    story.append(m_table)
    story.append(Spacer(1, 4))

    # Education
    add_section("Education & Continuous Academic Development")
    edu_table = Table([[
        Paragraph("<b>Serampore Vivekananda Academy</b> &nbsp;|&nbsp; Higher Secondary (Science, English Medium)", item_title_style),
        Paragraph("2022 – 2026", item_date_style)
    ]], colWidths=[420, 140])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)
    story.append(Paragraph("• &nbsp;<b>Medium & Subjects:</b> English Medium schooling. Physics, Chemistry, Math, Biology, English, PE.", bullet_style))
    story.append(Paragraph("• &nbsp;<b>Independent Study:</b> Data Structures & Algorithms, Modern Web Architecture, Agent-Based AI Systems.", bullet_style))
    story.append(Paragraph("• &nbsp;<b>Target:</b> Preparing for specialized higher education in Information Processing / Computer Science in Japan (MEXT).", bullet_style))

    doc.build(story)
    print(f"Generated 1-Page CV: {output_path}")

if __name__ == "__main__":
    generate_compact_1page_cv("e:/keep EXP/portfolio/Suraj_Das_Software_Engineer_CV.pdf")
