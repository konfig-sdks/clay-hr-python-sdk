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


class JobProfilesGetJobProfilesResponseItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            cid = schemas.StrSchema
            profileId = schemas.StrSchema
            profileName = schemas.StrSchema
            profileDescription = schemas.StrSchema
            orgId = schemas.StrSchema
            profileResponsibilities = schemas.StrSchema
            profileRequirements = schemas.StrSchema
            salaryBandMin = schemas.StrSchema
            salaryBandMax = schemas.StrSchema
            salaryBandCurrency = schemas.StrSchema
            managerProfileId = schemas.StrSchema
            managerProfileName = schemas.StrSchema
            customFieldValueModelList = schemas.StrSchema
            numberofUsers = schemas.StrSchema
            createuserid = schemas.StrSchema
            status = schemas.StrSchema
            careerPathwayModelList = schemas.StrSchema
            objectType = schemas.StrSchema
            objectName = schemas.StrSchema
            objectid = schemas.StrSchema
            __annotations__ = {
                "cid": cid,
                "profileId": profileId,
                "profileName": profileName,
                "profileDescription": profileDescription,
                "orgId": orgId,
                "profileResponsibilities": profileResponsibilities,
                "profileRequirements": profileRequirements,
                "salaryBandMin": salaryBandMin,
                "salaryBandMax": salaryBandMax,
                "salaryBandCurrency": salaryBandCurrency,
                "managerProfileId": managerProfileId,
                "managerProfileName": managerProfileName,
                "customFieldValueModelList": customFieldValueModelList,
                "numberofUsers": numberofUsers,
                "createuserid": createuserid,
                "status": status,
                "careerPathwayModelList": careerPathwayModelList,
                "objectType": objectType,
                "objectName": objectName,
                "objectid": objectid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileId"]) -> MetaOapg.properties.profileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileName"]) -> MetaOapg.properties.profileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileDescription"]) -> MetaOapg.properties.profileDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileResponsibilities"]) -> MetaOapg.properties.profileResponsibilities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileRequirements"]) -> MetaOapg.properties.profileRequirements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salaryBandMin"]) -> MetaOapg.properties.salaryBandMin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salaryBandMax"]) -> MetaOapg.properties.salaryBandMax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salaryBandCurrency"]) -> MetaOapg.properties.salaryBandCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managerProfileId"]) -> MetaOapg.properties.managerProfileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managerProfileName"]) -> MetaOapg.properties.managerProfileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFieldValueModelList"]) -> MetaOapg.properties.customFieldValueModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberofUsers"]) -> MetaOapg.properties.numberofUsers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createuserid"]) -> MetaOapg.properties.createuserid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["careerPathwayModelList"]) -> MetaOapg.properties.careerPathwayModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectType"]) -> MetaOapg.properties.objectType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectName"]) -> MetaOapg.properties.objectName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectid"]) -> MetaOapg.properties.objectid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cid", "profileId", "profileName", "profileDescription", "orgId", "profileResponsibilities", "profileRequirements", "salaryBandMin", "salaryBandMax", "salaryBandCurrency", "managerProfileId", "managerProfileName", "customFieldValueModelList", "numberofUsers", "createuserid", "status", "careerPathwayModelList", "objectType", "objectName", "objectid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileId"]) -> typing.Union[MetaOapg.properties.profileId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileName"]) -> typing.Union[MetaOapg.properties.profileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileDescription"]) -> typing.Union[MetaOapg.properties.profileDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> typing.Union[MetaOapg.properties.orgId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileResponsibilities"]) -> typing.Union[MetaOapg.properties.profileResponsibilities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileRequirements"]) -> typing.Union[MetaOapg.properties.profileRequirements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salaryBandMin"]) -> typing.Union[MetaOapg.properties.salaryBandMin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salaryBandMax"]) -> typing.Union[MetaOapg.properties.salaryBandMax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salaryBandCurrency"]) -> typing.Union[MetaOapg.properties.salaryBandCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managerProfileId"]) -> typing.Union[MetaOapg.properties.managerProfileId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managerProfileName"]) -> typing.Union[MetaOapg.properties.managerProfileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFieldValueModelList"]) -> typing.Union[MetaOapg.properties.customFieldValueModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberofUsers"]) -> typing.Union[MetaOapg.properties.numberofUsers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createuserid"]) -> typing.Union[MetaOapg.properties.createuserid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["careerPathwayModelList"]) -> typing.Union[MetaOapg.properties.careerPathwayModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectType"]) -> typing.Union[MetaOapg.properties.objectType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectName"]) -> typing.Union[MetaOapg.properties.objectName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectid"]) -> typing.Union[MetaOapg.properties.objectid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cid", "profileId", "profileName", "profileDescription", "orgId", "profileResponsibilities", "profileRequirements", "salaryBandMin", "salaryBandMax", "salaryBandCurrency", "managerProfileId", "managerProfileName", "customFieldValueModelList", "numberofUsers", "createuserid", "status", "careerPathwayModelList", "objectType", "objectName", "objectid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cid: typing.Union[MetaOapg.properties.cid, str, schemas.Unset] = schemas.unset,
        profileId: typing.Union[MetaOapg.properties.profileId, str, schemas.Unset] = schemas.unset,
        profileName: typing.Union[MetaOapg.properties.profileName, str, schemas.Unset] = schemas.unset,
        profileDescription: typing.Union[MetaOapg.properties.profileDescription, str, schemas.Unset] = schemas.unset,
        orgId: typing.Union[MetaOapg.properties.orgId, str, schemas.Unset] = schemas.unset,
        profileResponsibilities: typing.Union[MetaOapg.properties.profileResponsibilities, str, schemas.Unset] = schemas.unset,
        profileRequirements: typing.Union[MetaOapg.properties.profileRequirements, str, schemas.Unset] = schemas.unset,
        salaryBandMin: typing.Union[MetaOapg.properties.salaryBandMin, str, schemas.Unset] = schemas.unset,
        salaryBandMax: typing.Union[MetaOapg.properties.salaryBandMax, str, schemas.Unset] = schemas.unset,
        salaryBandCurrency: typing.Union[MetaOapg.properties.salaryBandCurrency, str, schemas.Unset] = schemas.unset,
        managerProfileId: typing.Union[MetaOapg.properties.managerProfileId, str, schemas.Unset] = schemas.unset,
        managerProfileName: typing.Union[MetaOapg.properties.managerProfileName, str, schemas.Unset] = schemas.unset,
        customFieldValueModelList: typing.Union[MetaOapg.properties.customFieldValueModelList, str, schemas.Unset] = schemas.unset,
        numberofUsers: typing.Union[MetaOapg.properties.numberofUsers, str, schemas.Unset] = schemas.unset,
        createuserid: typing.Union[MetaOapg.properties.createuserid, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        careerPathwayModelList: typing.Union[MetaOapg.properties.careerPathwayModelList, str, schemas.Unset] = schemas.unset,
        objectType: typing.Union[MetaOapg.properties.objectType, str, schemas.Unset] = schemas.unset,
        objectName: typing.Union[MetaOapg.properties.objectName, str, schemas.Unset] = schemas.unset,
        objectid: typing.Union[MetaOapg.properties.objectid, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobProfilesGetJobProfilesResponseItem':
        return super().__new__(
            cls,
            *args,
            cid=cid,
            profileId=profileId,
            profileName=profileName,
            profileDescription=profileDescription,
            orgId=orgId,
            profileResponsibilities=profileResponsibilities,
            profileRequirements=profileRequirements,
            salaryBandMin=salaryBandMin,
            salaryBandMax=salaryBandMax,
            salaryBandCurrency=salaryBandCurrency,
            managerProfileId=managerProfileId,
            managerProfileName=managerProfileName,
            customFieldValueModelList=customFieldValueModelList,
            numberofUsers=numberofUsers,
            createuserid=createuserid,
            status=status,
            careerPathwayModelList=careerPathwayModelList,
            objectType=objectType,
            objectName=objectName,
            objectid=objectid,
            _configuration=_configuration,
            **kwargs,
        )
