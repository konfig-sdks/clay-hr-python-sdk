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

from clay_hr_python_sdk.model.timesheets_update_status_by_timesheet_id409_response import TimesheetsUpdateStatusByTimesheetId409Response as TimesheetsUpdateStatusByTimesheetId409ResponseSchema
from clay_hr_python_sdk.model.timesheets_update_status_by_timesheet_id_response import TimesheetsUpdateStatusByTimesheetIdResponse as TimesheetsUpdateStatusByTimesheetIdResponseSchema
from clay_hr_python_sdk.model.timesheets_update_status_by_timesheet_id401_response import TimesheetsUpdateStatusByTimesheetId401Response as TimesheetsUpdateStatusByTimesheetId401ResponseSchema

from clay_hr_python_sdk.type.timesheets_update_status_by_timesheet_id_response import TimesheetsUpdateStatusByTimesheetIdResponse
from clay_hr_python_sdk.type.timesheets_update_status_by_timesheet_id401_response import TimesheetsUpdateStatusByTimesheetId401Response
from clay_hr_python_sdk.type.timesheets_update_status_by_timesheet_id409_response import TimesheetsUpdateStatusByTimesheetId409Response

from ...api_client import Dictionary
from clay_hr_python_sdk.pydantic.timesheets_update_status_by_timesheet_id_response import TimesheetsUpdateStatusByTimesheetIdResponse as TimesheetsUpdateStatusByTimesheetIdResponsePydantic
from clay_hr_python_sdk.pydantic.timesheets_update_status_by_timesheet_id401_response import TimesheetsUpdateStatusByTimesheetId401Response as TimesheetsUpdateStatusByTimesheetId401ResponsePydantic
from clay_hr_python_sdk.pydantic.timesheets_update_status_by_timesheet_id409_response import TimesheetsUpdateStatusByTimesheetId409Response as TimesheetsUpdateStatusByTimesheetId409ResponsePydantic

# Query params
TimesheetIdSchema = schemas.Int32Schema


class StatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def PD(cls):
        return cls("PD")
    
    @schemas.classproperty
    def PAP(cls):
        return cls("PAP")
    
    @schemas.classproperty
    def AP(cls):
        return cls("AP")
    
    @schemas.classproperty
    def NEW(cls):
        return cls("NEW")
    
    @schemas.classproperty
    def RJ(cls):
        return cls("RJ")
CommentsSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'timesheetId': typing.Union[TimesheetIdSchema, decimal.Decimal, int, ],
        'status': typing.Union[StatusSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'comments': typing.Union[CommentsSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_timesheet_id = api_client.QueryParameter(
    name="timesheetId",
    style=api_client.ParameterStyle.FORM,
    schema=TimesheetIdSchema,
    required=True,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    required=True,
    explode=True,
)
request_query_comments = api_client.QueryParameter(
    name="comments",
    style=api_client.ParameterStyle.FORM,
    schema=CommentsSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = TimesheetsUpdateStatusByTimesheetIdResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TimesheetsUpdateStatusByTimesheetIdResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TimesheetsUpdateStatusByTimesheetIdResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = TimesheetsUpdateStatusByTimesheetId401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: TimesheetsUpdateStatusByTimesheetId401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: TimesheetsUpdateStatusByTimesheetId401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor409ResponseBodyApplicationJson = TimesheetsUpdateStatusByTimesheetId409ResponseSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: TimesheetsUpdateStatusByTimesheetId409Response


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: TimesheetsUpdateStatusByTimesheetId409Response


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

    def _update_status_by_timesheet_id_mapped_args(
        self,
        timesheet_id: int,
        status: str,
        comments: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if timesheet_id is not None:
            _query_params["timesheetId"] = timesheet_id
        if status is not None:
            _query_params["status"] = status
        if comments is not None:
            _query_params["comments"] = comments
        args.query = _query_params
        return args

    async def _aupdate_status_by_timesheet_id_oapg(
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
        Update timesheet status by Timesheet ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_timesheet_id,
            request_query_status,
            request_query_comments,
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
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/timesheet/update',
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


    def _update_status_by_timesheet_id_oapg(
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
        Update timesheet status by Timesheet ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_timesheet_id,
            request_query_status,
            request_query_comments,
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
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/timesheet/update',
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


class UpdateStatusByTimesheetIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_status_by_timesheet_id(
        self,
        timesheet_id: int,
        status: str,
        comments: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_status_by_timesheet_id_mapped_args(
            timesheet_id=timesheet_id,
            status=status,
            comments=comments,
        )
        return await self._aupdate_status_by_timesheet_id_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def update_status_by_timesheet_id(
        self,
        timesheet_id: int,
        status: str,
        comments: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_status_by_timesheet_id_mapped_args(
            timesheet_id=timesheet_id,
            status=status,
            comments=comments,
        )
        return self._update_status_by_timesheet_id_oapg(
            query_params=args.query,
        )

class UpdateStatusByTimesheetId(BaseApi):

    async def aupdate_status_by_timesheet_id(
        self,
        timesheet_id: int,
        status: str,
        comments: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TimesheetsUpdateStatusByTimesheetIdResponsePydantic:
        raw_response = await self.raw.aupdate_status_by_timesheet_id(
            timesheet_id=timesheet_id,
            status=status,
            comments=comments,
            **kwargs,
        )
        if validate:
            return TimesheetsUpdateStatusByTimesheetIdResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimesheetsUpdateStatusByTimesheetIdResponsePydantic, raw_response.body)
    
    
    def update_status_by_timesheet_id(
        self,
        timesheet_id: int,
        status: str,
        comments: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TimesheetsUpdateStatusByTimesheetIdResponsePydantic:
        raw_response = self.raw.update_status_by_timesheet_id(
            timesheet_id=timesheet_id,
            status=status,
            comments=comments,
        )
        if validate:
            return TimesheetsUpdateStatusByTimesheetIdResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimesheetsUpdateStatusByTimesheetIdResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        timesheet_id: int,
        status: str,
        comments: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_status_by_timesheet_id_mapped_args(
            timesheet_id=timesheet_id,
            status=status,
            comments=comments,
        )
        return await self._aupdate_status_by_timesheet_id_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        timesheet_id: int,
        status: str,
        comments: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_status_by_timesheet_id_mapped_args(
            timesheet_id=timesheet_id,
            status=status,
            comments=comments,
        )
        return self._update_status_by_timesheet_id_oapg(
            query_params=args.query,
        )

