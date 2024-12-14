from typing import List
from apps.users.domain.repositories.user_repository import UserRepository
from apps.users.domain.entities.user import User
from apps.users.domain.entities.role import Role
from apps.users.domain.value_objects.email import Email
from apps.users.domain.value_objects.profile import Profile
from apps.users.domain.aggregates.user_aggregate import UserAggregate
from .django_models import DjangoUser, Role as DjangoRole
from django.contrib.auth.hashers import make_password

class DjangoUserRepository(UserRepository):
    
    def get_user_by_id(self, user_id: int) -> UserAggregate:
        django_user = DjangoUser.objects.get(id=user_id)
        roles = list(django_user.groups.all())
        role_entities = [Role(id=role.id, name=role.name) for role in roles]
        profile = Profile(bio=django_user.profile.bio, avatar_url=django_user.profile.avatar_url)
        user = User(
            id=django_user.id,
            username=django_user.username,
            email=Email(address=django_user.email),
            profile=profile
        )
        return UserAggregate(user=user, roles=role_entities, profile=profile)

    def get_all_users(self) -> List[UserAggregate]:
        django_users = DjangoUser.objects.all()
        user_aggregates = []
        for django_user in django_users:
            roles = list(django_user.groups.all())
            role_entities = [Role(id=role.id, name=role.name) for role in roles]
            profile = Profile(bio=django_user.profile.bio, avatar_url=django_user.profile.avatar_url)
            user = User(
                id=django_user.id,
                username=django_user.username,
                email=Email(address=django_user.email),
                profile=profile
            )
            user_aggregates.append(UserAggregate(user=user, roles=role_entities, profile=profile))
        return user_aggregates

    def add_user(self, user_aggregate: UserAggregate) -> None:
        django_user = DjangoUser(
            username=user_aggregate.user.username,
            email=user_aggregate.user.email.address,
            password=make_password(user_aggregate.user.password)  # Assuming password handling
        )
        django_user.save()
        # Assign roles
        for role in user_aggregate.roles:
            django_role, created = DjangoRole.objects.get_or_create(name=role.name)
            django_user.groups.add(django_role)
        # Assign profile
        django_user.profile.bio = user_aggregate.profile.bio
        django_user.profile.avatar_url = user_aggregate.profile.avatar_url
        django_user.profile.save()

    def remove_user(self, user_aggregate: UserAggregate) -> None:
        DjangoUser.objects.filter(id=user_aggregate.user.id).delete()

    # Implement other methods as needed
