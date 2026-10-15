
from recommendation import recommend_titles

def evaluate_title(title):
    print(f"\nEvaluating recommendations for: {title}")

    results = recommend_titles(title, top_n=5)

    if results is None or results.empty:
        print("No recommendations available.")
        return

    relevant_count = 0
    total_reviewed = 0

    print("\nReview each recommended title.")
    print("Judge relevance based on content similarity.")

    for _, row in results.iterrows():
        print("\nRecommended title:", row["title"])
        print("Type:", row["type"])
        print("Genres:", row["listed_in"])
        print("Similarity score:", row["similarity_score"])

        while True:
            answer = input(
                "Is this recommendation relevant? (y/n): "
            ).strip().lower()

            if answer in ("y", "n"):
                break

            print("Please enter y or n.")

        total_reviewed += 1

        if answer == "y":
            relevant_count += 1

    precision = relevant_count / total_reviewed

    print("\n========== EVALUATION REPORT ==========")
    print("Selected title:", title)
    print("Recommendations reviewed:", total_reviewed)
    print("Relevant recommendations:", relevant_count)
    print(f"Precision@5: {precision:.2f}")
    print(f"Precision percentage: {precision * 100:.1f}%")
    print("=======================================")

if __name__ == "__main__":
    evaluate_title("Ganglands")
    evaluate_title("Midnight Mass")
