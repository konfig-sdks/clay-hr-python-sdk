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

from clay_hr_python_sdk.model.org_units_create_new_org_unit409_response import OrgUnitsCreateNewOrgUnit409Response as OrgUnitsCreateNewOrgUnit409ResponseSchema
from clay_hr_python_sdk.model.org_units_create_new_org_unit_response import OrgUnitsCreateNewOrgUnitResponse as OrgUnitsCreateNewOrgUnitResponseSchema

from clay_hr_python_sdk.type.org_units_create_new_org_unit_response import OrgUnitsCreateNewOrgUnitResponse
from clay_hr_python_sdk.type.org_units_create_new_org_unit409_response import OrgUnitsCreateNewOrgUnit409Response

from ...api_client import Dictionary
from clay_hr_python_sdk.pydantic.org_units_create_new_org_unit_response import OrgUnitsCreateNewOrgUnitResponse as OrgUnitsCreateNewOrgUnitResponsePydantic
from clay_hr_python_sdk.pydantic.org_units_create_new_org_unit409_response import OrgUnitsCreateNewOrgUnit409Response as OrgUnitsCreateNewOrgUnit409ResponsePydantic

# Query params
NameSchema = schemas.StrSchema
DescriptionSchema = schemas.StrSchema
DeptHeadSchema = schemas.Int32Schema
DeptHeadNameSchema = schemas.StrSchema
DepartmentCodeSchema = schemas.StrSchema
DepartmentIdSchema = schemas.Int32Schema
DepartmentLabelSchema = schemas.StrSchema
NoOfEmployeesSchema = schemas.Int32Schema
ParentDepartmentIdSchema = schemas.Int32Schema
ParentDepartmentNameSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'name': typing.Union[NameSchema, str, ],
        'description': typing.Union[DescriptionSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'deptHead': typing.Union[DeptHeadSchema, decimal.Decimal, int, ],
        'deptHeadName': typing.Union[DeptHeadNameSchema, str, ],
        'departmentCode': typing.Union[DepartmentCodeSchema, str, ],
        'departmentId': typing.Union[DepartmentIdSchema, decimal.Decimal, int, ],
        'departmentLabel': typing.Union[DepartmentLabelSchema, str, ],
        'noOfEmployees': typing.Union[NoOfEmployeesSchema, decimal.Decimal, int, ],
        'parentDepartmentId': typing.Union[ParentDepartmentIdSchema, decimal.Decimal, int, ],
        'parentDepartmentName': typing.Union[ParentDepartmentNameSchema, str, ],
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
    required=True,
    explode=True,
)
request_query_dept_head = api_client.QueryParameter(
    name="deptHead",
    style=api_client.ParameterStyle.FORM,
    schema=DeptHeadSchema,
    explode=True,
)
request_query_dept_head_name = api_client.QueryParameter(
    name="deptHeadName",
    style=api_client.ParameterStyle.FORM,
    schema=DeptHeadNameSchema,
    explode=True,
)
request_query_department_code = api_client.QueryParameter(
    name="departmentCode",
    style=api_client.ParameterStyle.FORM,
    schema=DepartmentCodeSchema,
    explode=True,
)
request_query_department_id = api_client.QueryParameter(
    name="departmentId",
    style=api_client.ParameterStyle.FORM,
    schema=DepartmentIdSchema,
    explode=True,
)
request_query_department_label = api_client.QueryParameter(
    name="departmentLabel",
    style=api_client.ParameterStyle.FORM,
    schema=DepartmentLabelSchema,
    explode=True,
)
request_query_no_of_employees = api_client.QueryParameter(
    name="noOfEmployees",
    style=api_client.ParameterStyle.FORM,
    schema=NoOfEmployeesSchema,
    explode=True,
)
request_query_parent_department_id = api_client.QueryParameter(
    name="parentDepartmentId",
    style=api_client.ParameterStyle.FORM,
    schema=ParentDepartmentIdSchema,
    explode=True,
)
request_query_parent_department_name = api_client.QueryParameter(
    name="parentDepartmentName",
    style=api_client.ParameterStyle.FORM,
    schema=ParentDepartmentNameSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = OrgUnitsCreateNewOrgUnitResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OrgUnitsCreateNewOrgUnitResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OrgUnitsCreateNewOrgUnitResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor409ResponseBodyApplicationJson = OrgUnitsCreateNewOrgUnit409ResponseSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: OrgUnitsCreateNewOrgUnit409Response


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: OrgUnitsCreateNewOrgUnit409Response


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

    def _create_new_org_unit_mapped_args(
        self,
        name: str,
        description: str,
        dept_head: typing.Optional[int] = None,
        dept_head_name: typing.Optional[str] = None,
        department_code: typing.Optional[str] = None,
        department_id: typing.Optional[int] = None,
        department_label: typing.Optional[str] = None,
        no_of_employees: typing.Optional[int] = None,
        parent_department_id: typing.Optional[int] = None,
        parent_department_name: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if name is not None:
            _query_params["name"] = name
        if description is not None:
            _query_params["description"] = description
        if dept_head is not None:
            _query_params["deptHead"] = dept_head
        if dept_head_name is not None:
            _query_params["deptHeadName"] = dept_head_name
        if department_code is not None:
            _query_params["departmentCode"] = department_code
        if department_id is not None:
            _query_params["departmentId"] = department_id
        if department_label is not None:
            _query_params["departmentLabel"] = department_label
        if no_of_employees is not None:
            _query_params["noOfEmployees"] = no_of_employees
        if parent_department_id is not None:
            _query_params["parentDepartmentId"] = parent_department_id
        if parent_department_name is not None:
            _query_params["parentDepartmentName"] = parent_department_name
        args.query = _query_params
        return args

    async def _acreate_new_org_unit_oapg(
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
        Create new org unit
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
            request_query_dept_head,
            request_query_dept_head_name,
            request_query_department_code,
            request_query_department_id,
            request_query_department_label,
            request_query_no_of_employees,
            request_query_parent_department_id,
            request_query_parent_department_name,
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
            path_template='/api/orgunits/add',
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


    def _create_new_org_unit_oapg(
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
        Create new org unit
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
            request_query_dept_head,
            request_query_dept_head_name,
            request_query_department_code,
            request_query_department_id,
            request_query_department_label,
            request_query_no_of_employees,
            request_query_parent_department_id,
            request_query_parent_department_name,
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
            path_template='/api/orgunits/add',
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


class CreateNewOrgUnitRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_org_unit(
        self,
        name: str,
        description: str,
        dept_head: typing.Optional[int] = None,
        dept_head_name: typing.Optional[str] = None,
        department_code: typing.Optional[str] = None,
        department_id: typing.Optional[int] = None,
        department_label: typing.Optional[str] = None,
        no_of_employees: typing.Optional[int] = None,
        parent_department_id: typing.Optional[int] = None,
        parent_department_name: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_org_unit_mapped_args(
            name=name,
            description=description,
            dept_head=dept_head,
            dept_head_name=dept_head_name,
            department_code=department_code,
            department_id=department_id,
            department_label=department_label,
            no_of_employees=no_of_employees,
            parent_department_id=parent_department_id,
            parent_department_name=parent_department_name,
        )
        return await self._acreate_new_org_unit_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def create_new_org_unit(
        self,
        name: str,
        description: str,
        dept_head: typing.Optional[int] = None,
        dept_head_name: typing.Optional[str] = None,
        department_code: typing.Optional[str] = None,
        department_id: typing.Optional[int] = None,
        department_label: typing.Optional[str] = None,
        no_of_employees: typing.Optional[int] = None,
        parent_department_id: typing.Optional[int] = None,
        parent_department_name: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_org_unit_mapped_args(
            name=name,
            description=description,
            dept_head=dept_head,
            dept_head_name=dept_head_name,
            department_code=department_code,
            department_id=department_id,
            department_label=department_label,
            no_of_employees=no_of_employees,
            parent_department_id=parent_department_id,
            parent_department_name=parent_department_name,
        )
        return self._create_new_org_unit_oapg(
            query_params=args.query,
        )

class CreateNewOrgUnit(BaseApi):

    async def acreate_new_org_unit(
        self,
        name: str,
        description: str,
        dept_head: typing.Optional[int] = None,
        dept_head_name: typing.Optional[str] = None,
        department_code: typing.Optional[str] = None,
        department_id: typing.Optional[int] = None,
        department_label: typing.Optional[str] = None,
        no_of_employees: typing.Optional[int] = None,
        parent_department_id: typing.Optional[int] = None,
        parent_department_name: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OrgUnitsCreateNewOrgUnitResponsePydantic:
        raw_response = await self.raw.acreate_new_org_unit(
            name=name,
            description=description,
            dept_head=dept_head,
            dept_head_name=dept_head_name,
            department_code=department_code,
            department_id=department_id,
            department_label=department_label,
            no_of_employees=no_of_employees,
            parent_department_id=parent_department_id,
            parent_department_name=parent_department_name,
            **kwargs,
        )
        if validate:
            return OrgUnitsCreateNewOrgUnitResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OrgUnitsCreateNewOrgUnitResponsePydantic, raw_response.body)
    
    
    def create_new_org_unit(
        self,
        name: str,
        description: str,
        dept_head: typing.Optional[int] = None,
        dept_head_name: typing.Optional[str] = None,
        department_code: typing.Optional[str] = None,
        department_id: typing.Optional[int] = None,
        department_label: typing.Optional[str] = None,
        no_of_employees: typing.Optional[int] = None,
        parent_department_id: typing.Optional[int] = None,
        parent_department_name: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OrgUnitsCreateNewOrgUnitResponsePydantic:
        raw_response = self.raw.create_new_org_unit(
            name=name,
            description=description,
            dept_head=dept_head,
            dept_head_name=dept_head_name,
            department_code=department_code,
            department_id=department_id,
            department_label=department_label,
            no_of_employees=no_of_employees,
            parent_department_id=parent_department_id,
            parent_department_name=parent_department_name,
        )
        if validate:
            return OrgUnitsCreateNewOrgUnitResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OrgUnitsCreateNewOrgUnitResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        description: str,
        dept_head: typing.Optional[int] = None,
        dept_head_name: typing.Optional[str] = None,
        department_code: typing.Optional[str] = None,
        department_id: typing.Optional[int] = None,
        department_label: typing.Optional[str] = None,
        no_of_employees: typing.Optional[int] = None,
        parent_department_id: typing.Optional[int] = None,
        parent_department_name: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_org_unit_mapped_args(
            name=name,
            description=description,
            dept_head=dept_head,
            dept_head_name=dept_head_name,
            department_code=department_code,
            department_id=department_id,
            department_label=department_label,
            no_of_employees=no_of_employees,
            parent_department_id=parent_department_id,
            parent_department_name=parent_department_name,
        )
        return await self._acreate_new_org_unit_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        description: str,
        dept_head: typing.Optional[int] = None,
        dept_head_name: typing.Optional[str] = None,
        department_code: typing.Optional[str] = None,
        department_id: typing.Optional[int] = None,
        department_label: typing.Optional[str] = None,
        no_of_employees: typing.Optional[int] = None,
        parent_department_id: typing.Optional[int] = None,
        parent_department_name: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_org_unit_mapped_args(
            name=name,
            description=description,
            dept_head=dept_head,
            dept_head_name=dept_head_name,
            department_code=department_code,
            department_id=department_id,
            department_label=department_label,
            no_of_employees=no_of_employees,
            parent_department_id=parent_department_id,
            parent_department_name=parent_department_name,
        )
        return self._create_new_org_unit_oapg(
            query_params=args.query,
        )

