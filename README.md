# Gemini Data Analyst

This project leverages Google Gemini Pro, Retrieval-Augmented Generation (RAG), and Streamlit to create an advanced AI-powered data analysis tool. Designed to assist data analysts, the application uses cutting-edge AI to provide insightful analyses, visualizations, and data-driven recommendations. The integration of Streamlit ensures a user-friendly interface, making it easy to interact with and interpret the analytical results.

#### Installation

To install the required packages, run:

```bash
pip install -r requirements.txt
```

#### Setting Up Gemini API
1. ##### Create Google Gemini API Key:
   - Visit the Google Cloud Console and create a new project.
   - Enable the Google Gemini Pro API for your project.
   - Create credentials (API key) and copy it.
2. ##### Create .env File:
   - Create a file named .env in the root directory of your project.
   - Add the following line to the .env file:
     ```bash
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

#### Running the Application

To run the application, execute the following command:

```bash
streamlit run app.py
```

##### Contributors
- Michael (ssabrut) - Project Lead & Developer
