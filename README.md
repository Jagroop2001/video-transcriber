# YouTube Video Transcriber

This is a Streamlit application that allows you to fetch and transcribe the content of a YouTube video using the YouTube Data API and YouTube Transcript API.

## Features
- Extracts the video ID from a YouTube URL.
- Fetches the title and description of the YouTube video using the YouTube Data API.
- Retrieves and displays the transcript of the YouTube video.
- User-friendly interface built with Streamlit.

## Requirements

This project requires the following Python packages:

- `streamlit`
- `google-api-python-client`
- `youtube-transcript-api`

To install the necessary dependencies, create a virtual environment and install the packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Setting Up

1. Obtain a YouTube Data API key by following the instructions on the [Google Developers Console](https://console.developers.google.com/).
2. Clone or download this repository to your local machine.
3. Install the required dependencies using the command above.
4. Run the Streamlit app:

```bash
streamlit run app.py
```

## Usage

1. Open the application in your web browser (usually at `http://localhost:8501`).
2. Enter your YouTube Data API key in the input field.
3. Paste a valid YouTube video URL into the corresponding input field.
4. Click the "Transcribe" button.
5. The app will fetch the video details (title and description) and the transcript for the video, which will be displayed on the screen.

## Example YouTube URL

You can try using this YouTube video link as an example:

[https://vimeo.com/1041025173](https://vimeo.com/1041025173)
