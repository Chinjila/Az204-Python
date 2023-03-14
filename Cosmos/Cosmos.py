import os
import json
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential

endpoint = os.environ["COSMOS_ENDPOINT"]
DATABASE_NAME = "cosmicworks"
CONTAINER_NAME = "products"

credential = DefaultAzureCredential()
client = CosmosClient(url=endpoint, credential=credential)


new_item = {
    "id": "70b63682-b93a-4c77-aad2-65501347265f",
    "categoryId": "61dba35b-4f02-45c5-b648-c6badc0cbd79",
    "categoryName": "gear-surf-surfboards",
    "name": "Yamba Surfboard",
    "quantity": 12,
    "sale": False,
}

container.create_item(new_item)