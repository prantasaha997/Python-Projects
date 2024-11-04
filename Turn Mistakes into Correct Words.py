#inport library
from spellchecker import Spellchecker # type: ignore

#create app class
class SpellcheckerApp:  
    def __init__(self):
        self.spell = Spellchecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')

        #returning corrected word
        return ' '.join(corrected_words)     
    
    #run the app
    def run(self):
        print("\n ___Spell Checker___")

        while True:
            text = input("Put your word or EXIT: ")

            if text.lower() == 'exit':
                print('Closing the program...')
                break

            corrected_text = self.correct_text(text)
            print(f'Corrected Text : {corrected_text}')

# running main program

if __name__ == "__main__":
    SpellcheckerApp().run()