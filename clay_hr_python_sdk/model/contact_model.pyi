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


class ContactModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class addressModelList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AddressModel']:
                        return AddressModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AddressModel'], typing.List['AddressModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addressModelList':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AddressModel':
                    return super().__getitem__(i)
            candidateId = schemas.Int32Schema
            cid = schemas.Int32Schema
            contactType = schemas.StrSchema
            contactid = schemas.Int32Schema
            createuserid = schemas.Int32Schema
            dateOfBirth = schemas.DateSchema
            email1 = schemas.StrSchema
            gender = schemas.StrSchema
            lastName = schemas.StrSchema
            name = schemas.StrSchema
            notes = schemas.StrSchema
            otherRelationToUser = schemas.StrSchema
            phone1 = schemas.StrSchema
            phone1type = schemas.StrSchema
            phone2 = schemas.StrSchema
            phone2type = schemas.StrSchema
            phone3 = schemas.StrSchema
            phone3type = schemas.StrSchema
            relationToUser = schemas.StrSchema
            status = schemas.StrSchema
            taxNumber = schemas.StrSchema
            userId = schemas.Int32Schema
            __annotations__ = {
                "addressModelList": addressModelList,
                "candidateId": candidateId,
                "cid": cid,
                "contactType": contactType,
                "contactid": contactid,
                "createuserid": createuserid,
                "dateOfBirth": dateOfBirth,
                "email1": email1,
                "gender": gender,
                "lastName": lastName,
                "name": name,
                "notes": notes,
                "otherRelationToUser": otherRelationToUser,
                "phone1": phone1,
                "phone1type": phone1type,
                "phone2": phone2,
                "phone2type": phone2type,
                "phone3": phone3,
                "phone3type": phone3type,
                "relationToUser": relationToUser,
                "status": status,
                "taxNumber": taxNumber,
                "userId": userId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressModelList"]) -> MetaOapg.properties.addressModelList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidateId"]) -> MetaOapg.properties.candidateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactType"]) -> MetaOapg.properties.contactType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactid"]) -> MetaOapg.properties.contactid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createuserid"]) -> MetaOapg.properties.createuserid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateOfBirth"]) -> MetaOapg.properties.dateOfBirth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email1"]) -> MetaOapg.properties.email1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherRelationToUser"]) -> MetaOapg.properties.otherRelationToUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone1"]) -> MetaOapg.properties.phone1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone1type"]) -> MetaOapg.properties.phone1type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone2"]) -> MetaOapg.properties.phone2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone2type"]) -> MetaOapg.properties.phone2type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone3"]) -> MetaOapg.properties.phone3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone3type"]) -> MetaOapg.properties.phone3type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationToUser"]) -> MetaOapg.properties.relationToUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxNumber"]) -> MetaOapg.properties.taxNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["addressModelList", "candidateId", "cid", "contactType", "contactid", "createuserid", "dateOfBirth", "email1", "gender", "lastName", "name", "notes", "otherRelationToUser", "phone1", "phone1type", "phone2", "phone2type", "phone3", "phone3type", "relationToUser", "status", "taxNumber", "userId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressModelList"]) -> typing.Union[MetaOapg.properties.addressModelList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidateId"]) -> typing.Union[MetaOapg.properties.candidateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactType"]) -> typing.Union[MetaOapg.properties.contactType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactid"]) -> typing.Union[MetaOapg.properties.contactid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createuserid"]) -> typing.Union[MetaOapg.properties.createuserid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateOfBirth"]) -> typing.Union[MetaOapg.properties.dateOfBirth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email1"]) -> typing.Union[MetaOapg.properties.email1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherRelationToUser"]) -> typing.Union[MetaOapg.properties.otherRelationToUser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone1"]) -> typing.Union[MetaOapg.properties.phone1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone1type"]) -> typing.Union[MetaOapg.properties.phone1type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone2"]) -> typing.Union[MetaOapg.properties.phone2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone2type"]) -> typing.Union[MetaOapg.properties.phone2type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone3"]) -> typing.Union[MetaOapg.properties.phone3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone3type"]) -> typing.Union[MetaOapg.properties.phone3type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationToUser"]) -> typing.Union[MetaOapg.properties.relationToUser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxNumber"]) -> typing.Union[MetaOapg.properties.taxNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addressModelList", "candidateId", "cid", "contactType", "contactid", "createuserid", "dateOfBirth", "email1", "gender", "lastName", "name", "notes", "otherRelationToUser", "phone1", "phone1type", "phone2", "phone2type", "phone3", "phone3type", "relationToUser", "status", "taxNumber", "userId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        addressModelList: typing.Union[MetaOapg.properties.addressModelList, list, tuple, schemas.Unset] = schemas.unset,
        candidateId: typing.Union[MetaOapg.properties.candidateId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contactType: typing.Union[MetaOapg.properties.contactType, str, schemas.Unset] = schemas.unset,
        contactid: typing.Union[MetaOapg.properties.contactid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createuserid: typing.Union[MetaOapg.properties.createuserid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dateOfBirth: typing.Union[MetaOapg.properties.dateOfBirth, str, date, schemas.Unset] = schemas.unset,
        email1: typing.Union[MetaOapg.properties.email1, str, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        otherRelationToUser: typing.Union[MetaOapg.properties.otherRelationToUser, str, schemas.Unset] = schemas.unset,
        phone1: typing.Union[MetaOapg.properties.phone1, str, schemas.Unset] = schemas.unset,
        phone1type: typing.Union[MetaOapg.properties.phone1type, str, schemas.Unset] = schemas.unset,
        phone2: typing.Union[MetaOapg.properties.phone2, str, schemas.Unset] = schemas.unset,
        phone2type: typing.Union[MetaOapg.properties.phone2type, str, schemas.Unset] = schemas.unset,
        phone3: typing.Union[MetaOapg.properties.phone3, str, schemas.Unset] = schemas.unset,
        phone3type: typing.Union[MetaOapg.properties.phone3type, str, schemas.Unset] = schemas.unset,
        relationToUser: typing.Union[MetaOapg.properties.relationToUser, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        taxNumber: typing.Union[MetaOapg.properties.taxNumber, str, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContactModel':
        return super().__new__(
            cls,
            *args,
            addressModelList=addressModelList,
            candidateId=candidateId,
            cid=cid,
            contactType=contactType,
            contactid=contactid,
            createuserid=createuserid,
            dateOfBirth=dateOfBirth,
            email1=email1,
            gender=gender,
            lastName=lastName,
            name=name,
            notes=notes,
            otherRelationToUser=otherRelationToUser,
            phone1=phone1,
            phone1type=phone1type,
            phone2=phone2,
            phone2type=phone2type,
            phone3=phone3,
            phone3type=phone3type,
            relationToUser=relationToUser,
            status=status,
            taxNumber=taxNumber,
            userId=userId,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.address_model import AddressModel
