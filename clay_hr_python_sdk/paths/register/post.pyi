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
AccessoriesSchema = schemas.StrSchema
AcknowledgeSchema = schemas.Int32Schema
AssetIDSchema = schemas.Int32Schema
AssetnoSchema = schemas.StrSchema
AssetstatusSchema = schemas.StrSchema
AssettypeSchema = schemas.StrSchema
PurchaseDateSchema = schemas.DateSchema
SelfAssignSchema = schemas.Int32Schema
SerialnoSchema = schemas.StrSchema
ServiceSchema = schemas.StrSchema
SourceSchema = schemas.StrSchema
SpecsSchema = schemas.StrSchema
SupplierSchema = schemas.StrSchema
UseStatusCodeSchema = schemas.StrSchema
UserDomainSchema = schemas.StrSchema
UserMailSchema = schemas.StrSchema
UserPasswordSchema = schemas.StrSchema
UuidSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'accessories': typing.Union[AccessoriesSchema, str, ],
        'acknowledge': typing.Union[AcknowledgeSchema, decimal.Decimal, int, ],
        'assetID': typing.Union[AssetIDSchema, decimal.Decimal, int, ],
        'assetno': typing.Union[AssetnoSchema, str, ],
        'assetstatus': typing.Union[AssetstatusSchema, str, ],
        'assettype': typing.Union[AssettypeSchema, str, ],
        'purchaseDate': typing.Union[PurchaseDateSchema, str, date, ],
        'selfAssign': typing.Union[SelfAssignSchema, decimal.Decimal, int, ],
        'serialno': typing.Union[SerialnoSchema, str, ],
        'service': typing.Union[ServiceSchema, str, ],
        'source': typing.Union[SourceSchema, str, ],
        'specs': typing.Union[SpecsSchema, str, ],
        'supplier': typing.Union[SupplierSchema, str, ],
        'useStatusCode': typing.Union[UseStatusCodeSchema, str, ],
        'userDomain': typing.Union[UserDomainSchema, str, ],
        'userMail': typing.Union[UserMailSchema, str, ],
        'userPassword': typing.Union[UserPasswordSchema, str, ],
        'uuid': typing.Union[UuidSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_accessories = api_client.QueryParameter(
    name="accessories",
    style=api_client.ParameterStyle.FORM,
    schema=AccessoriesSchema,
    explode=True,
)
request_query_acknowledge = api_client.QueryParameter(
    name="acknowledge",
    style=api_client.ParameterStyle.FORM,
    schema=AcknowledgeSchema,
    explode=True,
)
request_query_asset_id = api_client.QueryParameter(
    name="assetID",
    style=api_client.ParameterStyle.FORM,
    schema=AssetIDSchema,
    explode=True,
)
request_query_assetno = api_client.QueryParameter(
    name="assetno",
    style=api_client.ParameterStyle.FORM,
    schema=AssetnoSchema,
    explode=True,
)
request_query_assetstatus = api_client.QueryParameter(
    name="assetstatus",
    style=api_client.ParameterStyle.FORM,
    schema=AssetstatusSchema,
    explode=True,
)
request_query_assettype = api_client.QueryParameter(
    name="assettype",
    style=api_client.ParameterStyle.FORM,
    schema=AssettypeSchema,
    explode=True,
)
request_query_purchase_date = api_client.QueryParameter(
    name="purchaseDate",
    style=api_client.ParameterStyle.FORM,
    schema=PurchaseDateSchema,
    explode=True,
)
request_query_self_assign = api_client.QueryParameter(
    name="selfAssign",
    style=api_client.ParameterStyle.FORM,
    schema=SelfAssignSchema,
    explode=True,
)
request_query_serialno = api_client.QueryParameter(
    name="serialno",
    style=api_client.ParameterStyle.FORM,
    schema=SerialnoSchema,
    explode=True,
)
request_query_service = api_client.QueryParameter(
    name="service",
    style=api_client.ParameterStyle.FORM,
    schema=ServiceSchema,
    explode=True,
)
request_query_source = api_client.QueryParameter(
    name="source",
    style=api_client.ParameterStyle.FORM,
    schema=SourceSchema,
    explode=True,
)
request_query_specs = api_client.QueryParameter(
    name="specs",
    style=api_client.ParameterStyle.FORM,
    schema=SpecsSchema,
    explode=True,
)
request_query_supplier = api_client.QueryParameter(
    name="supplier",
    style=api_client.ParameterStyle.FORM,
    schema=SupplierSchema,
    explode=True,
)
request_query_use_status_code = api_client.QueryParameter(
    name="useStatusCode",
    style=api_client.ParameterStyle.FORM,
    schema=UseStatusCodeSchema,
    explode=True,
)
request_query_user_domain = api_client.QueryParameter(
    name="userDomain",
    style=api_client.ParameterStyle.FORM,
    schema=UserDomainSchema,
    explode=True,
)
request_query_user_mail = api_client.QueryParameter(
    name="userMail",
    style=api_client.ParameterStyle.FORM,
    schema=UserMailSchema,
    explode=True,
)
request_query_user_password = api_client.QueryParameter(
    name="userPassword",
    style=api_client.ParameterStyle.FORM,
    schema=UserPasswordSchema,
    explode=True,
)
request_query_uuid = api_client.QueryParameter(
    name="uuid",
    style=api_client.ParameterStyle.FORM,
    schema=UuidSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
    'application/json',
)


class BaseApi(api_client.Api):

    def _register_device_for_clock_in_with_asset_model_mapped_args(
        self,
        accessories: typing.Optional[str] = None,
        acknowledge: typing.Optional[int] = None,
        asset_id: typing.Optional[int] = None,
        assetno: typing.Optional[str] = None,
        assetstatus: typing.Optional[str] = None,
        assettype: typing.Optional[str] = None,
        purchase_date: typing.Optional[date] = None,
        self_assign: typing.Optional[int] = None,
        serialno: typing.Optional[str] = None,
        service: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        specs: typing.Optional[str] = None,
        supplier: typing.Optional[str] = None,
        use_status_code: typing.Optional[str] = None,
        user_domain: typing.Optional[str] = None,
        user_mail: typing.Optional[str] = None,
        user_password: typing.Optional[str] = None,
        uuid: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if accessories is not None:
            _query_params["accessories"] = accessories
        if acknowledge is not None:
            _query_params["acknowledge"] = acknowledge
        if asset_id is not None:
            _query_params["assetID"] = asset_id
        if assetno is not None:
            _query_params["assetno"] = assetno
        if assetstatus is not None:
            _query_params["assetstatus"] = assetstatus
        if assettype is not None:
            _query_params["assettype"] = assettype
        if purchase_date is not None:
            _query_params["purchaseDate"] = purchase_date
        if self_assign is not None:
            _query_params["selfAssign"] = self_assign
        if serialno is not None:
            _query_params["serialno"] = serialno
        if service is not None:
            _query_params["service"] = service
        if source is not None:
            _query_params["source"] = source
        if specs is not None:
            _query_params["specs"] = specs
        if supplier is not None:
            _query_params["supplier"] = supplier
        if use_status_code is not None:
            _query_params["useStatusCode"] = use_status_code
        if user_domain is not None:
            _query_params["userDomain"] = user_domain
        if user_mail is not None:
            _query_params["userMail"] = user_mail
        if user_password is not None:
            _query_params["userPassword"] = user_password
        if uuid is not None:
            _query_params["uuid"] = uuid
        args.query = _query_params
        return args

    async def _aregister_device_for_clock_in_with_asset_model_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Register device for ClockIn with AssetModel.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_accessories,
            request_query_acknowledge,
            request_query_asset_id,
            request_query_assetno,
            request_query_assetstatus,
            request_query_assettype,
            request_query_purchase_date,
            request_query_self_assign,
            request_query_serialno,
            request_query_service,
            request_query_source,
            request_query_specs,
            request_query_supplier,
            request_query_use_status_code,
            request_query_user_domain,
            request_query_user_mail,
            request_query_user_password,
            request_query_uuid,
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
            path_template='/register',
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


    def _register_device_for_clock_in_with_asset_model_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Register device for ClockIn with AssetModel.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_accessories,
            request_query_acknowledge,
            request_query_asset_id,
            request_query_assetno,
            request_query_assetstatus,
            request_query_assettype,
            request_query_purchase_date,
            request_query_self_assign,
            request_query_serialno,
            request_query_service,
            request_query_source,
            request_query_specs,
            request_query_supplier,
            request_query_use_status_code,
            request_query_user_domain,
            request_query_user_mail,
            request_query_user_password,
            request_query_uuid,
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
            path_template='/register',
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


class RegisterDeviceForClockInWithAssetModelRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aregister_device_for_clock_in_with_asset_model(
        self,
        accessories: typing.Optional[str] = None,
        acknowledge: typing.Optional[int] = None,
        asset_id: typing.Optional[int] = None,
        assetno: typing.Optional[str] = None,
        assetstatus: typing.Optional[str] = None,
        assettype: typing.Optional[str] = None,
        purchase_date: typing.Optional[date] = None,
        self_assign: typing.Optional[int] = None,
        serialno: typing.Optional[str] = None,
        service: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        specs: typing.Optional[str] = None,
        supplier: typing.Optional[str] = None,
        use_status_code: typing.Optional[str] = None,
        user_domain: typing.Optional[str] = None,
        user_mail: typing.Optional[str] = None,
        user_password: typing.Optional[str] = None,
        uuid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._register_device_for_clock_in_with_asset_model_mapped_args(
            accessories=accessories,
            acknowledge=acknowledge,
            asset_id=asset_id,
            assetno=assetno,
            assetstatus=assetstatus,
            assettype=assettype,
            purchase_date=purchase_date,
            self_assign=self_assign,
            serialno=serialno,
            service=service,
            source=source,
            specs=specs,
            supplier=supplier,
            use_status_code=use_status_code,
            user_domain=user_domain,
            user_mail=user_mail,
            user_password=user_password,
            uuid=uuid,
        )
        return await self._aregister_device_for_clock_in_with_asset_model_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def register_device_for_clock_in_with_asset_model(
        self,
        accessories: typing.Optional[str] = None,
        acknowledge: typing.Optional[int] = None,
        asset_id: typing.Optional[int] = None,
        assetno: typing.Optional[str] = None,
        assetstatus: typing.Optional[str] = None,
        assettype: typing.Optional[str] = None,
        purchase_date: typing.Optional[date] = None,
        self_assign: typing.Optional[int] = None,
        serialno: typing.Optional[str] = None,
        service: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        specs: typing.Optional[str] = None,
        supplier: typing.Optional[str] = None,
        use_status_code: typing.Optional[str] = None,
        user_domain: typing.Optional[str] = None,
        user_mail: typing.Optional[str] = None,
        user_password: typing.Optional[str] = None,
        uuid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._register_device_for_clock_in_with_asset_model_mapped_args(
            accessories=accessories,
            acknowledge=acknowledge,
            asset_id=asset_id,
            assetno=assetno,
            assetstatus=assetstatus,
            assettype=assettype,
            purchase_date=purchase_date,
            self_assign=self_assign,
            serialno=serialno,
            service=service,
            source=source,
            specs=specs,
            supplier=supplier,
            use_status_code=use_status_code,
            user_domain=user_domain,
            user_mail=user_mail,
            user_password=user_password,
            uuid=uuid,
        )
        return self._register_device_for_clock_in_with_asset_model_oapg(
            query_params=args.query,
        )

class RegisterDeviceForClockInWithAssetModel(BaseApi):

    async def aregister_device_for_clock_in_with_asset_model(
        self,
        accessories: typing.Optional[str] = None,
        acknowledge: typing.Optional[int] = None,
        asset_id: typing.Optional[int] = None,
        assetno: typing.Optional[str] = None,
        assetstatus: typing.Optional[str] = None,
        assettype: typing.Optional[str] = None,
        purchase_date: typing.Optional[date] = None,
        self_assign: typing.Optional[int] = None,
        serialno: typing.Optional[str] = None,
        service: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        specs: typing.Optional[str] = None,
        supplier: typing.Optional[str] = None,
        use_status_code: typing.Optional[str] = None,
        user_domain: typing.Optional[str] = None,
        user_mail: typing.Optional[str] = None,
        user_password: typing.Optional[str] = None,
        uuid: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.aregister_device_for_clock_in_with_asset_model(
            accessories=accessories,
            acknowledge=acknowledge,
            asset_id=asset_id,
            assetno=assetno,
            assetstatus=assetstatus,
            assettype=assettype,
            purchase_date=purchase_date,
            self_assign=self_assign,
            serialno=serialno,
            service=service,
            source=source,
            specs=specs,
            supplier=supplier,
            use_status_code=use_status_code,
            user_domain=user_domain,
            user_mail=user_mail,
            user_password=user_password,
            uuid=uuid,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def register_device_for_clock_in_with_asset_model(
        self,
        accessories: typing.Optional[str] = None,
        acknowledge: typing.Optional[int] = None,
        asset_id: typing.Optional[int] = None,
        assetno: typing.Optional[str] = None,
        assetstatus: typing.Optional[str] = None,
        assettype: typing.Optional[str] = None,
        purchase_date: typing.Optional[date] = None,
        self_assign: typing.Optional[int] = None,
        serialno: typing.Optional[str] = None,
        service: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        specs: typing.Optional[str] = None,
        supplier: typing.Optional[str] = None,
        use_status_code: typing.Optional[str] = None,
        user_domain: typing.Optional[str] = None,
        user_mail: typing.Optional[str] = None,
        user_password: typing.Optional[str] = None,
        uuid: typing.Optional[str] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.register_device_for_clock_in_with_asset_model(
            accessories=accessories,
            acknowledge=acknowledge,
            asset_id=asset_id,
            assetno=assetno,
            assetstatus=assetstatus,
            assettype=assettype,
            purchase_date=purchase_date,
            self_assign=self_assign,
            serialno=serialno,
            service=service,
            source=source,
            specs=specs,
            supplier=supplier,
            use_status_code=use_status_code,
            user_domain=user_domain,
            user_mail=user_mail,
            user_password=user_password,
            uuid=uuid,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        accessories: typing.Optional[str] = None,
        acknowledge: typing.Optional[int] = None,
        asset_id: typing.Optional[int] = None,
        assetno: typing.Optional[str] = None,
        assetstatus: typing.Optional[str] = None,
        assettype: typing.Optional[str] = None,
        purchase_date: typing.Optional[date] = None,
        self_assign: typing.Optional[int] = None,
        serialno: typing.Optional[str] = None,
        service: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        specs: typing.Optional[str] = None,
        supplier: typing.Optional[str] = None,
        use_status_code: typing.Optional[str] = None,
        user_domain: typing.Optional[str] = None,
        user_mail: typing.Optional[str] = None,
        user_password: typing.Optional[str] = None,
        uuid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._register_device_for_clock_in_with_asset_model_mapped_args(
            accessories=accessories,
            acknowledge=acknowledge,
            asset_id=asset_id,
            assetno=assetno,
            assetstatus=assetstatus,
            assettype=assettype,
            purchase_date=purchase_date,
            self_assign=self_assign,
            serialno=serialno,
            service=service,
            source=source,
            specs=specs,
            supplier=supplier,
            use_status_code=use_status_code,
            user_domain=user_domain,
            user_mail=user_mail,
            user_password=user_password,
            uuid=uuid,
        )
        return await self._aregister_device_for_clock_in_with_asset_model_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        accessories: typing.Optional[str] = None,
        acknowledge: typing.Optional[int] = None,
        asset_id: typing.Optional[int] = None,
        assetno: typing.Optional[str] = None,
        assetstatus: typing.Optional[str] = None,
        assettype: typing.Optional[str] = None,
        purchase_date: typing.Optional[date] = None,
        self_assign: typing.Optional[int] = None,
        serialno: typing.Optional[str] = None,
        service: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        specs: typing.Optional[str] = None,
        supplier: typing.Optional[str] = None,
        use_status_code: typing.Optional[str] = None,
        user_domain: typing.Optional[str] = None,
        user_mail: typing.Optional[str] = None,
        user_password: typing.Optional[str] = None,
        uuid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._register_device_for_clock_in_with_asset_model_mapped_args(
            accessories=accessories,
            acknowledge=acknowledge,
            asset_id=asset_id,
            assetno=assetno,
            assetstatus=assetstatus,
            assettype=assettype,
            purchase_date=purchase_date,
            self_assign=self_assign,
            serialno=serialno,
            service=service,
            source=source,
            specs=specs,
            supplier=supplier,
            use_status_code=use_status_code,
            user_domain=user_domain,
            user_mail=user_mail,
            user_password=user_password,
            uuid=uuid,
        )
        return self._register_device_for_clock_in_with_asset_model_oapg(
            query_params=args.query,
        )

