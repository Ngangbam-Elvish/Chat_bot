from src.model import FAQChatbot

def start_chat():
    print("Loading FAQ Chatbot...")
    try:
        bot = FAQChatbot("d:\\Chat_bot\\Data\\Ecommerce_FAQ_Chatbot_dataset.csv")
    except Exception as e:
        print(f"Error loading chatbot: {e}")
        return
        
    print("Bot: FAQ Chatbot (type 'exit' to quit)\n")
    
    while True:
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break
            
        if user_input.lower().strip() in ['exit', 'quit']:
            print("Bot: Goodbye!")
            break
            
        if not user_input.strip():
            continue
            
        response = bot.get_response(user_input)
        print(f"Bot: {response}")