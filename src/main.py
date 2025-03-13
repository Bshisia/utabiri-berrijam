from nicegui import ui
from tab.create_tab import create_tabs

if __name__ in {"__main__", "__mp_main__"}:
    create_tabs()
    ui.run(title="Heart Attack Mortality Dashboard")
