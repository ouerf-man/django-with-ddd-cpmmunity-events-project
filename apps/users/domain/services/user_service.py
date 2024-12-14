from django.db import transaction
from apps.users.domain.repositories.user_repository import UserRepository
from apps.users.domain.aggregates.user_aggregate import UserAggregate
from apps.users.domain.entities.user import User
from apps.users.domain.entities.role import Role
from apps.users.domain.value_objects.email import Email
from apps.users.domain.value_objects.profile import Profile

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, username: str, email: Email, password: str, profile: Profile, roles: list[Role]) -> UserAggregate:
        with transaction.atomic():
            user = User(id=0, username=username, email=email, profile=profile)
            user_aggregate = UserAggregate(user=user, roles=roles, profile=profile)
            self.user_repository.add_user(user_aggregate)
            return user_aggregate
