from typing import Optional
from dataclasses import dataclass
from enum import Flag


class Language(Enum):
    PYTHON = "Dockerfile.py"
    JAVASCRIPT = "Dockerfile.js"
    GOLANG = "Dockerfile.go"
    RUST = "Dockerfile.rs"

    def __repr__(self):
        return "<{}.{}>".format(self.__class__.__name__, self.name)


@dataclass(frozen=True)
class Sandbox:
    """
    IDK what I'm going to do with this yet.

    Definitely something...
    """
    language: Language
    self_guided_project: Optional[str]
    remote_dir: str

    def build(self):
        raise NotImplementedError()
