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

from clay_hr_python_sdk.model.custom_fields_get_value409_response import CustomFieldsGetValue409Response as CustomFieldsGetValue409ResponseSchema
from clay_hr_python_sdk.model.custom_fields_get_value401_response import CustomFieldsGetValue401Response as CustomFieldsGetValue401ResponseSchema
from clay_hr_python_sdk.model.custom_fields_get_value_response import CustomFieldsGetValueResponse as CustomFieldsGetValueResponseSchema

from clay_hr_python_sdk.type.custom_fields_get_value401_response import CustomFieldsGetValue401Response
from clay_hr_python_sdk.type.custom_fields_get_value409_response import CustomFieldsGetValue409Response
from clay_hr_python_sdk.type.custom_fields_get_value_response import CustomFieldsGetValueResponse

from ...api_client import Dictionary
from clay_hr_python_sdk.pydantic.custom_fields_get_value_response import CustomFieldsGetValueResponse as CustomFieldsGetValueResponsePydantic
from clay_hr_python_sdk.pydantic.custom_fields_get_value401_response import CustomFieldsGetValue401Response as CustomFieldsGetValue401ResponsePydantic
from clay_hr_python_sdk.pydantic.custom_fields_get_value409_response import CustomFieldsGetValue409Response as CustomFieldsGetValue409ResponsePydantic

from . import path

# Query params
CustomFieldCodeSchema = schemas.StrSchema
CustomFieldIdSchema = schemas.Int32Schema
UserEmailSchema = schemas.StrSchema
EmpIdSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'customFieldId': typing.Union[CustomFieldIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'customFieldCode': typing.Union[CustomFieldCodeSchema, str, ],
        'userEmail': typing.Union[UserEmailSchema, str, ],
        'empId': typing.Union[EmpIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_custom_field_code = api_client.QueryParameter(
    name="customFieldCode",
    style=api_client.ParameterStyle.FORM,
    schema=CustomFieldCodeSchema,
    explode=True,
)
request_query_custom_field_id = api_client.QueryParameter(
    name="customFieldId",
    style=api_client.ParameterStyle.FORM,
    schema=CustomFieldIdSchema,
    required=True,
    explode=True,
)
request_query_user_email = api_client.QueryParameter(
    name="userEmail",
    style=api_client.ParameterStyle.FORM,
    schema=UserEmailSchema,
    explode=True,
)
request_query_emp_id = api_client.QueryParameter(
    name="empId",
    style=api_client.ParameterStyle.FORM,
    schema=EmpIdSchema,
    explode=True,
)
_auth = [
    'sec0',
    'sec1',
]
SchemaFor200ResponseBodyApplicationJson = CustomFieldsGetValueResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CustomFieldsGetValueResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CustomFieldsGetValueResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = CustomFieldsGetValue401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: CustomFieldsGetValue401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: CustomFieldsGetValue401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor409ResponseBodyTextPlain = CustomFieldsGetValue409ResponseSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: CustomFieldsGetValue409Response


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: CustomFieldsGetValue409Response


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor409ResponseBodyTextPlain),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '409': _response_for_409,
}
_all_accept_content_types = (
    'application/json',
    'text/plain',
)


class BaseApi(api_client.Api):

    def _get_value_mapped_args(
        self,
        custom_field_id: int,
        custom_field_code: typing.Optional[str] = None,
        user_email: typing.Optional[str] = None,
        emp_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if custom_field_code is not None:
            _query_params["customFieldCode"] = custom_field_code
        if custom_field_id is not None:
            _query_params["customFieldId"] = custom_field_id
        if user_email is not None:
            _query_params["userEmail"] = user_email
        if emp_id is not None:
            _query_params["empId"] = emp_id
        args.query = _query_params
        return args

    async def _aget_value_oapg(
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
        Retrieve Custom Field Value
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_custom_field_code,
            request_query_custom_field_id,
            request_query_user_email,
            request_query_emp_id,
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
            path_template='/customfieldvalues',
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


    def _get_value_oapg(
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
        Retrieve Custom Field Value
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_custom_field_code,
            request_query_custom_field_id,
            request_query_user_email,
            request_query_emp_id,
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
            path_template='/customfieldvalues',
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


class GetValueRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_value(
        self,
        custom_field_id: int,
        custom_field_code: typing.Optional[str] = None,
        user_email: typing.Optional[str] = None,
        emp_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_value_mapped_args(
            custom_field_id=custom_field_id,
            custom_field_code=custom_field_code,
            user_email=user_email,
            emp_id=emp_id,
        )
        return await self._aget_value_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_value(
        self,
        custom_field_id: int,
        custom_field_code: typing.Optional[str] = None,
        user_email: typing.Optional[str] = None,
        emp_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_value_mapped_args(
            custom_field_id=custom_field_id,
            custom_field_code=custom_field_code,
            user_email=user_email,
            emp_id=emp_id,
        )
        return self._get_value_oapg(
            query_params=args.query,
        )

class GetValue(BaseApi):

    async def aget_value(
        self,
        custom_field_id: int,
        custom_field_code: typing.Optional[str] = None,
        user_email: typing.Optional[str] = None,
        emp_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CustomFieldsGetValueResponsePydantic:
        raw_response = await self.raw.aget_value(
            custom_field_id=custom_field_id,
            custom_field_code=custom_field_code,
            user_email=user_email,
            emp_id=emp_id,
            **kwargs,
        )
        if validate:
            return CustomFieldsGetValueResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CustomFieldsGetValueResponsePydantic, raw_response.body)
    
    
    def get_value(
        self,
        custom_field_id: int,
        custom_field_code: typing.Optional[str] = None,
        user_email: typing.Optional[str] = None,
        emp_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CustomFieldsGetValueResponsePydantic:
        raw_response = self.raw.get_value(
            custom_field_id=custom_field_id,
            custom_field_code=custom_field_code,
            user_email=user_email,
            emp_id=emp_id,
        )
        if validate:
            return CustomFieldsGetValueResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CustomFieldsGetValueResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        custom_field_id: int,
        custom_field_code: typing.Optional[str] = None,
        user_email: typing.Optional[str] = None,
        emp_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_value_mapped_args(
            custom_field_id=custom_field_id,
            custom_field_code=custom_field_code,
            user_email=user_email,
            emp_id=emp_id,
        )
        return await self._aget_value_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        custom_field_id: int,
        custom_field_code: typing.Optional[str] = None,
        user_email: typing.Optional[str] = None,
        emp_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_value_mapped_args(
            custom_field_id=custom_field_id,
            custom_field_code=custom_field_code,
            user_email=user_email,
            emp_id=emp_id,
        )
        return self._get_value_oapg(
            query_params=args.query,
        )

