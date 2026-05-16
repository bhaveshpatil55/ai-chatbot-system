# ============================================
#        University Information Bot
# ============================================

import difflib


# Greeting Function
def greet():

    print("\n========================================")
    print("     Welcome to UniBot Assistant")
    print("========================================")

    print("\nHello!")
    print("I am UniversityBot.")
    print("I can help you with university-related information.\n")


# Ask User Name
def remind_name():

    name = input("Please enter your name: ")

    print(f"\nWelcome, {name}!")
    print("How can I help you today?\n")


# University Query Database
queries = {

    "admission": "University admission process starts in June.",

    "scholarship": "Scholarship forms are available on the university portal.",

    "research": "Research facilities are available for postgraduate students.",

    "hostel": "Hostel facilities are available for boys and girls.",

    "library": "Central university library is open from 7 AM to 11 PM.",

    "exam": "University examination schedule will be published online.",

    "result": "Results are declared through the university examination portal.",

    "attendance": "Students must maintain minimum attendance as per university rules.",

    "assignment": "Assignments should be submitted before university deadlines.",

    "placement": "Placement training sessions are conducted every semester.",

    "fees": "Fee details are available on the university website.",

    "course": "Multiple undergraduate and postgraduate courses are available."
}


# Chatbot Function
def university_help():

    print("You can ask about:")
    print("- Admission")
    print("- Scholarship")
    print("- Hostel")
    print("- Library")
    print("- Exams")
    print("- Results")
    print("- Placements")
    print("\nType 'exit' to close the chatbot.\n")

    while True:

        user_input = input("Ask your question: ").lower()

        # Exit chatbot
        if user_input == "exit":

            print("\n========================================")
            print(" Thank you for using UniBot Assistant ")
            print("========================================")

            print("\nHave a great day!")

            break

        words = user_input.split()

        found = False

        # Spelling correction using difflib
        for word in words:

            match = difflib.get_close_matches(
                word,
                queries.keys(),
                n=1,
                cutoff=0.7
            )

            if match:

                print("\n" + queries[match[0]] + "\n")

                found = True

                break

        if not found:

            print("\nSorry, I don't understand your query.\n")


# -------- Main Program --------

greet()

remind_name()

university_help()