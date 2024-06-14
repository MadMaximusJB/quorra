import os
from google.cloud import texttospeech
import pyaudio
from config import GOOGLE_APPLICATION_CREDENTIALS, DEFAULT_VOICE_NAME, DEFAULT_AUDIO_ENCODING

def text_to_speech_with_google(text, voice_name=DEFAULT_VOICE_NAME, audio_encoding=DEFAULT_AUDIO_ENCODING):
    try:
        # Set the environment variable for authentication
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS

        # Initialize the Text-to-Speech client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Build the voice request
        voice = texttospeech.VoiceSelectionParams(
            language_code='en-US',
            name=voice_name
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding[audio_encoding],
            sample_rate_hertz=24000,
            speaking_rate=1.3
        )

        # Perform the text-to-speech request
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        # Play the audio stream
        play_audio_stream(response.audio_content)
    except Exception as e:
        print(f"Error converting text to speech: {e}")

def play_audio_stream(audio_content):
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Define stream parameters
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=24000,  # Google Cloud TTS returns audio at 24000 Hz
                    output=True)

    # Stream the audio content
    stream.write(audio_content)

    # Close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()
