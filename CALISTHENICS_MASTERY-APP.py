#Author:Nunez, Jose Enrique ,and Catubig, Arwen
#(Final Project) APP + Demo: Calisthenic_mastery
#Date of Submission: 27/06/2023

import datetime

# Function to display the progression training details for a selected exercise
def display_progression_training(selected_exercise):
    # List of exercises and their progression details
    exercise_list = [
        {
            "name": "Muscle ups",
            "progression": [
                {"level": "1 Beginner pull-ups", "reps": 8, "sets": 3, "rest": 60},
                {"level": "2 Assisted muscle up drills", "reps": 6, "sets": 4, "rest": 90},
                {"level": "3 Negative muscle ups", "reps": 5, "sets": 4, "rest": 120},
                {"level": "4 Full muscle ups", "reps": 3, "sets": 5, "rest": 120}
            ]
        },
        {
            "name": "Planche",
            "progression": [
                {"level": "1 Tuck planche", "reps": 10, "sets": 3, "rest": 60},
                {"level": "2 Advanced tuck planche", "reps": 8, "sets": 4, "rest": 90},
                {"level": "3 Straddle planche", "reps": 6, "sets": 4, "rest": 120},
                {"level": "4 Full planche", "reps": 4, "sets": 5, "rest": 120}
            ]
        },
        {
            "name": "Pistol squat",
            "progression": [
                {"level": "1 Assisted pistol squat", "reps": 10, "sets": 3, "rest": 60},
                {"level": "2 Partial pistol squat", "reps": 8, "sets": 4, "rest": 90},
                {"level": "3 Full pistol squat", "reps": 6, "sets": 4, "rest": 120}
            ]
        },
        {
            "name": "Hand-stand push-ups",
            "progression": [
                {"level": "1 Wall-assisted hand-stand push-ups", "reps": 10, "sets": 3, "rest": 60},
                {"level": "2 Pike push-ups", "reps": 8, "sets": 4, "rest": 90},
                {"level": "3 Wall hand-stand push-ups", "reps": 6, "sets": 4, "rest": 120},
                {"level": "4 Free-standing hand-stand push-ups", "reps": 4, "sets": 5, "rest": 120}
            ]
        },
        {
            "name": "V-sit",
            "progression": [
                {"level": "1 Lying leg raise", "reps": 12, "sets": 3, "rest": 60},
                {"level": "2 V-sit tuck hold", "reps": "-", "sets": 4, "rest": 90},
                {"level": "3 V-sit with one leg extended", "reps": "-", "sets": 4, "rest": 120},
                {"level": "4 Full V-sit", "reps": "-", "sets": 5, "rest": 120}
            ]
        }
    ]

    # Validate the user input
    if selected_exercise < 1 or selected_exercise > len(exercise_list):
        print("Invalid selection. Please choose a number from the provided options.")
        return

    selected_exercise_data = exercise_list[selected_exercise - 1]

    # Display the progression training for the selected exercise
    print(f"\nProgression training for {selected_exercise_data['name']}:")
    for progression in selected_exercise_data['progression']:
        print(f"Level: {progression['level']}")
        print(f"Reps: {progression['reps']}")
        print(f"Sets: {progression['sets']}")
        print(f"Rest Time: {progression['rest']} seconds")
        print()

    # Prompt the user to enter the number of reps for each level of progression
    reps_data = []
    for progression in selected_exercise_data['progression']:
        reps = input(f"Enter the number of reps for {progression['level']}: ")
        reps_data.append({"level": progression['level'], "reps": reps})

    return reps_data


# Function to gather user information during signup
def user_information(username, password):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")
    filename = f"{username}_task.txt"

    # Write user information to a file
    with open(filename, 'a') as f:
        f.write(f"{password}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Age: {age}\n")


# Function for user signup
def signup():
    print("Please enter the username you wish to use for your account")
    username = input("Please enter here: ")
    password = input("Enter a password: ")
    user_information(username, password)
    print("Proceed to login")
    login()


# Function for user login
def login():
    print("Please enter a username: ")
    username = input("Enter here: ")
    password = input("Enter the password: ")
    filename = f"{username}_task.txt"

    try:
        with open(filename, 'r') as f:
            stored_password = f.readline().strip()

            if password == stored_password:
                # Display the exercise options
                print("Exercise options:")
                for i, exercise in enumerate(["Muscle ups", "Planche", "Pistol squat", "Hand-stand push-ups", "V-sit"], start=1):
                    print(f"{i}. {exercise}")

                selected_exercise = int(input("Enter the number of the exercise you want to see progression for: "))

                # Call the function to display progression training for the selected exercise
                reps_data = display_progression_training(selected_exercise)

                # Record the reps data
                record_reps_data(username, selected_exercise, reps_data)

                # Display all recorded reps inputs
                display_recorded_reps(username, selected_exercise)
            else:
                print("The password or username you entered is incorrect. Please try again.")
                login()

    except FileNotFoundError:
        print("The username you entered does not exist. Please try again.")
        login()


# Function to record the reps data
def record_reps_data(username, selected_exercise, reps_data):
    filename = f"{username}_reps.txt"

    # Append the reps data to a file
    with open(filename, 'a') as f:
        f.write(f"{datetime.datetime.now()}\n")
        f.write(f"Exercise: {selected_exercise}\n")
        for data in reps_data:
            f.write(f"Level: {data['level']}, Reps: {data['reps']}\n")
        f.write("\n")


# Function to display the recorded reps inputs
def display_recorded_reps(username, selected_exercise):
    filename = f"{username}_reps.txt"

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

            print(f"\nRecorded reps inputs for Exercise {selected_exercise}:")
            for line in lines:
                print(line.strip())

    except FileNotFoundError:
        print("No recorded reps inputs found.")


# Main program flow
if __name__ == '__main__':
    signup()
