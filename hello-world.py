print("Hello, world! My coding journey starts now.")


# secret_password = "PythonRocks"
# user_guess = ""  # Define it first so the loop has a value to check

# while user_guess != secret_password:  # While it's incorrect, keep looping
#     user_guess = input("Enter the secret password: ")

#     if user_guess == secret_password:
#         print("🏆 The treasure chest opens!")
#     else:
#         print("🚪 Wrong password! Try again.")

# I asked chatGPT why couldn't we define "user_guess" as input BEFORE the loop. Here is what was returned:

# ✅ This also works, but it changes the behavior slightly:
# 1️⃣ The first input happens before the loop starts.
# 2️⃣ If the user enters the correct password on the first try, the loop never runs at all!
# 3️⃣ The "Wrong! Try again:" message only appears if they make a mistake.

# So Which One Is Better?
# 👉 If you want the loop to always run at least once, the first approach (defining user_guess = "" before the loop) is better.
# 👉 If you want to check before entering the loop, the second approach works fine.

# Neither is wrong, but the first version is more standard for user input loops because it ensures the loop always starts and keeps all input-handling inside the loop.


# secret_password = "PythonRocks"
# user_guess = input("Enter the secret password: ")  # Ask before the loop starts

# while user_guess != secret_password:
#     user_guess = input("👎🏾 Wrong! Try again: ")

# print("🏆 The treasure chest opens!")

# I indeed tested this out and everything still worked functionally the same. It was a pretty magical moment 
# that my brain was picking it up and thinking intuitively. Out of curiosity, I asked about the defaul case sensativity of inputs. Here is the interaction:

# Me: This is all so much fun! I don't want to get ahead of myself but are inputs always case sensitive? 
# Is there a way to make the input not be case sensitive? 

# ChatGPT said:
# June, I love how your brain is thinking ahead! 🚀 You’re asking exactly the kind of questions that will make you a great programmer.

# 🔠 Are Inputs Always Case-Sensitive in Python?
# Yes! By default, Python treats strings as case-sensitive

# 🛠️ How to Make Input Not Case-Sensitive
# If you want the input to be case-insensitive, you need to convert it to the same format before comparing. The two most common ways are:

# ✅ Convert Input to Lowercase (.lower())
# This ensures that "PythonRocks", "PYTHONROCKS", and "pythonrocks" all match.

# password = "pythonrocks"  # Store in lowercase
# user_input = input("Enter password: ").lower()  # Convert input to lowercase

# if user_input == password:
#     print("✅ Access Granted!")
# else:
#     print("❌ Wrong password!")

# 🔥 Bonus: .casefold() for Full Case Insensitivity
# For even better case-insensitive matching, use .casefold(). It works like .lower(), 
# but it's even better at handling special characters and different alphabets.

# 💡 Challenge: Modify Your Code!
# 1️⃣ Modify your treasure chest password program so that it’s case-insensitive.
# 2️⃣ Experiment with .lower(), .upper(), and .casefold()—see if you notice any differences!
# 3️⃣ Try entering the password in different ways (like PYTHONrocks, pythonROCKS, etc.) and see what happens!

# def open_treasure_chest1():  # Define a function
#     secret_password = "PythonRocks"
#     user_guess = ""

#     while user_guess != secret_password:
#         user_guess = input("Enter the secret password to open the treasure chest: ")
        
#         if user_guess == secret_password:
#             print("🏆 Congratulations! The treasure chest opens, revealing a mountain of gold! You've unlocked the next level!")
#             open_treasure_chest2()
#         else:
#             print("🚪 Wrong password! Try again.")


# def open_treasure_chest2():  # Define a function
#     secret_password = "ButFlutterisCuter"
#     user_guess = ""

#     while user_guess != secret_password:
#         user_guess = input("Enter the top secret password to open the treasure chest: ")
        
#         if user_guess == secret_password:
#             print("🌟 Congratulations! The treasure chest opens, revealing an even bigger mountain of gold!")
#         else:
#             print("🚪 Wrong password! Try again.")

#     print("Game Over. Come again soon!")

# # Call the function
# open_treasure_chest1()

# Doing the same game but adding in a limited amount of tries

# def open_treasure_chest1():
#     secret_password = "PythonRocks"
#     user_guess = ""
#     attempts = 3  # Set the number of allowed tries

#     while user_guess != secret_password and attempts > 0:
#         user_guess = input(f"Enter the secret password to open the treasure chest ({attempts} tries left): ")

#         if user_guess == secret_password:
#             print(f"🏆 Congratulations! The treasure chest opens, revealing a mountain of gold! You've unlocked the next level with {attempts} left!")
#             open_treasure_chest2()
#         else:
#             attempts -= 1
#             if attempts > 0:
#                 print(f"🚪 Wrong password! Try again. ({attempts} tries left)")
#             else:
#                 print("⛔ The treasure chest locks forever! Game Over.")

# # Add the same logic for open_treasure_chest2
# def open_treasure_chest2():
#     secret_password = "ButFlutterisCuter"
#     user_guess = ""
#     attempts = 3  

#     while user_guess != secret_password and attempts > 0:
#         user_guess = input(f"Enter the top secret password to open the treasure chest ({attempts} tries left): ")

#         if user_guess == secret_password:
#             print(f"🌟 Congratulations! The treasure chest opens, revealing an even bigger mountain of gold with {attempts} left!")
#         else:
#             attempts -= 1
#             if attempts > 0:
#                 print(f"🚪 Wrong password! Try again. ({attempts} tries left)")
#             else:
#                 print("⛔ The treasure chest locks forever! Game Over.")

