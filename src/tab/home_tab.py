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
