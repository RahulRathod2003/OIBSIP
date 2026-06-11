print("=== Simple Chat Application ===")

while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Bot: Hello Rahul!")

    elif message == "how are you":
        print("Bot: I am fine. How are you?")

    elif message == "your name":
        print("Bot: My name is ChatBot.")

    elif message == "bye":
        print("Bot: Goodbye Rahul!")
        break

    else:
        print("Bot: Sorry, I don't understand.")