# quorra

This project is a custom voice assistant using GPT-4o and Google Cloud Text-to-Speech for advanced voice and text interaction. It features internet search and image generation capabilities using a combination of OpenAI and Google services.

### Features

- Voice input with keyboard shortcut (F9)
- Text processing using GPT-4o
- Text-to-speech using Google Cloud Text-to-Speech (is currently free if you use Journey voices)
- Immediate conversation history
- Internet search capability

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key
- A Google Cloud Text-to-Speech API key
- A Google Custom Search Engine API key (from the Google Cloud Console)
- A Google Custom Search Engine ID (from the Google Programmable Search site)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/madmaximusjb/quorra.git
    cd quorra
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install pyaudio
    ```

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your API keys:**

    Open `config.py` and replace the placeholders with your actual API keys:

    ```python
    OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
    GOOGLE_APPLICATION_CREDENTIALS = 'path/to/your/credentials.json'
    DEFAULT_VOICE_NAME = 'en-US-Wavenet-D'  # Replace with your desired voice
    DEFAULT_AUDIO_ENCODING = 'LINEAR16'  # Use LINEAR16 for streaming audio
    GOOGLE_CSE_API_KEY = 'YOUR_CSE_API_KEY'
    GOOGLE_CSE_ID = 'YOUR_CSE_ID'
    ```

### Usage

1. **Run the voice assistant:**

    ```bash
    python main.py # Note that you have to be in the venv to use the assistant if you created one
    ```

2. **Interact with the assistant:**

    - Press and hold `F9` to start listening.
    - Speak your query clearly into the microphone.
    - Release `F9` to process your input and get a response.
    - Use the word "search" at the beginning of your query to have Quorra search the web

### Project Structure

```
quorra/
│
├── README.md               # Project documentation
├── requirements.txt        # Required Python packages
├── main.py                 # Main script to run the voice assistant
├── config.py               # Configuration file for API keys and settings
├── utils/                  # Utility modules
│   ├── __init__.py         # Init file for utils package
│   ├── audio_input.py      # Module to handle audio input
│   ├── text_processing.py  # Module to process text using GPT-4o
│   ├── text_to_speech.py   # Module to convert text to speech using Google Cloud Text-to-Speech
```

### Details of Each Module

#### `main.py`

The main script that runs the voice assistant. It listens for user input when the F9 key is pressed, processes the input using GPT-4o, and responds with generated speech.

#### `config.py`

Contains the configuration settings for the project, including API keys and the default voice ID.

#### `utils/audio_input.py`

Handles capturing and processing audio input. It uses the `SpeechRecognition` library to convert voice to text and listens only when the F9 key is pressed.

#### `utils/text_processing.py`

Processes the text input using GPT-4o. *Note: To change initial prompt, edit within this file.*

#### `utils/text_to_speech.py`

Converts the text response from GPT-4o to speech using Google Cloud Text-to-Speech.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the GPL-3.0 License.

