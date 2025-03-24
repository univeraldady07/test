import aiml 
import os 
 
def main(): 
    # Create AIML Kernel 
    kernel = aiml.Kernel() 
    kernel.learn("p3aiml.aiml") 
      
    print("E-Commerce Chatbot is ready! Type 'exit' to end the chat.") 
     
    while True: 
        user_input = input("You: ") 
        if user_input.upper() == "EXIT": 
            print("Chatbot: Thank you for visiting! Goodbye!") 
            break 
        response = kernel.respond(user_input) 
        print(f"Chatbot: {response}") 
 
if __name__ == "__main__": 
    main() 
