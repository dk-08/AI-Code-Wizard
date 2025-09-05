from gemini_helper import generate_code

def main():
    print("Welcome to the Gemini CLI App!")
    print("Type your request (or type 'exit' to quit)\n")

    while True:
        user_input = input(">>> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            response = generate_code(user_input)
            print("\n--- Gemini's Response ---")
            print(response)
            print("-------------------------\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
