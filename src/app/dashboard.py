from nicegui import ui
from datetime import datetime
from data.loader import load_data, create_age_groups
from data.preview import show_data_preview
from visualizations.key_factors import show_key_factors
from visualizations.combined_factors import show_combined_risk_factors
from visualizations.risk_distribution import show_risk_distribution
from visualizations.model_results import show_model_results
from filters.filters import add_interactive_filters
from advanced_visualization.advanced_visualizations import add_advanced_visualizations

def create_collapsible_card(title, content_func, initially_expanded=True):
    """
    Creates a collapsible card with a title and content.
    
    Args:
        title (str): The card title
        content_func (callable): Function that creates the card content
        initially_expanded (bool): Whether the card should start expanded
    Returns:
        Any: The return value of content_func
    """
    card = ui.card().classes('w-full mb-4 transition-shadow hover:shadow-xl')
    
    with ui.row().classes('w-full items-center p-4 cursor-pointer bg-gray-50') as header:
        ui.label(title).classes('text-xl font-bold flex-grow')
        expand_icon = ui.icon('expand_more' if initially_expanded else 'expand_less')
    
    with ui.column().classes('w-full p-4') as content:
        pass  
        
    content.visible = initially_expanded
    
    with content:
        result = content_func()
    
    def toggle():
        content.visible = not content.visible
        expand_icon.props(f'icon={"expand_less" if content.visible else "expand_more"}')
    
    header.on('click', toggle)
    
    return result
def add_floating_buttons():
    with ui.element('div').classes('fixed bottom-24 right-6 flex flex-col gap-2 z-50'):
        ui.button(icon='arrow_upward', on_click=lambda: ui.run_javascript('window.scrollTo({top: 0, behavior: "smooth"});')).props('round color=primary')
        ui.button(icon='arrow_downward', on_click=lambda: ui.run_javascript('window.scrollTo({top: document.body.scrollHeight, behavior: "smooth"});')).props('round color=primary')
def create_report_info():
    """Creates the report information section with key details."""
    
    with ui.card().classes('w-full mb-4 bg-blue-50 transition-shadow hover:shadow-xl'):
        with ui.column().classes('p-4 gap-3'):  
            with ui.row().classes('items-center gap-3'):  
                ui.icon('local_hospital', size='24px').classes('text-blue-600')  
                ui.label('Industry:').classes('font-bold text-gray-700 text-lg')  
                ui.label('Healthcare Services').classes('text-gray-600 text-lg')
            
            with ui.row().classes('items-center gap-3'):
                ui.icon('folder', size='24px').classes('text-blue-600') 
                ui.label('Dataset:').classes('font-bold text-gray-700 text-lg')
                ui.label('Heart Attack Mortality Analysis').classes('text-gray-600 text-lg')
            
            with ui.row().classes('items-center gap-3'):
                ui.icon('calendar_today', size='24px').classes('text-blue-600')
                ui.label('Analysis Date:').classes('font-bold text-gray-700 text-lg')
                ui.label(datetime.now().strftime('%Y-%m-%d')).classes('text-gray-600 text-lg')
            
            with ui.row().classes('items-center gap-3'):
                ui.icon('analytics', size='24px').classes('text-blue-600') 
                ui.label('Target Variable:').classes('font-bold text-gray-700 text-lg')
                ui.label('Mortality (Patient Outcome)').classes('text-gray-600 text-lg')
            with ui.row().classes('items-center mb-4'):
                ui.icon('help_outline') \
                  .tooltip('Click for help') \
                  .props('aria-label="Help"') \
                  .classes('text-primary cursor-pointer transition-colors hover:text-primary-dark ml-2') \
                  .on('click', lambda: ui.open('help-modal'))
                ui.link('Help me understand this page', 'https://drive.google.com/file/d/1tQJNTrzI2eftTHTMtejS6q3XTDKoufjN/view?usp=sharing').classes('text-blue-1000 text-lg font-medium hover:underline').props('target=_blank')               


def init_dashboard():
    """
    Initialize the dashboard with collapsible preview and non-collapsible filters section.
    """
    try:
        df = load_data()
        if df is not None:
            df = create_age_groups(df)

            with ui.column().classes("w-full gap-4") as main_container:
                create_report_info()
                
                filters_section = ui.column().classes("w-full")
                
                results_section = ui.column().classes("w-full")
                
                with filters_section:
                    ui.label("Filters").classes("text-xl font-bold mt-4")
                    age_filter, gender_filter, anion_filter, renal_filter = (
                        add_interactive_filters(df, results_section)
                    )
                with results_section:
                    create_collapsible_card(
                        f"Data Preview ({len(df)} patients)", 
                        lambda: show_data_preview(df),
                        initially_expanded=True
                    )
                    
                    with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                        ui.label("Overview").classes("text-xl font-bold p-4 bg-gray-50")
                        with ui.column().classes("w-full p-4"):
                            show_key_factors(df)
                    
                    with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                        ui.label("Combined Risk Factors").classes("text-xl font-bold p-4 bg-gray-50")
                        with ui.column().classes("w-full p-4"):
                            show_combined_risk_factors(df)
                    
                    with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                        ui.label("Risk Distribution").classes("text-xl font-bold p-4 bg-gray-50")
                        with ui.column().classes("w-full p-4"):
                            show_risk_distribution(df)
                    
                    with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                        ui.label("Advanced Visualizations").classes("text-xl font-bold p-4 bg-gray-50")
                        with ui.column().classes("w-full p-4"):
                            add_advanced_visualizations(df)
                    
                    ui.separator().classes("my-8")
                    
                    with ui.card().classes("w-full mb-4 transition-shadow hover:shadow-xl"):
                        ui.label("Model Results").classes("text-xl font-bold p-4 bg-gray-50")
                        with ui.column().classes("w-full p-4"):
                            show_model_results()

                add_floating_buttons()
                return main_container, (age_filter, gender_filter, anion_filter, renal_filter)
                
    except Exception as ex:
        ui.notify(f"Error initializing dashboard: {ex}", type="negative")
        print(f"Dashboard initialization error: {ex}")
        return None, None
