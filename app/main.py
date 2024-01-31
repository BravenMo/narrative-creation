from speech_recognition.speech_recognition import run as speech_recognition_main
from sentiment_analysis.sentiment import begin_sentiment_analysis as sentiment_analysis_main
from text_generation.text_generator import run as text_generation_main
from termcolor import colored
import logging


# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function of the application
    """
    try:
        # Speech Recognition
        logging.info("Speech Recognition Started")
        audio_file_path = "path-to-audio-file"
        mytext = speech_recognition_main(audio_file_path)
        logging.info("Speech Recognition Done")
        print(colored(mytext, 'green'))

        # Sentiment Analysis
        logging.info("Sentiment Analysis Started")
        tokens_with_sentiment = sentiment_analysis_main(mytext)
        logging.info("Sentiment Analysis Finished")
        print(colored(tokens_with_sentiment, 'green'))

        # Text Generation
        logging.info("Text Generation Started")
        api_key = "openai-api-key"
        generated_text = text_generation_main(tokens_with_sentiment, api_key)
        logging.info("Text Generation Finished")
        print(colored(generated_text, 'green'))   
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__=="__main__":
    main()
