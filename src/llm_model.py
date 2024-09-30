import logging
from transformers import pipeline

# Configure logging
logging.basicConfig(filename='llm_model.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

class LLMModel:
    def __init__(self):
        try:
            self.generator = pipeline('text-generation', model='gpt2')
            logging.info("LLMModel initialized with GPT-2 model.")
        except Exception as e:
            logging.error(f"Failed to initialize LLMModel: {e}")
            raise RuntimeError("Model initialization failed.") from e

    def generate_response(self, user_input):
        try:
            logging.info(f"Generating response for user input: {user_input}")
            response = self.generator(user_input, max_length=50)[0]['generated_text']
            logging.info("Response generated successfully.")
            return response.strip()
        
        
        except Exception as e:
            logging.error(f"Error during response generation: {e}")
            return "I'm sorry, but something went wrong. Please try again later."
