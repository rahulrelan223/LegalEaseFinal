from preprocessing import preprocess_text
import nltk
from nltk.corpus import wordnet
from transformers import BartForConditionalGeneration, BartTokenizer

# Download NLTK resources if not already downloaded
nltk.download('wordnet')

# Load pre-trained BART model and tokenizer
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

def simplify_jargon(text):
    # Function to replace jargon words with simpler synonyms using WordNet
    words = nltk.word_tokenize(text)
    simplified_words = []
    for word in words:
        synsets = wordnet.synsets(word)
        if synsets:
            simplified_words.append(synsets[0].lemmas()[0].name())
        else:
            simplified_words.append(word)  # Append the original word if no synsets are found
    return ' '.join(simplified_words)

def paraphrase_text(text):
    # Tokenize the text
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate paraphrased text
    paraphrased_ids = model.generate(inputs["input_ids"], max_length=150, num_beams=4, early_stopping=True)
    
    # Decode paraphrased text
    paraphrased_text = tokenizer.decode(paraphrased_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
    
    return paraphrased_text

def preprocess_simplify_paraphrase(text):
    # Preprocess text using the function from preprocessing.py
    preprocessed_text = preprocess_text(text)

    # Simplify jargon words
    simplified_text = simplify_jargon(preprocessed_text)

    # Paraphrase the simplified text
    paraphrased_text = paraphrase_text(simplified_text)
    
    return paraphrased_text