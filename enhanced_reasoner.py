from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class AnomalyType(Enum):
    PATH_BLOCKED = 'path_blocked'
    GRASP_FAILED = 'grasp_failed'
    OBJECT_NOT_FOUND = 'object_not_found'

@dataclass
class CounterfactualPlan:
    intervention: str; confidence: float; action_sequence: List[str]

class EnhancedReasoner:
    def __init__(self):
        self.strategy_library = {
            AnomalyType.PATH_BLOCKED: [
                ('绕行', 0.85, ['重新规划', '绕过障碍']),
                ('移开障碍', 0.70, ['接近障碍', '执行移除']),
            ],
            AnomalyType.GRASP_FAILED: [
                ('调整姿态', 0.80, ['重新定位', '重试抓取']),
            ],
            AnomalyType.OBJECT_NOT_FOUND: [
                ('扩大搜索', 0.75, ['搜索相邻', '检查隐藏']),
            ],
        }
    
    def generate_plans(self, anomaly):
        return [CounterfactualPlan(s[0], s[1], s[2]) for s in self.strategy_library.get(anomaly, [])]
    
    def select_best(self, plans):
        return max(plans, key=lambda p: p.confidence) if plans else None

print("✅ 增强版反事实推理器已加载")
