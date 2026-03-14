"""
spell_corrector.py

Corrects spelling mistakes in student queries.
"""

from spellchecker import SpellChecker

spell = SpellChecker()

# Add domain specific words so spellchecker won't change them
spell.word_frequency.load_words([
    "vignan",
    "vsat",
    "eapcet",
    "btech",
    "mtech",
    "bba",
    "bca",
    "mba",
    "mca"
])


def correct_spelling(text):

    words = text.split()

    corrected_words = []

    for word in words:

        corrected = spell.correction(word)

        if corrected:
            corrected_words.append(corrected)
        else:
            corrected_words.append(word)

    return " ".join(corrected_words)