import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_JUSTIFY

def generate_authentic_student_cv(output_path="Suraj_Das_CV.pdf"):
    # Clean 1-page document with professional margins
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=28,
        rightMargin=28,
        topMargin=24,
        bottomMargin=24
    )
    
    PRIMARY = colors.HexColor("#0f172a")     # Slate 900
    ACCENT = colors.HexColor("#0284c7")      # Clean blue
    SECONDARY = colors.HexColor("#334155")   # Slate 700
    MUTED = colors.HexColor("#64748b")       # Slate 500
    LINE_COLOR = colors.HexColor("#cbd5e1")  # Slate 300
    LINK_COLOR = colors.HexColor("#0369a1")

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'NameTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=18, leading=20, textColor=PRIMARY
    )
    subtitle_style = ParagraphStyle(
        'SubTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=12, textColor=ACCENT
    )
    contact_style = ParagraphStyle(
        'ContactBar', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11, textColor=SECONDARY, alignment=TA_RIGHT
    )
    section_heading = ParagraphStyle(
        'SectionHeading', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=11.5, textColor=PRIMARY, spaceAfter=1
    )
    summary_style = ParagraphStyle(
        'SummaryText', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.2, leading=11.5, textColor=SECONDARY, alignment=TA_JUSTIFY
    )
    item_title_style = ParagraphStyle(
        'ItemTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=PRIMARY
    )
    item_date_style = ParagraphStyle(
        'ItemDate', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8, leading=11, textColor=ACCENT, alignment=TA_RIGHT
    )
    bullet_style = ParagraphStyle(
        'BulletPoint', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11, textColor=SECONDARY, leftIndent=8, firstLineIndent=-8
    )
    skill_category_style = ParagraphStyle(
        'SkillCategory', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8, leading=11, textColor=PRIMARY
    )
    skill_desc_style = ParagraphStyle(
        'SkillDesc', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11, textColor=SECONDARY
    )

    story = []

    # 1. Header
    header_left = [
        Paragraph("<b>SURAJ DAS</b>", title_style),
        Spacer(1, 1),
        Paragraph("Aspiring Computer Science Student & Prototyper", subtitle_style),
    ]
    
    header_right = [
        Paragraph("📍 West Bengal, India &nbsp;|&nbsp; 🌐 <i>Open to International Undergraduate Programs & Lab Internships</i>", contact_style),
        Paragraph('📧 <a href="mailto:itzzsuraj7@gmail.com" color="' + LINK_COLOR.hexval() + '">itzzsuraj7@gmail.com</a> &nbsp;|&nbsp; 🔗 <a href="https://linkedin.com/in/suraj-das-5801793aa" color="' + LINK_COLOR.hexval() + '">LinkedIn</a> &nbsp;|&nbsp; 💻 <a href="https://github.com/gitsuraj7" color="' + LINK_COLOR.hexval() + '">GitHub</a>', contact_style),
        Paragraph('🚀 <b>Live Portfolio:</b> <a href="https://gitsuraj7.github.io/PORTFOLIO" color="' + LINK_COLOR.hexval() + '">gitsuraj7.github.io/PORTFOLIO</a>', contact_style),
    ]

    header_table = Table([[header_left, header_right]], colWidths=[300, 256])
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

    # Profile / About Me
    add_section("Candidate Profile")
    summary_text = (
        "<b>Self-motivated high school student and hands-on learner</b> passionate about computer science, software building, "
        "and interactive web interfaces. Before beginning formal university coursework, I actively explore software development by building "
        "practical projects—from web tools and 2D canvas arcade games to AI-assisted developer workflows. I use modern AI coding tools "
        "as an accelerator to experiment rapidly, troubleshoot errors, and understand how applications work end-to-end. "
        "Seeking an international undergraduate program, research group, or laboratory internship where I can build a rigorous theoretical "
        "foundation in computer science under expert mentorship."
    )
    story.append(Paragraph(summary_text, summary_style))
    story.append(Spacer(1, 4))

    # Education
    add_section("Education & Academic Background")
    edu_table = Table([[
        Paragraph("<b>Higher Secondary Education (Science Stream: Mathematics, Physics, Chemistry)</b>", item_title_style),
        Paragraph("Expected 2026", item_date_style)
    ]], colWidths=[420, 136])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)
    story.append(Paragraph("• &nbsp;<b>Core Subjects:</b> Mathematics, Physics, Chemistry, and English.", bullet_style))
    story.append(Paragraph("• &nbsp;<b>Independent Study:</b> Introductory programming, algorithm logic, web fundamentals, and modern developer tooling.", bullet_style))
    story.append(Paragraph("• &nbsp;<b>Objective:</b> Pursuing Bachelor's degree opportunities abroad in Computer Science & Information Systems.", bullet_style))
    story.append(Spacer(1, 4))

    # Technical Skills & Tools Explored
    add_section("Technical Toolkit & Practical Skills")
    skills_data = [
        [Paragraph("<b>Languages & Web:</b>", skill_category_style), Paragraph("JavaScript (ES6+), TypeScript basics, HTML5, CSS3, React basics, Tailwind CSS", skill_desc_style)],
        [Paragraph("<b>Graphics & Games:</b>", skill_category_style), Paragraph("HTML5 2D Canvas, basic vector mathematics (velocity, friction, collision detection)", skill_desc_style)],
        [Paragraph("<b>Backend & Hosting:</b>", skill_category_style), Paragraph("Firebase (Authentication & hosting basics), Vercel, Git & GitHub for version control", skill_desc_style)],
        [Paragraph("<b>AI-Assisted Workflow:</b>", skill_category_style), Paragraph("AI coding assistants (prompting, code generation, debugging, refactoring, agent workflows)", skill_desc_style)],
    ]
    skills_table = Table(skills_data, colWidths=[120, 436])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 4))

    # Self-Initiated Projects (Authentic, clear descriptions)
    add_section("Self-Initiated Projects & Prototypes")
    projects = [
        {
            "title": "OfferIntel — Job Offer Comparison Tool",
            "link": "https://offerintel-7fcf6.web.app",
            "tag": "React • TypeScript • Tailwind • Firebase",
            "bullets": [
                "Built an interactive web tool that helps users compare job offers across multiple factors like growth potential, culture, and benefits alongside basic compensation.",
                "Integrated Firebase Auth for user sign-in and organized responsive form workflows."
            ]
        },
        {
            "title": "Interactive Developer Portfolio & Terminal Console",
            "link": "https://gitsuraj7.github.io/PORTFOLIO",
            "tag": "React • TypeScript • Tailwind • Vite",
            "bullets": [
                "Created an interactive portfolio with an in-browser developer terminal (<font name='Helvetica-Oblique'>developer-console.sh</font>) that simulates task commands and displays project info.",
                "Organized a catalog of 20 developer agent personas demonstrating how different AI roles collaborate on a coding task."
            ]
        },
        {
            "title": "FreeStack — Open Developer Resource Directory",
            "link": "https://freestack-sigma.vercel.app",
            "tag": "React • TypeScript • Tailwind • Vite",
            "bullets": [
                "Built a clean web directory cataloging useful learning resources, developer templates, and tools with instant search and category browsing."
            ]
        },
        {
            "title": "2D Canvas Arcade Games (Tank Shooter & Carrom Football Pro)",
            "link": "https://tank-pied.vercel.app",
            "tag": "HTML5 Canvas • JavaScript • Physics Logic",
            "bullets": [
                "Programmed 2D browser games from scratch using HTML5 Canvas, implementing simple 2D collision physics, velocity friction, score tracking, and keyboard controls."
            ]
        },
        {
            "title": "Chess & Scentscape Web Prototypes",
            "link": "https://chess-zeta-henna.vercel.app/",
            "tag": "React • CSS Grid • UI Design",
            "bullets": [
                "Built an interactive chess board UI with turn indicators, and an aesthetic dark-mode e-commerce storefront mockup focusing on UI layout and smooth interactions."
            ]
        }
    ]

    for proj in projects:
        p_table = Table([[
            Paragraph(f'<b>{proj["title"]}</b> &nbsp;[<a href="{proj["link"]}" color="{LINK_COLOR.hexval()}">Live Demo</a>]', item_title_style),
            Paragraph(proj["tag"], item_date_style)
        ]], colWidths=[340, 216])
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
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 2))

    # Learning Attitude & Research Readiness
    add_section("Learning Mindset & Academic Motivation")
    mindset_data = [
        [
            Paragraph("<b>Eagerness to Learn:</b>", skill_category_style),
            Paragraph("High curiosity and self-drive; eager to transition from practical experimentation into rigorous academic study in algorithms, data structures, and computer systems.", skill_desc_style)
        ],
        [
            Paragraph("<b>Hands-On Prototyping:</b>", skill_category_style),
            Paragraph("Quick to try new ideas, read documentation, use AI assistants to unblock technical hurdles, and deploy live demos on the web.", skill_desc_style)
        ],
        [
            Paragraph("<b>International Preparedness:</b>", skill_category_style),
            Paragraph("Fluent English communication, strong self-discipline, and enthusiasm for working in cross-cultural academic environments.", skill_desc_style)
        ]
    ]
    m_table = Table(mindset_data, colWidths=[125, 431])
    m_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
    ]))
    story.append(m_table)

    doc.build(story)
    print(f"Generated Authentic Student CV: {output_path}")

if __name__ == "__main__":
    generate_authentic_student_cv("e:/keep EXP/portfolio/Suraj_Das_CV.pdf")
    generate_authentic_student_cv("e:/keep EXP/portfolio/Suraj_Das_Software_Engineer_CV.pdf")
