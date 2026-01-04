import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Page configuration
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="✍️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for clean, modern styling
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 850px;
    }
    
    /* Remove default padding */
    .main > div {
        padding-top: 1rem;
    }
    
    /* Header Card */
    .header-card {
        background: linear-gradient(135deg, #0077B5 0%, #00A0DC 100%);
        border-radius: 24px;
        padding: 3.5rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(0, 119, 181, 0.4);
    }
    
    .header-card h1 {
        color: #ffffff;
        font-size: 3rem;
        margin: 0;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    .header-card p {
        color: #f0f9ff;
        font-size: 1.2rem;
        margin-top: 1rem;
        font-weight: 400;
    }
    
    /* Controls Box */
    .controls-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 2.5rem;
        margin-bottom: 2rem;
    }
    
    /* Box Title Styling */
    .box-title {
        color: #ffffff;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        text-align: center;
        display: block;
    }
    
    /* Dropdown Labels - Make visible */
    .stSelectbox label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Dropdown container styling */
    .stSelectbox > div > div {
        background: #ffffff !important;
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #0077B5;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #0077B5;
        box-shadow: 0 0 0 3px rgba(0, 119, 181, 0.2);
    }
    
    /* Make dropdown text visible - dark text on white background */
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #1e293b !important;
    }
    
    .stSelectbox div[data-baseweb="select"] span {
        color: #1e293b !important;
    }
    
    /* Dropdown options text */
    .stSelectbox input {
        color: #1e293b !important;
        background-color: #ffffff !important;
    }
    
    /* Dropdown arrow */
    .stSelectbox svg {
        fill: #1e293b !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #0077B5 0%, #00A0DC 100%);
        color: white;
        font-weight: 600;
        padding: 1rem 3rem;
        border-radius: 50px;
        border: none;
        font-size: 1.15rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0, 119, 181, 0.4);
        width: 100%;
        margin-top: 1.5rem;
        letter-spacing: 0.3px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0, 119, 181, 0.5);
        background: linear-gradient(135deg, #006399 0%, #0090c4 100%);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Post Display Box */
    .post-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 2.5rem;
        margin-top: 2rem;
        border-left: 5px solid #0077B5;
    }
    
    /* Post Content Box */
    .post-text {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 16px;
        line-height: 1.8;
        font-size: 1.05rem;
        color: #1e293b;
        white-space: pre-wrap;
        border: 1px solid rgba(255, 255, 255, 0.2);
        min-height: 100px;
        margin-bottom: 1.5rem;
    }
    
    /* Metadata Pills Container */
    .metadata-pills {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 1.5rem;
        justify-content: center;
    }
    
    .metadata-pill {
        background: rgba(96, 165, 250, 0.15);
        border: 1px solid rgba(96, 165, 250, 0.3);
        color: #93c5fd;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    .metadata-pill strong {
        color: #dbeafe;
        font-weight: 600;
    }
    
    /* Copy Button */
    div[data-testid="column"]:has(.copy-button) {
        display: flex;
        justify-content: center;
    }
    
    .copy-button button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4) !important;
        margin-top: 0.5rem;
    }
    
    .copy-button button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5) !important;
    }
    
    /* Success Alert */
    .stSuccess {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 12px;
        color: #6ee7b7;
    }
    
    /* Error Alert */
    .stError {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 12px;
        color: #fca5a5;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #0077B5 !important;
    }
    
    /* Footer */
    .custom-footer {
        text-align: center;
        padding: 2.5rem 0 1rem 0;
        color: #94a3b8;
        font-size: 0.9rem;
        margin-top: 3rem;
    }
    
    /* Remove all white boxes from columns */
    [data-testid="column"] {
        background: transparent !important;
    }
    
    [data-testid="stVerticalBlock"] {
        background: transparent !important;
    }
    
    [data-testid="stHorizontalBlock"] {
        background: transparent !important;
    }
    
    div[data-testid="stExpander"] {
        background: transparent !important;
        border: none !important;
    }
    
    /* Remove white background from all elements */
    div[class*="element-container"] {
        background: transparent !important;
    }
    </style>
""", unsafe_allow_html=True)

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    # Header Section
    st.markdown("""
        <div class="header-card">
            <h1>✍️ LinkedIn Post Generator</h1>
            <p>Create engaging, professional LinkedIn posts powered by AI</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Initialize FewShotPosts
    fs = FewShotPosts()
    tags = sorted(fs.get_tags())
    
    # Controls Section - Title INSIDE the box
    st.markdown("""
        <div class="controls-box">
            <div class="box-title">🎯 Customize Your Post</div>
    """, unsafe_allow_html=True)
    
    # Create three columns for dropdowns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_tag = st.selectbox(
            "📌 Topic",
            options=tags,
            help="Choose the topic for your LinkedIn post",
            key="topic_select"
        )
    
    with col2:
        selected_length = st.selectbox(
            "📏 Length",
            options=length_options,
            help="Select the desired length of your post",
            key="length_select"
        )
    
    with col3:
        selected_language = st.selectbox(
            "🌐 Language",
            options=language_options,
            help="Choose the language for your post",
            key="language_select"
        )
    
    # Generate button
    generate_clicked = st.button("✨ Generate Post", key="generate_btn")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Generate and display post
    if generate_clicked:
        with st.spinner("🤖 Crafting your perfect LinkedIn post..."):
            try:
                post = generate_post(selected_length, selected_language, selected_tag)
                
                # Store in session state
                st.session_state.generated_post = post
                st.session_state.post_metadata = {
                    'topic': selected_tag,
                    'length': selected_length,
                    'language': selected_language
                }
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
    
    # Display generated post if exists
    if 'generated_post' in st.session_state:
        # Post Section - Title INSIDE the box
        st.markdown("""
            <div class="post-box">
                <div class="box-title">📝 Your Generated Post</div>
        """, unsafe_allow_html=True)
        
        # Post content
        st.markdown(f'<div class="post-text">{st.session_state.generated_post}</div>', unsafe_allow_html=True)
        
        # Metadata pills INSIDE the box
        metadata = st.session_state.post_metadata
        st.markdown(f"""
            <div class="metadata-pills">
                <div class="metadata-pill">📌 <strong>Topic:</strong> {metadata['topic']}</div>
                <div class="metadata-pill">📏 <strong>Length:</strong> {metadata['length']}</div>
                <div class="metadata-pill">🌐 <strong>Language:</strong> {metadata['language']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Copy button below the box
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div class="copy-button">', unsafe_allow_html=True)
            if st.button("📋 Copy to Clipboard", key="copy_btn"):
                st.success("✅ Select the text above and press Ctrl+C (Cmd+C on Mac)")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div class="custom-footer">
            Made with ❤️ using Streamlit • Powered by Groq & LangChain
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()