import json
from lumeren_core.translator import translate_text
from lumeren_core.coherence import kappa_score

if __name__ == "__main__":
    print("\n--- Luméren Translator Demo ---")
    text = input("Enter a phrase to translate: ")
    glyphs = translate_text(text)
    score = kappa_score(text)

    print(f"\nInput: {text}")
    print(f"Glyphs: {' '.join(glyphs)}")
    print(f"κ-score: {score:.2f}")
