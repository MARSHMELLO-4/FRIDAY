import openai
from openai.error import RateLimitError

# Set the API key
openai.api_key = "sk-proj-pdPGNQWGtJcip2lI1EnKT3BlbkFJoGywRFgUeVRwn593eyjR"

try:
    # Generate a chat completion
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    # Print the response
    print(completion.choices[0].message['content'])

except RateLimitError as e:
    print("Rate limit exceeded. Please check your plan and billing details.")
    print(f"Error details: {e}")
