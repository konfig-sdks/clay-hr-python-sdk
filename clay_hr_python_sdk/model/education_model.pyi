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


class EducationModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            cid = schemas.Int32Schema
            city = schemas.StrSchema
            countryId = schemas.Int32Schema
            course = schemas.StrSchema
        
            @staticmethod
            def createts() -> typing.Type['Timestamp']:
                return Timestamp
            degree = schemas.StrSchema
            degreeId = schemas.Int32Schema
            degreeType = schemas.StrSchema
            educationId = schemas.Int32Schema
            endDate = schemas.DateSchema
            expirationDate = schemas.DateSchema
            gpa = schemas.StrSchema
            graduation = schemas.Int32Schema
            institution = schemas.StrSchema
            institutionId = schemas.Int32Schema
            isHighest = schemas.Int32Schema
            profileid = schemas.Int32Schema
            recruitid = schemas.Int32Schema
            startDate = schemas.DateSchema
            state = schemas.StrSchema
            userId = schemas.Int32Schema
            __annotations__ = {
                "cid": cid,
                "city": city,
                "countryId": countryId,
                "course": course,
                "createts": createts,
                "degree": degree,
                "degreeId": degreeId,
                "degreeType": degreeType,
                "educationId": educationId,
                "endDate": endDate,
                "expirationDate": expirationDate,
                "gpa": gpa,
                "graduation": graduation,
                "institution": institution,
                "institutionId": institutionId,
                "isHighest": isHighest,
                "profileid": profileid,
                "recruitid": recruitid,
                "startDate": startDate,
                "state": state,
                "userId": userId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryId"]) -> MetaOapg.properties.countryId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["course"]) -> MetaOapg.properties.course: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createts"]) -> 'Timestamp': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["degree"]) -> MetaOapg.properties.degree: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["degreeId"]) -> MetaOapg.properties.degreeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["degreeType"]) -> MetaOapg.properties.degreeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["educationId"]) -> MetaOapg.properties.educationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationDate"]) -> MetaOapg.properties.expirationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gpa"]) -> MetaOapg.properties.gpa: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["graduation"]) -> MetaOapg.properties.graduation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institution"]) -> MetaOapg.properties.institution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionId"]) -> MetaOapg.properties.institutionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isHighest"]) -> MetaOapg.properties.isHighest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileid"]) -> MetaOapg.properties.profileid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recruitid"]) -> MetaOapg.properties.recruitid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cid", "city", "countryId", "course", "createts", "degree", "degreeId", "degreeType", "educationId", "endDate", "expirationDate", "gpa", "graduation", "institution", "institutionId", "isHighest", "profileid", "recruitid", "startDate", "state", "userId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryId"]) -> typing.Union[MetaOapg.properties.countryId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["course"]) -> typing.Union[MetaOapg.properties.course, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createts"]) -> typing.Union['Timestamp', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["degree"]) -> typing.Union[MetaOapg.properties.degree, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["degreeId"]) -> typing.Union[MetaOapg.properties.degreeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["degreeType"]) -> typing.Union[MetaOapg.properties.degreeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["educationId"]) -> typing.Union[MetaOapg.properties.educationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationDate"]) -> typing.Union[MetaOapg.properties.expirationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gpa"]) -> typing.Union[MetaOapg.properties.gpa, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["graduation"]) -> typing.Union[MetaOapg.properties.graduation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institution"]) -> typing.Union[MetaOapg.properties.institution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionId"]) -> typing.Union[MetaOapg.properties.institutionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isHighest"]) -> typing.Union[MetaOapg.properties.isHighest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileid"]) -> typing.Union[MetaOapg.properties.profileid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recruitid"]) -> typing.Union[MetaOapg.properties.recruitid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cid", "city", "countryId", "course", "createts", "degree", "degreeId", "degreeType", "educationId", "endDate", "expirationDate", "gpa", "graduation", "institution", "institutionId", "isHighest", "profileid", "recruitid", "startDate", "state", "userId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        countryId: typing.Union[MetaOapg.properties.countryId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        course: typing.Union[MetaOapg.properties.course, str, schemas.Unset] = schemas.unset,
        createts: typing.Union['Timestamp', schemas.Unset] = schemas.unset,
        degree: typing.Union[MetaOapg.properties.degree, str, schemas.Unset] = schemas.unset,
        degreeId: typing.Union[MetaOapg.properties.degreeId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        degreeType: typing.Union[MetaOapg.properties.degreeType, str, schemas.Unset] = schemas.unset,
        educationId: typing.Union[MetaOapg.properties.educationId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, schemas.Unset] = schemas.unset,
        expirationDate: typing.Union[MetaOapg.properties.expirationDate, str, date, schemas.Unset] = schemas.unset,
        gpa: typing.Union[MetaOapg.properties.gpa, str, schemas.Unset] = schemas.unset,
        graduation: typing.Union[MetaOapg.properties.graduation, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        institution: typing.Union[MetaOapg.properties.institution, str, schemas.Unset] = schemas.unset,
        institutionId: typing.Union[MetaOapg.properties.institutionId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isHighest: typing.Union[MetaOapg.properties.isHighest, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        profileid: typing.Union[MetaOapg.properties.profileid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        recruitid: typing.Union[MetaOapg.properties.recruitid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EducationModel':
        return super().__new__(
            cls,
            *args,
            cid=cid,
            city=city,
            countryId=countryId,
            course=course,
            createts=createts,
            degree=degree,
            degreeId=degreeId,
            degreeType=degreeType,
            educationId=educationId,
            endDate=endDate,
            expirationDate=expirationDate,
            gpa=gpa,
            graduation=graduation,
            institution=institution,
            institutionId=institutionId,
            isHighest=isHighest,
            profileid=profileid,
            recruitid=recruitid,
            startDate=startDate,
            state=state,
            userId=userId,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.timestamp import Timestamp
