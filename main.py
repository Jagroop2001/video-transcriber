import streamlit as st
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extracts video ID from a YouTube URL."""
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def fetch_video_details(api_key, video_id):
    """Fetches video details using the YouTube Data API."""
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()

    if "items" in response and len(response["items"]) > 0:
        snippet = response["items"][0]["snippet"]
        title = snippet["title"]
        description = snippet["description"]
        return title, description
    return None, None

def fetch_transcript(video_id):
    """Fetches the transcript for a YouTube video."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return "\n".join([item['text'] for item in transcript])
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

# Streamlit UI
st.title("YouTube Video Transcriber")

youtube_api_key = st.text_input("Enter your YouTube Data API Key:", type="password")
youtube_url = st.text_input("Enter YouTube Video URL:")

if st.button("Transcribe"):
    if not youtube_api_key or not youtube_url:
        st.error("Please provide both API Key and Video URL.")
    else:
        video_id = get_video_id(youtube_url)

        if not video_id:
            st.error("Invalid YouTube URL.")
        else:
            with st.spinner("Fetching video details..."):
                title, description = fetch_video_details(youtube_api_key, video_id)

            if not title:
                st.error("Unable to fetch video details. Check API Key and URL.")
            else:
                st.success("Video details fetched successfully!")
                st.write(f"**Title:** {title}")
                st.write(f"**Description:** {description}")

                with st.spinner("Fetching transcript..."):
                    transcript = fetch_transcript(video_id)

                st.text_area("Transcript:", value=transcript, height=300)
                st.success("Transcript fetched successfully!")
