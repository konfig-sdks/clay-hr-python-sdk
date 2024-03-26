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


class UserTrainingModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            assessmentScore = schemas.Float64Schema
            assignedByUserId = schemas.Int32Schema
        
            @staticmethod
            def candidateModel() -> typing.Type['CandidateModel']:
                return CandidateModel
            candidateid = schemas.Int32Schema
            cid = schemas.Int32Schema
        
            @staticmethod
            def completionts() -> typing.Type['Timestamp']:
                return Timestamp
            coordinatorName = schemas.StrSchema
        
            @staticmethod
            def createts() -> typing.Type['Timestamp']:
                return Timestamp
            dueDate = schemas.DateSchema
            dynaFormAssignmentId = schemas.Int32Schema
            status = schemas.StrSchema
            testResult = schemas.StrSchema
            trainingCoordinator = schemas.Int32Schema
            trainingId = schemas.Int32Schema
        
            @staticmethod
            def trainingModel() -> typing.Type['TrainingModel']:
                return TrainingModel
            traininguserId = schemas.Int32Schema
        
            @staticmethod
            def userModel() -> typing.Type['UserViewModel']:
                return UserViewModel
            userid = schemas.Int32Schema
            __annotations__ = {
                "assessmentScore": assessmentScore,
                "assignedByUserId": assignedByUserId,
                "candidateModel": candidateModel,
                "candidateid": candidateid,
                "cid": cid,
                "completionts": completionts,
                "coordinatorName": coordinatorName,
                "createts": createts,
                "dueDate": dueDate,
                "dynaFormAssignmentId": dynaFormAssignmentId,
                "status": status,
                "testResult": testResult,
                "trainingCoordinator": trainingCoordinator,
                "trainingId": trainingId,
                "trainingModel": trainingModel,
                "traininguserId": traininguserId,
                "userModel": userModel,
                "userid": userid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assessmentScore"]) -> MetaOapg.properties.assessmentScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignedByUserId"]) -> MetaOapg.properties.assignedByUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidateModel"]) -> 'CandidateModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidateid"]) -> MetaOapg.properties.candidateid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completionts"]) -> 'Timestamp': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coordinatorName"]) -> MetaOapg.properties.coordinatorName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createts"]) -> 'Timestamp': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dueDate"]) -> MetaOapg.properties.dueDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dynaFormAssignmentId"]) -> MetaOapg.properties.dynaFormAssignmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["testResult"]) -> MetaOapg.properties.testResult: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingCoordinator"]) -> MetaOapg.properties.trainingCoordinator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingId"]) -> MetaOapg.properties.trainingId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingModel"]) -> 'TrainingModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["traininguserId"]) -> MetaOapg.properties.traininguserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userModel"]) -> 'UserViewModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userid"]) -> MetaOapg.properties.userid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assessmentScore", "assignedByUserId", "candidateModel", "candidateid", "cid", "completionts", "coordinatorName", "createts", "dueDate", "dynaFormAssignmentId", "status", "testResult", "trainingCoordinator", "trainingId", "trainingModel", "traininguserId", "userModel", "userid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assessmentScore"]) -> typing.Union[MetaOapg.properties.assessmentScore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignedByUserId"]) -> typing.Union[MetaOapg.properties.assignedByUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidateModel"]) -> typing.Union['CandidateModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidateid"]) -> typing.Union[MetaOapg.properties.candidateid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completionts"]) -> typing.Union['Timestamp', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coordinatorName"]) -> typing.Union[MetaOapg.properties.coordinatorName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createts"]) -> typing.Union['Timestamp', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dueDate"]) -> typing.Union[MetaOapg.properties.dueDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dynaFormAssignmentId"]) -> typing.Union[MetaOapg.properties.dynaFormAssignmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["testResult"]) -> typing.Union[MetaOapg.properties.testResult, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingCoordinator"]) -> typing.Union[MetaOapg.properties.trainingCoordinator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingId"]) -> typing.Union[MetaOapg.properties.trainingId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingModel"]) -> typing.Union['TrainingModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["traininguserId"]) -> typing.Union[MetaOapg.properties.traininguserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userModel"]) -> typing.Union['UserViewModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userid"]) -> typing.Union[MetaOapg.properties.userid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assessmentScore", "assignedByUserId", "candidateModel", "candidateid", "cid", "completionts", "coordinatorName", "createts", "dueDate", "dynaFormAssignmentId", "status", "testResult", "trainingCoordinator", "trainingId", "trainingModel", "traininguserId", "userModel", "userid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        assessmentScore: typing.Union[MetaOapg.properties.assessmentScore, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        assignedByUserId: typing.Union[MetaOapg.properties.assignedByUserId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        candidateModel: typing.Union['CandidateModel', schemas.Unset] = schemas.unset,
        candidateid: typing.Union[MetaOapg.properties.candidateid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        completionts: typing.Union['Timestamp', schemas.Unset] = schemas.unset,
        coordinatorName: typing.Union[MetaOapg.properties.coordinatorName, str, schemas.Unset] = schemas.unset,
        createts: typing.Union['Timestamp', schemas.Unset] = schemas.unset,
        dueDate: typing.Union[MetaOapg.properties.dueDate, str, date, schemas.Unset] = schemas.unset,
        dynaFormAssignmentId: typing.Union[MetaOapg.properties.dynaFormAssignmentId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        testResult: typing.Union[MetaOapg.properties.testResult, str, schemas.Unset] = schemas.unset,
        trainingCoordinator: typing.Union[MetaOapg.properties.trainingCoordinator, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingId: typing.Union[MetaOapg.properties.trainingId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingModel: typing.Union['TrainingModel', schemas.Unset] = schemas.unset,
        traininguserId: typing.Union[MetaOapg.properties.traininguserId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        userModel: typing.Union['UserViewModel', schemas.Unset] = schemas.unset,
        userid: typing.Union[MetaOapg.properties.userid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserTrainingModel':
        return super().__new__(
            cls,
            *args,
            assessmentScore=assessmentScore,
            assignedByUserId=assignedByUserId,
            candidateModel=candidateModel,
            candidateid=candidateid,
            cid=cid,
            completionts=completionts,
            coordinatorName=coordinatorName,
            createts=createts,
            dueDate=dueDate,
            dynaFormAssignmentId=dynaFormAssignmentId,
            status=status,
            testResult=testResult,
            trainingCoordinator=trainingCoordinator,
            trainingId=trainingId,
            trainingModel=trainingModel,
            traininguserId=traininguserId,
            userModel=userModel,
            userid=userid,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.candidate_model import CandidateModel
from clay_hr_python_sdk.model.timestamp import Timestamp
from clay_hr_python_sdk.model.training_model import TrainingModel
from clay_hr_python_sdk.model.user_view_model import UserViewModel
