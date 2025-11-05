def on_button_click(callback):
    print("Button was clicked")
    callback()
def show_message():
    print("Hello Harshal")



on_button_click(show_message)