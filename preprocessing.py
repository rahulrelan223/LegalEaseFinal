import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_text(text):
    # Normalize contractions
    contractions_dict = {
        "won't": "will not",
        "can't": "cannot",
        "n't": " not",
        "'re": " are",
        "'s": " is",
        "'d": " would",
        "'ll": " will",
        "'t": " not",
        "'ve": " have",
        "'m": " am"
    }
    contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()))
    def expand_contractions(s, contractions_dict=contractions_dict):
        def replace(match):
            return contractions_dict[match.group(0)]
        return contractions_re.sub(replace, s)
    
    text = expand_contractions(text)
    
    # Remove special characters, numbers, punctuation, and common legal section headers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\b\d+\b', '', text)
    section_headers = ["article", "section", "clause", "subparagraph", "part", "chapter", "schedule"]
    for header in section_headers:
        text = re.sub(r'\b{}\b'.format(header), '', text)
    
    # Remove extra whitespaces
    text = ' '.join(text.split())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    text = ' '.join(filtered_text)
    return text
