from sys import argv
from random import choice
import time

counter = 0

def answer_question():
    print "..."
    time.sleep(thinking_time_secs)
    return choice(answers)

# This version of Magic 8 ball requires you to provide the answer file
script_name, answer_file_name = argv
print answer_file_name

# Note that the file itself is different than the name of the file
answer_file = open(answer_file_name)

# This line reads the answers
answers = answer_file.read().split('\n')[:20]
answer_file.close()
# print answers

thinking_time_secs = 3

print "Hi! I'm your Magic 8 ball!\nWhat's your question?"
user_question = raw_input()
answer = answer_question()
print answer

if answer == 'Ask again later' or answer == 'Reply hazy try again' or answer == 'Concentrate and ask again':
    print "Try again!"
    print counter
    user_question = raw_input()
    answer = answer_question()
    print answer
else:
    print "thanks for asking"
    counter = counter +1
    print counter 
