from datetime import datetime

from src.core.base import BaseSchema
from src.core.enums import ChatRoleEnum


class ChatCreate(BaseSchema):
    role: ChatRoleEnum
    content: str


class ChatResponse(BaseSchema):
    id: str
    role: ChatRoleEnum
    content: str
    created_at: datetime
