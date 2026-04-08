from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_report(insights):
    doc = SimpleDocTemplate("report.pdf")

    elements = []

    for i in insights:
        elements.append(Paragraph(i))

    doc.build(elements)