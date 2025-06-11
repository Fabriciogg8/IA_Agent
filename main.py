import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
# This file should contain the GEMINI_API_KEY variable
load_dotenv()
# Check if the GEMINI_API_KEY environment variable is set
api_key = os.environ.get("GEMINI_API_KEY") 

# Client initialization
client = genai.Client(api_key=api_key)

# Check if the user provided a prompt
# If no prompt is provided, print an error message and exit
# The prompt should be passed as the first argument after the script name   
if len(sys.argv) <= 1:
    print("Error: No prompt provided. Usage: python main.py <prompt>")
    sys.exit(1)

# The prompt is the first argument after the script name
# It can be a single word or a full sentence
# Example: python main.py "What is the capital of France?"
user_prompt = sys.argv[1]

# Check if --verbose is present (can be in any position after the prompt)
verbose_mode = "--verbose" in sys.argv

# Save the user promppt in a list of messages
# This is required by the Gemini API to generate a response
# The messages list contains a single message with the role "user"
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# Generate a response using the Gemini API
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)

# If verbose mode is enabled, print the user prompt and token counts
if verbose_mode:
    print(f"User prompt: {user_prompt}")
    print("Prompt tokens:",response.usage_metadata.prompt_token_count)
    print("Response tokens:",response.usage_metadata.candidates_token_count)
# Print the response text
print(response.text)
