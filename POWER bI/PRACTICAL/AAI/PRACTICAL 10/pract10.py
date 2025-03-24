import aiml 
 
def gamePlay(): 
    # Create a Kernel instance 
    kernel = aiml.Kernel() 
 
    # Load the AIML file 
    kernel.learn("p10aiml.aiml") 
 
    print("Gamebot: Hi there! Type 'Rock', 'Paper', or 'Scissors' to play. Type 'Goodbye' to exit.") 
 
    # Start the game loop 
    while True: 
        user_input = input("You: ").strip().upper() 
        if user_input == "GOODBYE": 
            print("Gamebot: Goodbye! Thanks for playing.") 
            break 
        elif user_input in ["ROCK", "PAPER", "SCISSORS"]: 
            response = kernel.respond(user_input) 
            print(f"Gamebot: {response}") 
        else: 
            print("Gamebot: I didn't understand that. Please type 'Rock', 'Paper', or 'Scissors'.") 
 
gamePlay() 
