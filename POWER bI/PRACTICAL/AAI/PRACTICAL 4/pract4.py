def ask_question(question): 
    """Ask the user a question and get a yes/no response.""" 
    response = input(question + " (yes/no): ").strip().lower() 
    while response not in ["yes", "no"]: 
        print("Please answer with 'yes' or 'no'.") 
        response = input(question + " (yes/no): ").strip().lower() 
    return response == "yes" 
 
def collect_symptoms(): 
    """Collect symptoms from the user.""" 
    print("Please answer the following questions about your symptoms:") 
    symptoms = {} 
    symptoms["fever"] = ask_question("Do you have a fever or chills?") 
    symptoms["cough"] = ask_question("Do you have a cough?") 
    symptoms["sore_throat"] = ask_question("Do you have a sore throat?") 
    symptoms["runny_nose"] = ask_question("Do you have a runny or stuffy nose?") 
    symptoms["body_aches"] = ask_question("Do you have muscle or body aches?") 
    symptoms["fatigue"] = ask_question("Do you feel fatigued or very tired?") 
    symptoms["loss_of_taste_smell"] = ask_question("Have you lost your sense of taste or smell?") 
    return symptoms 
 
def evaluate(symptoms): 
    """Evaluate the symptoms and provide a diagnosis.""" 
    # Rule-based evaluation 
    if symptoms["fever"] and symptoms["cough"] and symptoms["fatigue"]: 
        if symptoms["loss_of_taste_smell"]: 
            return "Your symptoms suggest COVID-19. Please get tested and consult a healthcare provider." 
        return "Your symptoms suggest the flu. Rest, hydrate, and consult a doctor if symptoms worsen." 
    elif symptoms["sore_throat"] and not symptoms["fever"]: 
        return "Your symptoms suggest a common cold. Rest and stay hydrated." 
    else: 
        return "Your symptoms are inconclusive or may indicate another condition. Please consult a healthcare provider." 
 
def main(): 
    """Run the expert system.""" 
    print("Welcome to the Flu Expert System! Let's assess your symptoms.") 
    symptoms = collect_symptoms() 
    diagnosis = evaluate(symptoms) 
    print("\nDiagnosis:") 
    print(diagnosis) 
 
if __name__ == "__main__": 
    main()
