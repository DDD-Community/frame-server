import os
import json
from typing import Union


def load_secrets(key: str) -> Union[int, str, None]:
    """
    Load secrets from env variables, or a file.
    """
    def get_secret(secret_path: str, key: str):
        # pylint: disable=invalid-name
        with open(secret_path) as f:
            secrets = json.loads(f.read())
            return secrets.get(key)

    # validate
    if not key or not isinstance(key, str) or key == '':
        return None

    # check env variables
    if key in os.environ:
        return os.environ[key]

    # check secret file
    secret_path = os.path.join(os.path.dirname(__file__), 'secret.json')
    if os.path.exists(secret_path):
        return get_secret(secret_path, key)

    return None
