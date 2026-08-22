import random

def generate_mcq(topic, num):

    questions = []

    for i in range(num):

        q = {
            "question": f"What is {topic} concept {i+1}?",
            "options":[
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer":"Option A"
        }

        questions.append(q)

    return questions