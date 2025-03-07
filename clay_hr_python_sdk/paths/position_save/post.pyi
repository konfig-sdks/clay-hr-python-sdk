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

from clay_hr_python_sdk.model.positions_create_position409_response import PositionsCreatePosition409Response as PositionsCreatePosition409ResponseSchema
from clay_hr_python_sdk.model.positions_create_position_response import PositionsCreatePositionResponse as PositionsCreatePositionResponseSchema

from clay_hr_python_sdk.type.positions_create_position_response import PositionsCreatePositionResponse
from clay_hr_python_sdk.type.positions_create_position409_response import PositionsCreatePosition409Response

from ...api_client import Dictionary
from clay_hr_python_sdk.pydantic.positions_create_position409_response import PositionsCreatePosition409Response as PositionsCreatePosition409ResponsePydantic
from clay_hr_python_sdk.pydantic.positions_create_position_response import PositionsCreatePositionResponse as PositionsCreatePositionResponsePydantic

# Query params
NameSchema = schemas.StrSchema
DescriptionSchema = schemas.StrSchema
CountSchema = schemas.Int32Schema


class StatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def OPEN(cls):
        return cls("OPEN")
    
    @schemas.classproperty
    def HOLD(cls):
        return cls("HOLD")


class AccessLevelSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def PVT(cls):
        return cls("pvt")
    
    @schemas.classproperty
    def IJP(cls):
        return cls("ijp")
    
    @schemas.classproperty
    def PUB(cls):
        return cls("pub")
