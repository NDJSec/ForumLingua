from tkinter import *
from python.translate import Translate

class Ui():
    def __init__(self) -> None:
        self._ENTRY_X_POS = 380
        self._LABEL_X_POS = 220

        self._master = Tk()

        self._languagesDict = {
            'untranslatedText': StringVar(),
            'translated1Text': StringVar(),
            'translated2Text': StringVar(),
            'translated3Text': StringVar(),
            'translated4Text': StringVar(),
            'translated5Text': StringVar()
        }
        
        self._translationCodes = {
            'translationCode1': StringVar(),
            'translationCode2': StringVar(),
            'translationCode3': StringVar(),
            'translationCode4': StringVar(),
            'translationCode5': StringVar(),
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
        Label(self._master, text="English", width=20, font=("bold", 10)).place(x=self._LABEL_X_POS, y=130)
        Entry(self._master, textvariable=self._languagesDict['untranslatedText']).place(x=self._ENTRY_X_POS, y=130, width=230)

        # Create Language 1 Boxes
        self._createTranslateCodeEntry("", "translationCode1", 160)
        Entry(
            self._master,
            textvariable=self._languagesDict['translated1Text'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=160, width=230)

        # Create Language 2 Boxes
        self._createTranslateCodeEntry("", "translationCode2", 190)
        Entry(
            self._master,
            textvariable=self._languagesDict['translated2Text'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=190, width=230)

        # Create Language 3 Boxes
        self._createTranslateCodeEntry("", "translationCode3", 220)
        Entry(
            self._master,
            textvariable=self._languagesDict['translated3Text'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=220, width=230)

        # Create Language 4 Boxes
        self._createTranslateCodeEntry("", "translationCode4", 250)
        Entry(
            self._master,
            textvariable=self._languagesDict['translated4Text'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=250, width=230)

        # Create Language 5 Boxes
        self._createTranslateCodeEntry("", "translationCode5", 280)
        Entry(
            self._master,
            textvariable=self._languagesDict['translated5Text'],
            state=DISABLED
        ).place(x=self._ENTRY_X_POS, y=280, width=230)
        

        # Create translate button
        self._master.bind('<Return>', self._translate)
        Button(self._master, text="Translate").place(x=370, y=310)
        self._master.bind('<Button-1>', self._translate)

    def _createTranslateCodeEntry(self, displayText: str, translationCodeEntry: str, y_pos: int) -> Entry:
        self._translationCodes[translationCodeEntry].set(displayText)
        return Entry (
            self._master,
            textvariable=self._translationCodes[translationCodeEntry],
            justify=CENTER,
            width=20,
            font=("bold", 10)
        ).place(x=self._LABEL_X_POS, y=y_pos)

    def _translate(self, event) -> None:
        translations = {
                'translation1': '',
                'translation2': '',
                'translation3': '',
                'translation4': '',
                'translation5': ''
        }

        if self._languagesDict['untranslatedText'] != '':
            if self._translationCodes['translationCode1'].get() != '':
                translation1 = Translate(
                    self._languagesDict['untranslatedText'].get(),
                    self._translationCodes['translationCode1'].get().lower()
                )
                translations['translation1'] = translation1.getTranslatedText()
            if self._translationCodes['translationCode2'].get() != '':
                translation2 = Translate(
                    self._languagesDict['untranslatedText'].get(),
                    self._translationCodes['translationCode2'].get().lower()
                )
                translations['translation2'] = translation2.getTranslatedText()
            if self._translationCodes['translationCode3'].get() != '':
                translation3 = Translate(
                    self._languagesDict['untranslatedText'].get(),
                    self._translationCodes['translationCode3'].get().lower()
                )
                translations['translation3'] = translation3.getTranslatedText()
            if self._translationCodes['translationCode4'].get() != '':
                translation4 = Translate(
                    self._languagesDict['untranslatedText'].get(),
                    self._translationCodes['translationCode4'].get().lower()
                )
                translations['translation4'] = translation4.getTranslatedText()
            if self._translationCodes['translationCode5'].get() != '':
                translation5 = Translate(
                    self._languagesDict['untranslatedText'].get(),
                    self._translationCodes['translationCode5'].get().lower()
                )
                translations['translation5'] = translation5.getTranslatedText()

            self._languagesDict['translated1Text'].set(translations['translation1'])
            self._languagesDict['translated2Text'].set(translations['translation2'])
            self._languagesDict['translated3Text'].set(translations['translation3'])
            self._languagesDict['translated4Text'].set(translations['translation4'])
            self._languagesDict['translated5Text'].set(translations['translation5'])         

    def runMainLoop(self) -> None:
        self._master.mainloop()