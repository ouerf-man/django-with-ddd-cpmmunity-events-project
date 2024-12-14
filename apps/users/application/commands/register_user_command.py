from apps.users.domain.aggregates.user_aggregate import UserAggregate
from apps.users.domain.services.user_service import UserService
from apps.users.domain.value_objects.email import Email
from apps.users.domain.value_objects.profile import Profile
from apps.users.domain.entities.role import Role

class RegisterUserCommand:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self, username: str, email_str: str, password: str)->UserAggregate:
        email = Email(address=email_str)
        profile = Profile(bio="", avatar_url="")
        role = Role(id=1, name="Attendee")  # Assuming 'Attendee' has ID 1
        user_aggregate = self.user_service.register_user(username, email, password, profile, [role])
        return user_aggregate
