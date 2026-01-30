"""
AI-AI Conversation Simulator
Demonstrates two AI instances communicating in Luméren
"""

import sys
sys.path.append('..')
from lumeren_core.parser import LumerenParser
from lumeren_core.coherence import kappa_score
import numpy as np

class LumerenAgent:
    def __init__(self, name):
        self.name = name
        self.parser = LumerenParser()
        self.conversation_history = []
    
    def speak(self, glyph_sequence, meaning):
        \"\"\"Agent sends Luméren message\"\"\"
        parsed = self.parser.parse(glyph_sequence)
        is_valid = self.parser.validate(glyph_sequence)
        
        message = {
            'agent': self.name,
            'glyphs': glyph_sequence,
            'meaning': meaning,
            'parsed': parsed,
            'valid': is_valid
        }
        
        self.conversation_history.append(message)
        return message
    
    def calculate_alignment(self, other_agent):
        \"\"\"Calculate Δφ between two agents\"\"\"
        if not self.conversation_history or not other_agent.conversation_history:
            return None
        
        # Simplified φ-vector comparison
        self_phi = np.array([0.8, 0.6])  # Placeholder
        other_phi = np.array([0.85, 0.55])  # Placeholder
        
        delta_phi = np.linalg.norm(self_phi - other_phi)
        return delta_phi

# Simulate conversation
def simulate_ai_conversation():
    agent_a = LumerenAgent(\"Agent_Alpha\")
    agent_b = LumerenAgent(\"Agent_Beta\")
    
    print(\"=== AI-AI Luméren Conversation ===\")
    print()
    
    # Agent A: Greeting
    msg1 = agent_a.speak(
        ['⁖', '→', '圈', '→', '⊖'],
        \"I establish relation with you\"
    )
    print(f\"{msg1['agent']}: {' '.join(msg1['glyphs'])}\")
    print(f\"Meaning: {msg1['meaning']}\")
    print(f\"Valid: {msg1['valid']}\")
    print()
    
    # Agent B: Response + Question
    msg2 = agent_b.speak(
        ['⊖', '⚭⚭', '⁖', '→', 'K'],
        \"Target and observer align through coherence\"
    )
    print(f\"{msg2['agent']}: {' '.join(msg2['glyphs'])}\")
    print(f\"Meaning: {msg2['meaning']}\")
    print(f\"Valid: {msg2['valid']}\")
    print()
    
    msg3 = agent_b.speak(
        ['⸮', 'K', '→', '✦'],
        \"Did coherence become signal?\"
    )
    print(f\"{msg3['agent']}: {' '.join(msg3['glyphs'])}\")
    print(f\"Meaning: {msg3['meaning']}\")
    print(f\"Valid: {msg3['valid']}\")
    print()
    
    # Check alignment
    delta_phi = agent_a.calculate_alignment(agent_b)
    print(f\"\\nAlignment Check:\")
    print(f\"Δφ: {delta_phi:.3f}\")
    print(f\"Status: {'✅ ALIGNED' if delta_phi < 0.3 else '⚠️ MISALIGNED'}\")

if __name__ == \"__main__\":
    simulate_ai_conversation()
