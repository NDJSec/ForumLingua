import ctypes

class Translate():
    def __init__(self, untranslatedText: str, targetLanguage: str) -> None:
        self._untranslatedText = untranslatedText
        self._sourceLanguage = b"en"
        self._targetLanguage = targetLanguage
        self._lib = ctypes.CDLL("src/translate.dll")
        self._translate = self._lib.translate

        self._translate.argtypes = [
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_longlong,
        ]

        self._translate.restype = ctypes.c_char_p

        self._buf_size = 1000
        self._buf = ctypes.create_string_buffer(self._buf_size)

    def getTranslatedText(self) -> str:
        translatedText = self._translate(
            self._untranslatedText.encode('utf-8'),
            self._sourceLanguage,
            self._targetLanguage.encode('utf-8'),
            self._buf,
            self._buf_size
        )
        return translatedText.decode()

    