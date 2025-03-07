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


class SkillsGetUserAssignedSkillsResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            skillUserId = schemas.StrSchema
            skillId = schemas.StrSchema
            userId = schemas.StrSchema
            level = schemas.StrSchema
            cid = schemas.StrSchema
            lastUpdateUserModel = schemas.StrSchema
            createUserId = schemas.StrSchema
            status = schemas.StrSchema
            createts = schemas.StrSchema
            performancelevel = schemas.StrSchema
            candidateid = schemas.StrSchema
            weightage = schemas.StrSchema
            targetLevel = schemas.StrSchema
            targetLevelCreatets = schemas.StrSchema
            targetLevelCreateUserId = schemas.StrSchema
            skillCounsellor = schemas.StrSchema
            yearsOfExperience = schemas.StrSchema
            dateOfLastUse = schemas.StrSchema
            skillAcquireDate = schemas.StrSchema
        
            @staticmethod
            def skillModel() -> typing.Type['SkillsGetUserAssignedSkillsResponseDataItemSkillModel']:
                return SkillsGetUserAssignedSkillsResponseDataItemSkillModel
            __annotations__ = {
                "description": description,
                "skillUserId": skillUserId,
                "skillId": skillId,
                "userId": userId,
                "level": level,
                "cid": cid,
                "lastUpdateUserModel": lastUpdateUserModel,
                "createUserId": createUserId,
                "status": status,
                "createts": createts,
                "performancelevel": performancelevel,
                "candidateid": candidateid,
                "weightage": weightage,
                "targetLevel": targetLevel,
                "targetLevelCreatets": targetLevelCreatets,
                "targetLevelCreateUserId": targetLevelCreateUserId,
                "skillCounsellor": skillCounsellor,
                "yearsOfExperience": yearsOfExperience,
                "dateOfLastUse": dateOfLastUse,
                "skillAcquireDate": skillAcquireDate,
                "skillModel": skillModel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skillUserId"]) -> MetaOapg.properties.skillUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skillId"]) -> MetaOapg.properties.skillId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdateUserModel"]) -> MetaOapg.properties.lastUpdateUserModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createUserId"]) -> MetaOapg.properties.createUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createts"]) -> MetaOapg.properties.createts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["performancelevel"]) -> MetaOapg.properties.performancelevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidateid"]) -> MetaOapg.properties.candidateid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weightage"]) -> MetaOapg.properties.weightage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetLevel"]) -> MetaOapg.properties.targetLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetLevelCreatets"]) -> MetaOapg.properties.targetLevelCreatets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetLevelCreateUserId"]) -> MetaOapg.properties.targetLevelCreateUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skillCounsellor"]) -> MetaOapg.properties.skillCounsellor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yearsOfExperience"]) -> MetaOapg.properties.yearsOfExperience: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateOfLastUse"]) -> MetaOapg.properties.dateOfLastUse: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skillAcquireDate"]) -> MetaOapg.properties.skillAcquireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skillModel"]) -> 'SkillsGetUserAssignedSkillsResponseDataItemSkillModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "skillUserId", "skillId", "userId", "level", "cid", "lastUpdateUserModel", "createUserId", "status", "createts", "performancelevel", "candidateid", "weightage", "targetLevel", "targetLevelCreatets", "targetLevelCreateUserId", "skillCounsellor", "yearsOfExperience", "dateOfLastUse", "skillAcquireDate", "skillModel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skillUserId"]) -> typing.Union[MetaOapg.properties.skillUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skillId"]) -> typing.Union[MetaOapg.properties.skillId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> typing.Union[MetaOapg.properties.level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdateUserModel"]) -> typing.Union[MetaOapg.properties.lastUpdateUserModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createUserId"]) -> typing.Union[MetaOapg.properties.createUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createts"]) -> typing.Union[MetaOapg.properties.createts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["performancelevel"]) -> typing.Union[MetaOapg.properties.performancelevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidateid"]) -> typing.Union[MetaOapg.properties.candidateid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weightage"]) -> typing.Union[MetaOapg.properties.weightage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetLevel"]) -> typing.Union[MetaOapg.properties.targetLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetLevelCreatets"]) -> typing.Union[MetaOapg.properties.targetLevelCreatets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetLevelCreateUserId"]) -> typing.Union[MetaOapg.properties.targetLevelCreateUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skillCounsellor"]) -> typing.Union[MetaOapg.properties.skillCounsellor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yearsOfExperience"]) -> typing.Union[MetaOapg.properties.yearsOfExperience, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateOfLastUse"]) -> typing.Union[MetaOapg.properties.dateOfLastUse, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skillAcquireDate"]) -> typing.Union[MetaOapg.properties.skillAcquireDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skillModel"]) -> typing.Union['SkillsGetUserAssignedSkillsResponseDataItemSkillModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "skillUserId", "skillId", "userId", "level", "cid", "lastUpdateUserModel", "createUserId", "status", "createts", "performancelevel", "candidateid", "weightage", "targetLevel", "targetLevelCreatets", "targetLevelCreateUserId", "skillCounsellor", "yearsOfExperience", "dateOfLastUse", "skillAcquireDate", "skillModel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        skillUserId: typing.Union[MetaOapg.properties.skillUserId, str, schemas.Unset] = schemas.unset,
        skillId: typing.Union[MetaOapg.properties.skillId, str, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        level: typing.Union[MetaOapg.properties.level, str, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, str, schemas.Unset] = schemas.unset,
        lastUpdateUserModel: typing.Union[MetaOapg.properties.lastUpdateUserModel, str, schemas.Unset] = schemas.unset,
        createUserId: typing.Union[MetaOapg.properties.createUserId, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        createts: typing.Union[MetaOapg.properties.createts, str, schemas.Unset] = schemas.unset,
        performancelevel: typing.Union[MetaOapg.properties.performancelevel, str, schemas.Unset] = schemas.unset,
        candidateid: typing.Union[MetaOapg.properties.candidateid, str, schemas.Unset] = schemas.unset,
        weightage: typing.Union[MetaOapg.properties.weightage, str, schemas.Unset] = schemas.unset,
        targetLevel: typing.Union[MetaOapg.properties.targetLevel, str, schemas.Unset] = schemas.unset,
        targetLevelCreatets: typing.Union[MetaOapg.properties.targetLevelCreatets, str, schemas.Unset] = schemas.unset,
        targetLevelCreateUserId: typing.Union[MetaOapg.properties.targetLevelCreateUserId, str, schemas.Unset] = schemas.unset,
        skillCounsellor: typing.Union[MetaOapg.properties.skillCounsellor, str, schemas.Unset] = schemas.unset,
        yearsOfExperience: typing.Union[MetaOapg.properties.yearsOfExperience, str, schemas.Unset] = schemas.unset,
        dateOfLastUse: typing.Union[MetaOapg.properties.dateOfLastUse, str, schemas.Unset] = schemas.unset,
        skillAcquireDate: typing.Union[MetaOapg.properties.skillAcquireDate, str, schemas.Unset] = schemas.unset,
        skillModel: typing.Union['SkillsGetUserAssignedSkillsResponseDataItemSkillModel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SkillsGetUserAssignedSkillsResponseDataItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            skillUserId=skillUserId,
            skillId=skillId,
            userId=userId,
            level=level,
            cid=cid,
            lastUpdateUserModel=lastUpdateUserModel,
            createUserId=createUserId,
            status=status,
            createts=createts,
            performancelevel=performancelevel,
            candidateid=candidateid,
            weightage=weightage,
            targetLevel=targetLevel,
            targetLevelCreatets=targetLevelCreatets,
            targetLevelCreateUserId=targetLevelCreateUserId,
            skillCounsellor=skillCounsellor,
            yearsOfExperience=yearsOfExperience,
            dateOfLastUse=dateOfLastUse,
            skillAcquireDate=skillAcquireDate,
            skillModel=skillModel,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.skills_get_user_assigned_skills_response_data_item_skill_model import SkillsGetUserAssignedSkillsResponseDataItemSkillModel
