
import streamlit as st
import pandas as pd
from recommendation import recommend_titles, df

# Page configuration
st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Styling
st.markdown("""
<style>
.stApp {
    background-color: #111111;
    color: white;
}
h1 {
    color: #E50914;
}
div.stButton > button {
    background-color: #E50914;
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎬 Netflix Content Recommendation System")
st.write(
    "Discover similar movies and TV shows using "
    "machine learning and content similarity."
)

st.divider()

# Dataset information
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Titles", f"{len(df):,}")

with col2:
    st.metric("Movies", int((df["type"] == "Movie").sum()))

with col3:
    st.metric("TV Shows", int((df["type"] == "TV Show").sum()))

st.divider()

# Title selection
titles = sorted(
    df["title"].dropna().astype(str).unique().tolist()
)

selected_title = st.selectbox(
    "Choose a Netflix title",
    titles,
    index=titles.index("Midnight Mass")
    if "Midnight Mass" in titles else 0
)

top_n = st.slider(
    "Number of recommendations",
    min_value=3,
    max_value=10,
    value=5
)

if st.button("Find Similar Titles", use_container_width=True):
    results = recommend_titles(selected_title, top_n=top_n)

    if results is not None and not results.empty:
        st.subheader(f"Recommendations for {selected_title}")

        results = results.reset_index(drop=True)

        for start in range(0, len(results), 2):
            cols = st.columns(2)

            for col, (_, item) in zip(
                cols,
                results.iloc[start:start + 2].iterrows()
            ):
                with col:
                    with st.container(border=True):
                        st.markdown(f"### {item['title']}")
                        st.caption(item["type"])
                        st.write(f"**Genres:** {item['listed_in']}")
                        st.progress(
                            max(
                                0.0,
                                min(1.0, float(item["similarity_score"]))
                            )
                        )
                        st.write(
                            "Similarity score: "
                            f"{item['similarity_score']:.4f}"
                        )

        st.caption(
            "Similarity scores measure metadata similarity, "
            "not the probability that you will like a title."
        )
    else:
        st.warning("No recommendations were generated.")

st.divider()

st.caption(
    "Built with Python, Pandas, Streamlit and scikit-learn | "
    
)
