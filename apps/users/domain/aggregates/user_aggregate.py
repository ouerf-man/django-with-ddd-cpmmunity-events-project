from typing import List
from apps.users.domain.entities.user import User
from apps.users.domain.value_objects.email import Email
from apps.users.domain.value_objects.profile import Profile
from apps.users.domain.entities.role import Role

class UserAggregate:
    def __init__(self, user: User, roles: List[Role], profile: Profile):
        self.user = user
        self.roles = roles
        self.profile = profile

    def add_role(self, role: Role):
        if role not in self.roles:
            self.roles.append(role)

    def remove_role(self, role: Role):
        if role in self.roles:
            self.roles.remove(role)

    def update_profile(self, profile: Profile):
        self.profile = profile
