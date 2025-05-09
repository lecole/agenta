# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from ..types.list_api_keys_response import ListApiKeysResponse
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..core.client_wrapper import AsyncClientWrapper


class ApiKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_api_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListApiKeysResponse]:
        """
        List all API keys associated with the authenticated user.

        Args:
            request (Request): The incoming request object.

        Returns:
            List[ListAPIKeysResponse]: A list of API Keys associated with the user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListApiKeysResponse]
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.api_keys.list_api_keys()
        """
        _response = self._client_wrapper.httpx_client.request(
            "keys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ListApiKeysResponse],
                    parse_obj_as(
                        type_=typing.List[ListApiKeysResponse],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Creates an API key for a user.

        Args:
            request (Request): The request object containing the user ID in the request state.

        Returns:
            str: The created API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.api_keys.create_api_key()
        """
        _response = self._client_wrapper.httpx_client.request(
            "keys",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_api_key(
        self,
        key_prefix: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Delete an API key with the given key prefix for the authenticated user.

        Args:
            key_prefix (str): The prefix of the API key to be deleted.
            request (Request): The incoming request object.

        Returns:
            dict: A dictionary containing a success message upon successful deletion.

        Raises:
            HTTPException: If the API key is not found or does not belong to the user.

        Parameters
        ----------
        key_prefix : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.api_keys.delete_api_key(
            key_prefix="key_prefix",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"keys/{jsonable_encoder(key_prefix)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Dict[str, typing.Optional[typing.Any]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Optional[typing.Any]],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def validate_api_key(
        self,
        key_prefix: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        This Function is called by the CLI and is used to validate an API key provided by a user in agenta init setup.
        Returns:
            bool: True. If the request reaches this point, the API key is valid.

        Parameters
        ----------
        key_prefix : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.api_keys.validate_api_key(
            key_prefix="key_prefix",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"keys/{jsonable_encoder(key_prefix)}/validate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncApiKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_api_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListApiKeysResponse]:
        """
        List all API keys associated with the authenticated user.

        Args:
            request (Request): The incoming request object.

        Returns:
            List[ListAPIKeysResponse]: A list of API Keys associated with the user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListApiKeysResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.api_keys.list_api_keys()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "keys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ListApiKeysResponse],
                    parse_obj_as(
                        type_=typing.List[ListApiKeysResponse],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Creates an API key for a user.

        Args:
            request (Request): The request object containing the user ID in the request state.

        Returns:
            str: The created API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.api_keys.create_api_key()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "keys",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_api_key(
        self,
        key_prefix: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Delete an API key with the given key prefix for the authenticated user.

        Args:
            key_prefix (str): The prefix of the API key to be deleted.
            request (Request): The incoming request object.

        Returns:
            dict: A dictionary containing a success message upon successful deletion.

        Raises:
            HTTPException: If the API key is not found or does not belong to the user.

        Parameters
        ----------
        key_prefix : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.api_keys.delete_api_key(
                key_prefix="key_prefix",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"keys/{jsonable_encoder(key_prefix)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Dict[str, typing.Optional[typing.Any]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Optional[typing.Any]],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def validate_api_key(
        self,
        key_prefix: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        This Function is called by the CLI and is used to validate an API key provided by a user in agenta init setup.
        Returns:
            bool: True. If the request reaches this point, the API key is valid.

        Parameters
        ----------
        key_prefix : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.api_keys.validate_api_key(
                key_prefix="key_prefix",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"keys/{jsonable_encoder(key_prefix)}/validate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
