from .config import index
from .dataset import dataframe
from .encoder import fetch_encode_image, encode_text


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


if __name__ == "__main__":
    save_to_database(dataframe)
    vector_id = "2089163"
    vector_info = index.fetch([vector_id,])

    print(f"Vector ID: {vector_id}")
    print(f"Vector Embedding: {vector_info['vectors'][vector_id]}")
