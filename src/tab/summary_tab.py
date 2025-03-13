from nicegui import ui

def create_summary_tab() -> None:
    """Creates the summary tab with key findings and recommendations.
    
    Displays project insights and actionable recommendations in a
    responsive grid layout using cards and labels.
    """
    with ui.column().classes('w-full items-center p-4'):
        ui.label("Summary - Coming Soon").classes('text-2xl font-bold')
        ui.label("This section will contain key findings and recommendations.").classes('text-lg')