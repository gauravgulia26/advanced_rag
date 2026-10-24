from pathlib import Path
from typing import Any

import yaml


def load_param(
    key: str,
    param_file: str | Path = "params.yaml",
) -> Any:
    """Load a parameter from a YAML file using a dot-separated key."""

    path = Path(param_file)

    if not path.is_file():
        raise FileNotFoundError(f"Parameter file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        params = yaml.safe_load(file) or {}

    value = params

    for part in key.split("."):
        if not isinstance(value, dict) or part not in value:
            raise KeyError(f"Parameter '{key}' not found in {path}")
        value = value[part]

    return value
