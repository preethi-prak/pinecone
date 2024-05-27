from pinecone import Pinecone,PodSpec
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY=os.environ.get("API_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT")
METRIC = os.getenv("METRIC")
DIMENSION = int(os.getenv("DIMENSION"))
INDEX_NAME = "datacamp-index"

pc = Pinecone(
        api_key=API_KEY
    )
existing_indexes = pc.list_indexes()
print("\n Existing indexes:", existing_indexes.indexes)

# Check if the specified index exists and delete it
if any(index.name == INDEX_NAME for index in existing_indexes.indexes):
    pc.delete_index(INDEX_NAME)
    print(f"\n Index '{INDEX_NAME}' deleted successfully. ")


# Create the Pinecone index
pc.create_index(name=INDEX_NAME, spec=PodSpec(environment=ENVIRONMENT), dimension=DIMENSION, metric=METRIC)
print(f"\n Index '{INDEX_NAME}' created successfully.")

# Verify the index creation
print("\n Updated indexes:", pc.list_indexes())