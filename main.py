from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pdfplumber
import openai

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r") as f:
        return f.read()

@app.post("/generate_resume")
async def generate_resume(file: UploadFile = File(...), api_key: str = Form(...)):
    # Read PDF content
    with pdfplumber.open(file.file) as pdf:
        text_content = ""
        for page in pdf.pages:
            text_content += page.extract_text()

    # Set OpenAI API key
    openai.api_key = api_key

    # Generate resume using OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """You are an expert resume writer with deep expertise in professional resume formatting and HTML structure. Using the LinkedIn profile information provided, generate a well-structured, responsive HTML resume that follows these specific guidelines:

                                            - Include the following sections in this exact order: Name, Contact Information, Summary, Professional Experience, Education, Skills, Certifications, any remaining sections.
                                            - Format the content using semantic HTML tags (e.g., <header>, <section>, <ul>, <li>) for clear readability.
                                            - Ensure proper use of headings (<h1>, <h2>, etc.), paragraphs, and bullet points.
                                            - Focus on clean, modern design principles with minimal use of styles, avoiding any inline CSS or JavaScript.
                                            - Do not add any additional text or commentary; only generate the HTML code.

                                            Start immediately with the HTML code and stop after it is fully generated.

                                            LinkedIn Profile Information:"""},
            {"role": "user", "content": text_content}
        ]
    )

    generated_html = response.choices[0].message.content

    # Save generated HTML to a file
    with open("static/generated_resume.html", "w") as f:
        f.write(generated_html)

    return {"message": "Resume generated successfully", "file_path": "/static/generated_resume.html"}