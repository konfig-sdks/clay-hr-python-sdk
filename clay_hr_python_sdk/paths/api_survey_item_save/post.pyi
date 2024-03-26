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

from clay_hr_python_sdk.model.survey_create_item_response_response import SurveyCreateItemResponseResponse as SurveyCreateItemResponseResponseSchema

from clay_hr_python_sdk.type.survey_create_item_response_response import SurveyCreateItemResponseResponse

from ...api_client import Dictionary
from clay_hr_python_sdk.pydantic.survey_create_item_response_response import SurveyCreateItemResponseResponse as SurveyCreateItemResponseResponsePydantic

# Query params
AssignmentIdSchema = schemas.Int32Schema
ItemIdSchema = schemas.Int32Schema
ResponseValueSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'assignmentId': typing.Union[AssignmentIdSchema, decimal.Decimal, int, ],
        'itemId': typing.Union[ItemIdSchema, decimal.Decimal, int, ],
        'responseValue': typing.Union[ResponseValueSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_assignment_id = api_client.QueryParameter(
    name="assignmentId",
    style=api_client.ParameterStyle.FORM,
    schema=AssignmentIdSchema,
    required=True,
    explode=True,
)
request_query_item_id = api_client.QueryParameter(
    name="itemId",
    style=api_client.ParameterStyle.FORM,
    schema=ItemIdSchema,
    required=True,
    explode=True,
)
request_query_response_value = api_client.QueryParameter(
    name="responseValue",
    style=api_client.ParameterStyle.FORM,
    schema=ResponseValueSchema,
    required=True,
    explode=True,
)
# Header params
AuthorizationSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'Authorization': typing.Union[AuthorizationSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_authorization = api_client.HeaderParameter(
    name="Authorization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthorizationSchema,
)
SchemaFor200ResponseBody = SurveyCreateItemResponseResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SurveyCreateItemResponseResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SurveyCreateItemResponseResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        '*/*': api_client.MediaType(
            schema=SchemaFor200ResponseBody),
    },
)


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)
_all_accept_content_types = (
    '*/*',
)


class BaseApi(api_client.Api):

    def _create_item_response_mapped_args(
        self,
        assignment_id: int,
        item_id: int,
        response_value: str,
        authorization: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if assignment_id is not None:
            _query_params["assignmentId"] = assignment_id
        if item_id is not None:
            _query_params["itemId"] = item_id
        if response_value is not None:
            _query_params["responseValue"] = response_value
        if authorization is not None:
            _header_params["Authorization"] = authorization
        args.query = _query_params
        args.header = _header_params
        return args

    async def _acreate_item_response_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create the item&#x27;s response for a survey
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_assignment_id,
            request_query_item_id,
            request_query_response_value,
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
        for parameter in (
            request_header_authorization,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/survey/item/save',
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


    def _create_item_response_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create the item&#x27;s response for a survey
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_assignment_id,
            request_query_item_id,
            request_query_response_value,
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
        for parameter in (
            request_header_authorization,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/survey/item/save',
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


class CreateItemResponseRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_item_response(
        self,
        assignment_id: int,
        item_id: int,
        response_value: str,
        authorization: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_item_response_mapped_args(
            assignment_id=assignment_id,
            item_id=item_id,
            response_value=response_value,
            authorization=authorization,
        )
        return await self._acreate_item_response_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def create_item_response(
        self,
        assignment_id: int,
        item_id: int,
        response_value: str,
        authorization: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_item_response_mapped_args(
            assignment_id=assignment_id,
            item_id=item_id,
            response_value=response_value,
            authorization=authorization,
        )
        return self._create_item_response_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class CreateItemResponse(BaseApi):

    async def acreate_item_response(
        self,
        assignment_id: int,
        item_id: int,
        response_value: str,
        authorization: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> SurveyCreateItemResponseResponsePydantic:
        raw_response = await self.raw.acreate_item_response(
            assignment_id=assignment_id,
            item_id=item_id,
            response_value=response_value,
            authorization=authorization,
            **kwargs,
        )
        if validate:
            return SurveyCreateItemResponseResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SurveyCreateItemResponseResponsePydantic, raw_response.body)
    
    
    def create_item_response(
        self,
        assignment_id: int,
        item_id: int,
        response_value: str,
        authorization: typing.Optional[str] = None,
        validate: bool = False,
    ) -> SurveyCreateItemResponseResponsePydantic:
        raw_response = self.raw.create_item_response(
            assignment_id=assignment_id,
            item_id=item_id,
            response_value=response_value,
            authorization=authorization,
        )
        if validate:
            return SurveyCreateItemResponseResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SurveyCreateItemResponseResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        assignment_id: int,
        item_id: int,
        response_value: str,
        authorization: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_item_response_mapped_args(
            assignment_id=assignment_id,
            item_id=item_id,
            response_value=response_value,
            authorization=authorization,
        )
        return await self._acreate_item_response_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        assignment_id: int,
        item_id: int,
        response_value: str,
        authorization: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_item_response_mapped_args(
            assignment_id=assignment_id,
            item_id=item_id,
            response_value=response_value,
            authorization=authorization,
        )
        return self._create_item_response_oapg(
            query_params=args.query,
            header_params=args.header,
        )

