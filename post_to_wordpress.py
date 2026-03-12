
import requests
import json
import os
import base64

# WordPress API endpoint
api_url = os.environ.get("WP_API_URL", "https://blog.chaiko.info/wp-json/wp/v2/posts")

# Authentication credentials (from .env or environment)
username = os.environ.get("WP_USERNAME", "admin")
password = os.environ.get("WP_APP_PASSWORD", "")
if not password:
    # Fallback: read from credentials file
    cred_file = os.path.join(os.path.dirname(__file__), "wp_credentials.txt")
    if os.path.exists(cred_file):
        with open(cred_file) as f:
            for line in f:
                if "WP_APP_PASSWORD" in line:
                    password = line.split("=", 1)[1].strip().strip('"')
    if not password:
        print("Error: WP_APP_PASSWORD not set. Set env var or check wp_credentials.txt")
        exit(1)

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
