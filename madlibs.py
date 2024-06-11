with open("story.txt", "r") as s: #"r" is read only mode
    story = s.read()

words = set() #using set() instead of a [] list + words.add to get all the UNIQUE words 
start_of_word = -1 #I made it -1 because I assign an index to this variable that starts at 0.

target_start = "<" #so I can change the angled brackets in my story to something else later if I want to
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1] 
        words.add(word)
        start_of_word = -1

answers = {}

for word in words: #foreach loop from C#
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer  

for word in words:
    story = story.replace(word, answers[word]) #replaces every word variable with the input given by the user
    
print(story)