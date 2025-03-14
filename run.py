# Import necessary library
import time

def chatbot():
    print("Hello! I am a simple chatbot.")
    time.sleep(1)

    # Asking user for their name
    name = input("What is your name? ")
    time.sleep(1)
    print(f"Nice to meet you, {name}!")

    # Asking for basic bio-data information
    age = input("How old are you? ")
    time.sleep(1)
    gender = input("What is your gender? ")
    time.sleep(1)
    occupation = input("What is your occupation? ")
    time.sleep(1)
    hobby = input("What is your favorite hobby? ")
    time.sleep(1)

    # Displaying the collected information
    print("\nThank you for sharing your information.")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Occupation: {occupation}")
    print(f"Favorite Hobby: {hobby}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
