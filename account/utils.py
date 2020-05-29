from account.models import User


def jwt_payload_handler(user: User) -> dict:
    """
    Override default JWT_PAYLOAD_HANDLER. Because of UUID object json parsing.
    """
    from rest_framework_jwt.utils import jwt_payload_handler
    from rest_framework_jwt.compat import get_username_field

    username_field = get_username_field()
    payload = jwt_payload_handler(user).copy()

    payload['username'] = str(payload['username'])
    payload[username_field] = str(payload[username_field])

    return payload
