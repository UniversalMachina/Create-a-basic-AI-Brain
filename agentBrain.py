#fixes issue 105
#https://github.com/webaverse-studios/webaverse/issues/105

import random
import json
from textblob import TextBlob
from Text_generator import generate_text

class Agent:
    def __init__(self, name, faction, personality):
        self.name = name
        self.faction = faction
        self.personality = personality

    def __str__(self):
        return f"{self.name} ({self.faction}, {self.personality})"

    def respond(self, input_text):
        tone = self.determine_tone(input_text)
        response = self.generate_response(input_text, tone)
        return response

    def determine_tone(self, input_text):
        sentiment = TextBlob(input_text).sentiment.polarity
        print(sentiment)
        if self.personality == "Friendly":
            if sentiment > 0:
                return "positive"
            else:
                return "neutral"
        elif self.personality == "Aggressive":
            if sentiment < 0:
                return "Hostile"
            else:
                return "neutral"
        elif self.personality == "Hostile":
            return "Hostile"

        else:  # Reserved personality
            return "neutral"

    def generate_response(self, input_text, tone):
        varation_prompt = f"Reply to this from the pov of {self.name} who is part of the {self.faction} faction, return the reply and nothing else. The reply should sound casual and human. The tone should be {tone}:\n{input_text}"
        return generate_text(varation_prompt)



factions = ["Mages", "Warriors", "Thieves"]
personalities = ["Friendly", "Aggressive", "Reserved","Hostile"]

agent1 = Agent("Alice", random.choice(factions), random.choice(personalities))
agent2 = Agent("Bob", random.choice(factions), random.choice(personalities))

print(agent1)
print(agent2)

while True:
    input_text = input("Enter your message: ")
    # input_text = "What do you think about apples?"

    response1 = agent1.respond(input_text)
    response2 = agent2.respond(input_text)

    print(response1)
    print(response2)

