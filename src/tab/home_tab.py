from nicegui import ui
from typing import Any
from data.upload_csv import setup_data_upload

INDUSTRY_ICONS = {
    'ICU': 'local_hospital',
    'Blood-works': 'science', 
    'Medical': 'medical_services',
    'Research': 'biotech'
}

def create_home_tab(tabs: Any) -> None:
    """Creates home dashboard with navigation and key sections."""
    with ui.column().classes('w-full items-center gap-6 p-6 bg-gradient-to-r from-gray-100 to-blue-50'):
        with ui.card().classes('w-full bg-gradient-to-r from-blue-700 to-blue-900 text-white p-6'):
            with ui.column().classes('items-center justify-center w-full'):  
                ui.label("Heart Attack Mortality Analysis").classes('text-4xl font-bold text-center mb-4')
                ui.label("Advanced insights to improve patient outcomes").classes('text-xl text-center mb-6') 
                
                with ui.row().classes('gap-4 justify-center w-full'): 
                    ui.button('Watch Demo', icon='smart_display').props('outline color=white').on('click', lambda: ui.run_javascript('window.open("https://drive.google.com/file/d/1fvf65c2mcjzwv78j0GvjrOLiOuISfaZU/view?usp=sharing", "_blank")'))

            setup_data_upload()

        with ui.grid(columns=2).classes('w-full max-w-6xl gap-6'):
            with ui.card().classes('p-6 transition-shadow hover:shadow-xl'):
                ui.label("Goal").classes('text-xl font-bold mb-2')
                ui.label("Understand and predict Heart Attack mortality patterns to improve patient outcomes").classes('text-lg')

            with ui.card().classes('p-6 transition-shadow hover:shadow-xl'):
                ui.label("Why It Matters").classes('text-xl font-bold mb-2')
                ui.label("""Accurately triaging patients and reducing time to treatment can save lives. 
                        Early identification of high-risk patients enables faster intervention and better outcomes."""
                ).classes('text-lg')

        with ui.grid(columns=2).classes('w-full max-w-6xl gap-6'):
            with ui.card().classes('p-6 bg-blue-50 transition-shadow hover:shadow-xl'):
                ui.label("Key Findings").classes('text-xl font-bold mb-2')
                ui.html("""
                    <div class="text-lg">
                        <p>Berrijam AI's analysis of ICU data on heart failure patients revealed:</p>
                        <ul class="list-disc pl-5 mt-2">
                            <li>Two critical mortality indicators identified:
                                <ul class="list-circle pl-5">
                                    <li>Anion Gap</li>
                                    <li>Renal Failure</li>
                                </ul>
                            </li>
                            <li>These factors can increase mortality risk by approximately 2x</li>
                            <li>The combination of both factors presents the highest risk</li>
                        </ul>
                    </div>
                """)

            with ui.card().classes('p-6 transition-shadow hover:shadow-xl'):
                ui.label("Industry Application").classes('text-xl font-bold mb-2')
                with ui.row().classes('gap-2 flex-wrap'):
                    for industry, icon in INDUSTRY_ICONS.items():
                        with ui.badge().props('outline').classes('text-lg p-2'):
                            ui.icon(icon).classes('mr-2')
                            ui.label(industry)

    with ui.column().classes('w-full flex items-center justify-center'):
        with ui.grid(columns=3).classes('w-full max-w-6xl gap-6 mt-8'):
            # Report Story
            with ui.card().classes('p-6 transition-shadow hover:shadow-xl h-full').on('click', lambda: tabs.set_value('Report')):
                with ui.column().classes('gap-4 items-center text-center cursor-pointer'):
                    ui.icon('analytics').classes('text-4xl text-blue-600')
                    ui.label("Interactive Reports").classes('text-xl font-bold')
                    ui.label("""Access detailed analytical reports from your uploaded data. 
                            Interact with charts and visualizations to gain deeper insights.""").classes('text-lg')
            
            # Summary Story
            with ui.card().classes('p-6 transition-shadow hover:shadow-xl h-full').on('click', lambda: tabs.set_value('Summary')):
                with ui.column().classes('gap-4 items-center text-center cursor-pointer'):
                    ui.icon('summarize').classes('text-4xl text-green-600')
                    ui.label("Quick Summary").classes('text-xl font-bold')
                    ui.label("""Get a concise overview of your data without diving into 
                            complex reports. Perfect for quick insights.""").classes('text-lg')
            
            # Support Story
            with ui.card().classes('p-6 transition-shadow hover:shadow-xl h-full').on('click', lambda: tabs.set_value('Support')):
                with ui.column().classes('gap-4 items-center text-center cursor-pointer'):
                    ui.icon('support_agent').classes('text-4xl text-purple-600')
                    ui.label("AI Support Assistant").classes('text-xl font-bold')
                    ui.label("""Have questions? Our AI assistant can help with 
                            data interpretation and analysis.""").classes('text-lg')