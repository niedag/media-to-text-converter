from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from openai import OpenAI
import os

from moviepy.editor import *


# Load the environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt  # Temporarily disable CSRF protection for simplicity
def transcribe_audio(request):
    if request.method == "POST":
        audio_file = request.FILES.get('audio_file')
        if audio_file:
            # Read the uploaded file's content into bytes
            audio_bytes = audio_file.read()
            # Get the content type (MIME type) of the uploaded file
            content_type = audio_file.content_type
            try:
                # Use the file tuple (filename, file_bytes, content_type) for transcription
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=(audio_file.name, audio_bytes, content_type)
                )
                return HttpResponse(transcription.text)
            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}")
        else:
            return HttpResponse("No audio file provided.")
    else:
        # For GET requests, render an HTML form for file upload
        return render(request, 'transcribe_form.html')

def mp4Tomp3_convert(request):
    
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

VIDEO_FILE_PATH = "/Full/File/Path/ToSong.mp4"
AUDIO_FILE_PATH = "/Full/File/Path/ToSong.mp3"

MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
# MoviePy - Writing audio in /Full/File/Path/ToSong.mp3
# MoviePy - Done.    