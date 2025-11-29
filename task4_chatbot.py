def chatbot():
    print("Chatbot: Hi! I'm your simple Python chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        
        else:
            print("Chatbot: I don't understand. Please try again.")

#Run the chatbot
chatbot()
