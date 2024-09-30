Human and Social Services Chatbot

Overview

The Human and Social Services Chatbot is designed to enhance access to social services information for citizens. By leveraging advanced natural language processing (NLP) and large language models (LLMs), the chatbot provides users with timely, relevant responses to their inquiries about various social services.

Business Outcomes

Improved Accessibility: Citizens can easily access information about social services 24/7, reducing barriers to support.
Efficiency in Service Delivery: The chatbot streamlines the process of finding resources, minimizing the time users spend searching for assistance.
Enhanced User Experience: By providing immediate responses, the chatbot improves user satisfaction and engagement with social services.
Data-Driven Insights: Feedback and interaction data collected from users help refine services and identify gaps in community needs.

Technologies Used
Flask: A micro web framework for Python that provides the foundation for building the chatbot's web server.
Natural Language Toolkit (NLTK): A powerful library for NLP tasks, used for tokenizing and categorizing user input.
Pandas: A data manipulation library that facilitates handling user feedback and resource management through CSV files.
Transformers Library: Used for integrating pre-trained language models (e.g., GPT-2) to generate contextually relevant responses.
JSON: For structuring and managing resource data and user feedback.
Logging: Comprehensive logging is implemented across modules to track interactions, errors, and performance metrics.

Getting Started
Prerequisites
Python 3.x
Required libraries (install via pip):
pip install flask nltk pandas transformers
Installation
Clone the repository:


git clone <repository_url>
cd Human-and-Social-Services-Chatbot
Set up the environment (optional but recommended):

b
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Run the application:

python src/app.py
Usage
Send a POST request to the /chat endpoint with a JSON payload:

{
    "message": "Can you provide information on social services?"
}

Feedback and Logging
User interactions are logged, and feedback is stored in a CSV file for future analysis. Check user_feedback.csv in the data directory for logged interactions.