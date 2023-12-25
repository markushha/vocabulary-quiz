import math
from typing_effect import typing_effect

# simple quiz for preparation to my SAT

path = "/Users/markinger/Code/vocab-quiz/vocabulary.txt"

def get_words():
  try:
    with open(path) as file:
        return file.read()
  except UnicodeDecodeError as e:
    print("Please, use .txt file extension")
  except FileNotFoundError:
    print("Error: file not found. Please, correct your path and make sure it's available.")
  except Exception as e:
    print(f"Something went wrong. Error message: {e}")

init_str = get_words()

split_by_words = init_str.split('\n') # splitting a vocabulary into key - value items in an array

dict = {}

for item in split_by_words:
  [value, translation] = item.split('-')
  # don't forget to trim

  # formatting a dictionary

  dict.update({
    value.strip(): translation.strip()
  })

# at this point, dictionary is formed and we can start quiz

typing_effect(f"Welcome to your very own quiz. It consists of {len(dict)} questions. Good luck!")

while True:
  score = 0
  what_to_learn = {}

  for [key, value] in dict.items():
    typing_effect(f"\nEnter a translation for this word {key}: \n")
    user_input = input()

    if user_input.strip().lower() == value.strip().lower():
      score += 1
      typing_effect("\nThat's right! Keep going :)\n")
    else:
      typing_effect(f"\nThat's incorrect. The correct translation for word {key} is {value}\n")

      # adding unfamiliar subject to a new dictionary
      what_to_learn.update({
        key: value
      })

  # printing results

  percentage_score = math.floor(score/len(dict) * 100)
  typing_effect(f"You've finished quiz.\nYour score is {score} out of {len(dict)} which is {percentage_score}%")

  print(len(what_to_learn))
  if len(what_to_learn) > 0:
    typing_effect(f"\nHere are the list of words that you're unfamiliar with:\n")

    for [key, value] in what_to_learn.items():
      typing_effect(f"{key}: {value}\n")

  typing_effect(f"\nDo you want to proceed? Type yes/no:\n")
  proceed = input()

  if proceed.strip().lower() == "yes":
    continue
  else:
    break

print("Hope you had a good learning session!")