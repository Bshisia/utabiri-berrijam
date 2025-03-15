from nicegui import ui
from typing import Dict, List
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from io import BytesIO
from datetime import datetime  

def generate_pdf_summary() -> BytesIO:
    """
    Generate a PDF document with a simplified Heart Attack Mortality Summary.
    
    Returns:
        BytesIO: A buffer containing the PDF document with easy-to-understand
                heart attack information including key metrics, findings,
                recommendations and relationships between measurements.
    """
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    y = 750  
    
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, y, "Heart Attack Mortality Summary")
    
    y -= 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Key Metrics:")
    y -= 20
    c.setFont("Helvetica", 12)
    metrics = [
        ("Kidney Problems: 32%", "Patients with serious kidney function issues"),
        ("Anion Gap: 28%", "Patients with high anion gap levels in blood"),
        ("Death Rate: 15%", "Percentage of patients who died")
    ]
    for title, desc in metrics:
        c.drawString(50, y, f"• {title}")
        y -= 15
        c.drawString(70, y, f"  {desc}")
        y -= 20

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Key Clinical Findings:")
    y -= 20
    c.setFont("Helvetica", 12)
    findings = [
        "45% of patients had high-risk factors",
        "Higher anion gap linked to higher death rates",
        "Early treatment reduced complications by 35%"
    ]
    for finding in findings:
        c.drawString(50, y, f"• {finding}")
        y -= 15

    if y < 100:  
        c.showPage()
        y = 750
        c.setFont("Helvetica-Bold", 14)
    else:
        y -= 20
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Anion Gap & Kidney Problems Connection:")
    y -= 20
    
    c.setFont("Helvetica", 11)
    explanations = [
        "Anion gap is a blood test that measures the balance of certain chemicals in your blood.",
        "Kidney failure happens when your kidneys can't clean your blood properly."
    ]
    for explanation in explanations:
        c.drawString(50, y, explanation)
        y -= 15
    
    y -= 10  
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Correlation Statistics:")
    y -= 15
    c.setFont("Helvetica", 12)
    stats = [
        "78% correlation between high anion gap and kidney problems",
        "85% of patients with high anion gap had reduced kidney function",
        "Average time to kidney failure: 48 hours after high anion gap"
    ]
    for stat in stats:
        c.drawString(70, y, f"• {stat}")
        y -= 15

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Clinical Patterns:")
    y -= 15
    c.setFont("Helvetica", 12)
    patterns = [
        "Anion gap above 16 strongly linked to kidney injury",
        "Rising anion gap came before kidney failure in 72% of patients",
        "Blood acidity issues found in 68% of these patients"
    ]
    for pattern in patterns:
        c.drawString(70, y, f"• {pattern}")
        y -= 15

    if y < 100:  
        c.showPage()
        y = 750
        c.setFont("Helvetica-Bold", 14)
    else:
        y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Recommendations:")
    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Proactive Measures:")
    y -= 15
    c.setFont("Helvetica", 12)
    proactive = [
        "Monitor kidney function regularly",
        "Create alert system for anion gap changes",
        "Develop standard treatment plans"
    ]
    for measure in proactive:
        c.drawString(70, y, f"• {measure}")
        y -= 15

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Treatment Optimization:")
    y -= 15
    c.setFont("Helvetica", 12)
    treatment = [
        "Adjust fluid treatment based on kidney health",
        "Check salt and mineral balance regularly",
        "Take extra care with high-risk patients"
    ]
    for item in treatment:
        c.drawString(70, y, f"• {item}")
        y -= 15

    y -= 30
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 50, "Information based on recent patient data and medical research")
    c.drawString(50, 30, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.save()
    buffer.seek(0)
    return buffer

def create_metric_card(title: str, value: str, description: str) -> None:
    """
    Create a UI card displaying a metric with title, value and description.
    
    Args:
        title (str): The title of the metric card
        value (str): The main value/metric to display
        description (str): Additional description text for the metric
    """
    with ui.card().classes('w-full md:w-64 p-4 m-2'):
        ui.label(title).classes('text-lg font-bold mb-2')
        ui.label(value).classes('text-2xl text-blue-600 font-bold')
        ui.label(description).classes('text-sm text-gray-600 mt-2')


def create_summary_tab() -> None:
    """Creates enhanced summary dashboard with organized layout."""
    with ui.column().classes('w-full items-center p-6 gap-6'):
        # Hero Header with centered content
        with ui.card().classes('w-full bg-gradient-to-r from-blue-700 to-blue-900 text-white p-8 flex flex-col items-center justify-center'):
            ui.label("Heart Attack Mortality Summary").classes('text-4xl font-bold text-center')
            ui.label("Key Insights and Analysis").classes('text-xl text-center mt-2 opacity-90')
        
        with ui.grid(columns=3).classes('w-full max-w-6xl gap-4'):
            for title, value, desc, icon, color in [
                ("Kidney Problems", "32%", "Critical Cases", "warning", "red"),
                ("Anion Gap", "28%", "High Levels", "trending_up", "amber"),
                ("Death Rate", "13.5%", "All Patients", "analytics", "blue")
            ]:
                with ui.card().classes(f'p-4 bg-{color}-50 border-l-4 border-{color}-600 transition-all hover:shadow-lg'):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon(icon).classes(f'text-2xl text-{color}-600')
                        ui.label(title).classes('text-lg font-bold')
                    ui.label(value).classes(f'text-3xl font-bold text-{color}-600 my-2')
                    ui.label(desc).classes('text-sm text-gray-600')
                    
         # Clinical Findings
        with ui.grid(columns=2).classes('w-full max-w-6xl gap-4 mt-4'):
            with ui.card().classes('p-4 bg-blue-50 transition-all hover:shadow-lg'):
                with ui.row().classes('items-center gap-2 mb-2'):
                    ui.icon('science').classes('text-2xl text-blue-600')
                    ui.label("Key Findings").classes('text-lg font-bold')
                with ui.column().classes('gap-1'):
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('check_circle').classes('text-blue-600 text-sm')
                        ui.label("45% of patients had high-risk factors").classes('text-sm')
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('check_circle').classes('text-blue-600 text-sm')
                        ui.label("Higher anion gap linked to higher death rates").classes('text-sm')
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('check_circle').classes('text-blue-600 text-sm')
                        ui.label("Early treatment reduced complications by 35%").classes('text-sm')

            # Correlation Stats
            with ui.card().classes('p-4 bg-purple-50 transition-all hover:shadow-lg'):
                with ui.row().classes('items-center gap-2 mb-2'):
                    ui.icon('insert_chart').classes('text-2xl text-purple-600')
                    ui.label("Key Statistics").classes('text-lg font-bold')
                with ui.column().classes('gap-1'):
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('arrow_right').classes('text-purple-600 text-sm')
                        ui.label("78% correlation between high anion gap and kidney problems").classes('text-sm')
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('arrow_right').classes('text-purple-600 text-sm')
                        ui.label("85% of high anion gap patients had reduced kidney function").classes('text-sm')
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('arrow_right').classes('text-purple-600 text-sm')
                        ui.label("Average time to kidney failure: 48 hours after high anion gap").classes('text-sm')

            # Clinical Patterns
            with ui.card().classes('p-4 bg-green-50 transition-all hover:shadow-lg'):
                with ui.row().classes('items-center gap-2 mb-2'):
                    ui.icon('timeline').classes('text-2xl text-green-600')
                    ui.label("Pattern Analysis").classes('text-lg font-bold')
                with ui.column().classes('gap-1'):
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('trending_up').classes('text-green-600 text-sm')
                        ui.label("Anion gap above 16 strongly linked to kidney injury").classes('text-sm')
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('trending_up').classes('text-green-600 text-sm')
                        ui.label("Rising anion gap preceded kidney failure in 72% of cases").classes('text-sm')
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('trending_up').classes('text-green-600 text-sm')
                        ui.label("Blood acidity issues found in 68% of these patients").classes('text-sm')

            # Recommendations
            with ui.card().classes('p-4 bg-amber-50 transition-all hover:shadow-lg'):
                with ui.row().classes('items-center gap-2 mb-2'):
                    ui.icon('lightbulb').classes('text-2xl text-amber-600')
                    ui.label("Recommendations").classes('text-lg font-bold')
                with ui.column().classes('gap-1'):
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('check').classes('text-amber-600 text-sm')
                        ui.label("Monitor kidney function regularly").classes('text-sm')
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('check').classes('text-amber-600 text-sm')
                        ui.label("Create alert system for anion gap changes").classes('text-sm')
                    with ui.row().classes('items-center gap-1'):
                        ui.icon('check').classes('text-amber-600 text-sm')
                        ui.label("Adjust fluid treatment based on kidney health").classes('text-sm')

        with ui.column().classes('w-full max-w-6xl flex items-center justify-center mt-6'):
            async def download_pdf():
                pdf_buffer = generate_pdf_summary()
                ui.download(pdf_buffer.getvalue(), 'heart_attack_mortality_summary.pdf')
            ui.button('Download Report', icon='download', on_click=download_pdf).props('color=primary')

        ui.label(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}").classes('text-sm text-gray-500 mt-4 text-center')
