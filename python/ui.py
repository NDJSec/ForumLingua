from tkinter import *
from python.translate import Translate

class Ui():
    def __init__(self) -> None:
        self._ENTRY_X_POS = 380
        self._LABEL_X_POS = 220

        self._master = Tk()

        self._languagesDict = {
            'untranslatedText': StringVar(),
            'spanishText': StringVar(),
            'portugueseText': StringVar(),
            'italianText': StringVar(),
            'frenchText': StringVar(),
            'romanianText': StringVar()
        }

        self._createUiWindow()
    
    def _createUiWindow(self) -> None:
        
        self._master.geometry('750x750')
        self._master.title("Forum Lingua")

        # Create Title
        Label(
            self._master,
            text="Forum Lingua:",
            width=20, font=("bold", 20)
        ).place(x=250, y=53)
        Label(
            self._master,
            text="A multi-language translator",
            width=20,
            font=("bold", 20)
        ).place(x=250, y=93)

        #Create English Input Box
        self._createLabel("English", 130)
        Entry(self._master, textvariable=self._languagesDict['untranslatedText']).place(x=self._ENTRY_X_POS, y=130)

        # Create Spanish Boxes
        self._createLabel("Spanish", 160)
        Entry(
            self._master,
            textvariable=self._languagesDict['spanishText'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=160)

        # Create Portuguese Boxes
        self._createLabel("Portuguese", 190)
        Entry(
            self._master,
            textvariable=self._languagesDict['portugueseText'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=190)

        # Create Italian Boxes
        self._createLabel("Italian", 220)
        Entry(
            self._master,
            textvariable=self._languagesDict['italianText'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=220)

        # Create French Boxes
        self._createLabel("French", 250)
        Entry(
            self._master,
            textvariable=self._languagesDict['frenchText'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=250)

        # Create Romanian Boxes
        self._createLabel("Romanian", 280)
        Entry(
            self._master,
            textvariable=self._languagesDict['romanianText'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=280)
        

        # Create translate button
        Button(self._master, text="Translate", command=self._translate).place(x=370, y=310)

    def _createLabel(self, displayText:str, y_pos: int) -> Label:
        return Label (
            self._master,
            text=displayText,
            width=20,
            font=("bold", 10)
        ).place(x=self._LABEL_X_POS, y=y_pos)

    def _translate(self) -> None:
        if self._languagesDict['untranslatedText'] != '':
            spanishTranslation = Translate(
                self._languagesDict['untranslatedText'].get(),
                'es'
            )
            portugueseTranslation = Translate(
                self._languagesDict['untranslatedText'].get(),
                'pt'
            )
            italianTranslation = Translate(
                self._languagesDict['untranslatedText'].get(),
                'it'
            )
            frenchTranslation = Translate(
                self._languagesDict['untranslatedText'].get(),
                'fr'
            )
            romanianTranslation = Translate(
                self._languagesDict['untranslatedText'].get(),
                'ro'
            )

            translations = {
                'spanish': spanishTranslation.getTranslatedText(),
                'portuguese': portugueseTranslation.getTranslatedText(),
                'italian': italianTranslation.getTranslatedText(),
                'french': frenchTranslation.getTranslatedText(),
                'romanian':romanianTranslation.getTranslatedText()
            }

            self._languagesDict['spanishText'].set(translations['spanish'])
            self._languagesDict['portugueseText'].set(translations['portuguese'])
            self._languagesDict['italianText'].set(translations['italian'])
            self._languagesDict['frenchText'].set(translations['french'])
            self._languagesDict['romanianText'].set(translations['romanian'])


                

    def runMainLoop(self) -> None:
        self._master.mainloop()