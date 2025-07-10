import random

class MetatronicEngine:
    def __init__(self):
        self.nodes = [
            "Sensory",
            "Emotion",
            "Memory",
            "Language",
            "Vision",
            "Abstraction",
            "Imagination",
            "Metaphor",
            "Logic",
            "Compression",
            "Contrast",
            "Pattern",
            "CORE"
        ]

        self.node_transformations = {
            "Sensory": lambda x: f"[Sensory] Observed '{x}'",
            "Emotion": lambda x: f"[Emotion] Felt response to '{x}'",
            "Memory": lambda x: f"[Memory] Linked with past experiences of '{x}'",
            "Language": lambda x: f"[Language] Expressed '{x}' in words",
            "Vision": lambda x: f"[Vision] Visualized '{x}' as imagery",
            "Abstraction": lambda x: f"[Abstraction] Reduced '{x}' to core idea",
            "Imagination": lambda x: f"[Imagination] Morphed '{x}' into new form",
            "Metaphor": lambda x: f"[Metaphor] '{x}' became something symbolic",
            "Logic": lambda x: f"[Logic] Structured '{x}' rationally",
            "Compression": lambda x: f"[Compression] Compressed essence of '{x}'",
            "Contrast": lambda x: f"[Contrast] Opposed '{x}' to define it",
            "Pattern": lambda x: f"[Pattern] Found repetition within '{x}'",
            "CORE": lambda x: f"[CORE] Synthesized '{x}' into output"
        }

    def traverse_and_transform(self, input_idea, hops=4):
        path = random.sample(self.nodes[:-1], hops) + ["CORE"]
        result = input_idea
        trace = []

        for node in path:
            result = self.node_transformations[node](result)
            trace.append((node, result))

        return trace

# Example usage:
if __name__ == "__main__":
    engine = MetatronicEngine()
    input_idea = "a lonely tree in winter"
    trace = engine.traverse_and_transform(input_idea)

    for node, state in trace:
        print(f"{node}: {state}")
