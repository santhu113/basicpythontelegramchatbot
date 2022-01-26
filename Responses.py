from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "start"):
        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?",):
        return "I am a Responsive Bot Made by @dsurareddy"

    if user_message in ("time", "time?", "date", "date?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I Don't Understand You."
