import cohere

endangered_language = "french"

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Set up your OpenAI API credentials
co = cohere.Client(open_file('cohereapikey.txt')) # This is your trial API key

# Function to prompt the language model and get its response
def generate_response(prompt):
  core_prompt= f"you are a program that makes it easier for users to learn the {endangered_language} language. help the user learn by translating the user content to english and explain your learning process."
  response = co.generate(
    model='command-xlarge-nightly',
    prompt= core_prompt + prompt,
    max_tokens=300,
    temperature=0.6,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')

  return response.generations[0].text

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