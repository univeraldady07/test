import aiml 
import os 
 
# Initialize AIML kernel 
kernel = aiml.Kernel() 
 
# Load specific AIML files 
kernel.learn('botaiml.aiml')  # Replace with your specific AIML file path 
kernel.learn('p11aiml.aiml')  # Replace with your specific AIML file path 
 
# Start the conversation 
print("Welcome to the restaurant recommendation bot! Type 'goodbye' to exit.") 
 
while True: 
    # Get user input 
    user_input = input("You: ").strip() 
 
    # Handle exit commands 
    if user_input.lower() in ['exit', 'quit', 'goodbye']: 
        print("Bot: Goodbye! Enjoy your meal!") 
        break 
     
    # Get and print bot's response 
    response = kernel.respond(user_input) 
     
    # If the bot doesn't have a response, prompt for more details 
    if not response: 
        response = "Sorry, I didn't understand that. Can you tell me what kind of cuisine you're interested in?" 
         
    print(f"Bot: {response}") 
