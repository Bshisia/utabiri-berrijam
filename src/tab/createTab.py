from nicegui import ui

def create_tabs():
    # Create tabs
    with ui.tabs().classes('w-full') as tabs:
        home_tab = ui.tab('Home', icon='home')
        report_tab = ui.tab('Report', icon='analytics')
        summary_tab = ui.tab('Summary', icon='summarize')
        support_tab = ui.tab('Support', icon='help')
    

