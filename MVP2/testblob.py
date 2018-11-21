
from textblob import TextBlob
python -m textblob.download_corpora

wiki = TextBlob("Python is a high-level, general-purpose programming language.")

wiki.tags
