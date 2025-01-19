import eel
import time
class ChatBot:
    started = False
    user_input_queue = []  # Queue to store user inputs

    @staticmethod
    @eel.expose
    def getUserInput(msg):
        """Add user input to the queue."""
        ChatBot.user_input_queue.append(msg)

    @staticmethod
    @eel.expose
    def record_audio():
        """Handle audio recording and return a message."""
        return "This function will handle audio recording."

    @staticmethod
    def popUserInput():
        """Retrieve and remove the latest user input from the queue."""
        return ChatBot.user_input_queue.pop(0) if ChatBot.user_input_queue else None

    @staticmethod
    def isUserInput():
        """Check if there is user input in the queue."""
        return len(ChatBot.user_input_queue) > 0

    @staticmethod
    @eel.expose
    def addAppMsg(msg):
        """Send a message to the front-end."""
        eel.addAppMsg(msg)

    @staticmethod
    def start():
        """Initialize the Eel application and start processing messages."""
        try:
            eel.init("web", allowed_extensions=[".js", ".html"])
            eel.start("index.html", mode="chrome", block=False)
            ChatBot.started = True

            # Process messages in a loop
            while ChatBot.started:
                if ChatBot.isUserInput():
                    user_message = ChatBot.popUserInput()
                    print(f"User Input: {user_message}")
                    # Process bot response here
                    bot_response = f"Bot Response to: {user_message}"  # Placeholder bot response
                    ChatBot.addAppMsg(bot_response)
                time.sleep(1)  # Sleep for 1 second to simulate async behavior

        except Exception as e:
            print(f"Error starting ChatBot: {e}")