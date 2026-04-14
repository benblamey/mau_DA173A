# This is just for a demo!
# Not for the exam!
# You are not expected to understand this code - it's just for fun!
# (doesn't run the in the w3spaces)


import sys
# You need to install the package:
# https://pypi.org/project/transformers/
# python3 -m pip install transformers
# (the torch and sentencepiece packages may also need to be installed)
import transformers

# See: https://huggingface.co/Helsinki-NLP/opus-mt-sv-en
MODEL_NAME = "Helsinki-NLP/opus-mt-sv-en"
#MODEL_NAME = "Helsinki-NLP/opus-mt-en-sv"

# We normally use this check to ensure
# we are not being used as a module
# (it is used here for another reason)
if __name__ == "__main__":
    # See: https://huggingface.co/Helsinki-NLP/opus-mt-sv-en
    tokenizer = transformers.AutoTokenizer.from_pretrained(
        MODEL_NAME)
    model = transformers.AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_NAME)
    print("✔ Models loaded")

    print("Enter text:")
    for line_original in sys.stdin:
        if len(line_original.strip()) > 0:
            # Tokenize the input text and translate
            inputs = tokenizer(line_original, return_tensors="pt", padding=True)
            translated = model.generate(**inputs)
            # (returns a vector)

            # Decode the translated tokens
            line_translated = tokenizer.decode(translated[0], skip_special_tokens=True)
        else:
            line_translated = ""

        print("Translation:")
        print(line_translated)
        print("Enter text:")
