name = str(input("Enter your name: "))
choice = str(input("(H)ello\n(G)oodbye\n(Q)uit"))
while choice!= "H" and choice != "G" and choice != "Q":
    print("Invalid choice")
    choice = str(input("(H)ello\n(G)oodbye\n(Q)uit"))
while choice == "H" or choice == "G" or choice == "Q":
    if choice == "H":
        print("Hello ", name)
        choice = str(input("(H)ello\n(G)oodbye\n(Q)uit"))
    elif choice =="G":
        print("Goodbye ", name)
        choice = str(input("(H)ello\n(G)oodbye\n(Q)uit\nEnter your choice: "))
    elif choice == "Q":
        break
    while choice != "H" and choice != "G" and choice != "Q":
        print("Invalid choice")
        choice = str(input("(H)ello\n(G)oodbye\n(Q)uit"))
print("Finished")