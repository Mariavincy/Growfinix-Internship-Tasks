import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/ali-vilab/text-to-video-ms-1.7b"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

prompt = input("Enter video prompt: ")

print("Generating video... Please wait.")

try:
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt},
        timeout=300
    )

    if response.status_code == 200:
        with open("output.mp4", "wb") as f:
            f.write(response.content)

        print("✅ Video saved successfully as output.mp4")

    else:
        print("❌ Error:", response.status_code)
        print(response.text)

except requests.exceptions.ConnectionError:
    print("❌ Unable to connect to Hugging Face API.")
    print("Check your internet connection, DNS settings, or try another network.")

except Exception as e:
    print("❌", e)