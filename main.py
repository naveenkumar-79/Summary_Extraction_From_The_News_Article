import re
import string
from heapq import nlargest
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from newspaper import Article
import sys
import nltk
from log import setup_logging
import warnings
warnings.filterwarnings('ignore')
nltk.download('punkt')
nltk.download('stopwords')
logger = setup_logging('main')


class news_summarization:
    def __init__(self, url):
        try:
            self.url = url
            self.stopwords = set(STOP_WORDS)
            self.nlp = spacy.load("en_core_web_sm")
            self.punctuation = string.punctuation
            logger.info("NLP & Config Loaded Successfully")
        except Exception:
            er_ty, er_msg, er_lin = sys.exc_info()
            logger.info(f"Init Error : {er_lin.tb_lineno} : due to {er_msg}")

    def fetch_article(self):
        try:
            self.reg = Article(self.url)
            self.reg.download()
            self.reg.parse()
            self.text = self.reg.text
            logger.info("Article Downloaded & Parsed")
        except Exception:
            er_ty, er_msg, er_lin = sys.exc_info()
            logger.info(f"Fetch Error : {er_lin.tb_lineno} : due to {er_msg}")

    def summarization(self):
        try:
            doc = self.nlp(self.text)
            self.word_frequencies = {}

            # -------- WORD FREQUENCY (BUG FIXED) --------
            for token in doc:
                word = token.text.lower()

                if word not in self.stopwords and not token.is_punct:
                    if word not in self.word_frequencies:
                        self.word_frequencies[word] = 1
                    else:
                        self.word_frequencies[word] += 1

            if not self.word_frequencies:
                self.summary_main = ""
                return

            max_freq = max(self.word_frequencies.values())
            for word in self.word_frequencies:
                self.word_frequencies[word] /= max_freq

            sentence_tokens = list(doc.sents)
            self.sentence_scores = {}

            # -------- SENTENCE SCORING (BUG FIXED) --------
            for sent in sentence_tokens:
                for token in sent:
                    word = token.text.lower()
                    if word in self.word_frequencies:
                        self.sentence_scores[sent] = (
                            self.sentence_scores.get(sent, 0)
                            + self.word_frequencies[word]
                        )

            # -------- AVOID ZERO SUMMARY --------
            select_length = max(1, int(len(sentence_tokens) * 0.3))

            self.summary = nlargest(
                select_length,
                self.sentence_scores,
                key=self.sentence_scores.get
            )

            self.summary_main = ' '.join(sent.text for sent in self.summary)

            logger.info("\n----- Before Cleaning -----\n")
            logger.info(self.summary_main)

        except Exception:
            er_ty, er_msg, er_lin = sys.exc_info()
            logger.info(f"Summarization Error : {er_lin.tb_lineno} : due to {er_msg}")

    def cleaning(self):
        try:
            review = self.summary_main
            review = re.sub(r'http\S+', ' ', review)
            review = re.sub(r'RT|cc', '', review)
            review = re.sub(r'#\S+', ' ', review)
            review = re.sub(r'@\S+', ' ', review)
            review = re.sub(r'[!"#$%&\'()*+,/;<=>?@[\\\]^_`{|}~”“]', '', review)
            review = re.sub(r'\s+', ' ', review)

            self.cleaned_summary = review.strip()

            logger.info("\n----- Cleaned Summary -----\n")
            logger.info(self.cleaned_summary)

        except Exception:
            er_ty, er_msg, er_lin = sys.exc_info()
            logger.info(f"Cleaning Error : {er_lin.tb_lineno} : due to {er_msg}")


if __name__ == "__main__":
    url="https://timesofindia.indiatimes.com/sports/cricket/icc-mens-t20-world-cup/t20-world-cup-india-cancel-practice-session-in-delhi-ahead-of-match-against-namibia/articleshow/128070882.cms"
    obj = news_summarization(url)
    obj.fetch_article()
    obj.summarization()
    obj.cleaning()

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(obj.cleaned_summary)

    logger.info("\nSummary saved to summary.txt")
