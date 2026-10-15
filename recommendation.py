import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("Dataset.csv")

print("Dataset loaded:", df.shape)


features = [
    "title",
    "type",
    "director",
    "country",
    "rating",
    "listed_in"
]

content = df[features].fillna("").copy()


content["combined_features"] = (
    content["listed_in"].astype(str) + " " +
    content["type"].astype(str) + " " +
    content["director"].astype(str) + " " +
    content["country"].astype(str) + " " +
    content["rating"].astype(str)
)


tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(
    content["combined_features"]
)

print("TF-IDF matrix shape:", tfidf_matrix.shape)


def recommend_titles(title, top_n=5):
    matches = content.index[
        content["title"].str.casefold() == title.strip().casefold()
    ].tolist()

    if not matches:
        print("Title not found:", title)
        return

    index = matches[0]

    scores = cosine_similarity(
        tfidf_matrix[index],
        tfidf_matrix
    ).flatten()

    
    scores[index] = -1

    
    top_indices = scores.argsort()[::-1][:top_n]

    results = content.iloc[top_indices][
        ["title", "type", "listed_in"]
    ].copy()

    results["similarity_score"] = [
        round(float(scores[i]), 4) for i in top_indices
    ]

    return results


if __name__ == "__main__":
    selected_title = "Ganglands"

    print("\nRecommendations for:", selected_title)

    results = recommend_titles(selected_title)

    if results is not None:
        print(results.to_string(index=False))
