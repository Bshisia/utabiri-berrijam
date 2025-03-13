from nicegui import ui

def create_home_tab(tabs):
    with ui.column().classes('w-full items-center gap-4 p-4'):

        # Header Section
        ui.label("Heart Attack Mortality Analysis").classes('text-3xl font-bold text-center')

        # Goal Section
        with ui.card().classes('w-full max-w-3xl'):
            ui.label("Goal").classes('text-xl font-bold mb-2')
            ui.label("Understand and predict Heart Attack mortality patterns to improve patient outcomes").classes('text-lg')

        # Why Section
        with ui.card().classes('w-full max-w-3xl'):
            ui.label("Why It Matters").classes('text-xl font-bold mb-2')
            ui.label("""Accurately triaging patients and reducing time to treatment can save lives. 
                    Early identification of high-risk patients enables faster intervention and better outcomes."""
            ).classes('text-lg')

        # Key Findings Section
        with ui.card().classes('w-full max-w-3xl bg-blue-50'):
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
        # Industry Section
        with ui.card().classes('w-full max-w-3xl'):
            ui.label("Industry Application").classes('text-xl font-bold mb-2')
            with ui.row().classes('gap-2 flex-wrap'):
                for industry in ['ICU', 'Blood-works', 'Medical', 'Research']:
                    ui.badge(industry).props('outline').classes('text-lg')

        # Quick Navigation Section
        with ui.card().classes('w-full max-w-3xl'):
            ui.label("Quick Navigation").classes('text-xl font-bold mb-2')
            with ui.row().classes('gap-4 justify-center'):
                ui.button('View Full Report', 
                         icon='analytics',
                         on_click=lambda: tabs.set_value('Report')
                         ).props('color=primary')
                
                ui.button('View Summary', 
                         icon='summarize',
                         on_click=lambda: tabs.set_value('Summary')
                         ).props('color=secondary')
                
                ui.button('Get Support', 
                         icon='help',
                         on_click=lambda: tabs.set_value('Support')
                         ).props('outline')
