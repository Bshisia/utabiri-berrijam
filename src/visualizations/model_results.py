from nicegui import ui

def show_model_results():
    """
    Displays the model performance results in a user-friendly format.
    
    This section presents the analysis results using both technical and simplified terms,
    focusing on the model's ability to predict patient outcomes accurately.
    """
    with ui.card().classes("w-full mx-auto my-4 p-4"):
        ui.label("AI Analysis Performance").classes("text-2xl font-bold mb-4")
        
        with ui.row().classes("w-full gap-4"):
            with ui.card().classes("flex-1 p-4 bg-blue-50"):
                ui.label("Standard Model").classes("text-lg font-bold mb-2")
                ui.label("Accuracy Score: 82.51%").classes("text-3xl font-bold text-blue-600 mb-2")
                ui.label(
                    """This model provides clear explanations for its predictions, 
                    making it easier for medical staff to understand the reasoning 
                    behind each risk assessment."""
                ).classes("text-base text-gray-600")
                
            with ui.card().classes("flex-1 p-4 bg-purple-50"):
                ui.label("Advanced Model").classes("text-lg font-bold mb-2")
                ui.label("Accuracy Score: 90.56%").classes("text-3xl font-bold text-purple-600 mb-2")
                ui.label(
                     """This model uses complex patterns to achieve higher accuracy by analyzing 
                    subtle relationships in patient data. It offers enhanced prediction capabilities for 
                    complex cases."""
                ).classes("text-base text-gray-600")
        
        with ui.card().classes("w-full mt-4 p-4 bg-gray-50"):
            ui.label("About the Analysis").classes("text-lg font-bold mb-2")
            ui.html("""
                <div class="text-base text-gray-600">
                    <p class="mb-2">Our system evaluated 426 different analytical approaches to find the most reliable 
                    methods for predicting patient outcomes. We present two top-performing approaches:</p>
                    <ul class="list-disc pl-5">
                        <li class="mb-1">The <b>Standard Model</b> prioritizes clear, 
                        explainable results that medical staff can easily verify and understand.</li>
                        <li class="mb-1">The <b>Advanced Model</b> uses sophisticated 
                        techniques to achieve even higher accuracy, though with less transparent reasoning.</li>
                    </ul>
                    <p class="mt-2"><i>Note: These scores represent the models' ability to accurately 
                    predict patient outcomes based on historical data.</i></p>
                </div>
            """)
