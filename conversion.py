import os
import ffmpeg
import subprocess

def extract_audio(video_file, output_audio_file):
    """Extracts audio from a video file and saves it as a WAV file.

    Args:
        video_file (str): The path to the video file.
        output_audio_file (str): The path to save the audio file.

    Returns:
        bool: True if the audio extraction was successful, False otherwise.
    """
    try:
        # Construct the ffmpeg command to extract audio
        command = [
            'ffmpeg',
            '-i', video_file,    # Input video file
            '-vn',                # Disable video recording
            '-ac', '1',           # Set audio channels to mono
            '-ar', '16000',       # Set audio sampling rate to 16 kHz
            '-acodec', 'pcm_s16le',  # Set audio codec to PCM 16-bit little-endian
            output_audio_file    # Output audio file
        ]

        # Run the ffmpeg command
        subprocess.run(command, check=True)
        print(f"Audio extracted successfully to {output_audio_file}")
        return True
    
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio: {e}")
        return False