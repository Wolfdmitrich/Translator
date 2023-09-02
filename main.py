import eel
from googletrans import Translator

eel.init('web')  # Папка с файлом index.html


@eel.expose
def translate_text(target_language, text):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as err:
        return "Error"


eel.start('index.html', size=(450, 500))
