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



from ...api_client import Dictionary

# Query params
ValueSchema = schemas.StrSchema


class CompensationTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def SAL(cls):
        return cls("sal")
    
    @schemas.classproperty
    def PAY(cls):
        return cls("pay")
    
    @schemas.classproperty
    def BONUS(cls):
        return cls("bonus")
    
    @schemas.classproperty
    def INCTV(cls):
        return cls("INCTV")
    
    @schemas.classproperty
    def SVRC(cls):
        return cls("SVRC")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("other")
CurrencyCodeSchema = schemas.StrSchema


class PeriodSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def HRLY(cls):
        return cls("HRLY")
    
    @schemas.classproperty
    def DLY(cls):
        return cls("DLY")
    
    @schemas.classproperty
    def WKLY(cls):
        return cls("WKLY")
    
    @schemas.classproperty
    def BWKLY(cls):
        return cls("BWKLY")
    
    @schemas.classproperty
    def MTHLY(cls):
        return cls("MTHLY")
    
    @schemas.classproperty
    def BMTH(cls):
        return cls("BMTH")
    
    @schemas.classproperty
    def QTRLY(cls):
        return cls("QTRLY")
    
    @schemas.classproperty
    def BYRLY(cls):
        return cls("BYRLY")
    
    @schemas.classproperty
    def YRLY(cls):
        return cls("YRLY")
    
    @schemas.classproperty
    def ONEF(cls):
        return cls("ONEF")
EffectivedateSchema = schemas.StrSchema
EnddateSchema = schemas.StrSchema


class StatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ACTV(cls):
        return cls("ACTV")
    
    @schemas.classproperty
    def ARCHV(cls):
        return cls("ARCHV")
    
    @schemas.classproperty
    def PVNL(cls):
        return cls("PVNL")
NotesSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'value': typing.Union[ValueSchema, str, ],
        'compensationType': typing.Union[CompensationTypeSchema, str, ],
        'currencyCode': typing.Union[CurrencyCodeSchema, str, ],
        'period': typing.Union[PeriodSchema, str, ],
        'effectivedate': typing.Union[EffectivedateSchema, str, ],
        'status': typing.Union[StatusSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'enddate': typing.Union[EnddateSchema, str, ],
        'notes': typing.Union[NotesSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_value = api_client.QueryParameter(
    name="value",
    style=api_client.ParameterStyle.FORM,
    schema=ValueSchema,
    required=True,
    explode=True,
)
request_query_compensation_type = api_client.QueryParameter(
    name="compensationType",
    style=api_client.ParameterStyle.FORM,
    schema=CompensationTypeSchema,
    required=True,
    explode=True,
)
request_query_currency_code = api_client.QueryParameter(
    name="currencyCode",
    style=api_client.ParameterStyle.FORM,
    schema=CurrencyCodeSchema,
    required=True,
    explode=True,
)
request_query_period = api_client.QueryParameter(
    name="period",
    style=api_client.ParameterStyle.FORM,
    schema=PeriodSchema,
    required=True,
    explode=True,
)
request_query_effectivedate = api_client.QueryParameter(
    name="effectivedate",
    style=api_client.ParameterStyle.FORM,
    schema=EffectivedateSchema,
    required=True,
    explode=True,
)
request_query_enddate = api_client.QueryParameter(
    name="enddate",
    style=api_client.ParameterStyle.FORM,
    schema=EnddateSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    required=True,
    explode=True,
)
request_query_notes = api_client.QueryParameter(
    name="notes",
    style=api_client.ParameterStyle.FORM,
    schema=NotesSchema,
    explode=True,
)
SchemaFor201ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_user_compensation_mapped_args(
        self,
        value: str,
        compensation_type: str,
        currency_code: str,
        period: str,
        effectivedate: str,
        status: str,
        enddate: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if value is not None:
            _query_params["value"] = value
        if compensation_type is not None:
            _query_params["compensationType"] = compensation_type
        if currency_code is not None:
            _query_params["currencyCode"] = currency_code
        if period is not None:
            _query_params["period"] = period
        if effectivedate is not None:
            _query_params["effectivedate"] = effectivedate
        if enddate is not None:
            _query_params["enddate"] = enddate
        if status is not None:
            _query_params["status"] = status
        if notes is not None:
            _query_params["notes"] = notes
        args.query = _query_params
        return args

    async def _acreate_user_compensation_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create compensation for user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_value,
            request_query_compensation_type,
            request_query_currency_code,
            request_query_period,
            request_query_effectivedate,
            request_query_enddate,
            request_query_status,
            request_query_notes,
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
            path_template='/api/user/compensation/add',
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


    def _create_user_compensation_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create compensation for user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_value,
            request_query_compensation_type,
            request_query_currency_code,
            request_query_period,
            request_query_effectivedate,
            request_query_enddate,
            request_query_status,
            request_query_notes,
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
            path_template='/api/user/compensation/add',
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


class CreateUserCompensationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_user_compensation(
        self,
        value: str,
        compensation_type: str,
        currency_code: str,
        period: str,
        effectivedate: str,
        status: str,
        enddate: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_user_compensation_mapped_args(
            value=value,
            compensation_type=compensation_type,
            currency_code=currency_code,
            period=period,
            effectivedate=effectivedate,
            status=status,
            enddate=enddate,
            notes=notes,
        )
        return await self._acreate_user_compensation_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def create_user_compensation(
        self,
        value: str,
        compensation_type: str,
        currency_code: str,
        period: str,
        effectivedate: str,
        status: str,
        enddate: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_user_compensation_mapped_args(
            value=value,
            compensation_type=compensation_type,
            currency_code=currency_code,
            period=period,
            effectivedate=effectivedate,
            status=status,
            enddate=enddate,
            notes=notes,
        )
        return self._create_user_compensation_oapg(
            query_params=args.query,
        )

class CreateUserCompensation(BaseApi):

    async def acreate_user_compensation(
        self,
        value: str,
        compensation_type: str,
        currency_code: str,
        period: str,
        effectivedate: str,
        status: str,
        enddate: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.acreate_user_compensation(
            value=value,
            compensation_type=compensation_type,
            currency_code=currency_code,
            period=period,
            effectivedate=effectivedate,
            status=status,
            enddate=enddate,
            notes=notes,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def create_user_compensation(
        self,
        value: str,
        compensation_type: str,
        currency_code: str,
        period: str,
        effectivedate: str,
        status: str,
        enddate: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.create_user_compensation(
            value=value,
            compensation_type=compensation_type,
            currency_code=currency_code,
            period=period,
            effectivedate=effectivedate,
            status=status,
            enddate=enddate,
            notes=notes,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        value: str,
        compensation_type: str,
        currency_code: str,
        period: str,
        effectivedate: str,
        status: str,
        enddate: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_user_compensation_mapped_args(
            value=value,
            compensation_type=compensation_type,
            currency_code=currency_code,
            period=period,
            effectivedate=effectivedate,
            status=status,
            enddate=enddate,
            notes=notes,
        )
        return await self._acreate_user_compensation_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        value: str,
        compensation_type: str,
        currency_code: str,
        period: str,
        effectivedate: str,
        status: str,
        enddate: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_user_compensation_mapped_args(
            value=value,
            compensation_type=compensation_type,
            currency_code=currency_code,
            period=period,
            effectivedate=effectivedate,
            status=status,
            enddate=enddate,
            notes=notes,
        )
        return self._create_user_compensation_oapg(
            query_params=args.query,
        )

