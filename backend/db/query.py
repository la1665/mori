from .config import index
from .encoder import encode_text


def search_database(query, top_k=5):
    """searching database with given query."""
    query_vector = encode_text(query)
    query_vector_list = query_vector.tolist()
    results = index.query(vector=query_vector_list, top_k=top_k,
                          include_metadata=True, include_values=True)

    return results


if __name__ == "__main__":
    search_database("black shoes")
