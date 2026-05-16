# Medical Chatbot

medical_problems = {
    "fever": "Drink plenty of fluids, take rest, and consult a doctor if fever continues.",
    "cold": "Take proper rest and drink warm fluids.",
    "headache": "Take rest and stay hydrated.",
    "stomach pain": "Avoid oily food and drink enough water.",
    "cough": "Drink warm water and avoid cold drinks.",
    "vomiting": "Drink ORS and stay hydrated."
}


def handle_problem(user_input):

    user_input = user_input.lower()

    if user_input == "exit":
        return "Take care! Goodbye."

    elif user_input in medical_problems:
        return medical_problems[user_input]

    else:
        return "Sorry, I don't have information about that problem."


while True:

    user_input = input("Enter your medical problem (or type 'exit'): ")

    response = handle_problem(user_input)

    print(response)

    if user_input.lower() == "exit":
        break