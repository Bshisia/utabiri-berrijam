from nicegui import ui
from .home_tab import create_home_tab
from .report_tab import create_report_tab
from .summary_tab import create_summary_tab
from .support_tab import create_support_tab


def create_tabs() -> None:
    """Creates main application tab interface with Home, Report, Summary and Support sections.
    
    Creates responsive tab layout with icons and associated content panels.
    Default tab is 'Home'. All tabs span full width using 'w-full' class.
    """
    # Create tabs
    with ui.tabs().classes('w-full') as tabs:
        home_tab = ui.tab('Home', icon='home')
        report_tab = ui.tab('Report', icon='analytics')
        summary_tab = ui.tab('Summary', icon='summarize') 
        support_tab = ui.tab('Support', icon='help')

    # Create tab panels
    with ui.tab_panels(tabs, value='Home').classes('w-full'):
        with ui.tab_panel('Home'):
            create_home_tab(tabs)
        with ui.tab_panel('Report'):
            create_report_tab()
        with ui.tab_panel('Summary'):
            create_summary_tab()
        with ui.tab_panel('Support'):
            create_support_tab()