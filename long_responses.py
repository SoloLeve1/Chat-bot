import random

R_EATING = "I eat anything that any other human being eat!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sorry I don't understand what you mean.",
                "What does that mean?"][
        random.randrange(4)]
    return response
