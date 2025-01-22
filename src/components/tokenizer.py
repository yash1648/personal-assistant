

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob


# Preprocessing function
def preprocess_input(input_text):
    """Preprocess the input filter out the word and return the lemmatized words"""
    # Correct spelling using TextBlob
    corrected_text = str(TextBlob(input_text).correct())
    
    # Tokenize
    words = word_tokenize(corrected_text.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    
    return " ".join(lemmatized_words)


# Match input to the closest task
def find_best_match(processed_text):
    """Finding best match for the words and return the match result """
    from src import Boa
    best_match = None
    best_score = 0
    for task, phrases in Boa.task_patterns.items():
        for phrase in phrases:
            phrase_tokens = set(word_tokenize(phrase))
            input_tokens = set(word_tokenize(processed_text))
            match_score = len(phrase_tokens & input_tokens) / len(phrase_tokens)
            if match_score > best_score:  # Update if a better match is found
                best_score = match_score
                best_match = task
    return best_match if best_score > 0.3 else "unknown_command"  # Adjust threshold as needed

