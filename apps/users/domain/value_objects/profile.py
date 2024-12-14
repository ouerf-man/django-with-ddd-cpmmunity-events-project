from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Profile:
    bio: Optional[str] = ""
    avatar_url: Optional[str] = ""
