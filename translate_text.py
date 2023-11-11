import translators as ts

def get_translation(text, language="de"):
    translated_text = ts.translate_text(query_text=text, translator="google", to_language=language)
    return translated_text
