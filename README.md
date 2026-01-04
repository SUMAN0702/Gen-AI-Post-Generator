# 🚀 LinkedIn Post Generator

An AI-powered application that generates engaging, professional LinkedIn posts based on topic, length, and language preferences. Built with Streamlit, LangChain, and Groq's LLM API.

<img width="1267" height="904" alt="Screenshot 2026-01-04 150243" src="https://github.com/user-attachments/assets/cec637c7-9a7b-4ad0-90f0-6d854b9336d1" />


## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Configuration](#configuration)
- [Future Enhancements](#future-enhancements)

## 🎯 Overview

The LinkedIn Post Generator leverages AI and few-shot learning to create contextually relevant LinkedIn posts. It analyzes existing high-engagement posts and generates new content that matches the style, tone, and format of successful posts in your chosen topic area.

## ✨ Features

- **Topic Selection**: Choose from multiple categories (Job Search, Mental Health, Career Advice, etc.)
- **Length Control**: Select post length (Short: 1-5 lines, Medium: 6-10 lines, Long: 11-15 lines)
- **Bilingual Support**: Generate posts in English or Hinglish (Hindi-English mix)
- **Few-Shot Learning**: Uses existing successful posts as examples for better output
- **Modern UI**: Beautiful, dark-themed interface with glassmorphism effects
- **Real-time Generation**: Fast post creation powered by Groq's LLaMA 3.3 70B model

## 🏗️ Architecture

### High-Level Architecture
![architecture](https://github.com/user-attachments/assets/17501b76-a38e-437d-8442-7b08869ff5b6)

```
┌─────────────────────────────────────────────────────────────────┐
│                         Streamlit Web App                        │
│                          (main.py)                               │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       │ User Input (Topic, Length, Language)
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Post Generator Layer                         │
│                     (post_generator.py)                          │
└──────────┬───────────────────────────────┬──────────────────────┘
           │                               │
           │                               │ Fetch Examples
           ▼                               ▼
┌──────────────────────┐      ┌──────────────────────────────────┐
│   LLM Helper         │      │    Few-Shot Posts Manager        │
│   (llm_helper.py)    │      │    (few_shot.py)                 │
│                      │      │                                  │
│  • Groq API Client   │      │  • Load processed posts          │
│  • LLaMA 3.3 70B     │      │  • Filter by criteria            │
│                      │      │  • Return matching examples      │
└──────────────────────┘      └──────────────────────────────────┘
           │                               │
           │                               │
           │                               ▼
           │                  ┌──────────────────────────────────┐
           │                  │   Processed Posts Database       │
           │                  │   (processed_posts.json)         │
           │                  │                                  │
           │                  │  • Tagged posts                  │
           │                  │  • Categorized by length         │
           │                  │  • Language-specific             │
           │                  └──────────────────────────────────┘
           │
           │ Generate Post
           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Generated Post                              │
│                  (Displayed in UI)                               │
└─────────────────────────────────────────────────────────────────┘
```

### Data Processing Pipeline

```
Raw Posts (raw_posts.json)
         │
         │ preprocess.py
         ▼
Extract Metadata (LLM)
   • Line count
   • Language detection
   • Topic tags
         │
         ▼
Unify Tags (LLM)
   • Merge similar tags
   • Standardize naming
         │
         ▼
Processed Posts (processed_posts.json)
         │
         ▼
Used for Few-Shot Learning
```

## 📁 Project Structure

```
linkedin-post-generator/
│
├── main.py                    # Streamlit UI application
├── post_generator.py          # Core post generation logic
├── few_shot.py               # Few-shot learning manager
├── llm_helper.py             # LLM API wrapper
├── preprocess.py             # Data preprocessing script
├── requirements.txt          # Python dependencies
│
├── data/
│   ├── raw_posts.json        # Original LinkedIn posts
│   └── processed_posts.json  # Processed & tagged posts
│
└── README.md                 # Project documentation
```

## 🛠️ Technologies Used

### Core Technologies

- **Streamlit** (v1.x): Web framework for the interactive UI
- **LangChain** (v0.x): Framework for LLM integration and prompt management
- **Groq API**: Fast inference with LLaMA 3.3 70B Versatile model
- **Python 3.8+**: Primary programming language

### Key Libraries

- **pandas**: Data manipulation and filtering
- **python-dotenv**: Environment variable management
- **langchain-groq**: Groq integration for LangChain
- **langchain-core**: Core LangChain components

### AI Model

- **LLaMA 3.3 70B Versatile**: Advanced large language model via Groq
  - Fast inference times (~1-2 seconds)
  - High-quality text generation
  - Context-aware responses

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com))

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/linkedin-post-generator.git
   cd linkedin-post-generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Prepare the data**
   
   If you need to reprocess posts:
   ```bash
   python preprocess.py
   ```

6. **Run the application**
   ```bash
   streamlit run main.py
   ```

