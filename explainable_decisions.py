class DecisionExplainer:
    def __init__(self):
        self.decision_history = []
    
    def explain(self, anomaly, selected, alternatives):
        explanation = {
            'anomaly': anomaly,
            'selected': selected.intervention,
            'confidence': selected.confidence,
            'alternatives': [a.intervention for a in alternatives]
        }
        self.decision_history.append(explanation)
        return explanation

print("✅ 决策可解释性模块已加载")
