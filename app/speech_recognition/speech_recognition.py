import os
import logging
from transformers import pipeline
import soundfile as sf

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def transcribe(speech_input):
    """
    Transcribes the given speech input using the Whisper model.
    Flattens the speech input to match the model's expected input shape.
    """
    model = pipeline("automatic-speech-recognition", model="openai/whisper-medium", device=0)
    speech_input = speech_input.flatten()
    transcription = model(speech_input)
    return transcription['text']


def load_audio_file(file_path, sample_rate=16000):
    """
    Loads audio from a file using soundfile.
    Logs the process and handles errors.
    """
    try:
        logging.info("Loading audio file")
        audio, _ = sf.read(file_path, dtype='float32')
        return audio
    except Exception as e:
        logging.error(f"Error loading audio file: {e}")
        return None

def record_text(file_path):
    """
    Captures and recognizes speech from an audio file.
    Returns the recognized text, or an empty string if an error occurs.
    """

    audio_data = load_audio_file(file_path)
    if audio_data is not None:
        text = transcribe(audio_data)
        logging.info("Speech recognized")
        return text
    return ""

def run(file_path):
    """
    Main method to run the speech recognition process.
    Takes a file path as input and returns the recognized text.
    """
    text = record_text(file_path)
    if text:
        logging.info("Returning raw text")
        return text
    else:
        logging.info("No text to return")
