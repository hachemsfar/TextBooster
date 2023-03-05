from deep_translator import GoogleTranslator

import nltk
from nltk.corpus import wordnet

import spacy
from spacy.symbols import NOUN, VERB, ADJ, ADV

from textblob import TextBlob
from textblob import Word

import random

nltk.download("wordnet")
nltk.download("punkt")
nltk.download("omw-1.4")

class Text_Generation:
    def __init__(self,text):
        self.__text=text
        
    def back_Translation(self) -> list[str]:
        """
        Augments the given text by translating it to the target language and back to the source
        language.

        :param text: the text to augment
        :param translations: a list of translation providers to use

        :return: a list of augmented samples
        """
        augmented_texts = set()
        list_lang=GoogleTranslator().get_supported_languages()
        for lang in random.choices(list_lang, k=nbre_samples):
            try:
                translated_text = GoogleTranslator(source="en", target=lang).translate(text)
                back_translated_text = GoogleTranslator(source=lang, target="en").translate(translated_text)
                augmented_texts.add(back_translated_text)

            except Exception:
                pass

        return(list(augmented_texts))


    def synonym_Replacement_nltk(self) -> str:
        """
        Augments the given text by replacing the words with synonyms.

        :param text: the text to augment

        :return: the augmented sample
        """

        words = nltk.word_tokenize(text)
        augmented_text = []
        for word in words:
            # Get synonyms for the word
            syns = wordnet.synsets(word)
            if syns:
                # Get the first synonym for the word
                new_word = syns[0].lemmas()[0].name()
            else:
                new_word = word
            augmented_text.append(new_word)

        return " ".join(augmented_text)



    def synonym_Replacement(self) -> list[str]:
        """
        Augments the given text by replacing the words with synonyms.

        :param text: the text to augment
        :param bliblio: blibo used to get each word synonym

        :return: the augmented sample
        """
        augmented_texts = []
        return synonym_Replacement_nltk(text)

