from nicegui import ui
from .home_tab import create_home_tab
from .report_tab import create_report_tab
from .summary_tab import create_summary_tab
from .support_tab import create_support_tab
from .footer import create_footer


def create_tabs() -> None:
    """Creates main application tab interface with Home, Report, Summary and Support sections.
    
    Creates responsive tab layout with icons and associated content panels.
    Default tab is 'Home'. All tabs span full width using 'w-full' class.
    """
    
    with ui.header().classes('w-full flex items-center bg-blue-900 text-white px-4 py-2'):
        
        with ui.tabs().classes('w-full flex justify-end h-12') as tabs:
            for icon, label in [
                ('home', 'Home'),
                ('analytics', 'Report'),
                ('summarize', 'Summary'),
                ('help', 'Support')
            ]:
                with ui.tab(label, icon=icon).classes('hover:bg-blue-800 text-md border-b-2 border-transparent [&.active]:border-white'):
                    ui.icon(icon, size='24px').classes('mr-2')
                    ui.label(label).classes('text-md')

    with ui.tab_panels(tabs, value='Home').classes('w-full'):
        with ui.tab_panel('Home'):
            create_home_tab(tabs)
        with ui.tab_panel('Report'):
            create_report_tab()
        with ui.tab_panel('Summary'):
            create_summary_tab()
        with ui.tab_panel('Support'):
            create_support_tab()
    
    create_footer()
