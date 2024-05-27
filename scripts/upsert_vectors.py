from pinecone import Pinecone, PodSpec
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.environ.get("API_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT")
METRIC = os.getenv("METRIC")
DIMENSION = int(os.getenv("DIMENSION"))
INDEX_NAME = "datacamp-index"

pc = Pinecone(api_key=API_KEY)
index = pc.Index(INDEX_NAME)


index.upsert(
    vectors=[
        {
            "id": "1",
            "values": [0.22, 0.33, 0.33, 0.55, 0.66],
            "metadata": {"genre": "romance", "year": "2022"},
        },
        {
            "id": "2",
            "values": [0.35, 0.45, 0.55, 0.65, 0.75],
            "metadata": {"genre": "thriller", "year": "2015"},
        },
        {
            "id": "3",
            "values": [0.25, 0.36, 0.45, 0.52, 0.61],
            "metadata": {"genre": "documentry", "year": "2010"},
        },
        {
            "id": "4",
            "values": [0.22, 0.37, 0.39, 0.66, 0.64],
            "metadata": {"genre": "crime", "year": "2024"},
        },
    ]
)


print("\n Index Description : \n \n ", index.describe_index_stats())