7. **Access the app**
   
   Open your browser and navigate to `http://localhost:8501`

## 🎮 Usage

### Basic Workflow

1. **Select Topic**: Choose from available topics (e.g., Job Search, Mental Health, Career Advice)
2. **Choose Length**: Pick Short (1-5 lines), Medium (6-10 lines), or Long (11-15 lines)
3. **Select Language**: Choose English or Hinglish
4. **Generate**: Click "✨ Generate Post" button
5. **Copy**: Use the "📋 Copy to Clipboard" button to copy the generated post

### Example

**Input:**
- Topic: Mental Health
- Length: Medium
- Language: English

**Output:**
```
Taking care of your mental health isn't a luxury—it's essential.

In a world that glorifies hustle culture, remember that rest is productive too.

Your worth isn't measured by your productivity.

It's okay to take a break. It's okay to not be okay.

Prioritize yourself. You deserve it. 💚
```

## 🔧 How It Works

### 1. Data Preprocessing (`preprocess.py`)

The preprocessing pipeline:

1. **Loads raw posts** from `raw_posts.json`
2. **Extracts metadata** using LLM:
   - Line count
   - Language (English/Hinglish)
   - Topic tags
3. **Unifies tags** across all posts:
   - Merges similar tags (e.g., "Job Hunting" → "Job Search")
   - Standardizes capitalization
4. **Saves processed data** to `processed_posts.json`

### 2. Few-Shot Learning (`few_shot.py`)

The `FewShotPosts` class:

- Loads processed posts into a pandas DataFrame
- Categorizes posts by length (Short/Medium/Long)
- Filters posts based on:
  - Topic tags
  - Language
  - Length category
- Returns up to 2 matching examples for prompt engineering

### 3. Post Generation (`post_generator.py`)

Generation workflow:

1. **Build prompt** with:
   - User preferences (topic, length, language)
   - Retrieved few-shot examples (max 2)
   - Specific instructions
2. **Send to LLM** via Groq API
3. **Return generated post** to UI

### 4. LLM Integration (`llm_helper.py`)

- Initializes Groq client with API key
- Configures LLaMA 3.3 70B model
- Provides simple interface for LLM calls

### 5. User Interface (`main.py`)

Features:

- **Modern Design**: Glassmorphism with dark theme
- **Responsive Layout**: Centered design with proper spacing
- **Interactive Controls**: Dropdowns and buttons
- **Real-time Feedback**: Loading spinners and success messages
- **Session State**: Persists generated posts

## ⚙️ Configuration

### Environment Variables

Create a `.env` file:

```env
# Required
GROQ_API_KEY=gsk_your_api_key_here

# Optional (with defaults)
MODEL_NAME=llama-3.3-70b-versatile
MAX_TOKENS=1000
TEMPERATURE=0.7
```

### Customization Options

**Add New Topics:**

1. Add posts with new tags to `raw_posts.json`
2. Run `python preprocess.py` to reprocess
3. New tags will appear in the Topic dropdown

**Modify Post Lengths:**

Edit `post_generator.py`:
```python
def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"  # Modify as needed
    # ...
```

**Change UI Theme:**

Edit CSS in `main.py`:
```python
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        # Change colors here
    }
    </style>
""", unsafe_allow_html=True)
```

## 🚀 Future Enhancements

### Planned Features

- [ ] **Engagement Prediction**: Predict potential engagement score
- [ ] **Emoji Suggestions**: AI-powered emoji recommendations
- [ ] **Hashtag Generator**: Automatic relevant hashtag generation
- [ ] **Post Scheduler**: Integration with LinkedIn API for direct posting
- [ ] **Analytics Dashboard**: Track generated posts performance
- [ ] **Multi-language Support**: Add more languages (Spanish, French, etc.)
- [ ] **Post Variations**: Generate multiple variations of the same post
- [ ] **Style Transfer**: Match specific influencer writing styles
- [ ] **Image Generation**: AI-generated images to accompany posts
- [ ] **A/B Testing**: Compare different post versions

### Technical Improvements

- [ ] Implement caching for faster response times
- [ ] Add user authentication and post history
- [ ] Deploy on cloud platform (AWS/GCP/Azure)
- [ ] Add automated tests (pytest)
- [ ] Implement logging and monitoring
- [ ] Create Docker containerization
- [ ] Add CI/CD pipeline

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Karthik**
- Role: Data Scientist, State of Michigan
- Expertise: Machine Learning, AI Applications, Data Science

## 🙏 Acknowledgments

- **Groq** for providing fast LLM inference
- **LangChain** for the excellent LLM framework
- **Streamlit** for the amazing web framework
- **Meta** for the LLaMA model series

## 📧 Contact

For questions, suggestions, or collaboration opportunities:
- Create an issue on GitHub
- Connect on LinkedIn

---

**Made with ❤️ using Streamlit • Powered by Groq & LangChain**
