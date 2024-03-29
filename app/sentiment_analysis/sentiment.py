import logging
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

# Configuring logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess_text(text):
    """
    Preprocess the given text by tokenizing, removing stopwords, and lemmatizing.
    Args:
        text (str): The text to be processed.

    Returns:
        str: The processed text.
    """
    logging.info("Starting text preprocessing")
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_text = ' '.join(lemmatized_tokens)
    logging.info("Text preprocessing completed")
    return processed_text


def get_sentiment(text):
    """
    Determine the sentiment of the provided text.
    Args:
        text (str): The text to analyze.

    Returns:
        dict: The sentiment analysis scores.
    """
    logging.info("Analyzing sentiment")
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)

def tokenize(sentence):
    """
    Tokenize a sentence into its component tokens

    Args:
        sentence (str): Text to be tokenized
    
    Returns:
        list of str: List of all the tokens
    """
    tokens = word_tokenize(sentence.lower())
    return tokens

def split_sentence(text):
    """
    Splits a sentence into smaller sentences at commas, full stops, and exclamation marks.

    Args:
        text (str): The text to be split.

    Returns:
        list of str: List of split sentences.
    """
    # Regex pattern for splitting at ',', '.', and '!'
    pattern = r'[,.!?]'
    # Splitting the text
    split_sentences = re.split(pattern, text)
    # Removing empty strings and stripping whitespace
    split_sentences = [sentence.strip() for sentence in split_sentences if sentence.strip()]
    return split_sentences

def maxsentiment(sentiment_value):
    """
    Function used to calculate the maximum sentiment between positive, negative and neutral
    Args:
        sentiment_values: All the sentiment values including positive, negative and neutral
    
    Returns:
        max_positive and max_negative sentiment value
    """
    pos_value=sentiment_value['pos']
    neg_value=sentiment_value['neg']
    neu_value=sentiment_value['neu']
    if neu_value>pos_value and neu_value>neg_value:
        return neu_value
    elif pos_value>neg_value:
        return pos_value
    else:
        return (-neg_value)

def begin_sentiment_analysis(input_from_speech):
    """
    Function called when sentiment analysis is to begin
    Args:
        input_from_speech (str): The text form of the speech inputted from the previous module
    
    Returns:
        List of tuples of tokens and their appropriate sentiment values
    """
    try:

        sentences=split_sentence(input_from_speech)
        final_list=[]

        for sentence in sentences:
            pre_sentence=preprocess_text(sentence)
            sentiment_value=get_sentiment(pre_sentence)
            final_sentiment_value=maxsentiment(sentiment_value)
            tokens=tokenize(pre_sentence)
            for token in tokens:
                values=(token,final_sentiment_value)
                final_list.append(values)

        return final_list



    except Exception as e:
        logging.error(f"An error occurred: {e}")

    



