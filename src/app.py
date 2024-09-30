from flask import Flask, request, jsonify
import logging
from chatbot import Chatbot

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        
        if not user_input:
            logging.warning("Received empty message from client.")
            return jsonify({'error': 'Message is required'}), 400

        logging.info(f"User input: {user_input}")
        response = chatbot.get_response(user_input)
        logging.info(f"Chatbot response: {response}")

        return jsonify({'response': response})
    
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
