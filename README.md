# EasySubber

EasySubber is a Python-based tool that allows you to generate `.srt` subtitle files from video files in various formats (e.g., `.mkv`, `.mp4`, `.avi`). It utilizes OpenAI's Whisper model for speech-to-text transcription, FFmpeg for audio extraction, and Tkinter for a simple graphical user interface (GUI).

## Features

- Supports a variety of video formats: `.mkv`, `.mp4`, `.avi`, etc.
- Automatically creates subtitles in the `.srt` format.
- Whisper model provides high quality speech recognition.
- GUI interface built with Tkinter for ease of use.
- Uses FFmpeg to efficiently extract audio from video files.

## Requirements

Before using EasySubber, make sure you have the following installed:

- **Python 3.x**
- [Whisper](https://github.com/openai/whisper)
- **FFmpeg**
- **Tkinter** (tipically included with Python)

Install the required Python packages:

```bash
pip install whisper ffmpeg-python tkinter
```

To install FFmpeg:
- **Windows**: [FFmpeg Windows Installation Guide](https://ffmpeg.org/download.html#build-windows)
- **Linux**: `sudo apt install ffmpeg`
- **macOS**: `brew install ffmpeg`

## Usage

1. Clone the repository:
```bash
git clone https://github.com/ignabelitzky/easy-subber.git
cd easy-subber
```
2. Run the program:
```
python main.py
```
3. Select the video file you want to process.
4. EasySubber will generate an `.srt` subtitle file in the same directory as the video.

## How It Works

1. **File Selection**: Use the Tkinter GUI to select a video file.
2. **Audio Extraction**: FFmpeg extracts the audio track from the video.
3. **Transcription**: Whisper transcribes the audio into text.
4. **Subtitle Creation**: The transcription is formatted into `.srt` subtitles with proper timestamps.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve EasySubber.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE). You can find the full text of the license here [LICENSE](LICENSE).
