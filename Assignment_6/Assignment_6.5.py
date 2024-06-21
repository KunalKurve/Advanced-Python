# 11. In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A simple set of heuristic rules can be given as follows:
# If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, change ie to y and add ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding ing
# By default just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
# returns its present participle form. Test your function with words such as lie, see, move and hug.

def make_ing_form(word):
  word=word.lower()
  vow=['a','e','i','o','u']

  #If the verb ends in ie, change ie to y and add ing
  if word[-2] == "i" and word[-1] == "e":
    word = word.replace("ie", "ying")
    print(word)

  # If the verb ends in e, drop the e and add ing
  elif word[-1] == "e":
    word = word.replace(word[-1], "ing")
    print(word)

  # For words consisting of consonant-vowel-consonant, double the final letter before adding ing
  elif (word[-3] not in vow) and (word[-2] in vow) and (word[-1] not in vow):
    word = word.replace(word[-1], word[-1]+"ing")
    print(word)

  #default
  else:
    word = word + "ing"
    print(word)


word = input("Enter the word: ")
make_ing_form(word)