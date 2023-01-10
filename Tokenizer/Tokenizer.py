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
            self._tokens.append(str(tokens)) # i get all the objects, 
            #set them to strings and insert them in my list of tokens
        return self._tokens 
t=Tokenizer()
t.tokenizer() #calling this function returns the list of tokens into a desired list or variable