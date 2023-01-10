from normalizer import Normalizer
import spacy

class Tokenizer():
    def __init__(self)->None:
        self._n =Normalizer.verify_sentence(self) #The text to split
    def tokenizer(self)->list:
        self._tokens = []
        self._nlp = spacy.load('en_core_web_sm')
        self._doc= self._nlp(self._n)
        for tokens in self._doc:
            self._tokens.append(str(tokens))
        return self._tokens
        # return (string)
        # return str(self._tokens)
        
        # self._tokens = self._doc.split()
        # return self._tokens
t=Tokenizer()
t.tokenizer()