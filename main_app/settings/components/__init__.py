from pathlib import PurePath

# Loading `.env` files
from decouple import config  # noqa F401

# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing: dirname(dirname(dirname(__file__)))
BASE_DIR = PurePath(__file__).parent.parent.parent.parent


def to_list(val: str) -> list:
    return [d for d in [s.strip() for s in val.split(' ')] if d]
