## OCR API

This is a FastAPI application that performs OCR (Optical Character Recognition) on an uploaded image.
## Getting Started

### Prerequisites

- Python 3.7 or higher
- Dependencies from requirements.txt (install using `pip install -r requirements.txt`)
- Google Cloud Vision API credentials (JSON key file)

### Setup

1. Clone the repository:
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
3. Set up Google Cloud Vision API credentials:
Download a Service Account Key JSON file from the Google Cloud Console.
Save the JSON key file as `google-credentials.json` in the root directory.
4. Run the FastAPI application
  Replace main with the name of your FastAPI app instance if different.
   ```bash
   pipenv shell
   uvicorn main:app --reload
5. http://127.0.0.1:8000/evaluate is the endpoint that accepts form-data as a request body.