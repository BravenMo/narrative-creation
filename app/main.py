from speech_recognition.speech_recognition import run as speech_recognition_main
from sentiment_analysis.sentiment import begin_sentiment_analysis as sentiment_analysis_main
from text_generation.text_generator import run as text_generation_main
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function of the application
    """

    try:
        mytext=speech_recognition_main("D:\\college\\NLP - BCSE409L\\project\\narrative-creation\\resources\\OSR_us_000_0061_8k.wav")
        logging.info("Speech Recognition Done")
        # print(mytext)
        logging.info("Sentiment Analysis Started")
        tokens_with_sentiment = sentiment_analysis_main(mytext)
        logging.info("Sentiment Analysis Finished")
        # print(tokens_with_sentiment)
        logging.info("Text Generation Started")
        generated_text = text_generation_main(tokens_with_sentiment, "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")
        logging.info("Text Generation Finished")
        print(generated_text)
        

        
        
        
        

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__=="__main__":
    main()
