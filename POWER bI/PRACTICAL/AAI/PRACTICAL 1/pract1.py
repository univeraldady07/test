import random 
responses={ 
        "Hello":["Hi","Hey Whatsup"], 
        "Bye":["See you soon","Have a nice day"], 
        "How are you":["I'm Fine","What about you"], 
        "What is your name":["Chatbot"], 
        "Default":["I don't understand","I'm a simple chatbot kindly explain in detail"] 
    } 
 
def chatbot(): 
    while True: 
        user_input=input("You: ") 
        if user_input=="exit": 
            print("Goodbye") 
            break 
        response=responses.get(user_input,responses["Default"]) 
        result="".join(random.choices(response)) 
        print("Bot: ",result)         
 
chatbot()
