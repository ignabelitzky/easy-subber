import tkinter as tk
from tkinter import filedialog

def select_video_file():
    """Open a file dialog to select a video file."""
    video_file_dialog = filedialog.askopenfilename(
        title="Select a video file",
        filetypes=[("Video files", "*.mp4 *.avi *.mkv")]
    )
    return video_file_dialog

def save_subtitle_file():
    """Open a file dialog to select the save location."""
    save_path = filedialog.asksaveasfilename(
        title="Save Subtitle As",
        defaultextension=".srt",
        filetypes=[("Subtitle files", "*.srt")]
    )
    return save_path
