# FAQ Bot with Spelling Correction using difflib

import difflib

faq_data = {
    "python": "Python is a popular programming language.",
    "ai": "AI stands for Artificial Intelligence.",
    "machine learning": "Machine Learning is a branch of AI.",
    "github": "GitHub is a platform used to store and manage code.",
    "chatbot": "A chatbot is a software application that interacts with users.",
    "computer": "A computer is an electronic device that processes data.",
    "internet": "The internet is a global network connecting millions of computers."
}


def answer_question(user_input):

    user_input = user_input.lower()

    if user_input == "exit":
        return "Thank you for using FAQ Bot!"

    # Split sentence into words
    words = user_input.split()

    # Check each word for close matches
    for word in words:

        match = difflib.get_close_matches(
            word,
            faq_data.keys(),
            n=1,
            cutoff=0.7
        )

        if match:
            return faq_data[match[0]]

    return "Sorry, I don't know the answer to that question."


while True:

    user_input = input("Ask a question (or type 'exit'): ")

    response = answer_question(user_input)

    print(response)

    if user_input.lower() == "exit":
        break