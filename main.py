from datetime import datetime
from wish.wish import speak, wish
from voiceinp.voiceinp import voiceinp
from ai.ai import ai

if __name__ == "__main__":
    wish()  

    while True:
        # Update time on every loop
        now = datetime.now()
        t = now.strftime('%I:%M %p')
        y = now.year
        d = now.strftime('%A')

        print(t, y)
        print(d)

        # Take voice input
        query = voiceinp().lower().strip()

        if query == "" or query == " ":
            speak("Please say that again.")
            continue

        # Get AI response
        ans = ai(query)
        print(ans)

        # Speak the response
        speak(ans)
