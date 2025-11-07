import json
import os

def load_lexicon():
    """Load the Luméren lexicon from data/lexicon.json"""
    path = os.path.join(os.path.dirname(__file__), "..", "data", "lexicon.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def translate_text(text):
    """Convert words in text to glyphs using the lexicon."""
    lexicon = load_lexicon()
    words = text.lower().split()
    glyphs = [lexicon.get(word, "□") for word in words]
    return glyphs
  Add Luméren translator module
