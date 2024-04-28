candidates = {}
votes = {}

while True:
    print("1. Add candidate")
    print("2. Vote")
    print("3. Get winner")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        candidate_name = input("Enter candidate name: ")
        candidates[candidate_name] = 0
    elif choice == "2":
        candidate_name = input("Enter candidate name: ")
        if candidate_name in candidates:
            votes[candidate_name] = votes.get(candidate_name, 0) + 1
            print("Vote cast successfully.")
        else:
            print("Invalid candidate.")
    elif choice == "3":
        if not candidates:
            print("No candidates available.")
        else:
            max_votes = max(votes.values(), default=0)
            winners = [name for name, votes in votes.items() if votes == max_votes]
            if len(winners) == 1:
                print(f"The winner is: {winners[0]}")
            else:
                print("Tie.")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")