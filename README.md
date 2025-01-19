# atat_voicebot
# ChatBot Project

This project is a voice-activated assistant built using Python. It utilizes the `pyttsx3` library for speech synthesis and `speech_recognition` for capturing voice commands. The chatbot can help with various tasks such as booking appointments, providing car specifications, and performing web searches.

## Features
- **Voice Interaction**: Responds to and processes voice commands.
- **Appointment Booking**: Assists with booking an appointment at Tata Motors.
- **Tata Motors & Nexon Information**: Provides details about Tata Motors vehicles, specifically the Tata Nexon.
- **Web Search**: Can search Google for various queries.
- **Brochure Download**: Downloads the Tata Nexon brochure in PDF format.
- **Competitive Product Suggestions**: Suggests other cars in the market.

To run the project, install the following Python libraries:

```
run main.py
```
# voice commands
# Refer this
```
def respond(voice_data):
    """Process user commands."""
    if "book an appointment" in voice_data:
        book_appointment()
    elif "search" in voice_data:
        query = voice_data.split("search", 1)[1].strip()
        google_search(input("TYpe Here:"))
    elif "open tata motors website" in voice_data:
        open_tata_motors()
    elif "tata nexon" in voice_data:
        tata_nexon_specifications()
    elif "hello" in voice_data or "hi" in voice_data:
        wish()
    elif "stop" in voice_data or "exit" in voice_data:
        reply("Goodbye! Have a great day.")
        ChatBot.started = False  # Properly stopping the chatbot
        os._exit(0)
    else:
        reply("I'm not sure how to help with that.")
```
