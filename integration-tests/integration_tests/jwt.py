import secrets
import time
from datetime import datetime, timedelta, timezone
from threading import Lock

import jwt


class JwtGenerator:
    def __init__(self, key: str, kid: str, exp: int):
        self.key = key
        self.kid = kid
        self.exp = exp

        self._expires: float = 0
        self._jwt: str = ""
        self._lock = Lock()

        # generate a new token 10 seconds earlier than the 'exp' header to give
        # enough time for the request to be made
        self._expires_leeway = 10

    def generate(self) -> str:
        if self._needs_refresh():
            with self._lock:
                self._generate()

        return self._jwt

    def _needs_refresh(self) -> bool:
        return not self._jwt or self._expires < time.monotonic()

    def _generate(self) -> None:
        jti = secrets.token_hex(16)
        now = datetime.now(tz=timezone.utc)
        exp = now + timedelta(seconds=self.exp)

        payload = {"jti": jti, "nbf": now, "exp": exp, "iat": now, "aud": "api"}
        headers = {"kid": self.kid}

        self._expires = time.monotonic() + self.exp - self._expires_leeway

        if self._expires < 0:
            self._expires = 0

        self._jwt = jwt.encode(payload=payload, headers=headers, algorithm="ES256", key=self.key)
