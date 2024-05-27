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
print("\n Existing indexes: \n \n", existing_indexes.indexes)

#connection to index

index = pc.Index(INDEX_NAME) 
print("\n Index Description : \n \n ", index.describe_index_stats())

