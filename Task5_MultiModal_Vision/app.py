from flask import Flask, request, render_template
from google import genai
from dotenv import load_dotenv
from PIL import Image
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["image"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    image = Image.open(path)

    prompt = """
    Analyze the uploaded image.

    1. If the image contains handwritten or printed text,
     transcribe the text accurately.

    2. If the image shows a damaged or broken appliance,
    identify the problem and suggest a possible solution.

    3. If neither applies, describe what is present in the image.

    Return the answer clearly and neatly.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, image]
    )

    return f"""<h2>Analysis Result</h2><pre>{response.text}</pre>"""


if __name__ == "__main__":
    app.run(debug=True)