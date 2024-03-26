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


class PositionModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            accessLevel = schemas.StrSchema
            applicationDueDate = schemas.DateSchema
            applicationFormId = schemas.Int32Schema
            approvalFlowId = schemas.Int32Schema
            approvalStatus = schemas.StrSchema
            assessmentFormId = schemas.Int32Schema
            assessmentTemplateId = schemas.Int32Schema
            
            
            class candidatePositionModelList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CandidateApplicationsModel']:
                        return CandidateApplicationsModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CandidateApplicationsModel'], typing.List['CandidateApplicationsModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'candidatePositionModelList':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CandidateApplicationsModel':
                    return super().__getitem__(i)
            cid = schemas.Int32Schema
            count = schemas.Int32Schema
            createDate = schemas.DateSchema
            createUserId = schemas.Int32Schema
            customLocation = schemas.StrSchema
            dateClose = schemas.DateSchema
            departmentId = schemas.Int32Schema
            funnelId = schemas.Int64Schema
            hiringManagerId = schemas.Int32Schema
            htmlTemplate = schemas.StrSchema
            isRecommended = schemas.BoolSchema
            lastUpdatets = schemas.DateSchema
            lastupdateuserid = schemas.Int32Schema
        
            @staticmethod
            def locationModel() -> typing.Type['LocationModel']:
                return LocationModel
            locationid = schemas.Int32Schema
            name = schemas.StrSchema
            
            
            class positionApprovalLevelList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PositionApprovalLevelModel']:
                        return PositionApprovalLevelModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PositionApprovalLevelModel'], typing.List['PositionApprovalLevelModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'positionApprovalLevelList':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PositionApprovalLevelModel':
                    return super().__getitem__(i)
            positionUID = schemas.StrSchema
            positionid = schemas.Int32Schema
        
            @staticmethod
            def profileModel() -> typing.Type['UserProfileModel']:
                return UserProfileModel
            profileid = schemas.Int32Schema
        
            @staticmethod
            def projectModel() -> typing.Type['ProjectModel']:
                return ProjectModel
            projectid = schemas.Int32Schema
            recommended = schemas.BoolSchema
            recruiterId = schemas.Int32Schema
        
            @staticmethod
            def recruiterModel() -> typing.Type['UserViewModel']:
                return UserViewModel
            requestApprovalId = schemas.Int32Schema
            requirements = schemas.StrSchema
            responsibilities = schemas.StrSchema
            seoUrl = schemas.StrSchema
            status = schemas.StrSchema
            totalcandidate = schemas.Int32Schema
            userName = schemas.StrSchema
        
            @staticmethod
            def userViewModel() -> typing.Type['UserViewModel']:
                return UserViewModel
            
            
            class userapprovalList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserPositionApprovalModel']:
                        return UserPositionApprovalModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UserPositionApprovalModel'], typing.List['UserPositionApprovalModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'userapprovalList':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserPositionApprovalModel':
                    return super().__getitem__(i)
            id = schemas.Int32Schema
            __annotations__ = {
                "description": description,
                "accessLevel": accessLevel,
                "applicationDueDate": applicationDueDate,
                "applicationFormId": applicationFormId,
                "approvalFlowId": approvalFlowId,
                "approvalStatus": approvalStatus,
                "assessmentFormId": assessmentFormId,
                "assessmentTemplateId": assessmentTemplateId,
                "candidatePositionModelList": candidatePositionModelList,
                "cid": cid,
                "count": count,
                "createDate": createDate,
                "createUserId": createUserId,
                "customLocation": customLocation,
                "dateClose": dateClose,
                "departmentId": departmentId,
                "funnelId": funnelId,
                "hiringManagerId": hiringManagerId,
                "htmlTemplate": htmlTemplate,
                "isRecommended": isRecommended,
                "lastUpdatets": lastUpdatets,
                "lastupdateuserid": lastupdateuserid,
                "locationModel": locationModel,
                "locationid": locationid,
                "name": name,
                "positionApprovalLevelList": positionApprovalLevelList,
                "positionUID": positionUID,
                "positionid": positionid,
                "profileModel": profileModel,
                "profileid": profileid,
                "projectModel": projectModel,
                "projectid": projectid,
                "recommended": recommended,
                "recruiterId": recruiterId,
                "recruiterModel": recruiterModel,
                "requestApprovalId": requestApprovalId,
                "requirements": requirements,
                "responsibilities": responsibilities,
                "seoUrl": seoUrl,
                "status": status,
                "totalcandidate": totalcandidate,
                "userName": userName,
                "userViewModel": userViewModel,
                "userapprovalList": userapprovalList,
                "id": id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessLevel"]) -> MetaOapg.properties.accessLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationDueDate"]) -> MetaOapg.properties.applicationDueDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationFormId"]) -> MetaOapg.properties.applicationFormId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalFlowId"]) -> MetaOapg.properties.approvalFlowId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalStatus"]) -> MetaOapg.properties.approvalStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assessmentFormId"]) -> MetaOapg.properties.assessmentFormId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assessmentTemplateId"]) -> MetaOapg.properties.assessmentTemplateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidatePositionModelList"]) -> MetaOapg.properties.candidatePositionModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createDate"]) -> MetaOapg.properties.createDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createUserId"]) -> MetaOapg.properties.createUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customLocation"]) -> MetaOapg.properties.customLocation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateClose"]) -> MetaOapg.properties.dateClose: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["departmentId"]) -> MetaOapg.properties.departmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["funnelId"]) -> MetaOapg.properties.funnelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hiringManagerId"]) -> MetaOapg.properties.hiringManagerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["htmlTemplate"]) -> MetaOapg.properties.htmlTemplate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isRecommended"]) -> MetaOapg.properties.isRecommended: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdatets"]) -> MetaOapg.properties.lastUpdatets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastupdateuserid"]) -> MetaOapg.properties.lastupdateuserid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationModel"]) -> 'LocationModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationid"]) -> MetaOapg.properties.locationid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positionApprovalLevelList"]) -> MetaOapg.properties.positionApprovalLevelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positionUID"]) -> MetaOapg.properties.positionUID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positionid"]) -> MetaOapg.properties.positionid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileModel"]) -> 'UserProfileModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileid"]) -> MetaOapg.properties.profileid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectModel"]) -> 'ProjectModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectid"]) -> MetaOapg.properties.projectid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recommended"]) -> MetaOapg.properties.recommended: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recruiterId"]) -> MetaOapg.properties.recruiterId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recruiterModel"]) -> 'UserViewModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestApprovalId"]) -> MetaOapg.properties.requestApprovalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requirements"]) -> MetaOapg.properties.requirements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["responsibilities"]) -> MetaOapg.properties.responsibilities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seoUrl"]) -> MetaOapg.properties.seoUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalcandidate"]) -> MetaOapg.properties.totalcandidate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userViewModel"]) -> 'UserViewModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userapprovalList"]) -> MetaOapg.properties.userapprovalList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "accessLevel", "applicationDueDate", "applicationFormId", "approvalFlowId", "approvalStatus", "assessmentFormId", "assessmentTemplateId", "candidatePositionModelList", "cid", "count", "createDate", "createUserId", "customLocation", "dateClose", "departmentId", "funnelId", "hiringManagerId", "htmlTemplate", "isRecommended", "lastUpdatets", "lastupdateuserid", "locationModel", "locationid", "name", "positionApprovalLevelList", "positionUID", "positionid", "profileModel", "profileid", "projectModel", "projectid", "recommended", "recruiterId", "recruiterModel", "requestApprovalId", "requirements", "responsibilities", "seoUrl", "status", "totalcandidate", "userName", "userViewModel", "userapprovalList", "id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessLevel"]) -> typing.Union[MetaOapg.properties.accessLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationDueDate"]) -> typing.Union[MetaOapg.properties.applicationDueDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationFormId"]) -> typing.Union[MetaOapg.properties.applicationFormId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalFlowId"]) -> typing.Union[MetaOapg.properties.approvalFlowId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalStatus"]) -> typing.Union[MetaOapg.properties.approvalStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assessmentFormId"]) -> typing.Union[MetaOapg.properties.assessmentFormId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assessmentTemplateId"]) -> typing.Union[MetaOapg.properties.assessmentTemplateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidatePositionModelList"]) -> typing.Union[MetaOapg.properties.candidatePositionModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createDate"]) -> typing.Union[MetaOapg.properties.createDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createUserId"]) -> typing.Union[MetaOapg.properties.createUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customLocation"]) -> typing.Union[MetaOapg.properties.customLocation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateClose"]) -> typing.Union[MetaOapg.properties.dateClose, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["departmentId"]) -> typing.Union[MetaOapg.properties.departmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["funnelId"]) -> typing.Union[MetaOapg.properties.funnelId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hiringManagerId"]) -> typing.Union[MetaOapg.properties.hiringManagerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["htmlTemplate"]) -> typing.Union[MetaOapg.properties.htmlTemplate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isRecommended"]) -> typing.Union[MetaOapg.properties.isRecommended, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdatets"]) -> typing.Union[MetaOapg.properties.lastUpdatets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastupdateuserid"]) -> typing.Union[MetaOapg.properties.lastupdateuserid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationModel"]) -> typing.Union['LocationModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationid"]) -> typing.Union[MetaOapg.properties.locationid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positionApprovalLevelList"]) -> typing.Union[MetaOapg.properties.positionApprovalLevelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positionUID"]) -> typing.Union[MetaOapg.properties.positionUID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positionid"]) -> typing.Union[MetaOapg.properties.positionid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileModel"]) -> typing.Union['UserProfileModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileid"]) -> typing.Union[MetaOapg.properties.profileid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectModel"]) -> typing.Union['ProjectModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectid"]) -> typing.Union[MetaOapg.properties.projectid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recommended"]) -> typing.Union[MetaOapg.properties.recommended, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recruiterId"]) -> typing.Union[MetaOapg.properties.recruiterId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recruiterModel"]) -> typing.Union['UserViewModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestApprovalId"]) -> typing.Union[MetaOapg.properties.requestApprovalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requirements"]) -> typing.Union[MetaOapg.properties.requirements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["responsibilities"]) -> typing.Union[MetaOapg.properties.responsibilities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seoUrl"]) -> typing.Union[MetaOapg.properties.seoUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalcandidate"]) -> typing.Union[MetaOapg.properties.totalcandidate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userName"]) -> typing.Union[MetaOapg.properties.userName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userViewModel"]) -> typing.Union['UserViewModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userapprovalList"]) -> typing.Union[MetaOapg.properties.userapprovalList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "accessLevel", "applicationDueDate", "applicationFormId", "approvalFlowId", "approvalStatus", "assessmentFormId", "assessmentTemplateId", "candidatePositionModelList", "cid", "count", "createDate", "createUserId", "customLocation", "dateClose", "departmentId", "funnelId", "hiringManagerId", "htmlTemplate", "isRecommended", "lastUpdatets", "lastupdateuserid", "locationModel", "locationid", "name", "positionApprovalLevelList", "positionUID", "positionid", "profileModel", "profileid", "projectModel", "projectid", "recommended", "recruiterId", "recruiterModel", "requestApprovalId", "requirements", "responsibilities", "seoUrl", "status", "totalcandidate", "userName", "userViewModel", "userapprovalList", "id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        accessLevel: typing.Union[MetaOapg.properties.accessLevel, str, schemas.Unset] = schemas.unset,
        applicationDueDate: typing.Union[MetaOapg.properties.applicationDueDate, str, date, schemas.Unset] = schemas.unset,
        applicationFormId: typing.Union[MetaOapg.properties.applicationFormId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        approvalFlowId: typing.Union[MetaOapg.properties.approvalFlowId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        approvalStatus: typing.Union[MetaOapg.properties.approvalStatus, str, schemas.Unset] = schemas.unset,
        assessmentFormId: typing.Union[MetaOapg.properties.assessmentFormId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        assessmentTemplateId: typing.Union[MetaOapg.properties.assessmentTemplateId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        candidatePositionModelList: typing.Union[MetaOapg.properties.candidatePositionModelList, list, tuple, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createDate: typing.Union[MetaOapg.properties.createDate, str, date, schemas.Unset] = schemas.unset,
        createUserId: typing.Union[MetaOapg.properties.createUserId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        customLocation: typing.Union[MetaOapg.properties.customLocation, str, schemas.Unset] = schemas.unset,
        dateClose: typing.Union[MetaOapg.properties.dateClose, str, date, schemas.Unset] = schemas.unset,
        departmentId: typing.Union[MetaOapg.properties.departmentId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        funnelId: typing.Union[MetaOapg.properties.funnelId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hiringManagerId: typing.Union[MetaOapg.properties.hiringManagerId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        htmlTemplate: typing.Union[MetaOapg.properties.htmlTemplate, str, schemas.Unset] = schemas.unset,
        isRecommended: typing.Union[MetaOapg.properties.isRecommended, bool, schemas.Unset] = schemas.unset,
        lastUpdatets: typing.Union[MetaOapg.properties.lastUpdatets, str, date, schemas.Unset] = schemas.unset,
        lastupdateuserid: typing.Union[MetaOapg.properties.lastupdateuserid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        locationModel: typing.Union['LocationModel', schemas.Unset] = schemas.unset,
        locationid: typing.Union[MetaOapg.properties.locationid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        positionApprovalLevelList: typing.Union[MetaOapg.properties.positionApprovalLevelList, list, tuple, schemas.Unset] = schemas.unset,
        positionUID: typing.Union[MetaOapg.properties.positionUID, str, schemas.Unset] = schemas.unset,
        positionid: typing.Union[MetaOapg.properties.positionid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        profileModel: typing.Union['UserProfileModel', schemas.Unset] = schemas.unset,
        profileid: typing.Union[MetaOapg.properties.profileid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        projectModel: typing.Union['ProjectModel', schemas.Unset] = schemas.unset,
        projectid: typing.Union[MetaOapg.properties.projectid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        recommended: typing.Union[MetaOapg.properties.recommended, bool, schemas.Unset] = schemas.unset,
        recruiterId: typing.Union[MetaOapg.properties.recruiterId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        recruiterModel: typing.Union['UserViewModel', schemas.Unset] = schemas.unset,
        requestApprovalId: typing.Union[MetaOapg.properties.requestApprovalId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        requirements: typing.Union[MetaOapg.properties.requirements, str, schemas.Unset] = schemas.unset,
        responsibilities: typing.Union[MetaOapg.properties.responsibilities, str, schemas.Unset] = schemas.unset,
        seoUrl: typing.Union[MetaOapg.properties.seoUrl, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        totalcandidate: typing.Union[MetaOapg.properties.totalcandidate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        userName: typing.Union[MetaOapg.properties.userName, str, schemas.Unset] = schemas.unset,
        userViewModel: typing.Union['UserViewModel', schemas.Unset] = schemas.unset,
        userapprovalList: typing.Union[MetaOapg.properties.userapprovalList, list, tuple, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PositionModel':
        return super().__new__(
            cls,
            *args,
            description=description,
            accessLevel=accessLevel,
            applicationDueDate=applicationDueDate,
            applicationFormId=applicationFormId,
            approvalFlowId=approvalFlowId,
            approvalStatus=approvalStatus,
            assessmentFormId=assessmentFormId,
            assessmentTemplateId=assessmentTemplateId,
            candidatePositionModelList=candidatePositionModelList,
            cid=cid,
            count=count,
            createDate=createDate,
            createUserId=createUserId,
            customLocation=customLocation,
            dateClose=dateClose,
            departmentId=departmentId,
            funnelId=funnelId,
            hiringManagerId=hiringManagerId,
            htmlTemplate=htmlTemplate,
            isRecommended=isRecommended,
            lastUpdatets=lastUpdatets,
            lastupdateuserid=lastupdateuserid,
            locationModel=locationModel,
            locationid=locationid,
            name=name,
            positionApprovalLevelList=positionApprovalLevelList,
            positionUID=positionUID,
            positionid=positionid,
            profileModel=profileModel,
            profileid=profileid,
            projectModel=projectModel,
            projectid=projectid,
            recommended=recommended,
            recruiterId=recruiterId,
            recruiterModel=recruiterModel,
            requestApprovalId=requestApprovalId,
            requirements=requirements,
            responsibilities=responsibilities,
            seoUrl=seoUrl,
            status=status,
            totalcandidate=totalcandidate,
            userName=userName,
            userViewModel=userViewModel,
            userapprovalList=userapprovalList,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.candidate_applications_model import CandidateApplicationsModel
from clay_hr_python_sdk.model.location_model import LocationModel
from clay_hr_python_sdk.model.position_approval_level_model import PositionApprovalLevelModel
from clay_hr_python_sdk.model.project_model import ProjectModel
from clay_hr_python_sdk.model.user_position_approval_model import UserPositionApprovalModel
from clay_hr_python_sdk.model.user_profile_model import UserProfileModel
from clay_hr_python_sdk.model.user_view_model import UserViewModel
