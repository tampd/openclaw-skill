
import requests
import json
import os

# WordPress API endpoint
api_url = "https://blog.chaiko.info/wp-json/wp/v2/posts"

# Authentication credentials
username = "admin"
password = "tRy5 Bx9U 3sHl 92A7 ayNs ZxfH"

# Read content from the Markdown file
file_path = "agentic_ai_2026.md"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: File not found: {file_path}")
    exit()
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Prepare the payload
payload = {
    "title": "Agentic AI in 2026",  # You might want to extract this from the file content
    "content": content,
    "status": "publish",  # Set to "draft" if you want to save as a draft
}

# Encode credentials
import base64
auth_string = f"{username}:{password}"
encoded_auth = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

# Set headers
headers = {
    "Authorization": f"Basic {encoded_auth}",
    "Content-Type": "application/json",
}

# Make the API request
try:
    response = requests.post(api_url, headers=headers, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"))
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    # Print the response
    print("Status Code:", response.status_code)
    print("Response:", response.json())

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
