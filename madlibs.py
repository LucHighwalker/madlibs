import json
import random
import os


def user_input(prompt, blank):
    user_input = input(prompt.format(blank))
    return user_input


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


f = open('sentences.json')
data = json.load(f)
templates = data["templates"]

template = random.choice(templates)

print(template["title"])
input()

blanks = template["blanks"]
inputs = list()

for blank in blanks:
    clear_console()
    inputs.append(user_input("Enter a(n) {}: ", blank))

phrases = template["value"]
story = ""
index = 0
for phrase in phrases:
    if index < len(inputs):
        story = story + str(phrase) + str(inputs[index])
    else:
        story = story + str(phrase)
    index += 1

print(story)
