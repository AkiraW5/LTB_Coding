# Made by Kitten Team in Brazil :)

from ast import Store
from operator import rshift

a = "| Howdy Folks! Welcome to LDU! |"
print(len(a))
print(a.center(300))

print("================================")
print("\n            Now, what you wanna do?")
print("\n 1- Show the store ", "2- Want to suggest us something?",
      "3- Custom downloader(BETA)")
print("\n 4- Look our Github page!", "5- What's LDU?", "6- Let me out! (quit)")

Option_Selector = input("")

print(Option_Selector == True)

if Option_Selector == "1" == True:
    print("====================================================")
    print("Application", "Arch", "Version", "Repository", "Size")
    print("====================================================")

elif Option_Selector == "2" == True:
    print("==================================")
    print("| Oh, so you have an suggestion? |")
    print("==================================")