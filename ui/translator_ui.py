"""Interface gráfica do tradutor multilíngue usando Tkinter."""

import tkinter as tk
from tkinter import ttk
from services.translator import translate_text, detect_language

LANGUAGES = {
    "Inglês": "EN",
    "Português": "PT",
    "Espanhol": "ES",
    "Francês": "FR",
    "Alemão": "DE",
    "Italiano": "IT"
}

def start_ui():
    """
    Inicializa a interface gráfica do tradutor.
    Permite entrada de texto, seleção de idiomas, detecção automática e exibição da tradução.
    """

    def on_translate_click():
        """Callback para o botão 'Traduzir'. Realiza a tradução do texto inserido."""
        text = text_input.get("1.0", tk.END).strip()
        source_language = source_lang_input.get()
        target_language = target_lang_input.get()

        try:
            translated_text = translate_text(text, source_language, target_language)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, translated_text)
        except Exception as e:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, f"Erro: {str(e)}")

    def on_detect_click():
        """Callback para o botão 'Detectar idioma'. Identifica o idioma do texto inserido."""
        text = text_input.get("1.0", tk.END).strip()
        if not text:
            return

        try:
            detected_code = detect_language(text)
            reversed_map = {v: k for k, v in LANGUAGES.items()}
            detected_name = reversed_map.get(detected_code, f"({detected_code})")
            source_lang_input.set(detected_name)
        except Exception as e:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, f"Erro na detecção: {str(e)}")
    
    # Inicialização da janela principal
    app = tk.Tk()
    app.title("TRADUTOR")
    app.geometry("820x480")
    app.resizable(False, False)

    # Título
    title = ttk.Label(app, text="Tradutor Multilíngue", font=("Arial", 16, "bold"))
    title.pack(pady=10)

    # Seção de seleção de idiomas
    selector_frame = ttk.Frame(app)
    selector_frame.pack(pady=5)

    ttk.Label(selector_frame, text="Traduzir de:").grid(row=0, column=1, padx=5)
    source_lang_input = ttk.Combobox(selector_frame, values=list(LANGUAGES.keys()), state="readonly", width=20)
    source_lang_input.current(0)
    source_lang_input.grid(row=0, column=2, padx=5)

    detect_button = ttk.Button(selector_frame, text="Detectar idioma", command=on_detect_click)
    detect_button.grid(row=0, column=0, padx=5)

    ttk.Label(selector_frame, text="Para:").grid(row=0, column=3, padx=5)
    target_lang_input = ttk.Combobox(selector_frame, values=list(LANGUAGES.keys()), state="readonly", width=20)
    target_lang_input.current(1)
    target_lang_input.grid(row=0, column=4, padx=5)

    # Área de entrada e saída de texto
    text_frame = ttk.Frame(app)
    text_frame.pack(padx=10, pady=10)

    text_input = tk.Text(text_frame, height=12, width=45)
    text_input.grid(row=0, column=0, padx=5)

    output_text = tk.Text(text_frame, height=12, width=45, bg="#f0f0f0", state="normal")
    output_text.grid(row=0, column=1, padx=5)

     # Botão de tradução
    translate_button = ttk.Button(app, text="Traduzir", command=on_translate_click)
    translate_button.pack(pady=10)

    app.mainloop()