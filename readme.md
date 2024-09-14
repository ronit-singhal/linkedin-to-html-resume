# LinkedIn to HTML Resume Generator

This project is a web application that generates an HTML resume from a LinkedIn PDF download using OpenAI's API. It provides a simple and efficient way to convert your LinkedIn profile into a well-structured, professional HTML resume.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload LinkedIn PDF profile
- Secure OpenAI API key input
- Generate HTML resume from LinkedIn PDF
- Modern and responsive user interface
- Easy-to-use web application

## Technologies Used

- Backend: Python, FastAPI
- Frontend: HTML, CSS, JavaScript
- PDF Processing: PDFplumber
- AI Integration: OpenAI API
- Deployment: GitHub Pages

## How It Works

1. The user uploads their LinkedIn profile PDF and provides their OpenAI API key.
2. The backend extracts text content from the PDF using PDFplumber.
3. The extracted content is sent to OpenAI's API, which generates a well-structured HTML resume.
4. The generated HTML resume is saved and made available for viewing.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/ronit-singhal/linkedin-to-html-resume.git
   cd linkedin-to-html-resume
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

2. Open your web browser and navigate to `http://localhost:8000`.

3. Upload your LinkedIn PDF and enter your OpenAI API key.

4. Click "Generate Resume" and wait for the process to complete.

5. View your generated HTML resume by clicking the provided link.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.