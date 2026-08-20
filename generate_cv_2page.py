import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY

def draw_clean_background(canvas, doc):
    canvas.saveState()
    width, height = letter
    
    # 1. Base clean white canvas
    canvas.setFillColor(colors.HexColor("#ffffff"))
    canvas.rect(0, 0, width, height, fill=1, stroke=0)
    
    # 2. Clean editorial footer
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#94a3b8"))
    page_num = canvas.getPageNumber()
    canvas.drawString(28, 20, "SURAJ DAS  •  ACADEMIC PORTFOLIO CV")
    canvas.drawRightString(width - 28, 20, f"PAGE {page_num} OF 2")
    
    canvas.restoreState()

def generate_academic_cv():
    output_paths = [
        "e:/keep EXP/portfolio/Suraj_Das_Software_Engineer_CV.pdf",
        "e:/keep EXP/portfolio/Suraj_Das_CV.pdf",
        "e:/keep EXP/portfolio/Suraj_Das_Software_Engineer_CV_Extended.pdf",
        os.path.join(os.environ['USERPROFILE'], 'Downloads', 'Suraj_Das_Software_Engineer_CV.pdf'),
        os.path.join(os.environ['USERPROFILE'], 'Downloads', 'cv.pdf')
    ]

    PRIMARY = colors.HexColor("#0f172a")
    SECONDARY = colors.HexColor("#334155")
    MUTED = colors.HexColor("#64748b")
    ACCENT_BLUE = colors.HexColor("#0284c7")
    DARK_BLUE = colors.HexColor("#0369a1")
    BORDER_COLOR = colors.HexColor("#cbd5e1")
    HEADER_BG = colors.HexColor("#f8fafc")
    
    styles = getSampleStyleSheet()
    FULL_W = 556

    name_style = ParagraphStyle(
        'HeroName', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=22, leading=25, textColor=PRIMARY
    )
    contact_style = ParagraphStyle(
        'ContactPill', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=13, textColor=SECONDARY, alignment=TA_RIGHT
    )
    section_title_style = ParagraphStyle(
        'SectionTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=12, textColor=DARK_BLUE
    )
    card_title_style = ParagraphStyle(
        'CardTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=PRIMARY
    )
    card_date_style = ParagraphStyle(
        'CardDate', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=13, textColor=MUTED, alignment=TA_RIGHT
    )
    body_style = ParagraphStyle(
        'GlassBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=12.5, textColor=SECONDARY
    )
    bullet_style = ParagraphStyle(
        'GlassBullet', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=12.5, textColor=SECONDARY, leftIndent=10, firstLineIndent=-10
    )

    story = []

    # -------------------------------------------------------------
    # HEADER
    # -------------------------------------------------------------
    hero_left = [
        Paragraph("<b>SURAJ DAS</b>", name_style),
    ]
    hero_right = [
        Paragraph('West Bengal, India &nbsp;|&nbsp; Phone: +91 83360 41207', contact_style),
        Paragraph('Email: <a href="mailto:sun007official@gmail.com" color="#0284c7"><b>sun007official@gmail.com</b></a> &nbsp;|&nbsp; LinkedIn: <a href="https://linkedin.com/in/suraj-das-5801793aa" color="#0284c7"><b>suraj-das</b></a>', contact_style),
        Paragraph('GitHub: <a href="https://github.com/gitsuraj7" color="#0284c7"><b>gitsuraj7</b></a> &nbsp;|&nbsp; Portfolio: <a href="https://portfolio-phi-nine-m7qu98woxl.vercel.app" color="#0369a1"><b>Live Portfolio</b></a>', contact_style)
    ]
    hero_table = Table([[hero_left, hero_right]], colWidths=[240, 316])
    hero_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LINEBELOW', (0,0), (-1,-1), 1.2, ACCENT_BLUE),
    ]))
    story.append(hero_table)
    story.append(Spacer(1, 8))

    def make_section_banner(title):
        p_title = Paragraph(f"<b>{title.upper()}</b>", section_title_style)
        t = Table([[p_title]], colWidths=[FULL_W])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), HEADER_BG),
            ('BOX', (0,0), (-1,-1), 0.8, BORDER_COLOR),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('TOPPADDING', (0,0), (-1,-1), 3.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ]))
        return t

    # -------------------------------------------------------------
    # 1. EDUCATION
    # -------------------------------------------------------------
    story.append(make_section_banner("Education & Academic Performance"))
    story.append(Spacer(1, 5))

    edu_1 = Table([[
        Paragraph("<b>Serampore Vivekananda Academy</b> | Senior Secondary (Class 11–12, Science Stream)", card_title_style),
        Paragraph("2024 – 2026", card_date_style)
    ]], colWidths=[440, 116])
    edu_1.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    edu_2 = Table([[
        Paragraph("<b>Serampore Vivekananda Academy</b> | Secondary (Class 9–10)", card_title_style),
        Paragraph("2022 – 2024", card_date_style)
    ]], colWidths=[440, 116])
    edu_2.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
    
    edu_3 = Table([[
        Paragraph("<b>Baidyabati Sacred Heart</b> | Primary & Middle School (Class 1–8)", card_title_style),
        Paragraph("2014 – 2022", card_date_style)
    ]], colWidths=[440, 116])
    edu_3.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))

    story.append(edu_1)
    story.append(Spacer(1, 2))
    story.append(Paragraph("• <b>Academic Score:</b> Achieved <b>75% Aggregate Score</b> in Higher Secondary Class 12 Board Examinations.", bullet_style))
    story.append(Paragraph("• <b>Science Subjects:</b> Mathematics, Physics, Chemistry, Biology, English, and Physical Education.", bullet_style))
    story.append(Spacer(1, 6))

    story.append(edu_2)
    story.append(Spacer(1, 2))
    story.append(Paragraph("• <b>Academic Score:</b> Achieved <b>89% Overall Aggregate</b> on Class 10 Secondary Board Examinations.", bullet_style))
    story.append(Paragraph("• <b>Mathematics Award:</b> Recognized as the <b>Class Subject Topper in Mathematics</b> for earning the highest marks in class.", bullet_style))
    story.append(Spacer(1, 6))

    story.append(edu_3)
    story.append(Spacer(1, 2))
    story.append(Paragraph("• <b>Medium of Instruction:</b> 100% English Medium schooling completed continuously from Class 1 through Class 12.", bullet_style))
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # 2. PRACTICAL WORKFLOW & LEARNING APPROACH
    # -------------------------------------------------------------
    story.append(make_section_banner("Practical Workflow & Learning Approach"))
    story.append(Spacer(1, 5))

    skills_data = [
        [
            Paragraph("<b>AI-Assisted Building:</b>", body_style), 
            Paragraph("Use modern AI tools (Cursor, Claude, ChatGPT) to generate starter code, structure web layouts, debug errors, and turn ideas into working applications quickly.", body_style)
        ],
        [
            Paragraph("<b>Applied Physics & Math:</b>", body_style), 
            Paragraph("Apply classroom geometry, trigonometry, and vector principles to build interactive 2D graphics, game loops, bounce angles, and surface friction models.", body_style)
        ],
        [
            Paragraph("<b>Web Hosting & Deployment:</b>", body_style), 
            Paragraph("Deploy self-built projects live on the internet using hosting services like Vercel and Firebase so they can be viewed online.", body_style)
        ],
        [
            Paragraph("<b>Code Tracking:</b>", body_style), 
            Paragraph("Organize, update, and publish project source code publicly on GitHub.", body_style)
        ],
    ]
    skills_table = Table(skills_data, colWidths=[140, 416])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # 3. FEATURED PROJECTS
    # -------------------------------------------------------------
    story.append(make_section_banner("Featured Self-Built Projects"))
    story.append(Spacer(1, 5))

    def make_project_entry(title, tag, link, bullets):
        head = Table([[
            Paragraph(f"<b>{title}</b> &nbsp;|&nbsp; <font color='#64748b'>{tag}</font>", card_title_style),
            Paragraph(f"<a href='{link}' color='#0284c7'><b>[ Live Demo ]</b></a>", card_date_style)
        ]], colWidths=[420, 136])
        head.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
        
        elements = [head]
        for bullet in bullets:
            elements.append(Paragraph(f"• {bullet}", bullet_style))
            elements.append(Spacer(1, 2))
        return elements

    # Project 1
    story.extend(make_project_entry(
        "OfferIntel — Job Offer Comparison Tool", 
        "Web Application", 
        "https://offerintel-7fcf6.web.app",
        [
            "<b>What it does:</b> Built a web application designed to help job seekers compare different job offers by looking beyond base salary—evaluating performance bonuses, stock options, health benefits, and growth potential.",
            "<b>How it works:</b> Created input forms and calculation rules that weigh different offer components to produce a clear, side-by-side comparison overview.",
            "<b>Key Feature:</b> Integrated user sign-in so users can securely save their offer calculations and revisit them anytime."
        ]
    ))
    story.append(Spacer(1, 6))

    # Project 2
    story.extend(make_project_entry(
        "FreeStack — Developer Resource Directory", 
        "Web Directory", 
        "https://freestack-sigma.vercel.app",
        [
            "<b>What it does:</b> Created an organized online directory to help beginner coders quickly find useful learning resources, coding templates, and free developer tools.",
            "<b>How it works:</b> Built a instant search bar and category filters (such as Frontend, Backend, Design, and AI tools) for easy browsing.",
            "<b>Key Feature:</b> Published and hosted live on the web for community use."
        ]
    ))

    # PAGE BREAK FOR EXACT 2-PAGE SPREAD
    story.append(PageBreak())

    # Page 2 Heading Continuation
    story.append(make_section_banner("Featured Self-Built Projects (Continued)"))
    story.append(Spacer(1, 6))

    # Project 3
    story.extend(make_project_entry(
        "2D Physics Games (Tank Shooter & Carrom Football)", 
        "Browser Games", 
        "https://tank-pied.vercel.app",
        [
            "<b>What it does:</b> Built two playable 2D arcade games in the browser to experiment with physics formulas and game loops directly on screen.",
            "<b>How it works:</b> Programmed ball bounce angles, surface friction slowdown, trajectory paths, and collision reactions using coordinate math.",
            "<b>Key Feature:</b> Features real-time sound effects and smooth animation movement."
        ]
    ))
    story.append(Spacer(1, 8))

    # Project 4
    story.extend(make_project_entry(
        "Interactive Developer Portfolio & Web Terminal", 
        "Interactive Website", 
        "https://portfolio-phi-nine-m7qu98woxl.vercel.app",
        [
            "<b>What it does:</b> Designed a personal portfolio website featuring both a clean standard web interface and an interactive computer terminal simulation.",
            "<b>How it works:</b> Visitors can type simple commands (like `help` or `projects`) into the terminal box to view project information dynamically.",
            "<b>Key Feature:</b> Includes detailed descriptions of various developer roles and self-built projects."
        ]
    ))
    story.append(Spacer(1, 8))

    # Project 5
    story.extend(make_project_entry(
        "Interactive Web Chess & Online Shop Showcase", 
        "Web Showcase", 
        "https://chess-zeta-henna.vercel.app/",
        [
            "<b>What it does:</b> Built a playable web chess game along with a modern dark-themed online store interface ('Scentscape').",
            "<b>How it works:</b> Programmed basic chess piece rules and move validation so players can make valid chess moves on screen.",
            "<b>Key Feature:</b> Demonstrates clean visual layouts, interactive button controls, and responsive page design."
        ]
    ))
    story.append(Spacer(1, 14))

    # -------------------------------------------------------------
    # 4. ACADEMIC REFERENCES
    # -------------------------------------------------------------
    story.append(make_section_banner("Academic References & Recommendations"))
    story.append(Spacer(1, 6))

    ref_data = [
        [
            Paragraph("<b>Mr. Sarbajit</b>", card_title_style), 
            Paragraph("Mathematics Faculty", body_style),
            Paragraph("Phone: <a href='tel:+919831885664' color='#0284c7'><b>+91 98318 85664</b></a>", card_date_style)
        ],
        [
            Paragraph("<b>Mr. Sadashiv</b>", card_title_style), 
            Paragraph("Physics Faculty", body_style),
            Paragraph("Phone: <a href='tel:+918013436054' color='#0284c7'><b>+91 80134 36054</b></a>", card_date_style)
        ],
        [
            Paragraph("<b>Mrs. Ananna</b>", card_title_style), 
            Paragraph("Chemistry Faculty", body_style),
            Paragraph("Phone: <a href='tel:+918017087317' color='#0284c7'><b>+91 80170 87317</b></a>", card_date_style)
        ],
        [
            Paragraph("<b>Mr. Jisu</b>", card_title_style), 
            Paragraph("English Faculty", body_style),
            Paragraph("Phone: <a href='tel:+918017196649' color='#0284c7'><b>+91 80171 96649</b></a>", card_date_style)
        ]
    ]
    
    ref_table = Table(ref_data, colWidths=[150, 220, 186])
    ref_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor("#f1f5f9")),
        ('BACKGROUND', (0,0), (-1,-1), HEADER_BG),
        ('BOX', (0,0), (-1,-1), 0.8, BORDER_COLOR),
    ]))
    story.append(ref_table)

    # Build primary PDF
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
        onFirstPage=draw_clean_background,
        onLaterPages=draw_clean_background
    )
    print(f"Generated Academic CV: {primary_path}")

    for target in output_paths[1:]:
        shutil.copyfile(primary_path, target)
        print(f"Synced to: {target}")

if __name__ == "__main__":
    generate_academic_cv()
