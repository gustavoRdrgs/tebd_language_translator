import tkinter as tk
from tkinter import ttk
from services.translator import translate_text

def start_ui():
    def on_translate_click():
        text = text_input.get()
        target_language = target_lang_input.get()

        try:
            translated_text = translate_text(text, target_language)
            result_label.config(text=translated_text)
        except Exception as e:
            result_label.config(text=f"Erro: {str(e)}")

    app = tk.Tk()
    app.title("Ferramenta de Tradução de Linguagens")

    ttk.Label(app, text="Text:").grid(column=0, row=0)
    text_input = ttk.Entry(app)
    text_input.grid(column=1, row=0)

    ttk.Label(app, text="Línguagem atual:").grid(column=0, row=1)
    source_lang_input = ttk.Entry(app)
    source_lang_input.grid(column=1, row=1)

    ttk.Label(app, text="Línguagem para tradução:").grid(column=0, row=2)
    target_lang_input = ttk.Entry(app)
    target_lang_input.grid(column=1, row=2)

    ttk.Button(app, text="Traduzir", command=on_translate_click).grid(column=1, row=3)

    result_label = ttk.Label(app, text="")
    result_label.grid(column=0, row=4, columnspan=2)

    app.mainloop()
