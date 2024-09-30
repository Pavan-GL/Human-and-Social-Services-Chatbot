import logging
import nltk
from nltk.tokenize import word_tokenize

# Ensure that the punkt tokenizer is downloaded
nltk.download('punkt')

# Configure logging
logging.basicConfig(filename='nlp_utils.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

class NLPUtils:
    def __init__(self):
        logging.info("NLPUtils initialized.")

    def categorize_request(self, user_input):
        try:
            logging.info(f"Categorizing user input: {user_input}")
            tokens = word_tokenize(user_input.lower())
            logging.debug(f"Tokenized input: {tokens}")

            if 'housing' in tokens:
                category = 'housing'
            elif 'health' in tokens:
                category = 'healthcare'
            elif 'food' in tokens:
                category = 'food assistance'
            else:
                category = 'general inquiry'
            
            logging.info(f"Categorized input as: {category}")
            return category

        except Exception as e:
            logging.error(f"Error in categorize_request: {e}")
            return 'general inquiry'  # Fallback category on error
