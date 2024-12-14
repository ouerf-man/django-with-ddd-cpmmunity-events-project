from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Email:
    address: str

    def __post_init__(self):
        if not self.validate_email(self.address):
            raise ValueError(f"Invalid email address: {self.address}")

    @staticmethod
    def validate_email(email: str) -> bool:
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(regex, email) is not None