# # Start the game
# open_treasure_chest1()

# Making attempts global so that the number of attempts can be shared accross password attempts

# attempts = 3

# def open_treasure_chest1():
#     global attempts
#     secret_password = "PythonRocks"
#     user_guess = ""
#       # Set the number of allowed tries

#     while user_guess != secret_password and attempts > 0:
#         user_guess = input(f"Enter the secret password to open the treasure chest ({attempts} tries left): ")

#         if user_guess == secret_password:
#             attempts += attempts
#             print(f"🏆 Congratulations! The treasure chest opens, revealing a mountain of gold! You've unlocked the next level!")
#             open_treasure_chest2()
#         else:
#             attempts -= 1
#             if attempts > 0:
#                 print(f"🚪 Wrong password! Try again. ({attempts} tries left)")
#             else:
#                 print("⛔ The treasure chest locks forever! Game Over.")

# # Add the same logic for open_treasure_chest2
# def open_treasure_chest2():
#     global attempts
#     secret_password = "ButFlutterisCuter"
#     user_guess = ""

#     while user_guess != secret_password and attempts > 0:
#         user_guess = input(f"Enter the top secret password to open the treasure chest ({attempts} tries left): ")

#         if user_guess == secret_password:
#             print(f"🌟 Congratulations! The treasure chest opens, revealing an even bigger mountain of gold with {attempts} diamonds!")
#         else:
#             attempts -= 1
#             if attempts > 0:
#                 print(f"🚪 Wrong password! Try again. ({attempts} tries left)")
#             else:
#                 print("⛔ The treasure chest locks forever! Game Over.")


# # Start the game
# open_treasure_chest1()

# The program above worked as expected. Now the task is to create a tries variable separately from a points variable. 

# score = 0

# def open_treasure_chest1():
#     attempts = 3
#     secret_password = "PythonRocks"
#     user_guess = ""
#     global score
#       # Set the number of allowed tries

#     while user_guess != secret_password and attempts > 0:
#         user_guess = input(f"Enter the secret password to open the treasure chest ({attempts} tries left): ")

#         if user_guess == secret_password:
#             score += attempts
#             print(f"🏆 Congratulations! The treasure chest opens, revealing a mountain of gold! You've unlocked the next level!")
#             open_treasure_chest2()
#         else:
#             attempts -= 1
#             if attempts > 0:
#                 print(f"🚪 Wrong password! Try again. ({attempts} tries left)")
#             else:
#                 print("⛔ The treasure chest locks forever! Game Over.")

# # Add the same logic for open_treasure_chest2
# def open_treasure_chest2():
#     attempts = 3
#     secret_password = "ButFlutterisCuter"
#     user_guess = ""
#     global score

#     while user_guess != secret_password and attempts > 0:
#         user_guess = input(f"Enter the top secret password to open the treasure chest ({attempts} tries left): ")

#         if user_guess == secret_password:
#             score += attempts
#             print(f"🌟 Congratulations! The treasure chest opens, revealing an even bigger mountain of gold with {score} diamonds!")
#         else:
#             attempts -= 1
#             if attempts > 0:
#                 print(f"🚪 Wrong password! Try again. ({attempts} tries left)")
#             else:
#                 print("⛔ The treasure chest locks forever! Game Over.")


# # Start the game
# open_treasure_chest1()

def open_treasure_chest1(score):
    attempts = 3
    secret_password = "PythonRocks"
    user_guess = ""

    while user_guess != secret_password and attempts > 0:
        user_guess = input(f"Enter the secret password to open the treasure chest ({attempts} tries left): ")

        if user_guess == secret_password:
            score += attempts  # Add remaining attempts to score
            print(f"🏆 Congratulations! The treasure chest opens, revealing a mountain of gold! You've unlocked the next level!")
            return open_treasure_chest2(score)  # Pass score to next function
        else:
            attempts -= 1
            if attempts > 0:
                print(f"🚪 Wrong password! Try again. ({attempts} tries left)")
            else:
                print("⛔ The treasure chest locks forever! Game Over.")
    
    return score  # Return the score at the end

def open_treasure_chest2(score):
    attempts = 3
    secret_password = "ButFlutterisCuter"
    user_guess = ""

    while user_guess != secret_password and attempts > 0:
        user_guess = input(f"Enter the top secret password to open the treasure chest ({attempts} tries left): ")

        if user_guess == secret_password:
            score += attempts
            print(f"🌟 Congratulations! The treasure chest opens, revealing an even bigger mountain of gold with {score} diamonds!")
            return score  # Return final score
        else:
            attempts -= 1
            if attempts > 0:
                print(f"🚪 Wrong password! Try again. ({attempts} tries left)")
            else:
                print("⛔ The treasure chest locks forever! Game Over.")
    
    return score  # Return the score at the end


def get_rank(score):
    if score >= 6:
        return print (f"🏆 **Master Codebreaker**! You cracked the chest with ease! Your final score: {final_score}")
    elif score >= 3:
        return print(f"🌟 **Treasure Hunter**! Not bad, but you had some struggles! Your final score: {final_score}")
    elif score >= 1:
        return print(f"😅 **Lucky Explorer**! You barely made it! Your final score: {final_score}")
    else:
        return print(f"💀 **Lost Adventurer**... The chest remains locked forever. Your final score: {final_score}")

# Start the game

final_score = open_treasure_chest1(0)  # Start with 0 score
rank_message = get_rank(final_score)

print(rank_message)
# print(f"🏅 Your final score: {final_score}")



