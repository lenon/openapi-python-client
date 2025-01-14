from http import HTTPStatus
from typing import Any, Dict, Union

import httpx

from ... import errors
from ...client import Client
from ...models.post_parameters_header_response_200 import PostParametersHeaderResponse200
from ...models.public_error import PublicError
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    boolean_header: bool,
    string_header: str,
    number_header: float,
    integer_header: int,
) -> Dict[str, Any]:
    url = "{}/parameters/header".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()

    headers["Boolean-Header"] = "true" if boolean_header else "false"

    headers["String-Header"] = string_header

    headers["Number-Header"] = str(number_header)

    headers["Integer-Header"] = str(integer_header)

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Union[PostParametersHeaderResponse200, PublicError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostParametersHeaderResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = PublicError.from_dict(response.json())

        return response_400
    else:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}", response=response)


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[PostParametersHeaderResponse200, PublicError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    boolean_header: bool,
    string_header: str,
    number_header: float,
    integer_header: int,
) -> Response[Union[PostParametersHeaderResponse200, PublicError]]:
    """
    Args:
        boolean_header (bool):
        string_header (str):
        number_header (float):
        integer_header (int):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostParametersHeaderResponse200, PublicError]]
    """

    kwargs = _get_kwargs(
        client=client,
        boolean_header=boolean_header,
        string_header=string_header,
        number_header=number_header,
        integer_header=integer_header,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    boolean_header: bool,
    string_header: str,
    number_header: float,
    integer_header: int,
) -> Union[PostParametersHeaderResponse200, PublicError]:
    """
    Args:
        boolean_header (bool):
        string_header (str):
        number_header (float):
        integer_header (int):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostParametersHeaderResponse200, PublicError]]
    """

    return sync_detailed(
        client=client,
        boolean_header=boolean_header,
        string_header=string_header,
        number_header=number_header,
        integer_header=integer_header,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    boolean_header: bool,
    string_header: str,
    number_header: float,
    integer_header: int,
) -> Response[Union[PostParametersHeaderResponse200, PublicError]]:
    """
    Args:
        boolean_header (bool):
        string_header (str):
        number_header (float):
        integer_header (int):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostParametersHeaderResponse200, PublicError]]
    """

    kwargs = _get_kwargs(
        client=client,
        boolean_header=boolean_header,
        string_header=string_header,
        number_header=number_header,
        integer_header=integer_header,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    boolean_header: bool,
    string_header: str,
    number_header: float,
    integer_header: int,
) -> Union[PostParametersHeaderResponse200, PublicError]:
    """
    Args:
        boolean_header (bool):
        string_header (str):
        number_header (float):
        integer_header (int):

    Raises:
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostParametersHeaderResponse200, PublicError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            boolean_header=boolean_header,
            string_header=string_header,
            number_header=number_header,
            integer_header=integer_header,
        )
    ).parsed