RequirementsSchema = schemas.StrSchema
ResponsibilitiesSchema = schemas.StrSchema
DateOpenSchema = schemas.StrSchema
DateCloseSchema = schemas.StrSchema
PositionUIDSchema = schemas.StrSchema
ProjectidSchema = schemas.Int32Schema
FunnelIdSchema = schemas.IntSchema
ApprovalFlowIdSchema = schemas.Int32Schema
LocationidSchema = schemas.Int32Schema
DepartmentIdSchema = schemas.StrSchema
ProfileidSchema = schemas.Int32Schema
RecruiterIdSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'name': typing.Union[NameSchema, str, ],
        'count': typing.Union[CountSchema, decimal.Decimal, int, ],
        'status': typing.Union[StatusSchema, str, ],
        'accessLevel': typing.Union[AccessLevelSchema, str, ],
        'dateOpen': typing.Union[DateOpenSchema, str, ],
        'dateClose': typing.Union[DateCloseSchema, str, ],
        'positionUID': typing.Union[PositionUIDSchema, str, ],
        'funnelId': typing.Union[FunnelIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'description': typing.Union[DescriptionSchema, str, ],
        'requirements': typing.Union[RequirementsSchema, str, ],
        'responsibilities': typing.Union[ResponsibilitiesSchema, str, ],
        'projectid': typing.Union[ProjectidSchema, decimal.Decimal, int, ],
        'approvalFlowId': typing.Union[ApprovalFlowIdSchema, decimal.Decimal, int, ],
        'locationid': typing.Union[LocationidSchema, decimal.Decimal, int, ],
        'departmentId': typing.Union[DepartmentIdSchema, str, ],
        'profileid': typing.Union[ProfileidSchema, decimal.Decimal, int, ],
        'recruiterId': typing.Union[RecruiterIdSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_name = api_client.QueryParameter(
    name="name",
    style=api_client.ParameterStyle.FORM,
    schema=NameSchema,
    required=True,
    explode=True,
)
request_query_description = api_client.QueryParameter(
    name="description",
    style=api_client.ParameterStyle.FORM,
    schema=DescriptionSchema,
    explode=True,
)
request_query_count = api_client.QueryParameter(
    name="count",
    style=api_client.ParameterStyle.FORM,
    schema=CountSchema,
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
request_query_access_level = api_client.QueryParameter(
    name="accessLevel",
    style=api_client.ParameterStyle.FORM,
    schema=AccessLevelSchema,
    required=True,
    explode=True,
)
request_query_requirements = api_client.QueryParameter(
    name="requirements",
    style=api_client.ParameterStyle.FORM,
    schema=RequirementsSchema,
    explode=True,
)
request_query_responsibilities = api_client.QueryParameter(
    name="responsibilities",
    style=api_client.ParameterStyle.FORM,
    schema=ResponsibilitiesSchema,
    explode=True,
)
request_query_date_open = api_client.QueryParameter(
    name="dateOpen",
    style=api_client.ParameterStyle.FORM,
    schema=DateOpenSchema,
    required=True,
    explode=True,
)
request_query_date_close = api_client.QueryParameter(
    name="dateClose",
    style=api_client.ParameterStyle.FORM,
    schema=DateCloseSchema,
    required=True,
    explode=True,
)
request_query_position_uid = api_client.QueryParameter(
    name="positionUID",
    style=api_client.ParameterStyle.FORM,
    schema=PositionUIDSchema,
    required=True,
    explode=True,
)
request_query_projectid = api_client.QueryParameter(
    name="projectid",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectidSchema,
    explode=True,
)
request_query_funnel_id = api_client.QueryParameter(
    name="funnelId",
    style=api_client.ParameterStyle.FORM,
    schema=FunnelIdSchema,
    required=True,
    explode=True,
)
request_query_approval_flow_id = api_client.QueryParameter(
    name="approvalFlowId",
    style=api_client.ParameterStyle.FORM,
    schema=ApprovalFlowIdSchema,
    explode=True,
)
request_query_locationid = api_client.QueryParameter(
    name="locationid",
    style=api_client.ParameterStyle.FORM,
    schema=LocationidSchema,
    explode=True,
)
request_query_department_id = api_client.QueryParameter(
    name="departmentId",
    style=api_client.ParameterStyle.FORM,
    schema=DepartmentIdSchema,
    explode=True,
)
request_query_profileid = api_client.QueryParameter(
    name="profileid",
    style=api_client.ParameterStyle.FORM,
    schema=ProfileidSchema,
    explode=True,
)
request_query_recruiter_id = api_client.QueryParameter(
    name="recruiterId",
    style=api_client.ParameterStyle.FORM,
    schema=RecruiterIdSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PositionsCreatePositionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PositionsCreatePositionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PositionsCreatePositionResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = schemas.StrSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: str


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyText = schemas.DictSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'text': api_client.MediaType(
            schema=SchemaFor404ResponseBodyText),
    },
)
SchemaFor409ResponseBodyApplicationJson = PositionsCreatePosition409ResponseSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: PositionsCreatePosition409Response


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: PositionsCreatePosition409Response


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
    'text',
)


class BaseApi(api_client.Api):

    def _create_position_mapped_args(
        self,
        name: str,
        count: int,
        status: str,
        access_level: str,
        date_open: str,
        date_close: str,
        position_uid: str,
        funnel_id: int,
        description: typing.Optional[str] = None,
        requirements: typing.Optional[str] = None,
        responsibilities: typing.Optional[str] = None,
        projectid: typing.Optional[int] = None,
        approval_flow_id: typing.Optional[int] = None,
        locationid: typing.Optional[int] = None,
        department_id: typing.Optional[str] = None,
        profileid: typing.Optional[int] = None,
        recruiter_id: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if name is not None:
            _query_params["name"] = name
        if description is not None:
            _query_params["description"] = description
        if count is not None:
            _query_params["count"] = count
        if status is not None:
            _query_params["status"] = status
        if access_level is not None:
            _query_params["accessLevel"] = access_level
        if requirements is not None:
            _query_params["requirements"] = requirements
        if responsibilities is not None:
            _query_params["responsibilities"] = responsibilities
        if date_open is not None:
            _query_params["dateOpen"] = date_open
        if date_close is not None:
            _query_params["dateClose"] = date_close
        if position_uid is not None:
            _query_params["positionUID"] = position_uid
        if projectid is not None:
            _query_params["projectid"] = projectid
        if funnel_id is not None:
            _query_params["funnelId"] = funnel_id
        if approval_flow_id is not None:
            _query_params["approvalFlowId"] = approval_flow_id
        if locationid is not None:
            _query_params["locationid"] = locationid
        if department_id is not None:
            _query_params["departmentId"] = department_id
        if profileid is not None:
            _query_params["profileid"] = profileid
        if recruiter_id is not None:
            _query_params["recruiterId"] = recruiter_id
        args.query = _query_params
        return args

    async def _acreate_position_oapg(
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
        Save Position
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_name,
            request_query_description,
            request_query_count,
            request_query_status,
            request_query_access_level,
            request_query_requirements,
            request_query_responsibilities,
            request_query_date_open,
            request_query_date_close,
            request_query_position_uid,
            request_query_projectid,
            request_query_funnel_id,
            request_query_approval_flow_id,
            request_query_locationid,
            request_query_department_id,
            request_query_profileid,
            request_query_recruiter_id,
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
            path_template='/position/save',
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


    def _create_position_oapg(
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
        Save Position
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_name,
            request_query_description,
            request_query_count,
            request_query_status,
            request_query_access_level,
            request_query_requirements,
            request_query_responsibilities,
            request_query_date_open,
            request_query_date_close,
            request_query_position_uid,
            request_query_projectid,
            request_query_funnel_id,
            request_query_approval_flow_id,
            request_query_locationid,
            request_query_department_id,
            request_query_profileid,
            request_query_recruiter_id,
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
            path_template='/position/save',
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


class CreatePositionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_position(
        self,
        name: str,
        count: int,
        status: str,
        access_level: str,
        date_open: str,
        date_close: str,
        position_uid: str,
        funnel_id: int,
        description: typing.Optional[str] = None,
        requirements: typing.Optional[str] = None,
        responsibilities: typing.Optional[str] = None,
        projectid: typing.Optional[int] = None,
        approval_flow_id: typing.Optional[int] = None,
        locationid: typing.Optional[int] = None,
        department_id: typing.Optional[str] = None,
        profileid: typing.Optional[int] = None,
        recruiter_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_position_mapped_args(
            name=name,
            count=count,
            status=status,
            access_level=access_level,
            date_open=date_open,
            date_close=date_close,
            position_uid=position_uid,
            funnel_id=funnel_id,
            description=description,
            requirements=requirements,
            responsibilities=responsibilities,
            projectid=projectid,
            approval_flow_id=approval_flow_id,
            locationid=locationid,
            department_id=department_id,
            profileid=profileid,
            recruiter_id=recruiter_id,
        )
        return await self._acreate_position_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def create_position(
        self,
        name: str,
        count: int,
        status: str,
        access_level: str,
        date_open: str,
        date_close: str,
        position_uid: str,
        funnel_id: int,
        description: typing.Optional[str] = None,
        requirements: typing.Optional[str] = None,
        responsibilities: typing.Optional[str] = None,
        projectid: typing.Optional[int] = None,
        approval_flow_id: typing.Optional[int] = None,
        locationid: typing.Optional[int] = None,
        department_id: typing.Optional[str] = None,
        profileid: typing.Optional[int] = None,
        recruiter_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_position_mapped_args(
            name=name,
            count=count,
            status=status,
            access_level=access_level,
            date_open=date_open,
            date_close=date_close,
            position_uid=position_uid,
            funnel_id=funnel_id,
            description=description,
            requirements=requirements,
            responsibilities=responsibilities,
            projectid=projectid,
            approval_flow_id=approval_flow_id,
            locationid=locationid,
            department_id=department_id,
            profileid=profileid,
            recruiter_id=recruiter_id,
        )
        return self._create_position_oapg(
            query_params=args.query,
        )

class CreatePosition(BaseApi):

    async def acreate_position(
        self,
        name: str,
        count: int,
        status: str,
        access_level: str,
        date_open: str,
        date_close: str,
        position_uid: str,
        funnel_id: int,
        description: typing.Optional[str] = None,
        requirements: typing.Optional[str] = None,
        responsibilities: typing.Optional[str] = None,
        projectid: typing.Optional[int] = None,
        approval_flow_id: typing.Optional[int] = None,
        locationid: typing.Optional[int] = None,
        department_id: typing.Optional[str] = None,
        profileid: typing.Optional[int] = None,
        recruiter_id: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> PositionsCreatePositionResponsePydantic:
        raw_response = await self.raw.acreate_position(
            name=name,
            count=count,
            status=status,
            access_level=access_level,
            date_open=date_open,
            date_close=date_close,
            position_uid=position_uid,
            funnel_id=funnel_id,
            description=description,
            requirements=requirements,
            responsibilities=responsibilities,
            projectid=projectid,
            approval_flow_id=approval_flow_id,
            locationid=locationid,
            department_id=department_id,
            profileid=profileid,
            recruiter_id=recruiter_id,
            **kwargs,
        )
        if validate:
            return PositionsCreatePositionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PositionsCreatePositionResponsePydantic, raw_response.body)
    
    
    def create_position(
        self,
        name: str,
        count: int,
        status: str,
        access_level: str,
        date_open: str,
        date_close: str,
        position_uid: str,
        funnel_id: int,
        description: typing.Optional[str] = None,
        requirements: typing.Optional[str] = None,
        responsibilities: typing.Optional[str] = None,
        projectid: typing.Optional[int] = None,
        approval_flow_id: typing.Optional[int] = None,
        locationid: typing.Optional[int] = None,
        department_id: typing.Optional[str] = None,
        profileid: typing.Optional[int] = None,
        recruiter_id: typing.Optional[int] = None,
        validate: bool = False,
    ) -> PositionsCreatePositionResponsePydantic:
        raw_response = self.raw.create_position(
            name=name,
            count=count,
            status=status,
            access_level=access_level,
            date_open=date_open,
            date_close=date_close,
            position_uid=position_uid,
            funnel_id=funnel_id,
            description=description,
            requirements=requirements,
            responsibilities=responsibilities,
            projectid=projectid,
            approval_flow_id=approval_flow_id,
            locationid=locationid,
            department_id=department_id,
            profileid=profileid,
            recruiter_id=recruiter_id,
        )
        if validate:
            return PositionsCreatePositionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PositionsCreatePositionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        count: int,
        status: str,
        access_level: str,
        date_open: str,
        date_close: str,
        position_uid: str,
        funnel_id: int,
        description: typing.Optional[str] = None,
        requirements: typing.Optional[str] = None,
        responsibilities: typing.Optional[str] = None,
        projectid: typing.Optional[int] = None,
        approval_flow_id: typing.Optional[int] = None,
        locationid: typing.Optional[int] = None,
        department_id: typing.Optional[str] = None,
        profileid: typing.Optional[int] = None,
        recruiter_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_position_mapped_args(
            name=name,
            count=count,
            status=status,
            access_level=access_level,
            date_open=date_open,
            date_close=date_close,
            position_uid=position_uid,
            funnel_id=funnel_id,
            description=description,
            requirements=requirements,
            responsibilities=responsibilities,
            projectid=projectid,
            approval_flow_id=approval_flow_id,
            locationid=locationid,
            department_id=department_id,
            profileid=profileid,
            recruiter_id=recruiter_id,
        )
        return await self._acreate_position_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        count: int,
        status: str,
        access_level: str,
        date_open: str,
        date_close: str,
        position_uid: str,
        funnel_id: int,
        description: typing.Optional[str] = None,
        requirements: typing.Optional[str] = None,
        responsibilities: typing.Optional[str] = None,
        projectid: typing.Optional[int] = None,
        approval_flow_id: typing.Optional[int] = None,
        locationid: typing.Optional[int] = None,
        department_id: typing.Optional[str] = None,
        profileid: typing.Optional[int] = None,
        recruiter_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_position_mapped_args(
            name=name,
            count=count,
            status=status,
            access_level=access_level,
            date_open=date_open,
            date_close=date_close,
            position_uid=position_uid,
            funnel_id=funnel_id,
            description=description,
            requirements=requirements,
            responsibilities=responsibilities,
            projectid=projectid,
            approval_flow_id=approval_flow_id,
            locationid=locationid,
            department_id=department_id,
            profileid=profileid,
            recruiter_id=recruiter_id,
        )
        return self._create_position_oapg(
            query_params=args.query,
        )

