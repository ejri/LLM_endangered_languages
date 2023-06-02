import openai


# Define the endangered language you want to learn
endangered_language = "french"

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Set up your OpenAI API credentials
openai.api_key = open_file('openaiapikey.txt')

# Function to prompt the language model and get its response
def generate_response(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"you are a learning program that makes it easier to learn the {endangered_language} language. help the user learn by translating the user content to english and explain your learning process."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message['content']

# Start a conversation with the language model
def start_conversation():
    print(f"Welcome to the {endangered_language} language learning program!")
    print("You can start by saying 'Hello' or asking any question.")

    while True:
        user_input = input("You: ")
        prompt = f"You: {user_input}\nAI: "

        if user_input.lower() == "bye":
            print("AI: Goodbye!")
            break

        response = generate_response(prompt)
        print(f"AI: {response}")

# Main program
if __name__ == '__main__':
    start_conversation()
