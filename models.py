from dataclasses import dataclass

@dataclass
class DebtItem:
    id: int
    title: str
    area: str
    impact: int
    effort: int
    risk: int
    notes: str = ''
