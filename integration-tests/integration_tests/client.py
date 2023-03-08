import ssl
from typing import Dict, Union

import attr

from .jwt import JwtGenerator


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API

    Attributes:
        base_url: The base URL for the API, all requests are made to a relative path to this URL
        headers: A dictionary of headers to be sent with every request
        timeout: The maximum amount of a time in seconds a request can take. API functions will raise
            httpx.TimeoutException if this is exceeded.
        verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
            but can be set to False for testing purposes.
        key: The private key used to sign the JWT encoded with ES256.
        key_fingerprint: Key ID or fingerprint.
        jwt_expiration: Controls the expiration time for a JWT. 60 seconds by default.
    """

    base_url: str
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)

    key: str = attr.ib(kw_only=True)
    key_fingerprint: str = attr.ib(kw_only=True)
    jwt_expiration: int = attr.ib(60, kw_only=True)

    def __attrs_post_init__(self) -> None:
        self._jwt_generator = JwtGenerator(key=self.key, kid=self.key_fingerprint, exp=self.jwt_expiration)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        token = self._jwt_generator.generate()
        return {"Authorization": f"Bearer {token}", **self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)
