from pinecone import Pinecone, ServerlessSpec

# config pincone database connection
pc_api_key = "f084e9ba-0c29-4010-95ad-b63b0dda2263"
pc = Pinecone(api_key=pc_api_key)

index_name = "mori-image-search"
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
index = pc.Index(index_name)
