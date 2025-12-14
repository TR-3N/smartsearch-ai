import streamlit as st
import requests
from streamlit_extras.buy_me_a_coffee import button
from streamlit_option_menu import option_menu

# Set Streamlit page config
st.set_page_config(
    page_title="SmartSearch-AI",
    page_icon="🔍",
    layout="wide",
)

# Glassmorphism CSS for the UI design
glass_style = """
<style>
    body {
        background: linear-gradient(to right, #dfe9f3, #ffffff);
        font-family: 'Arial', sans-serif;
    }
    .glass {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
        margin: 2rem;
    }
    .title {
        font-size: 4rem;
        font-weight: bold;
        text-align: center;
        color: #0f2027;
        margin-bottom: 20px;
        text-transform: uppercase;
        background: linear-gradient(to right, #6a11cb, #2575fc);
        -webkit-background-clip: text;
        color: transparent;
        animation: headlineAnimation 3s ease-in-out infinite;
    }
    @keyframes headlineAnimation {
        0% { opacity: 0.8; }
        50% { opacity: 1; }
        100% { opacity: 0.8; }
    }
    .subtitle {
        font-size: 1.5rem;
        text-align: center;
        color: #333;
        margin-bottom: 30px;
    }
    .searchbox {
        width: 100%;
        padding: 14px;
        border-radius: 10px;
        border: 1px solid #ccc;
        margin-bottom: 20px;
        font-size: 1.1rem;
        background-color: #f7f7f7;
    }
    .searchbox:focus {
        border-color: #0f2027;
        outline: none;
    }
    .tool-card {
        padding: 15px;
        margin-bottom: 15px;
        background: rgba(255, 255, 255, 0.75);
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .tool-card h3 {
        color: #0f2027;
    }
    .tool-card p {
        color: #555;
    }
</style>
"""

st.markdown(glass_style, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="SmartSearch-AI",
        options=["Home", "About", "Contact"],
        icons=["house", "info-circle", "envelope"],
        menu_icon="robot",
        default_index=0,
    )

if selected == "Home":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown('<div class="title">SmartSearch-AI 🔍</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Discover futuristic AI tools smarter than ever!</div>', unsafe_allow_html=True)

    query = st.text_input("🔎 Search for AI tools by name, industry, or use-case...", key="search", placeholder="e.g., healthcare, education, chatbots...")

    if query:
        try:
            response = requests.post("http://localhost:5000/search", json={"query": query})
            results = response.json()

            if results:
                for tool in results:
                    st.markdown('<div class="tool-card">', unsafe_allow_html=True)
                    st.write(f"**Tool Name:** {tool['name']}")
                    st.write(f"**Description:** {tool['description']}")
                    if 'link' in tool and tool['link']:
                        st.write(f"**Link:** [Click here]({tool['link']})")
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("No AI tool found matching your search 🚀")
        except Exception as e:
            st.error("Failed to fetch search results from backend.")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "About":
    st.title("About SmartSearch-AI")
    st.info("""
    SmartSearch-AI is your personalized futuristic AI tool discovery platform.
    Curated with love ❤️ to help you find the best AI innovations across the globe.
    """)

elif selected == "Contact":
    st.title("Contact Us")
    st.write("📩 Email: contact@smartsearchai.tech")
    button(username="achalsinha", floating=True, width=221)
