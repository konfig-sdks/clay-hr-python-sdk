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


class AwardModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            appraisalId = schemas.Int32Schema
            attribution = schemas.StrSchema
            awardDate = schemas.DateSchema
            awardId = schemas.Int64Schema
        
            @staticmethod
            def awardTypeModel() -> typing.Type['AwardTypeModel']:
                return AwardTypeModel
            cid = schemas.Int32Schema
        
            @staticmethod
            def createts() -> typing.Type['Timestamp']:
                return Timestamp
        
            @staticmethod
            def currencyModel() -> typing.Type['CurrencyModel']:
                return CurrencyModel
            feedbackId = schemas.Int32Schema
            finAccountCode = schemas.StrSchema
            finAmount = schemas.Float64Schema
            finCurrencyCode = schemas.StrSchema
            finPaymentDate = schemas.DateSchema
            finPaymentStatus = schemas.StrSchema
            nonMonetaryCompensation = schemas.StrSchema
            notes = schemas.StrSchema
        
            @staticmethod
            def userViewModel() -> typing.Type['UserViewModel']:
                return UserViewModel
            __annotations__ = {
                "appraisalId": appraisalId,
                "attribution": attribution,
                "awardDate": awardDate,
                "awardId": awardId,
                "awardTypeModel": awardTypeModel,
                "cid": cid,
                "createts": createts,
                "currencyModel": currencyModel,
                "feedbackId": feedbackId,
                "finAccountCode": finAccountCode,
                "finAmount": finAmount,
                "finCurrencyCode": finCurrencyCode,
                "finPaymentDate": finPaymentDate,
                "finPaymentStatus": finPaymentStatus,
                "nonMonetaryCompensation": nonMonetaryCompensation,
                "notes": notes,
                "userViewModel": userViewModel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appraisalId"]) -> MetaOapg.properties.appraisalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attribution"]) -> MetaOapg.properties.attribution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["awardDate"]) -> MetaOapg.properties.awardDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["awardId"]) -> MetaOapg.properties.awardId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["awardTypeModel"]) -> 'AwardTypeModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createts"]) -> 'Timestamp': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyModel"]) -> 'CurrencyModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feedbackId"]) -> MetaOapg.properties.feedbackId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finAccountCode"]) -> MetaOapg.properties.finAccountCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finAmount"]) -> MetaOapg.properties.finAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finCurrencyCode"]) -> MetaOapg.properties.finCurrencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finPaymentDate"]) -> MetaOapg.properties.finPaymentDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finPaymentStatus"]) -> MetaOapg.properties.finPaymentStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonMonetaryCompensation"]) -> MetaOapg.properties.nonMonetaryCompensation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userViewModel"]) -> 'UserViewModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["appraisalId", "attribution", "awardDate", "awardId", "awardTypeModel", "cid", "createts", "currencyModel", "feedbackId", "finAccountCode", "finAmount", "finCurrencyCode", "finPaymentDate", "finPaymentStatus", "nonMonetaryCompensation", "notes", "userViewModel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appraisalId"]) -> typing.Union[MetaOapg.properties.appraisalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attribution"]) -> typing.Union[MetaOapg.properties.attribution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["awardDate"]) -> typing.Union[MetaOapg.properties.awardDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["awardId"]) -> typing.Union[MetaOapg.properties.awardId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["awardTypeModel"]) -> typing.Union['AwardTypeModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createts"]) -> typing.Union['Timestamp', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyModel"]) -> typing.Union['CurrencyModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feedbackId"]) -> typing.Union[MetaOapg.properties.feedbackId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finAccountCode"]) -> typing.Union[MetaOapg.properties.finAccountCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finAmount"]) -> typing.Union[MetaOapg.properties.finAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finCurrencyCode"]) -> typing.Union[MetaOapg.properties.finCurrencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finPaymentDate"]) -> typing.Union[MetaOapg.properties.finPaymentDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finPaymentStatus"]) -> typing.Union[MetaOapg.properties.finPaymentStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonMonetaryCompensation"]) -> typing.Union[MetaOapg.properties.nonMonetaryCompensation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userViewModel"]) -> typing.Union['UserViewModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["appraisalId", "attribution", "awardDate", "awardId", "awardTypeModel", "cid", "createts", "currencyModel", "feedbackId", "finAccountCode", "finAmount", "finCurrencyCode", "finPaymentDate", "finPaymentStatus", "nonMonetaryCompensation", "notes", "userViewModel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        appraisalId: typing.Union[MetaOapg.properties.appraisalId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        attribution: typing.Union[MetaOapg.properties.attribution, str, schemas.Unset] = schemas.unset,
        awardDate: typing.Union[MetaOapg.properties.awardDate, str, date, schemas.Unset] = schemas.unset,
        awardId: typing.Union[MetaOapg.properties.awardId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        awardTypeModel: typing.Union['AwardTypeModel', schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createts: typing.Union['Timestamp', schemas.Unset] = schemas.unset,
        currencyModel: typing.Union['CurrencyModel', schemas.Unset] = schemas.unset,
        feedbackId: typing.Union[MetaOapg.properties.feedbackId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        finAccountCode: typing.Union[MetaOapg.properties.finAccountCode, str, schemas.Unset] = schemas.unset,
        finAmount: typing.Union[MetaOapg.properties.finAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        finCurrencyCode: typing.Union[MetaOapg.properties.finCurrencyCode, str, schemas.Unset] = schemas.unset,
        finPaymentDate: typing.Union[MetaOapg.properties.finPaymentDate, str, date, schemas.Unset] = schemas.unset,
        finPaymentStatus: typing.Union[MetaOapg.properties.finPaymentStatus, str, schemas.Unset] = schemas.unset,
        nonMonetaryCompensation: typing.Union[MetaOapg.properties.nonMonetaryCompensation, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        userViewModel: typing.Union['UserViewModel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AwardModel':
        return super().__new__(
            cls,
            *args,
            appraisalId=appraisalId,
            attribution=attribution,
            awardDate=awardDate,
            awardId=awardId,
            awardTypeModel=awardTypeModel,
            cid=cid,
            createts=createts,
            currencyModel=currencyModel,
            feedbackId=feedbackId,
            finAccountCode=finAccountCode,
            finAmount=finAmount,
            finCurrencyCode=finCurrencyCode,
            finPaymentDate=finPaymentDate,
            finPaymentStatus=finPaymentStatus,
            nonMonetaryCompensation=nonMonetaryCompensation,
            notes=notes,
            userViewModel=userViewModel,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.award_type_model import AwardTypeModel
from clay_hr_python_sdk.model.currency_model import CurrencyModel
from clay_hr_python_sdk.model.timestamp import Timestamp
from clay_hr_python_sdk.model.user_view_model import UserViewModel
