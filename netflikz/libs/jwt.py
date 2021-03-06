import datetime
import jwt
from typing import Dict, Any

from instance.config import SECRET_KEY
from netflikz.libs.models import BlacklistedToken


class JWT:
    @staticmethod
    def encode(user_id: Any, data: Dict[str, Any] = Dict) -> str:
        """Create a Token.

        :param
            data: Dictionary with string and any format.

        :return
            String
        """

        try:
            payload = {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=60),
                "iat": datetime.datetime.utcnow(),
                "sub": user_id,
                **data
            }

            return jwt.encode(
                payload,
                SECRET_KEY
            )
        except Exception as e:
            raise e

    @staticmethod
    def decode(token: str) -> Any:
        """Decode the specified token.

        :param
            token: The token from the header.

        :return
            Any
        """

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            is_blacklisted = JWT.is_blacklisted(token=token)

            if is_blacklisted:
                raise Exception("The token has been blacklisted")

            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise Exception("The token has expired")
        except jwt.InvalidTokenError:
            raise Exception("The token is invalid")

    @staticmethod
    def is_blacklisted(token: str) -> bool:
        """Check the specified token has been blacklisted.

        :param
            token

        :return
            Boolean
        """

        blacklisted = BlacklistedToken.query.filter_by(token=token).first()

        return True if blacklisted else False
