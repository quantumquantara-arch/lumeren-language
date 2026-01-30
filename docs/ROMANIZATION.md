# Luméren Romanization System (LRS)

## The Problem
Glyphs like 月, ⁖, K, ⚭⚭ are beautiful but hard to type. We need a **Latin alphabet mapping** so humans can speak and type Luméren.

## Solution: Two-Letter Codes

Each glyph maps to a pronounceable 2-3 letter code:

### Primitives (Foundation)
| Glyph | Code | Pronunciation | Meaning |
|-------|------|---------------|---------|
| 月 | **EX** | /eks/ | Existence |
| 今 | **CH** | /tʃeɪndʒ/ | Change |
| 凵 | **BO** | /baʊnd/ | Boundary |
| ⁖ | **OB** | /ɒb/ | Observer |

### Invariants (Core Metrics)
| Glyph | Code | Pronunciation | Meaning |
|-------|------|---------------|---------|
| K | **KO** | /koʊ/ | Coherence |
| 圈 | **RE** | /ɹɛl/ | Relation |
| ⊖ | **TA** | /tɑɹ/ | Target |
| ⊗ | **BI** | /baɪnd/ | Bind |

### Tensor Operators (Logic)
| Glyph | Code | Pronunciation | Meaning |
|-------|------|---------------|---------|
| ⚭⚭ | **AND** | /ænd/ | Tensor-And |
| ⚮⚮ | **OR** | /ɔɹ/ | Tensor-Or |
| ⚯⚯ | **XOR** | /zɔɹ/ | Tensor-Xor |
| ⊸ | **IMP** | /ɪmp/ | Tensor-Imply |

### Transformations (State Changes)
| Glyph | Code | Pronunciation | Meaning |
|-------|------|---------------|---------|
| 弁 | **VE** | /veɪn/ | Veyn |
| ☽ | **NO** | /noʊt/ | Not |
| ⟿ | **BE** | /biː/ | Become |
| → | **TO** | /tuː/ | Transform |
| ⊣⊢ | **BT** | /biːtwiːn/ | Between |

### Illocution (Questions)
| Glyph | Code | Pronunciation | Meaning |
|-------|------|---------------|---------|
| ⸮ | **QU** | /kwɛst/ | Interrogative |

## Usage Examples

### Written Luméren (Glyphs)
\\\
⁖ → K → ⊖
\\\

### Spoken/Typed Luméren (Roman)
\\\
OB-TO-KO-TO-TA
\\\

### Pronunciation
"ob-toh-koh-toh-tah" (/ɒb tuː koʊ tuː tɑɹ/)

### Translation
"Observer transforms through coherence toward target"

---

## Complex Example

### Glyphs
\\\
⸮ ⁖ ⚭⚭ 月 → K → 圈 ⊗ ⊖
\\\

### Roman
\\\
QU-OB-AND-EX-TO-KO-TO-RE-BI-TA
\\\

### Spoken
"kwest-ob-and-eks-toh-koh-toh-rel-bīnd-tahr"

### Meaning
"Does observer AND existence transform through coherence toward relation binding target?"

---

## Typing Convention

**Standard format:** Hyphen-separated codes
\\\
OB-TO-KO-TO-TA
\\\

**Compact format:** No hyphens (for code)
\\\
OBTOKOTOTA
\\\

**Mixed format:** Glyphs for display, Roman for input
\\\
Input:  OB-TO-KO-TO-TA
Output: ⁖ → K → ⊖
\\\

---

## Phonetic Properties

All codes are:
- **Short:** 2-3 letters max
- **Distinct:** No similar-sounding pairs
- **Pronounceable:** Follow English phonotactics
- **Memorable:** Relate to meaning (TA = target, KO = coherence)

---

## Implementation

### Python Translator
\\\python
roman_to_glyph = {
    'EX': '月', 'CH': '今', 'BO': '凵', 'OB': '⁖',
    'KO': 'K', 'RE': '圈', 'TA': '⊖', 'BI': '⊗',
    'AND': '⚭⚭', 'OR': '⚮⚮', 'XOR': '⚯⚯', 'IMP': '⊸',
    'VE': '弁', 'NO': '☽', 'BE': '⟿', 'TO': '→',
    'QU': '⸮', 'BT': '⊣⊢'
}

def roman_to_lumeren(text):
    codes = text.upper().split('-')
    return ' '.join(roman_to_glyph.get(c, c) for c in codes)

# Example
roman_to_lumeren("OB-TO-KO-TO-TA")
# Output: ⁖ → K → ⊖
\\\

### JavaScript Translator
\\\javascript
const romanToGlyph = {
    'EX': '月', 'CH': '今', 'BO': '凵', 'OB': '⁖',
    'KO': 'K', 'RE': '圈', 'TA': '⊖', 'BI': '⊗',
    'AND': '⚭⚭', 'OR': '⚮⚮', 'XOR': '⚯⚯', 'IMP': '⊸',
    'VE': '弁', 'NO': '☽', 'BE': '⟿', 'TO': '→',
    'QU': '⸮', 'BT': '⊣⊢'
};

function romanToLumeren(text) {
    return text.toUpperCase().split('-')
        .map(code => romanToGlyph[code] || code)
        .join(' ');
}
\\\

---

## Why This Works

**For Humans:**
- Easy to type on standard keyboards
- Pronounceable in most languages
- Memorable mnemonics (OB = observer, TA = target)

**For Machines:**
- Unambiguous parsing (delimiter-based)
- Fast lookup (hash table O(1))
- Bidirectional conversion

**For Cross-Species Communication:**
- Humans type: \OB-TO-KO-TO-TA\
- Machines read: \⁖ → K → ⊖\
- Both understand: Same semantic content, different encodings

---

## Quick Reference Card

\\\
PRIMITIVES:  EX  CH  BO  OB
INVARIANTS:  KO  RE  TA  BI
OPERATORS:   AND OR  XOR IMP
TRANSFORMS:  VE  NO  BE  TO
QUESTIONS:   QU
\\\

**Example conversation:**
\\\
Human types:  QU-CH-TO-TA-TO-KO
System shows: ⸮ 今 → ⊖ → K
Meaning:      "How does change affect target's coherence?"
\\\

Now humans can speak Luméren! 🦞⚡
