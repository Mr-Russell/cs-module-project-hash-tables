import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

markov = {}
word_list = words.split()

for i in range(len(word_list)):
    word = word_list[i]
    if word not in markov:
        markov[word] = []
    if i < (len(word_list) - 1):
        followers = markov[word]
        followers.append(word_list[i+1])

def markov_chain():
    string = ''
    first_word = ''
    
    starter = False
    while starter == False:
        first_word = random.choice(word_list)
        if first_word[0] == first_word[0].upper():
            string += f"{first_word} "
            starter = True

    ending = False
    current = first_word
    while ending == False:
        next_word = markov[current]
        random_int = random.randint(0, len(next_word) - 1)
        next_word = next_word[random_int]
        string += f"{next_word} "
        if next_word.endswith(".") or next_word.endswith("?") or next_word.endswith("!"):
            ending = True
        current = next_word
    
    return string.strip()




# TODO: construct 5 random sentences
# Your code here

print(f"{markov_chain()}\n")
print(f"{markov_chain()}\n")
print(f"{markov_chain()}\n")
print(f"{markov_chain()}\n")
print(f"{markov_chain()}\n")
