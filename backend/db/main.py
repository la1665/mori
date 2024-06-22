from pinecone import Pinecone, ServerlessSpec

from .dataset import dataframe
from .encoder import fetch_encode_image, encode_text

print("Running Pinecone ...")
# config pincone database connection
pc_api_key = "f084e9ba-0c29-4010-95ad-b63b0dda2263"
pc = Pinecone(api_key=pc_api_key)

index_name = "mori-image-search"
# check for available index name in Pinecone
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=512,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

    def truncate_text(text, max_length=77):
        return text[:max_length]

    def save_to_database(dataset):
        for data in dataset:
            text = data.get("name") + " " + data.get("description")
            text = truncate_text(text)
            text_vector = encode_text(text)

            image_vector = fetch_encode_image(data)
            combined_vector = (text_vector + image_vector) / 2

            metadata = {
                "description": data.get("description"),
                "link": data.get("link"),
                "images": data.get("images"),
                "name": data.get("name")
            }
            index.upsert([(str(data.get("id")), combined_vector, metadata)])

    save_to_database(dataframe)

index = pc.Index(index_name)
