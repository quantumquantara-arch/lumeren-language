"""
FastAPI Web Service for Luméren Translation
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
sys.path.append('..')
from lumeren_core.enhanced_parser import EnhancedLumerenParser
from lumeren_core.coherence import kappa_score

app = FastAPI(
    title="Luméren API",
    description="Translate natural language to Luméren glyphs with κ-φ-ψ scoring",
    version="1.0.0"
)

parser = EnhancedLumerenParser()

class TranslationRequest(BaseModel):
    text: str
    
class GlyphRequest(BaseModel):
    glyphs: list[str]

@app.get("/")
def root():
    return {
        "service": "Luméren Translation API",
        "version": "1.0.0",
        "endpoints": ["/translate", "/validate", "/score"]
    }

@app.post("/translate")
def translate_text(request: TranslationRequest):
    \"\"\"Translate natural language to Luméren glyphs\"\"\"
    # Simplified translation (in production, use full NLP pipeline)
    sample_glyphs = ['⁖', '→', 'K', '→', '⊖']
    result = parser.parse_with_repair(sample_glyphs)
    
    return {
        "input": request.text,
        "glyphs": sample_glyphs,
        "valid": result['valid'],
        "kappa_score": parser.kappa_score_optimized(sample_glyphs)
    }

@app.post("/validate")
def validate_glyphs(request: GlyphRequest):
    \"\"\"Validate a Luméren glyph sequence\"\"\"
    result = parser.parse_with_repair(request.glyphs)
    return {
        "glyphs": request.glyphs,
        "valid": result['valid'],
        "errors": result['errors'],
        "repaired": result.get('repaired')
    }

@app.post("/score")
def score_glyphs(request: GlyphRequest):
    \"\"\"Calculate κ-φ-ψ scores for glyph sequence\"\"\"
    kappa = parser.kappa_score_optimized(request.glyphs)
    return {
        "glyphs": request.glyphs,
        "kappa": kappa,
        "phi_vector": [0.8, 0.6],  # Placeholder
        "psi_type": "FORMAL-DIRECT"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
