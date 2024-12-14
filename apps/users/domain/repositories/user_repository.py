from abc import ABC, abstractmethod
from typing import List
from apps.users.domain.entities.user import User

class UserRepository(ABC):
    
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass
    
    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass
    
    @abstractmethod
    def add_user(self, user: User) -> None:
        pass
    
    @abstractmethod
    def remove_user(self, user: User) -> None:
        pass
    
    # Add other necessary methods
