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


class SkillsCreateNewSkillRequestAssessmentModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "scoretemplateid",
        }
        
        class properties:
            scoretemplateid = schemas.Int32Schema
        
            @staticmethod
            def rangeModelList() -> typing.Type['SkillsCreateNewSkillRequestAssessmentModelRangeModelList']:
                return SkillsCreateNewSkillRequestAssessmentModelRangeModelList
            scoreMax = schemas.Float32Schema
            scoreMin = schemas.Float32Schema
            scoreName = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "A": "A",
                        "ARCHV": "ARCHV",
                    }
                
                @schemas.classproperty
                def A(cls):
                    return cls("A")
                
                @schemas.classproperty
                def ARCHV(cls):
                    return cls("ARCHV")
            __annotations__ = {
                "scoretemplateid": scoretemplateid,
                "rangeModelList": rangeModelList,
                "scoreMax": scoreMax,
                "scoreMin": scoreMin,
                "scoreName": scoreName,
                "status": status,
            }
    
    scoretemplateid: MetaOapg.properties.scoretemplateid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoretemplateid"]) -> MetaOapg.properties.scoretemplateid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rangeModelList"]) -> 'SkillsCreateNewSkillRequestAssessmentModelRangeModelList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoreMax"]) -> MetaOapg.properties.scoreMax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoreMin"]) -> MetaOapg.properties.scoreMin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoreName"]) -> MetaOapg.properties.scoreName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["scoretemplateid", "rangeModelList", "scoreMax", "scoreMin", "scoreName", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoretemplateid"]) -> MetaOapg.properties.scoretemplateid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rangeModelList"]) -> typing.Union['SkillsCreateNewSkillRequestAssessmentModelRangeModelList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoreMax"]) -> typing.Union[MetaOapg.properties.scoreMax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoreMin"]) -> typing.Union[MetaOapg.properties.scoreMin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoreName"]) -> typing.Union[MetaOapg.properties.scoreName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["scoretemplateid", "rangeModelList", "scoreMax", "scoreMin", "scoreName", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        scoretemplateid: typing.Union[MetaOapg.properties.scoretemplateid, decimal.Decimal, int, ],
        rangeModelList: typing.Union['SkillsCreateNewSkillRequestAssessmentModelRangeModelList', schemas.Unset] = schemas.unset,
        scoreMax: typing.Union[MetaOapg.properties.scoreMax, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        scoreMin: typing.Union[MetaOapg.properties.scoreMin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        scoreName: typing.Union[MetaOapg.properties.scoreName, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SkillsCreateNewSkillRequestAssessmentModel':
        return super().__new__(
            cls,
            *args,
            scoretemplateid=scoretemplateid,
            rangeModelList=rangeModelList,
            scoreMax=scoreMax,
            scoreMin=scoreMin,
            scoreName=scoreName,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.skills_create_new_skill_request_assessment_model_range_model_list import SkillsCreateNewSkillRequestAssessmentModelRangeModelList
