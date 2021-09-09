import time
import webbrowser

class User:
  def __init__(self, name):
    name = self.name

name = input("What is your name?: ")
user_1 = User(name)

time.sleep(1)
print("Hey There! I'm the memory address register chat bot, but you can just call me chat bot :)")
time.sleep(1)
question = input(f"Hi "{user_1.name}", do you have any questions?: ")
question = question.lower()

if question == "what do you do":
  time.sleep(0.8)
  print("I hold the address of where data should go or be fetched from")
elif question == "where are you":
  print("I work in the CPU!")
elif question == "how big are you":
  print("I am very very small")
else:
  print("Ask it here :)")
  time.sleep(1)
  webbrowser.open_new("https://www.google.com")

#if question=
#responses = {"What is the purpose of the MAR?":" 
#"The MAR holds the address of the current instruction that is to be fetched from memory, or the address in memory to which data is to be transferred."}

responses[""]
#This is my basic idea for the bot, we can add more responses later. Feel free to change or re write it 