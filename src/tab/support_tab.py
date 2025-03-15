from nicegui import ui

specified_responses = {
    "How can I get support?": "You can get support by contacting our support team at support.utabiri@gmail.com.",
    "How do I generate a report?": "To generate a report, navigate to the 'Report' tab and click on the 'Generate Report' button.",
    "What is the summary section for?": "The summary section contains key findings and recommendations based on the data analysis.",
    "How do I use the dashboard?": "The dashboard provides various visualizations of the data. You can interact with the charts and graphs to explore the data further.",
    "What is the purpose of this project?": "This project aims to provide a comprehensive analysis of the data, generate reports, and offer support through a virtual assistant.",
    "What is anion gap?": "The anion gap is a value calculated from the results of an electrolyte blood test. It is used to identify the cause of metabolic acidosis, a condition where there is too much acid in the body.",
    "What is renal failure?": "Renal failure, also known as kidney failure, occurs when the kidneys are no longer able to filter waste products from the blood effectively.",
    "How can I prevent heart attacks?": "Preventing heart attacks involves maintaining a healthy lifestyle, including regular exercise, a balanced diet, avoiding smoking, and managing stress and medical conditions like hypertension and diabetes.",
    "How does anion gap increase mortality rate?": "An increased anion gap indicates severe metabolic acidosis, which is associated with higher mortality rates.",
    "What causes an increased anion gap?": "An increased anion gap can be caused by conditions such as diabetic ketoacidosis, lactic acidosis, and renal failure.",
    "How is anion gap calculated?": "The anion gap is calculated using the formula: [Na+] - ([Cl-] + [HCO3-]).",
    "What is a normal anion gap value?": "A normal anion gap value typically ranges from 8 to 16 mEq/L."
}

def get_chatbot_response(question):
    return specified_responses.get(question, "")

def on_question_click(question):
    chat_container.clear()
    response = get_chatbot_response(question)
    with chat_container:
        ui.html(f'<div class="user-message">You: {question}</div>')
        ui.html(f'<div class="bot-message">UtabiriBot: {response}</div>')

def create_support_tab() -> None:
    with ui.column().classes('support-container'):
        with ui.column().classes('chat-panel'):
            ui.label("Chat with UtabiriBot").classes('text-xl font-bold mb-4 text-center')
            global chat_container
            chat_container = ui.column().classes('chat-messages')
            with chat_container:
                ui.html('<div class="initial-bot-message">Select a question below to chat with UtabiriBot</div>')

        with ui.column().classes('questions-panel'):
            for question in specified_responses.keys():
                ui.button(question, on_click=lambda q=question: on_question_click(q)).classes('question-card')

results_container = ui.column().classes("w-full items-center mt-4")

ui.add_head_html('''
<style>
    .support-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        gap: 20px;
        padding: 20px;
    }
  .questions-panel {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        width: 100%;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        gap: 15px;
    }

    .question-card {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #f1f1f1;
        border-radius: 8px;
        padding: 15px;
        height: 70px;
        text-align: center;
        font-size: 16px;
        font-weight: 500;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: all 0.2s ease;
    }

    .chat-panel {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        background-color: #f9fafb;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        height: 300px;
    }

    .chat-messages {
        width: 100%;
        height: 400px;
        overflow-y: auto;
        padding: 10px;
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        padding-left: 10px;
    }

    .user-message {
        background-color: #3b82f6;
        color: white;
        padding: 8px 12px;
        border-radius: 8px;
        margin-left: 0;
        margin-bottom: 8px;
        padding-left: 10px;
    }

    .bot-message {
        background-color: #10b981;
        color: white;
        padding: 8px 12px;
        border-radius: 8px;
        max-width: 70%;
        margin-bottom: 8px;
        padding-right: 10px;
        margin-left: 800px;
        margin-right: 0;
    }

    .initial-bot-message {
        background-color: #ffcc00;
        color: black;
        padding: 8px 12px;
        border-radius: 8px;
        max-width: 70%;
        margin-bottom: 8px;
        padding-right: 10px;
        margin-left: 700px;
        margin-right: auto;
    }
</style>
''')