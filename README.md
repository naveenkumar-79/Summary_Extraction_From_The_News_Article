# Summary_Extraction_From_The_News_Article
📌 Project Overview

This project is an Automatic News Article Summarization System built using Python and Natural Language Processing (NLP) techniques. It extracts important information from lengthy news articles and generates a concise, meaningful summary automatically.

The system takes a news article URL as input, processes the text using NLP libraries, and outputs a clean summary, reducing reading time while preserving key information.

🚀 ***Features***

Extracts news articles directly from live URLs

Performs text preprocessing and cleaning

Uses frequency-based extractive summarization

Sentence scoring and ranking for summary generation

Clean and readable output summary

Modular and class-based Python implementation

Logging and exception handling for robustness

🛠 ***Technologies & Libraries Used***

Python 3

NLTK – Tokenization and stopword handling

spaCy – NLP pipeline and sentence segmentation

Newspaper3k – News article extraction

Regex (re) – Text cleaning

Heapq – Selecting top-ranked sentences

🧠 ***How It Works***

Takes a news article URL as input

Downloads and parses the article text

Tokenizes text into words and sentences

Removes stopwords and punctuation

Calculates word frequencies

Scores sentences based on word importance

Selects top-ranked sentences (30%)

Cleans and generates the final summary

📂 ***Project Structure***
news-article-summarization/
│
├── main.py           # Main source code
├── summary.txt       # Generated summary output
├── log.py            # Logging configuration
├── README.md         # Project documentation
▶️ How to Run the Project
1️⃣ Install Dependencies
pip install nltk spacy newspaper3k
python -m spacy download en_core_web_sm
2️⃣ Run the Application
python main.py
3️⃣ Output

The summarized content will be saved in summary.txt

Logs will show each processing step

📌 ***Sample Input***
url = "https://timesofindia.indiatimes.com/..."
📄 Sample Output

A concise summary extracted from the original news article.

🎯 ***Use Cases***

News aggregation platforms

Content summarization tools

Research and analysis

NLP learning and experimentation

📈 ***Learning Outcomes***

Practical understanding of NLP pipelines

Hands-on experience with text summarization

Improved Python OOP and debugging skills

Working with real-world unstructured text data

🔮 ***Future Enhancements***

Add abstractive summarization using deep learning

Build a web interface using Flask or Streamlit

Support multiple news sources and languages

Improve summary quality with TF-IDF or transformers

🤝 ***Contributing***

Contributions, suggestions, and improvements are always welcome!

📬 ***Contact***
Name: P.Naveen Kumar
📧 LinkedIn: www.linkedin.com/in/naveenkumar-puppala-b87737332
🐙 Gmail: puppalanaveenkumar11@gmail.com
