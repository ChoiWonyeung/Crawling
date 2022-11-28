from googletrans import Translator


def trans(text):
    text = Translator().translate(text, dest="ko").text
    return text
