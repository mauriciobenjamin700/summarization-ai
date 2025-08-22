from enum import Enum


class ChatRoleEnum(Enum):
    """
    Attributes:
        USER: The user role.
        ASSISTANT: The assistant role.
        SYSTEM: The system role.
    """

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
