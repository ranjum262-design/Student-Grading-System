def main():
    students = {} 
    
    print("--- Welcome to the Student Record Tracker ---")

    while True:
        print("\nOptions: [1] Add Student  [2] View All  [3] Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter student name: ").strip()
            
            try:
                score = float(input(f"Enter grade for {name}: "))
                students[name] = score
                print(f"Success: {name} added.")
            except ValueError:
                print("Please enter a valid numerical score.")

        elif choice == '2':
            if not students:
                print("The list is currently empty.")
            else:
                print("\n--- Current Records ---")
                for name, score in students.items():
                    print(f"Student: {name} | Grade: {score}")

        elif choice == '3':
            print("Closing application. Goodbye!")
            break
        
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()