import tkinter as tk

def choose_whisper_model():
    """Prompt the user to choose a Whisper model using a dropdown menu."""
    models = ["tiny", "base", "small", "medium", "large"]

    # Create a Tkinter window
    model_window = tk.Tk()
    model_window.title("Choose a Whisper Model")
    model_var = tk.StringVar(value="large")
    tk.Label(model_window, text="Select a Whisper model").pack(pady=10)
    model_menu = tk.OptionMenu(model_window, model_var, *models)
    model_menu.pack(pady=10)
    tk.Button(model_window, text="Select", command=model_window.quit).pack(pady=10)
    model_window.mainloop()
    selected_model = model_var.get()
    model_window.destroy()
    return selected_model

def choose_language():
    """Prompt the user to choose the video language using a dropdown menu."""
    languages = ["English", "Spanish", "French", "German", "Italian"]

    # Create a Tkinter window
    language_window = tk.Tk()
    language_window.title("Choose a Language")
    language_var = tk.StringVar(value="English")
    tk.Label(language_window, text="Select the video language").pack(pady=10)
    language_menu = tk.OptionMenu(language_window, language_var, *languages)
    language_menu.pack(pady=10)
    tk.Button(language_window, text="Select", command=language_window.quit).pack(pady=10)
    language_window.mainloop()
    selected_language = language_var.get()
    language_window.destroy()
    return selected_language