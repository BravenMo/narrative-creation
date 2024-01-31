# narrative-creation
Enhancing Narrative Creation Through Voice Recognition and NLP.  Implementation of a voice recognition system that allows you to narrate a dialogue which is then transcribed in the format of a paragraph for a novel.

## Project idea
This project introduces an approach to narrative creation by integrating voice recognition
technology with advanced Natural Language Processing (NLP) techniques. Our system allows
users to orally narrate dialogues, which are then seamlessly transcribed and formatted into
well-structured novel paragraphs. The system not only transcribes verbatim speech but also
employs NLP to enhance the text with appropriate punctuation, dialogue tags, and paragraph
breaks, reflecting the nuances of written storytelling. The sentiments of the original dialogue is
maintained while generating the remaining text.

## Methodology
The project first analyzes the speech supplied and then passes them to a sentiment
analyzer. The sentiment analyzer preprocesses the text by tokenizing and then lemmatizing the
words. Based on typical English stop words, the sentences are split. They are also split about the
question marks, exclamation marks and commas. The individual sentences are analyzed and the
same sentiment is applied to all tokens of the split sentences. These tokens with their sentiment
values are then passed to a text generator (using openAI GPT 3.5) which while maintaining the
sentiment generates a paragraph based on the tokens of the original dialogue which can be
transcribed and formatted for purposes such as writing a novel. Following are each of the
modules with the methodology used in each.

## Resources used
1. https://huggingface.co/openai/whisper-medium
2. https://platform.openai.com/docs/models/gpt-3-5
3. https://huggingface.co/datasets/lj_speech
4. https://www.nltk.org/
