# apps/users/domain/entities/user.py

from dataclasses import dataclass
from typing import List
from apps.users.domain.value_objects.email import Email
from apps.users.domain.value_objects.profile import Profile
from apps.users.domain.entities.role import Role

@dataclass
class User:
    id: int
    username: str
    email: Email
    profile: Profile
    roles: List[Role]