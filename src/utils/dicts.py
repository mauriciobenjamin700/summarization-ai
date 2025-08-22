from typing import Any, Optional


def to_dict(
    obj: object,
    exclude: Optional[set[str]] = None,
    include: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """
    Converte a object to a dict
    """
    if exclude is None:
        exclude = set()

    data = {}

    if hasattr(obj, "__dict__"):
        data = {
            key: value
            for key, value in obj.__dict__.items()
            if key not in exclude and (not include or key in include)
        }
        if include:
            data.update(include)

    return data
