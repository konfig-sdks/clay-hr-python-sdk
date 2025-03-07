# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

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


class BankAccountModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            accountCode = schemas.StrSchema
            accountNumber = schemas.StrSchema
            accountType = schemas.StrSchema
            bankAccountId = schemas.Int32Schema
            bankCountryId = schemas.Int32Schema
            branchCode = schemas.StrSchema
            branchName = schemas.StrSchema
            cid = schemas.Int32Schema
            countryId = schemas.Int32Schema
            createUserId = schemas.Int32Schema
            name = schemas.StrSchema
            ownerType = schemas.StrSchema
            paymentEmail = schemas.StrSchema
            routingNumber = schemas.StrSchema
            status = schemas.StrSchema
            swiftCode = schemas.StrSchema
            userId = schemas.Int32Schema
            __annotations__ = {
                "accountCode": accountCode,
                "accountNumber": accountNumber,
                "accountType": accountType,
                "bankAccountId": bankAccountId,
                "bankCountryId": bankCountryId,
                "branchCode": branchCode,
                "branchName": branchName,
                "cid": cid,
                "countryId": countryId,
                "createUserId": createUserId,
                "name": name,
                "ownerType": ownerType,
                "paymentEmail": paymentEmail,
                "routingNumber": routingNumber,
                "status": status,
                "swiftCode": swiftCode,
                "userId": userId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountCode"]) -> MetaOapg.properties.accountCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountNumber"]) -> MetaOapg.properties.accountNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountType"]) -> MetaOapg.properties.accountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bankAccountId"]) -> MetaOapg.properties.bankAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bankCountryId"]) -> MetaOapg.properties.bankCountryId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branchCode"]) -> MetaOapg.properties.branchCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branchName"]) -> MetaOapg.properties.branchName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryId"]) -> MetaOapg.properties.countryId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createUserId"]) -> MetaOapg.properties.createUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerType"]) -> MetaOapg.properties.ownerType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentEmail"]) -> MetaOapg.properties.paymentEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routingNumber"]) -> MetaOapg.properties.routingNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["swiftCode"]) -> MetaOapg.properties.swiftCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountCode", "accountNumber", "accountType", "bankAccountId", "bankCountryId", "branchCode", "branchName", "cid", "countryId", "createUserId", "name", "ownerType", "paymentEmail", "routingNumber", "status", "swiftCode", "userId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountCode"]) -> typing.Union[MetaOapg.properties.accountCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountNumber"]) -> typing.Union[MetaOapg.properties.accountNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountType"]) -> typing.Union[MetaOapg.properties.accountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bankAccountId"]) -> typing.Union[MetaOapg.properties.bankAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bankCountryId"]) -> typing.Union[MetaOapg.properties.bankCountryId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branchCode"]) -> typing.Union[MetaOapg.properties.branchCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branchName"]) -> typing.Union[MetaOapg.properties.branchName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryId"]) -> typing.Union[MetaOapg.properties.countryId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createUserId"]) -> typing.Union[MetaOapg.properties.createUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerType"]) -> typing.Union[MetaOapg.properties.ownerType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentEmail"]) -> typing.Union[MetaOapg.properties.paymentEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routingNumber"]) -> typing.Union[MetaOapg.properties.routingNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["swiftCode"]) -> typing.Union[MetaOapg.properties.swiftCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountCode", "accountNumber", "accountType", "bankAccountId", "bankCountryId", "branchCode", "branchName", "cid", "countryId", "createUserId", "name", "ownerType", "paymentEmail", "routingNumber", "status", "swiftCode", "userId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accountCode: typing.Union[MetaOapg.properties.accountCode, str, schemas.Unset] = schemas.unset,
        accountNumber: typing.Union[MetaOapg.properties.accountNumber, str, schemas.Unset] = schemas.unset,
        accountType: typing.Union[MetaOapg.properties.accountType, str, schemas.Unset] = schemas.unset,
        bankAccountId: typing.Union[MetaOapg.properties.bankAccountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        bankCountryId: typing.Union[MetaOapg.properties.bankCountryId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        branchCode: typing.Union[MetaOapg.properties.branchCode, str, schemas.Unset] = schemas.unset,
        branchName: typing.Union[MetaOapg.properties.branchName, str, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        countryId: typing.Union[MetaOapg.properties.countryId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createUserId: typing.Union[MetaOapg.properties.createUserId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        ownerType: typing.Union[MetaOapg.properties.ownerType, str, schemas.Unset] = schemas.unset,
        paymentEmail: typing.Union[MetaOapg.properties.paymentEmail, str, schemas.Unset] = schemas.unset,
        routingNumber: typing.Union[MetaOapg.properties.routingNumber, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        swiftCode: typing.Union[MetaOapg.properties.swiftCode, str, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BankAccountModel':
        return super().__new__(
            cls,
            *args,
            accountCode=accountCode,
            accountNumber=accountNumber,
            accountType=accountType,
            bankAccountId=bankAccountId,
            bankCountryId=bankCountryId,
            branchCode=branchCode,
            branchName=branchName,
            cid=cid,
            countryId=countryId,
            createUserId=createUserId,
            name=name,
            ownerType=ownerType,
            paymentEmail=paymentEmail,
            routingNumber=routingNumber,
            status=status,
            swiftCode=swiftCode,
            userId=userId,
            _configuration=_configuration,
            **kwargs,
        )
