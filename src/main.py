from nicegui import ui

def greet():
    name = name_input.value
    ui.notify(f'Hello, {name}!')

ui.label('Enter your name:')
name_input = ui.input(placeholder='Your name...')
ui.button('Greet Me', on_click=greet)

ui.run()
