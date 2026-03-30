import streamlit as st
import pickle
# import nbimporter
from model import recommend

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');
 
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
 
/* Background */
.stApp {
    background: #0f0e17;
}
 
/* Sidebar */
[data-testid="stSidebar"] {
    background: #13121f !important;
    border-right: 1px solid #2a2840;
}
 
/* Header */
.main-header {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem;
    font-weight: 900;
    background: linear-gradient(135deg, #f5a623 0%, #f76b1c 50%, #e84393 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin-bottom: 0.2rem;
}
 
.sub-header {
    color: #7b7a8e;
    font-size: 1rem;
    font-weight: 300;
    letter-spacing: 0.05em;
    margin-bottom: 2rem;
}
 
/* Book card */
.book-card {
    background: linear-gradient(145deg, #1c1b2e, #14131f);
    border: 1px solid #2a2840;
    border-radius: 16px;
    padding: 16px 12px;
    text-align: center;
    height: 360px;
    overflow: hidden;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    position: relative;
}
.book-card:hover {
    transform: translateY(-6px);
    border-color: #f5a623;
    box-shadow: 0 12px 32px rgba(245,166,35,0.15);
}
.book-card img {
    width: 110px;
    height: 155px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 10px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.5);
}
.book-title {
    font-family: 'Playfair Display', serif;
    font-size: 13px;
    font-weight: 700;
    color: #e8e6f0;
    line-height: 1.35;
    margin-bottom: 5px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.book-author {
    font-size: 11px;
    color: #7b7a8e;
    margin-bottom: 8px;
    font-style: italic;
}
.book-meta {
    font-size: 11px;
    color: #f5a623;
    font-weight: 500;
    letter-spacing: 0.03em;
}
.badge {
    display: inline-block;
    background: rgba(245,166,35,0.12);
    border: 1px solid rgba(245,166,35,0.3);
    color: #f5a623;
    font-size: 10px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 20px;
    margin-top: 5px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
 
/* Section label */
.section-label {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #e8e6f0;
    margin: 1.5rem 0 0.25rem 0;
    border-left: 4px solid #f5a623;
    padding-left: 12px;
}
 
/* Divider */
.fancy-divider {
    border: none;
    height: 1px;
    background: linear-gradient(to right, #f5a623, transparent);
    margin: 1rem 0 1.5rem 0;
}
 
/* Streamlit button override */
.stButton > button {
    background: linear-gradient(135deg, #f5a623, #f76b1c) !important;
    color: #0f0e17 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 2rem !important;
    font-family: 'DM Sans', sans-serif !important;
    letter-spacing: 0.04em !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
}
 
/* Selectbox / text_input labels */
label {
    color: #a09fb8 !important;
    font-size: 0.85rem !important;
}
 
/* Metric cards */
.metric-row {
    display: flex;
    gap: 12px;
    margin-bottom: 1.5rem;
}
.metric-box {
    flex: 1;
    background: #1c1b2e;
    border: 1px solid #2a2840;
    border-radius: 12px;
    padding: 14px 16px;
    text-align: center;
}
.metric-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    font-weight: 900;
    color: #f5a623;
}
.metric-label {
    font-size: 11px;
    color: #7b7a8e;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 2px;
}
 
/* Sidebar nav */
.nav-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 900;
    color: #f5a623;
    margin-bottom: 0.2rem;
}
.nav-subtitle {
    font-size: 0.75rem;
    color: #7b7a8e;
    margin-bottom: 1.5rem;
    letter-spacing: 0.05em;
}
</style>
""", unsafe_allow_html=True)


books = pickle.load(open('books.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
popular_df = pickle.load(open('popular_df.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

st.title("📖 Book Recommendation System")

page = st.sidebar.radio("Menu", ["Popular", "Recommend"])

if page == "Popular":
    st.header("🔥 Popular Books")

    for i in range(0, len(popular_df), 5):
        cols = st.columns(5)
        for col, (_, row) in zip(cols, popular_df.iloc[i:i+5].iterrows()):
            with col:
                st.image(row["Image-URL-M"], width=120)
                st.write(row["Book-Title"])
                st.caption(row["Book-Author"])
                st.write(f"⭐ {round(row['avg_rating'], 2)}")

else:
    st.header("🔍 Get Recommendations")

    book_name = st.selectbox("Select a book", pt.index.tolist())

    if st.button("Recommend"):
        results = recommend(book_name)

        # st.write(results)

        cols = st.columns(5)

        for col, book in zip(cols, results):
            with col:
                st.image(book[2], width=120)   # list format
                st.write(book[0])
                st.caption(book[1])
         
          
