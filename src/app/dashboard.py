import ui
from data.loader import load_data, create_age_groups
from data.preview import show_data_preview


def init_dashboard():
    """
    Initialize the dashboard.

    This function loads the data, creates age groups, and sets up the UI components
    for displaying the data preview and results section.
    """
    df = load_data()
    if df is not None:
    
        df = create_age_groups(df)

        with ui.column().classes("w-full"):

            global results_section
            results_section = ui.column().classes("w-full")
            
            with results_section:
                show_data_preview(df)
