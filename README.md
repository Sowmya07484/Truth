# 🛡️ TruthGuard

**TruthGuard** is an AI-powered platform designed to detect misinformation across digital media. It helps users identify fake news, deepfake images, verify sources, and report suspicious content in the community.  

This project was developed for hackathon purposes and includes an interactive, user-friendly Streamlit interface with light and dark mode support.

---

## 🌟 Features

### Home Page
- Overview of TruthGuard capabilities
- Hackathon-style feature cards:
  - 📰 **Fake News Detection**
  - 🖼 **Image Deepfake Detection**
  - 🌐 **Source Verification**
  - 👥 **Community Reporting**

### Fake News Detector
- Paste a news article to check its credibility.
- Displays a **credibility score** and verdict:
  - ✅ Real
  - ℹ️ Likely Real
  - ⚠️ Likely Fake
  - ❌ Fake

### Image Deepfake Detector
- Upload images (`.png`, `.jpg`, `.jpeg`) to detect AI-generated or manipulated content.
- Returns **image authenticity score** and verdict.

### Source Verification
- Check a news URL for trustworthiness.
- Classifies sources as:
  - Trusted
  - Unreliable
  - Neutral/Unknown

### Community Report
- Users can report suspicious news or content.
- View all flagged content and reasons submitted by the community.

---

## 🎨 UI / UX Features
- Light Mode and Dark Mode with clear, readable text in all modes.
- Hackathon-style feature cards for a modern look.
- Responsive layout using Streamlit columns.
- Styled buttons, inputs, and text areas for better user experience.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/TruthGuard.git
   cd TruthGuard
