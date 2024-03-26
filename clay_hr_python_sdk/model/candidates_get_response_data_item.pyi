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


class CandidatesGetResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            recruitId = schemas.StrSchema
            name = schemas.StrSchema
            referrerId = schemas.StrSchema
            referrer = schemas.StrSchema
            recruiter = schemas.StrSchema
            score = schemas.StrSchema
            updatedOn = schemas.StrSchema
            status = schemas.StrSchema
            notes = schemas.StrSchema
            dateOfBirth = schemas.StrSchema
            joiningDate = schemas.StrSchema
            cid = schemas.StrSchema
            email = schemas.StrSchema
            phone = schemas.StrSchema
            createts = schemas.StrSchema
            templateId = schemas.StrSchema
            recruiterUserId = schemas.StrSchema
            workflowId = schemas.StrSchema
            statusid = schemas.StrSchema
            workflowModel = schemas.StrSchema
            candidateStatusModel = schemas.StrSchema
            assessmentModel = schemas.StrSchema
            workflowName = schemas.StrSchema
            employmentModelList = schemas.StrSchema
            educationModelList = schemas.StrSchema
            customFieldValueModelList = schemas.StrSchema
            addressModelList = schemas.StrSchema
            skillModelList = schemas.StrSchema
            positionName = schemas.StrSchema
        
            @staticmethod
            def candidatePositionsModelList() -> typing.Type['CandidatesGetResponseDataItemCandidatePositionsModelList']:
                return CandidatesGetResponseDataItemCandidatePositionsModelList
            createuserid = schemas.StrSchema
            lastupdateuserid = schemas.StrSchema
            accessCode = schemas.StrSchema
            source = schemas.StrSchema
            passwordHash = schemas.StrSchema
            acceptance1 = schemas.StrSchema
            acceptance2 = schemas.StrSchema
            summaryByCandidate = schemas.StrSchema
            systemReco = schemas.StrSchema
            systemRecoHelp = schemas.StrSchema
            candidateLock = schemas.StrSchema
            salaryCurrencyCode = schemas.StrSchema
            salaryAmount = schemas.StrSchema
            educationStr = schemas.StrSchema
            languagePreference = schemas.StrSchema
            userId = schemas.StrSchema
            verified = schemas.StrSchema
            verificationCode = schemas.StrSchema
            isInternalCand = schemas.StrSchema
            isNewCand = schemas.StrSchema
            timezone = schemas.StrSchema
            trainingAccess = schemas.StrSchema
            customfieldvalue = schemas.StrSchema
            cloudSearchSync = schemas.StrSchema
            jobBoardAccess = schemas.StrSchema
            bgScreeningOrderGuid = schemas.StrSchema
            bgScreeningOrderCreateDate = schemas.StrSchema
            checkrCandidateId = schemas.StrSchema
            positionModel = schemas.StrSchema
            certificationModelList = schemas.StrSchema
            attachmentModelList = schemas.StrSchema
            __annotations__ = {
                "recruitId": recruitId,
                "name": name,
                "referrerId": referrerId,
                "referrer": referrer,
                "recruiter": recruiter,
                "score": score,
                "updatedOn": updatedOn,
                "status": status,
                "notes": notes,
                "dateOfBirth": dateOfBirth,
                "joiningDate": joiningDate,
                "cid": cid,
                "email": email,
                "phone": phone,
                "createts": createts,
                "templateId": templateId,
                "recruiterUserId": recruiterUserId,
                "workflowId": workflowId,
                "statusid": statusid,
                "workflowModel": workflowModel,
                "candidateStatusModel": candidateStatusModel,
                "assessmentModel": assessmentModel,
                "workflowName": workflowName,
                "employmentModelList": employmentModelList,
                "educationModelList": educationModelList,
                "customFieldValueModelList": customFieldValueModelList,
                "addressModelList": addressModelList,
                "skillModelList": skillModelList,
                "positionName": positionName,
                "candidatePositionsModelList": candidatePositionsModelList,
                "createuserid": createuserid,
                "lastupdateuserid": lastupdateuserid,
                "accessCode": accessCode,
                "source": source,
                "passwordHash": passwordHash,
                "acceptance1": acceptance1,
                "acceptance2": acceptance2,
                "summaryByCandidate": summaryByCandidate,
                "systemReco": systemReco,
                "systemRecoHelp": systemRecoHelp,
                "candidateLock": candidateLock,
                "salaryCurrencyCode": salaryCurrencyCode,
                "salaryAmount": salaryAmount,
                "educationStr": educationStr,
                "languagePreference": languagePreference,
                "userId": userId,
                "verified": verified,
                "verificationCode": verificationCode,
                "isInternalCand": isInternalCand,
                "isNewCand": isNewCand,
                "timezone": timezone,
                "trainingAccess": trainingAccess,
                "customfieldvalue": customfieldvalue,
                "cloudSearchSync": cloudSearchSync,
                "jobBoardAccess": jobBoardAccess,
                "bgScreeningOrderGuid": bgScreeningOrderGuid,
                "bgScreeningOrderCreateDate": bgScreeningOrderCreateDate,
                "checkrCandidateId": checkrCandidateId,
                "positionModel": positionModel,
                "certificationModelList": certificationModelList,
                "attachmentModelList": attachmentModelList,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recruitId"]) -> MetaOapg.properties.recruitId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referrerId"]) -> MetaOapg.properties.referrerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referrer"]) -> MetaOapg.properties.referrer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recruiter"]) -> MetaOapg.properties.recruiter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedOn"]) -> MetaOapg.properties.updatedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateOfBirth"]) -> MetaOapg.properties.dateOfBirth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["joiningDate"]) -> MetaOapg.properties.joiningDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createts"]) -> MetaOapg.properties.createts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recruiterUserId"]) -> MetaOapg.properties.recruiterUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowId"]) -> MetaOapg.properties.workflowId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusid"]) -> MetaOapg.properties.statusid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowModel"]) -> MetaOapg.properties.workflowModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidateStatusModel"]) -> MetaOapg.properties.candidateStatusModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assessmentModel"]) -> MetaOapg.properties.assessmentModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowName"]) -> MetaOapg.properties.workflowName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employmentModelList"]) -> MetaOapg.properties.employmentModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["educationModelList"]) -> MetaOapg.properties.educationModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFieldValueModelList"]) -> MetaOapg.properties.customFieldValueModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressModelList"]) -> MetaOapg.properties.addressModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skillModelList"]) -> MetaOapg.properties.skillModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positionName"]) -> MetaOapg.properties.positionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidatePositionsModelList"]) -> 'CandidatesGetResponseDataItemCandidatePositionsModelList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createuserid"]) -> MetaOapg.properties.createuserid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastupdateuserid"]) -> MetaOapg.properties.lastupdateuserid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessCode"]) -> MetaOapg.properties.accessCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["passwordHash"]) -> MetaOapg.properties.passwordHash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acceptance1"]) -> MetaOapg.properties.acceptance1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acceptance2"]) -> MetaOapg.properties.acceptance2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summaryByCandidate"]) -> MetaOapg.properties.summaryByCandidate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["systemReco"]) -> MetaOapg.properties.systemReco: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["systemRecoHelp"]) -> MetaOapg.properties.systemRecoHelp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidateLock"]) -> MetaOapg.properties.candidateLock: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salaryCurrencyCode"]) -> MetaOapg.properties.salaryCurrencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salaryAmount"]) -> MetaOapg.properties.salaryAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["educationStr"]) -> MetaOapg.properties.educationStr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["languagePreference"]) -> MetaOapg.properties.languagePreference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verified"]) -> MetaOapg.properties.verified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verificationCode"]) -> MetaOapg.properties.verificationCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isInternalCand"]) -> MetaOapg.properties.isInternalCand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isNewCand"]) -> MetaOapg.properties.isNewCand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingAccess"]) -> MetaOapg.properties.trainingAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customfieldvalue"]) -> MetaOapg.properties.customfieldvalue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloudSearchSync"]) -> MetaOapg.properties.cloudSearchSync: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobBoardAccess"]) -> MetaOapg.properties.jobBoardAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bgScreeningOrderGuid"]) -> MetaOapg.properties.bgScreeningOrderGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bgScreeningOrderCreateDate"]) -> MetaOapg.properties.bgScreeningOrderCreateDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkrCandidateId"]) -> MetaOapg.properties.checkrCandidateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positionModel"]) -> MetaOapg.properties.positionModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["certificationModelList"]) -> MetaOapg.properties.certificationModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachmentModelList"]) -> MetaOapg.properties.attachmentModelList: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["recruitId", "name", "referrerId", "referrer", "recruiter", "score", "updatedOn", "status", "notes", "dateOfBirth", "joiningDate", "cid", "email", "phone", "createts", "templateId", "recruiterUserId", "workflowId", "statusid", "workflowModel", "candidateStatusModel", "assessmentModel", "workflowName", "employmentModelList", "educationModelList", "customFieldValueModelList", "addressModelList", "skillModelList", "positionName", "candidatePositionsModelList", "createuserid", "lastupdateuserid", "accessCode", "source", "passwordHash", "acceptance1", "acceptance2", "summaryByCandidate", "systemReco", "systemRecoHelp", "candidateLock", "salaryCurrencyCode", "salaryAmount", "educationStr", "languagePreference", "userId", "verified", "verificationCode", "isInternalCand", "isNewCand", "timezone", "trainingAccess", "customfieldvalue", "cloudSearchSync", "jobBoardAccess", "bgScreeningOrderGuid", "bgScreeningOrderCreateDate", "checkrCandidateId", "positionModel", "certificationModelList", "attachmentModelList", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recruitId"]) -> typing.Union[MetaOapg.properties.recruitId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referrerId"]) -> typing.Union[MetaOapg.properties.referrerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referrer"]) -> typing.Union[MetaOapg.properties.referrer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recruiter"]) -> typing.Union[MetaOapg.properties.recruiter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> typing.Union[MetaOapg.properties.score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedOn"]) -> typing.Union[MetaOapg.properties.updatedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateOfBirth"]) -> typing.Union[MetaOapg.properties.dateOfBirth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["joiningDate"]) -> typing.Union[MetaOapg.properties.joiningDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createts"]) -> typing.Union[MetaOapg.properties.createts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateId"]) -> typing.Union[MetaOapg.properties.templateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recruiterUserId"]) -> typing.Union[MetaOapg.properties.recruiterUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowId"]) -> typing.Union[MetaOapg.properties.workflowId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusid"]) -> typing.Union[MetaOapg.properties.statusid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowModel"]) -> typing.Union[MetaOapg.properties.workflowModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidateStatusModel"]) -> typing.Union[MetaOapg.properties.candidateStatusModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assessmentModel"]) -> typing.Union[MetaOapg.properties.assessmentModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowName"]) -> typing.Union[MetaOapg.properties.workflowName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employmentModelList"]) -> typing.Union[MetaOapg.properties.employmentModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["educationModelList"]) -> typing.Union[MetaOapg.properties.educationModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFieldValueModelList"]) -> typing.Union[MetaOapg.properties.customFieldValueModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressModelList"]) -> typing.Union[MetaOapg.properties.addressModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skillModelList"]) -> typing.Union[MetaOapg.properties.skillModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positionName"]) -> typing.Union[MetaOapg.properties.positionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidatePositionsModelList"]) -> typing.Union['CandidatesGetResponseDataItemCandidatePositionsModelList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createuserid"]) -> typing.Union[MetaOapg.properties.createuserid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastupdateuserid"]) -> typing.Union[MetaOapg.properties.lastupdateuserid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessCode"]) -> typing.Union[MetaOapg.properties.accessCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["passwordHash"]) -> typing.Union[MetaOapg.properties.passwordHash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acceptance1"]) -> typing.Union[MetaOapg.properties.acceptance1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acceptance2"]) -> typing.Union[MetaOapg.properties.acceptance2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summaryByCandidate"]) -> typing.Union[MetaOapg.properties.summaryByCandidate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["systemReco"]) -> typing.Union[MetaOapg.properties.systemReco, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["systemRecoHelp"]) -> typing.Union[MetaOapg.properties.systemRecoHelp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidateLock"]) -> typing.Union[MetaOapg.properties.candidateLock, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salaryCurrencyCode"]) -> typing.Union[MetaOapg.properties.salaryCurrencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salaryAmount"]) -> typing.Union[MetaOapg.properties.salaryAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["educationStr"]) -> typing.Union[MetaOapg.properties.educationStr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["languagePreference"]) -> typing.Union[MetaOapg.properties.languagePreference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verified"]) -> typing.Union[MetaOapg.properties.verified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verificationCode"]) -> typing.Union[MetaOapg.properties.verificationCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isInternalCand"]) -> typing.Union[MetaOapg.properties.isInternalCand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isNewCand"]) -> typing.Union[MetaOapg.properties.isNewCand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingAccess"]) -> typing.Union[MetaOapg.properties.trainingAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customfieldvalue"]) -> typing.Union[MetaOapg.properties.customfieldvalue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloudSearchSync"]) -> typing.Union[MetaOapg.properties.cloudSearchSync, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobBoardAccess"]) -> typing.Union[MetaOapg.properties.jobBoardAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bgScreeningOrderGuid"]) -> typing.Union[MetaOapg.properties.bgScreeningOrderGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bgScreeningOrderCreateDate"]) -> typing.Union[MetaOapg.properties.bgScreeningOrderCreateDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkrCandidateId"]) -> typing.Union[MetaOapg.properties.checkrCandidateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positionModel"]) -> typing.Union[MetaOapg.properties.positionModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["certificationModelList"]) -> typing.Union[MetaOapg.properties.certificationModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachmentModelList"]) -> typing.Union[MetaOapg.properties.attachmentModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["recruitId", "name", "referrerId", "referrer", "recruiter", "score", "updatedOn", "status", "notes", "dateOfBirth", "joiningDate", "cid", "email", "phone", "createts", "templateId", "recruiterUserId", "workflowId", "statusid", "workflowModel", "candidateStatusModel", "assessmentModel", "workflowName", "employmentModelList", "educationModelList", "customFieldValueModelList", "addressModelList", "skillModelList", "positionName", "candidatePositionsModelList", "createuserid", "lastupdateuserid", "accessCode", "source", "passwordHash", "acceptance1", "acceptance2", "summaryByCandidate", "systemReco", "systemRecoHelp", "candidateLock", "salaryCurrencyCode", "salaryAmount", "educationStr", "languagePreference", "userId", "verified", "verificationCode", "isInternalCand", "isNewCand", "timezone", "trainingAccess", "customfieldvalue", "cloudSearchSync", "jobBoardAccess", "bgScreeningOrderGuid", "bgScreeningOrderCreateDate", "checkrCandidateId", "positionModel", "certificationModelList", "attachmentModelList", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        recruitId: typing.Union[MetaOapg.properties.recruitId, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        referrerId: typing.Union[MetaOapg.properties.referrerId, str, schemas.Unset] = schemas.unset,
        referrer: typing.Union[MetaOapg.properties.referrer, str, schemas.Unset] = schemas.unset,
        recruiter: typing.Union[MetaOapg.properties.recruiter, str, schemas.Unset] = schemas.unset,
        score: typing.Union[MetaOapg.properties.score, str, schemas.Unset] = schemas.unset,
        updatedOn: typing.Union[MetaOapg.properties.updatedOn, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        dateOfBirth: typing.Union[MetaOapg.properties.dateOfBirth, str, schemas.Unset] = schemas.unset,
        joiningDate: typing.Union[MetaOapg.properties.joiningDate, str, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        createts: typing.Union[MetaOapg.properties.createts, str, schemas.Unset] = schemas.unset,
        templateId: typing.Union[MetaOapg.properties.templateId, str, schemas.Unset] = schemas.unset,
        recruiterUserId: typing.Union[MetaOapg.properties.recruiterUserId, str, schemas.Unset] = schemas.unset,
        workflowId: typing.Union[MetaOapg.properties.workflowId, str, schemas.Unset] = schemas.unset,
        statusid: typing.Union[MetaOapg.properties.statusid, str, schemas.Unset] = schemas.unset,
        workflowModel: typing.Union[MetaOapg.properties.workflowModel, str, schemas.Unset] = schemas.unset,
        candidateStatusModel: typing.Union[MetaOapg.properties.candidateStatusModel, str, schemas.Unset] = schemas.unset,
        assessmentModel: typing.Union[MetaOapg.properties.assessmentModel, str, schemas.Unset] = schemas.unset,
        workflowName: typing.Union[MetaOapg.properties.workflowName, str, schemas.Unset] = schemas.unset,
        employmentModelList: typing.Union[MetaOapg.properties.employmentModelList, str, schemas.Unset] = schemas.unset,
        educationModelList: typing.Union[MetaOapg.properties.educationModelList, str, schemas.Unset] = schemas.unset,
        customFieldValueModelList: typing.Union[MetaOapg.properties.customFieldValueModelList, str, schemas.Unset] = schemas.unset,
        addressModelList: typing.Union[MetaOapg.properties.addressModelList, str, schemas.Unset] = schemas.unset,
        skillModelList: typing.Union[MetaOapg.properties.skillModelList, str, schemas.Unset] = schemas.unset,
        positionName: typing.Union[MetaOapg.properties.positionName, str, schemas.Unset] = schemas.unset,
        candidatePositionsModelList: typing.Union['CandidatesGetResponseDataItemCandidatePositionsModelList', schemas.Unset] = schemas.unset,
        createuserid: typing.Union[MetaOapg.properties.createuserid, str, schemas.Unset] = schemas.unset,
        lastupdateuserid: typing.Union[MetaOapg.properties.lastupdateuserid, str, schemas.Unset] = schemas.unset,
        accessCode: typing.Union[MetaOapg.properties.accessCode, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        passwordHash: typing.Union[MetaOapg.properties.passwordHash, str, schemas.Unset] = schemas.unset,
        acceptance1: typing.Union[MetaOapg.properties.acceptance1, str, schemas.Unset] = schemas.unset,
        acceptance2: typing.Union[MetaOapg.properties.acceptance2, str, schemas.Unset] = schemas.unset,
        summaryByCandidate: typing.Union[MetaOapg.properties.summaryByCandidate, str, schemas.Unset] = schemas.unset,
        systemReco: typing.Union[MetaOapg.properties.systemReco, str, schemas.Unset] = schemas.unset,
        systemRecoHelp: typing.Union[MetaOapg.properties.systemRecoHelp, str, schemas.Unset] = schemas.unset,
        candidateLock: typing.Union[MetaOapg.properties.candidateLock, str, schemas.Unset] = schemas.unset,
        salaryCurrencyCode: typing.Union[MetaOapg.properties.salaryCurrencyCode, str, schemas.Unset] = schemas.unset,
        salaryAmount: typing.Union[MetaOapg.properties.salaryAmount, str, schemas.Unset] = schemas.unset,
        educationStr: typing.Union[MetaOapg.properties.educationStr, str, schemas.Unset] = schemas.unset,
        languagePreference: typing.Union[MetaOapg.properties.languagePreference, str, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        verified: typing.Union[MetaOapg.properties.verified, str, schemas.Unset] = schemas.unset,
        verificationCode: typing.Union[MetaOapg.properties.verificationCode, str, schemas.Unset] = schemas.unset,
        isInternalCand: typing.Union[MetaOapg.properties.isInternalCand, str, schemas.Unset] = schemas.unset,
        isNewCand: typing.Union[MetaOapg.properties.isNewCand, str, schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        trainingAccess: typing.Union[MetaOapg.properties.trainingAccess, str, schemas.Unset] = schemas.unset,
        customfieldvalue: typing.Union[MetaOapg.properties.customfieldvalue, str, schemas.Unset] = schemas.unset,
        cloudSearchSync: typing.Union[MetaOapg.properties.cloudSearchSync, str, schemas.Unset] = schemas.unset,
        jobBoardAccess: typing.Union[MetaOapg.properties.jobBoardAccess, str, schemas.Unset] = schemas.unset,
        bgScreeningOrderGuid: typing.Union[MetaOapg.properties.bgScreeningOrderGuid, str, schemas.Unset] = schemas.unset,
        bgScreeningOrderCreateDate: typing.Union[MetaOapg.properties.bgScreeningOrderCreateDate, str, schemas.Unset] = schemas.unset,
        checkrCandidateId: typing.Union[MetaOapg.properties.checkrCandidateId, str, schemas.Unset] = schemas.unset,
        positionModel: typing.Union[MetaOapg.properties.positionModel, str, schemas.Unset] = schemas.unset,
        certificationModelList: typing.Union[MetaOapg.properties.certificationModelList, str, schemas.Unset] = schemas.unset,
        attachmentModelList: typing.Union[MetaOapg.properties.attachmentModelList, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CandidatesGetResponseDataItem':
        return super().__new__(
            cls,
            *args,
            recruitId=recruitId,
            name=name,
            referrerId=referrerId,
            referrer=referrer,
            recruiter=recruiter,
            score=score,
            updatedOn=updatedOn,
            status=status,
            notes=notes,
            dateOfBirth=dateOfBirth,
            joiningDate=joiningDate,
            cid=cid,
            email=email,
            phone=phone,
            createts=createts,
            templateId=templateId,
            recruiterUserId=recruiterUserId,
            workflowId=workflowId,
            statusid=statusid,
            workflowModel=workflowModel,
            candidateStatusModel=candidateStatusModel,
            assessmentModel=assessmentModel,
            workflowName=workflowName,
            employmentModelList=employmentModelList,
            educationModelList=educationModelList,
            customFieldValueModelList=customFieldValueModelList,
            addressModelList=addressModelList,
            skillModelList=skillModelList,
            positionName=positionName,
            candidatePositionsModelList=candidatePositionsModelList,
            createuserid=createuserid,
            lastupdateuserid=lastupdateuserid,
            accessCode=accessCode,
            source=source,
            passwordHash=passwordHash,
            acceptance1=acceptance1,
            acceptance2=acceptance2,
            summaryByCandidate=summaryByCandidate,
            systemReco=systemReco,
            systemRecoHelp=systemRecoHelp,
            candidateLock=candidateLock,
            salaryCurrencyCode=salaryCurrencyCode,
            salaryAmount=salaryAmount,
            educationStr=educationStr,
            languagePreference=languagePreference,
            userId=userId,
            verified=verified,
            verificationCode=verificationCode,
            isInternalCand=isInternalCand,
            isNewCand=isNewCand,
            timezone=timezone,
            trainingAccess=trainingAccess,
            customfieldvalue=customfieldvalue,
            cloudSearchSync=cloudSearchSync,
            jobBoardAccess=jobBoardAccess,
            bgScreeningOrderGuid=bgScreeningOrderGuid,
            bgScreeningOrderCreateDate=bgScreeningOrderCreateDate,
            checkrCandidateId=checkrCandidateId,
            positionModel=positionModel,
            certificationModelList=certificationModelList,
            attachmentModelList=attachmentModelList,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.candidates_get_response_data_item_candidate_positions_model_list import CandidatesGetResponseDataItemCandidatePositionsModelList
