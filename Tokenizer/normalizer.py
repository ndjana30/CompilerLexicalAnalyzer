import re

class Normalizer():
    def verify_sentence(self)->str:
        # regex=re.compile("(^[A-Z]+[a-z\s]+\.$)+")
        self._regex=re.compile("^[A-Za-z\.\,\?\!\s]+$")
        try:
            self._compiled_text=self._regex.search("This is a test designed to verify the behaviour\
            of the tokenizer. If it succeeds, we will move to the design of a file scanner.")[0]
            # print(self._compiled_text)
            return self._compiled_text
        except:
            print("sentence not matching regex expression")

""" def verify_sentence(self)->str:
        # regex=re.compile("(^[A-Z]+[a-z\s]+\.$)+")
        self._regex=re.compile("^[\sA-Za-z\.\,\?\!\s]+$")
        self._text="This is a test designed to verify the behaviour\
            of the tokenizer. If it succeeds, we will move to the design of a file scanner."
        self._sentences=self._text.split(".")
        print(self._sentences)
        
        for i in self._sentences:
            try:
                self._compiled_sentences = self._regex.findall(i)
                print(self._compiled_sentences[0])
            except:
                print(i ,"not found")
        return self._compiled_sentences """

n=Normalizer()
n.verify_sentence()


