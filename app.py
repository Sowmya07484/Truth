import streamlit as st
from fake_news_detector import detect_fake_news
from image_detector import detect_fake_image
from source_checker import check_source
from community_report import submit_report, get_all_reports
from PIL import Image

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="TruthGuard",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("🛡️ TruthGuard")
st.sidebar.markdown("AI Fake News & Deepfake Detector")

dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=True)

# ---------------- THEME STYLING ---------------- #
if dark_mode:
    st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top, #0b132b, #020617);
        color: white;
    }

    h1, h2, h3, h4, h5, h6, label, p, span {
        color: white !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #020617;
    }

    textarea, input {
        background-color: #1e293b !important;
        color: white !important;
        border-radius: 8px;
    }

    .stButton > button {
        background-color: #4f46e5;
        color: white !important;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
    }

    .stButton > button:hover {
        background-color: #6366f1;
    }

    .stFileUploader {
        border: 1px solid #475569;
        border-radius: 10px;
        padding: 10px;
    }

    hr {
        border: 1px solid #475569;
    }

    .feature-card {
        background: #1e293b;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }

    .stButton > button {
        background-color: #fbbf24;
        color: #0f172a !important;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
    }

    .stButton > button:hover {
        background-color: #f59e0b;
    }

    .feature-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------- NAVIGATION ---------------- #
option = st.sidebar.radio(
    "Select Feature",
    (
        "Home",
        "Fake News Detector",
        "Image Deepfake Detector",
        "Source Verification",
        "Community Report"
    )
)

# ---------------- HOME ---------------- #
if option == "Home":

    st.title("🛡️ TruthGuard")
    st.subheader("AI-Powered Fake News & Deepfake Detection Platform")

    st.markdown("""
    TruthGuard helps detect misinformation across digital media using Artificial Intelligence.

    ### 🔍 Platform Capabilities
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
        <h4>📰 Fake News Detection</h4>
        Detect misleading or fabricated news articles using AI.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
        <h4>🌐 Source Verification</h4>
        Verify whether a news source is trusted or unreliable.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
        <h4>🖼 Image Deepfake Detection</h4>
        Detect manipulated or AI generated images.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
        <h4>👥 Community Reporting</h4>
        Users can flag suspicious or misleading content.
        </div>
        """, unsafe_allow_html=True)

    st.info("Upload media or paste news to check authenticity.")

# ---------------- FAKE NEWS DETECTOR ---------------- #
elif option == "Fake News Detector":

    st.header("📰 Fake News Detector")
    news_text = st.text_area("Paste News Article Here", height=200)

    if st.button("Analyze News"):

        if news_text.strip() == "":
            st.warning("Please paste a news article first.")
        else:
            result = detect_fake_news(news_text)
            score = result["credibility_score"]
            verdict = result["verdict"]

            st.subheader("Analysis Result")
            st.progress(score / 100)
            st.write("Credibility Score:", score, "%")
            st.write("Verdict:", verdict)

            if verdict == "Fake":
                st.error("⚠️ This news is Fake")
            elif verdict == "Likely Fake":
                st.warning("⚠️ This news is Likely Fake")
            elif verdict == "Likely Real":
                st.info("ℹ️ This news is Likely Real")
            else:
                st.success("✅ This news appears Real")

# ---------------- IMAGE DEEPFAKE DETECTOR ---------------- #
elif option == "Image Deepfake Detector":

    st.header("🖼 Image Deepfake Detector")
    uploaded_image = st.file_uploader(
        "Upload an Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image is not None:

        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        result = detect_fake_image(uploaded_image)
        st.write("Image Score:", result["score"])
        st.write("Verdict:", result["verdict"])

        if result["verdict"] == "Fake":
            st.error("⚠️ This image may be a deepfake")
        else:
            st.success("✅ Image appears authentic")

# ---------------- SOURCE VERIFICATION ---------------- #
elif option == "Source Verification":

    st.header("🌐 Source Verification")
    url = st.text_input("Enter news URL")

    if st.button("Check Source"):

        if url.strip() == "":
            st.warning("Please enter a URL")
        else:
            result = check_source(url)
            if "Trusted" in result:
                st.success(result)
            elif "Unreliable" in result:
                st.error(result)
            else:
                st.info(result)

# ---------------- COMMUNITY REPORT ---------------- #
elif option == "Community Report":

    st.header("👥 Report Suspicious News")
    content = st.text_area("Report suspicious content")

    reason = st.selectbox(
        "Reason for report",
        [
            "Fake News",
            "Deepfake",
            "Misleading Information",
            "Other"
        ]
    )

    if st.button("Submit Report"):

        if content.strip() == "":
            st.warning("Please enter suspicious content")
        else:
            message = submit_report(content, reason)
            st.success(message)

    st.subheader("Community Flagged Content")
    reports = get_all_reports()

    if len(reports) == 0:
        st.info("No reports yet")

    for r in reports:
        st.markdown("---")
        st.write("**Content:**", r["content"])
        st.write("**Reason:**", r["reason"])
