import pyttsx3
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

VOICE_MAP = {
    "EN": 2,
    "PT": 0,
}

tts_engine = pyttsx3.init()

def speak(text, lang_code="EN"):
    voices = tts_engine.getProperty('voices')

    if lang_code == "PT":
        voice_index = 0
    else:
        voice_index = 2

    tts_engine.setProperty('voice', voices[voice_index].id)
    tts_engine.say(text)
    tts_engine.runAndWait()

def start_ui():

    def on_translate_click():
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

    # Botões de áudio
    audio_frame = ttk.Frame(app)
    audio_frame.pack()

    listen_input_btn = ttk.Button(
        text_frame,
        text="🔊 Ouvir texto original",
        command=lambda: speak(
            text_input.get("1.0", tk.END).strip(),
            lang_code=LANGUAGES[source_lang_input.get()]
        )
    )
    listen_input_btn.grid(row=1, column=0, sticky="w", padx=5, pady=(2, 0))

    listen_output_btn = ttk.Button(
        text_frame,
        text="🔊 Ouvir tradução",
        command=lambda: speak(
            output_text.get("1.0", tk.END).strip(),
            lang_code=LANGUAGES[target_lang_input.get()]
        )
    )
    listen_output_btn.grid(row=1, column=1, sticky="w", padx=5, pady=(2, 0))

     # Botão de tradução
    translate_button = ttk.Button(app, text="Traduzir", command=on_translate_click)
    translate_button.pack(pady=10)

    app.mainloop()