import eel
from googletrans import Translator

eel.init('web')  # Папка с файлом index.html


@eel.expose
def translate_text(target_language, text):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text


eel.start('index.html', size=(450, 500), mode="chrome")
