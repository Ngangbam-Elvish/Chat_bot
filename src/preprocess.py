import string
import re
import nltk
from nltk.corpus import stopwords

def setup_nltk():
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        try:
            nltk.download('stopwords', quiet=True)
        except Exception:
            pass

setup_nltk()

try:
    stop_words = set(stopwords.words('english'))
except Exception:
    stop_words = set()  # Fallback just in case

def preprocess_text(text):
    """
    Lowercases, removes punctuation, and removes stopwords.
    Uses regex for tokenization to avoid NLTK punkt dependency.
    """
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = re.findall(r'\b\w+\b', text)
    filtered_tokens = [w for w in tokens if w not in stop_words]
    return " ".join(filtered_tokens)