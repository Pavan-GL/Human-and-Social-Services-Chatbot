import logging
from llm_model import LLMModel
from nlp_utils import NLPUtils
from resource_manager import ResourceManager
from feedback_handler import FeedbackHandler

# Configure logging
logging.basicConfig(filename='chatbot.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

class Chatbot:
    def __init__(self):
        self.llm_model = LLMModel()
        self.nlp_utils = NLPUtils()
        self.resource_manager = ResourceManager()
        self.feedback_handler = FeedbackHandler()
        logging.info("Chatbot initialized.")

    def get_response(self, user_input):
        try:
            logging.info(f"Received user input: {user_input}")
            category = self.nlp_utils.categorize_request(user_input)
            resources = self.resource_manager.fetch_resources(category)

            if resources:
                # Extracting relevant details from the resources
                resource_strings = []
                for resource in resources:
                    details = (
                        f"{resource['name']} (Address: {resource['address']}, "
                        f"Phone: {resource['phone']}, Website: {resource['website']})"
                    )
                    resource_strings.append(details)
                response = f"I found some resources for you: {', '.join(resource_strings)}"
                logging.info(f"Found resources: {resources}")
            else:
                response = self.llm_model.generate_response(user_input)
                logging.info("No resources found, generating response using LLM.")
            
            return response
        
        except Exception as e:
            logging.error(f"Error in get_response: {e}")
            return "I'm sorry, but something went wrong. Please try again later."

    def log_user_feedback(self, user_input, feedback):
        self.feedback_handler.log_feedback(user_input, feedback)
