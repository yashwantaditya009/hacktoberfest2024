import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def perform_calculation(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation."

# Listen for user input
def listen_for_input():
    with sr.Microphone() as source:
        print("Listening for a math operation...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            return "Could not request results; {0}".format(e)

while True:
    user_input = listen_for_input()

    if user_input is not None:
        if "exit" in user_input:
            print("Exiting the calculator.")
            break

        # Split the input into words
        words = user_input.split()
        
        # Check if there are enough words to perform a calculation
        if len(words) == 3:
            operation, num1, num2 = words[0], float(words[1]), float(words[2])
            result = perform_calculation(operation, num1, num2)
            print("Result:", result)
        else:
            print("Invalid input. Please say something like 'add 5 and 3'.")

