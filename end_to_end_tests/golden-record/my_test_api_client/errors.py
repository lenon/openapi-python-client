""" Contains shared errors types that can be raised from API functions """
import httpx


class UnexpectedStatus(Exception):
    """Raised by api functions when the response status is an undocumented status."""

    response: httpx.Response

    def __init__(self, *args: object, response: httpx.Response) -> None:
        super().__init__(*args)
        self.response = response


__all__ = ["UnexpectedStatus"]
