from typing import Optional
from dataclasses import dataclass
from enum import Enum


class Language(Enum):
    PYTHON = 1
    JAVASCRIPT = 2
    GOLANG = 3


@dataclass(frozen=True)
class Sandbox:
    """
    IDK what I'm going to do with this yet.

    Definitely something...
    """
    language: str
    self_guided_project: Optional[str]
    remote_dir: str
