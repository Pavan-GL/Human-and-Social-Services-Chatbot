import json
import logging

# Configure logging
logging.basicConfig(filename='resource_manager.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

class ResourceManager:
    def __init__(self, resource_file='D:\Human and Social Services Chatbot\data\local_resources.json'):
        self.resource_file = resource_file
        logging.info("ResourceManager initialized with resource file: %s", resource_file)

    def fetch_resources(self, category):
        try:
            logging.info("Fetching resources for category: %s", category)
            with open(self.resource_file) as f:
                resources = json.load(f)

            fetched_resources = resources.get(category, [])
            logging.info("Fetched resources: %s", fetched_resources)
            return fetched_resources
        
        except FileNotFoundError:
            logging.error("Resource file not found: %s", self.resource_file)
            return []
        
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from resource file: %s", self.resource_file)
            return []
        
        except Exception as e:
            logging.error("Error fetching resources: %s", e)
            return []

# Example usage:
if __name__ == '__main__':
    resource_manager = ResourceManager()
    category = "housing"
    resources = resource_manager.fetch_resources(category)
    print(f"Resources for '{category}': {resources}")
