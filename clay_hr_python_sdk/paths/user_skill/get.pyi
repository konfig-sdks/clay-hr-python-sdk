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

from clay_hr_python_sdk.model.skills_get_user_assigned_skills_response import SkillsGetUserAssignedSkillsResponse as SkillsGetUserAssignedSkillsResponseSchema
from clay_hr_python_sdk.model.skills_get_user_assigned_skills401_response import SkillsGetUserAssignedSkills401Response as SkillsGetUserAssignedSkills401ResponseSchema
from clay_hr_python_sdk.model.skills_get_user_assigned_skills409_response import SkillsGetUserAssignedSkills409Response as SkillsGetUserAssignedSkills409ResponseSchema

from clay_hr_python_sdk.type.skills_get_user_assigned_skills409_response import SkillsGetUserAssignedSkills409Response
from clay_hr_python_sdk.type.skills_get_user_assigned_skills_response import SkillsGetUserAssignedSkillsResponse
from clay_hr_python_sdk.type.skills_get_user_assigned_skills401_response import SkillsGetUserAssignedSkills401Response

from ...api_client import Dictionary
from clay_hr_python_sdk.pydantic.skills_get_user_assigned_skills_response import SkillsGetUserAssignedSkillsResponse as SkillsGetUserAssignedSkillsResponsePydantic
from clay_hr_python_sdk.pydantic.skills_get_user_assigned_skills401_response import SkillsGetUserAssignedSkills401Response as SkillsGetUserAssignedSkills401ResponsePydantic
from clay_hr_python_sdk.pydantic.skills_get_user_assigned_skills409_response import SkillsGetUserAssignedSkills409Response as SkillsGetUserAssignedSkills409ResponsePydantic

# Query params
AssignedUserIDSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'assignedUserID': typing.Union[AssignedUserIDSchema, decimal.Decimal, int, ],
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


request_query_assigned_user_id = api_client.QueryParameter(
    name="assignedUserID",
    style=api_client.ParameterStyle.FORM,
    schema=AssignedUserIDSchema,
    required=True,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = SkillsGetUserAssignedSkillsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SkillsGetUserAssignedSkillsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SkillsGetUserAssignedSkillsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = SkillsGetUserAssignedSkills401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: SkillsGetUserAssignedSkills401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: SkillsGetUserAssignedSkills401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor409ResponseBodyApplicationJson = SkillsGetUserAssignedSkills409ResponseSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: SkillsGetUserAssignedSkills409Response


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: SkillsGetUserAssignedSkills409Response


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_user_assigned_skills_mapped_args(
        self,
        assigned_user_id: int,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if assigned_user_id is not None:
            _query_params["assignedUserID"] = assigned_user_id
        args.query = _query_params
        return args

    async def _aget_user_assigned_skills_oapg(
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
        Retrieve skills assigned to a user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_assigned_user_id,
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
            path_template='/userSkill',
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


    def _get_user_assigned_skills_oapg(
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
        Retrieve skills assigned to a user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_assigned_user_id,
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
            path_template='/userSkill',
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


class GetUserAssignedSkillsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_assigned_skills(
        self,
        assigned_user_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_assigned_skills_mapped_args(
            assigned_user_id=assigned_user_id,
        )
        return await self._aget_user_assigned_skills_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_user_assigned_skills(
        self,
        assigned_user_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_assigned_skills_mapped_args(
            assigned_user_id=assigned_user_id,
        )
        return self._get_user_assigned_skills_oapg(
            query_params=args.query,
        )

class GetUserAssignedSkills(BaseApi):

    async def aget_user_assigned_skills(
        self,
        assigned_user_id: int,
        validate: bool = False,
        **kwargs,
    ) -> SkillsGetUserAssignedSkillsResponsePydantic:
        raw_response = await self.raw.aget_user_assigned_skills(
            assigned_user_id=assigned_user_id,
            **kwargs,
        )
        if validate:
            return SkillsGetUserAssignedSkillsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SkillsGetUserAssignedSkillsResponsePydantic, raw_response.body)
    
    
    def get_user_assigned_skills(
        self,
        assigned_user_id: int,
        validate: bool = False,
    ) -> SkillsGetUserAssignedSkillsResponsePydantic:
        raw_response = self.raw.get_user_assigned_skills(
            assigned_user_id=assigned_user_id,
        )
        if validate:
            return SkillsGetUserAssignedSkillsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SkillsGetUserAssignedSkillsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        assigned_user_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_assigned_skills_mapped_args(
            assigned_user_id=assigned_user_id,
        )
        return await self._aget_user_assigned_skills_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        assigned_user_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_assigned_skills_mapped_args(
            assigned_user_id=assigned_user_id,
        )
        return self._get_user_assigned_skills_oapg(
            query_params=args.query,
        )

