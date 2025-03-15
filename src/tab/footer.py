from nicegui import ui

def create_footer() -> None:
    """Creates footer with copyright."""
    with ui.footer().classes('w-full bg-blue-900 text-white p-4 mt-auto'):
        with ui.column().classes('max-w-6xl mx-auto items-center'):
            ui.label('© 2025 Berrijam AI Analysis. All rights reserved.').classes('text-sm text-center')