from nicegui import ui
from app.dashboard import init_dashboard


def create_report_tab():
    """Creates the report tab content with dashboard and visualizations"""

    try:
        with ui.column().classes("w-full p-4"):
            with ui.row().classes("items-center mb-4"):
                ui.label("Patient Risk Analysis Dashboard").classes(
                    "text-2xl font-bold mb-2"
                )
            results_section, filters = init_dashboard()

            if not results_section or not filters:
                ui.label("Error loading dashboard content").classes("text-red-500")
                return

    except Exception as ex:
        ui.notify(f"Error creating report tab: {ex}", type="negative")
        ui.label("Failed to load dashboard").classes("text-red-500")
