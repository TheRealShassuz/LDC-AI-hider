from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

def main():
    print("--LDC  AI Hider--")
    print("Writen by TheRealShassuz")
    print("Version 1.0  Release 15-11-2023 ")
    text_to_translate = input("Enter the text you want to rephrase in any language you want : ")

    # List of languages to translate to
    languages = ['no', 'da', 'de', 'nl', 'pl', 'en']

    print("\nOriginal Text: ", text_to_translate)
    print ("Generating text...")

    for lang_code in languages:
        # Translate to the target language
        translated_text = translate_text(text_to_translate, lang_code)

        # Translate back to Swedish
        back_to_english = translate_text(translated_text, 'sv')

    print(f"Finished text in Swedish: {back_to_english}")



if __name__ == "__main__":
    main()
