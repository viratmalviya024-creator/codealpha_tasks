def run_chatbot():
    print("===================================")
    print("      Welcome to PyBot 1.0         ")
    print("===================================")
    print("Type 'bye' to exit the chat.\n")

   
    while True:
       
        user_input = input("You: ").lower().strip()
        
        
        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! How can I help you today?")
            
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How are you?")
            
        elif user_input == "what is your name":
            print("Bot: I'm PyBot, your simple rule-based assistant.")
            
        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break  
            
        else:
           
            print("Bot: Sorry, I don't understand that. Try saying 'hello' or 'bye'.")


if __name__ == "__main__":
    run_chatbot()