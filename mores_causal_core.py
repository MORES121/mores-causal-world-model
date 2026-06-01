from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum

class EntityType(Enum):
    ROBOT = 'robot'
    WALL = 'wall'
    DOOR = 'door'
    FURNITURE = 'furniture'
    OBJECT = 'object'

class AnomalyType(Enum):
    PATH_BLOCKED = 'path_blocked'
    GRASP_FAILED = 'grasp_failed'
    OBJECT_NOT_FOUND = 'object_not_found'
    COLLISION = 'collision'

@dataclass
class Position:
    x: float; y: float; z: float

@dataclass
class Entity:
    id: str; name: str; type: EntityType; position: Position

@dataclass
class CausalEdge:
    source_id: str; target_id: str; strength: float = 1.0

@dataclass
class CausalGraph:
    entities: Dict[str, Entity] = field(default_factory=dict)
    edges: List[CausalEdge] = field(default_factory=list)
    
    def add_entity(self, entity: Entity):
        self.entities[entity.id] = entity
    def add_edge(self, edge: CausalEdge):
        self.edges.append(edge)

print("✅ MORES 因果世界模型核心代码已加载")
