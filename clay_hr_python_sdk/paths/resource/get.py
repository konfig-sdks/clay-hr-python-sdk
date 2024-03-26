# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from clay_hr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from clay_hr_python_sdk.api_response import AsyncGeneratorResponse
from clay_hr_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from clay_hr_python_sdk import schemas  # noqa: F401

from clay_hr_python_sdk.model.people_and_permissions_get_users_response import PeopleAndPermissionsGetUsersResponse as PeopleAndPermissionsGetUsersResponseSchema

from clay_hr_python_sdk.type.people_and_permissions_get_users_response import PeopleAndPermissionsGetUsersResponse

from ...api_client import Dictionary
from clay_hr_python_sdk.pydantic.people_and_permissions_get_users_response import PeopleAndPermissionsGetUsersResponse as PeopleAndPermissionsGetUsersResponsePydantic

from . import path

# Query params
NameSchema = schemas.StrSchema
PageSchema = schemas.Int32Schema
PageSizeSchema = schemas.Int32Schema
SortBySchema = schemas.StrSchema


class SortOrderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "asc": "ASC",
            "desc": "DESC",
        }
    
    @schemas.classproperty
    def ASC(cls):
        return cls("asc")
    
    @schemas.classproperty
    def DESC(cls):
        return cls("desc")


class StatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "A": "A",
            "I": "I",
            "F": "F",
        }
    
    @schemas.classproperty
    def A(cls):
        return cls("A")
    
    @schemas.classproperty
    def I(cls):
        return cls("I")
    
    @schemas.classproperty
    def F(cls):
        return cls("F")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'name': typing.Union[NameSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'pageSize': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'sortBy': typing.Union[SortBySchema, str, ],
        'sortOrder': typing.Union[SortOrderSchema, str, ],
        'status': typing.Union[StatusSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_name = api_client.QueryParameter(
    name="name",
    style=api_client.ParameterStyle.FORM,
    schema=NameSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="pageSize",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sortBy",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
request_query_sort_order = api_client.QueryParameter(
    name="sortOrder",
    style=api_client.ParameterStyle.FORM,
    schema=SortOrderSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
_auth = [
    'sec0',
    'sec1',
]
SchemaFor200ResponseBody = PeopleAndPermissionsGetUsersResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PeopleAndPermissionsGetUsersResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PeopleAndPermissionsGetUsersResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        '*/*': api_client.MediaType(
            schema=SchemaFor200ResponseBody),
    },
)
SchemaFor409ResponseBody = schemas.DictSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        '*/*': api_client.MediaType(
            schema=SchemaFor409ResponseBody),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '409': _response_for_409,
}
_all_accept_content_types = (
    '*/*',
)


class BaseApi(api_client.Api):

    def _get_users_mapped_args(
        self,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if name is not None:
            _query_params["name"] = name
        if page is not None:
            _query_params["page"] = page
        if page_size is not None:
            _query_params["pageSize"] = page_size
        if sort_by is not None:
            _query_params["sortBy"] = sort_by
        if sort_order is not None:
            _query_params["sortOrder"] = sort_order
        if status is not None:
            _query_params["status"] = status
        args.query = _query_params
        return args

    async def _aget_users_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_name,
            request_query_page,
            request_query_page_size,
            request_query_sort_by,
            request_query_sort_order,
            request_query_status,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/resource',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_users_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_name,
            request_query_page,
            request_query_page_size,
            request_query_sort_by,
            request_query_sort_order,
            request_query_status,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/resource',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetUsersRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_users(
        self,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_users_mapped_args(
            name=name,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            status=status,
        )
        return await self._aget_users_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_users(
        self,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_users_mapped_args(
            name=name,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            status=status,
        )
        return self._get_users_oapg(
            query_params=args.query,
        )

class GetUsers(BaseApi):

    async def aget_users(
        self,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PeopleAndPermissionsGetUsersResponsePydantic:
        raw_response = await self.raw.aget_users(
            name=name,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            status=status,
            **kwargs,
        )
        if validate:
            return PeopleAndPermissionsGetUsersResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PeopleAndPermissionsGetUsersResponsePydantic, raw_response.body)
    
    
    def get_users(
        self,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PeopleAndPermissionsGetUsersResponsePydantic:
        raw_response = self.raw.get_users(
            name=name,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            status=status,
        )
        if validate:
            return PeopleAndPermissionsGetUsersResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PeopleAndPermissionsGetUsersResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_users_mapped_args(
            name=name,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            status=status,
        )
        return await self._aget_users_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_users_mapped_args(
            name=name,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            status=status,
        )
        return self._get_users_oapg(
            query_params=args.query,
        )

