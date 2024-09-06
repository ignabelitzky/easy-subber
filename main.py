import os
import tkinter as tk
from tkinter import messagebox
from file_dialogs import select_video_file, save_subtitle_file
from conversion import extract_audio
from options import choose_whisper_model, choose_language
from transcription import transcribe_audio

def main():
    # Hide the main Tkinter window
    root = tk.Tk()
    root.withdraw()

    # Select the video file
    video_file = select_video_file()
    if not video_file:
        messagebox.showerror("Error", "No video file selected.")
        return
    
    # Extract audio from the video
    audio_file = "audio.wav"
    success = extract_audio(video_file, audio_file)
    if not success:
        messagebox.showerror("Error", "Audio extraction failed.")
        return
    
    # Choose the Whisper model and language
    model_name = choose_whisper_model()
    language = choose_language()
    if not model_name or not language:
        messagebox.showerror("Error", "Model or language not selected.")
        return
    
    # Select the save location for the subtitle file
    save_path = save_subtitle_file()
    if not save_path:
        messagebox.showerror("Error", "No save location selected.")
        return
    
    # Transcribe the audio and save the subtitles
    transcribe_audio(audio_file, save_path, model_name, language)
    messagebox.showinfo("Success", f"Subtitles saved to {save_path}")

    # Clean up temporary audio file
    os.remove(audio_file)

if __name__ == "__main__":
    main()