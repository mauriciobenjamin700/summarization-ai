from typing import Any, Optional

from pydantic import BaseModel, ConfigDict

from src.utils import to_dict


class BaseSchema(BaseModel):

    model_config = ConfigDict(
        extra="ignore", use_enum_values=True, from_attributes=True
    )

    def to_dict(
        self,
        exclude: Optional[set[str]] = None,
        include: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        return to_dict(self, exclude=exclude, include=include)
