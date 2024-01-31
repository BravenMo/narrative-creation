from speech_recognition.speech_recognition import run as speech_recognition_main
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function of the application
    """

    try:
        mytext=speech_recognition_main("D:\\VIT sem 6\\BCSE409L Natural Language Processing Theory\\project\\final project\\narrative-creation\\resources\\OSR_us_000_0061_8k.wav")
        print(mytext)

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__=="__main__":
    main()
