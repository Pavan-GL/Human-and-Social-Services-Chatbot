import pandas as pd
import logging
import os

# Configure logging
logging.basicConfig(filename='feedback_handler.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

class FeedbackHandler:
    def __init__(self, feedback_file='D:/Human and Social Services Chatbot/data/user_feedback.csv'):

        self.feedback_file = feedback_file
        logging.info("FeedbackHandler initialized with feedback file: %s", feedback_file)

        # Create the feedback file and add headers if it does not exist
        if not os.path.exists(self.feedback_file):
            with open(self.feedback_file, 'w') as f:
                f.write('User Input,Bot Response\n')
            logging.info("Feedback file created: %s", self.feedback_file)

    def log_feedback(self, user_input, response):
        try:
            logging.info("Logging feedback for user input: %s", user_input)
            feedback = pd.DataFrame([[user_input, response]], columns=['User Input', 'Bot Response'])
            feedback.to_csv(self.feedback_file, mode='a', header=False, index=False)
            logging.info("Feedback logged successfully.")

        except Exception as e:
            logging.error("Error logging feedback: %s", e)

# Example usage
if __name__ == '__main__':
    feedback_handler = FeedbackHandler()
    feedback_handler.log_feedback("What is the capital of France?", "The capital of France is Paris.")
