
# Netflix Content Recommendation System

## Project Overview
A content-based recommendation system that suggests
similar Netflix titles using metadata such as genres,
content type, director, country, and rating.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## Dataset
The supplied Netflix dataset contains 8,790 titles
and 10 columns.

## Methodology
1. Load and inspect the dataset.
2. Prepare content-related features.
3. Convert text into numerical representations using TF-IDF.
4. Calculate cosine similarity between titles.
5. Rank titles and return the top five recommendations.

## Model Evaluation and Experiments

### Test Cases
- Ganglands
- Midnight Mass

### Experiment 1: Genre Weighting
The genre field was repeated to give genre information
additional influence in the TF-IDF representation.

### Experiment 2: Standard Genre Weighting
The genre field was included once alongside content
type, director, country, and rating.

### Observations
Both configurations generated five recommendations
for each selected title. Recommendation rankings and
similarity scores changed when feature representation
was modified.

## Recommendation Quality Evaluation

### Evaluation Method
Precision@5 was used to evaluate recommendation
relevance. Each of the five recommendations for a
selected title was manually judged as relevant or
not relevant based on content similarity.

### Results

| Selected Title | Relevant | Reviewed | Precision@5 |
|---|---:|---:|---:|
| Ganglands | 3 | 5 | 0.60 (60%) |
| Midnight Mass | 2 | 5 | 0.40 (40%) |
| Combined | 5 | 10 | 0.50 (50%) |

### Interpretation
Three of five recommendations for Ganglands and
two of five recommendations for Midnight Mass were
judged relevant. Across both test cases, five of
ten recommendations were judged relevant.

### Limitations
The evaluation uses subjective manual judgments and
only two selected titles. It does not measure actual
user satisfaction or general recommendation accuracy.
The dataset does not contain user feedback or
ground-truth preference labels for this evaluation.

### Future Improvements
- Test additional titles.
- Compare different feature configurations.
- Evaluate genre overlap and content relevance.
- Improve feature selection based on observed results.

## How to Run

1. Install the required dependencies:
   pip install -r requirements.txt

2. Place Dataset.csv in the project folder.

3. Run the recommendation system:
   python recommendation.py

4. Run the manual evaluation:
   python evaluate_recommendations.py

## Project Files
- recommendation.py: Recommendation system implementation.
- evaluate_recommendations.py: Manual relevance evaluation.
- Dataset.csv: Dataset used by the model.
- requirements.txt: Python dependencies.
- screenshots/: Project and evaluation screenshots.
