from http import HTTPStatus
from typing import Any, Dict

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    import_: str,
) -> Dict[str, Any]:
    url = "{}/naming/keywords".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()

    params: Dict[str, Any] = {}
    params["import"] = import_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Any:
    if response.status_code == HTTPStatus.OK:
        return None
    else:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}", response=response)


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    import_: str,
) -> Response[Any]:
    """
    Args:
        import_ (str):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        import_=import_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    import_: str,
) -> Response[Any]:
    """
    Args:
        import_ (str):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        import_=import_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
