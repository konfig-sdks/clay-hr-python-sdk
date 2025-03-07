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


class PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactListItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            lastName = schemas.StrSchema
            
            
            class relationToUser(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SPOUSE(cls):
                    return cls("Spouse")
                
                @schemas.classproperty
                def PARENT(cls):
                    return cls("Parent")
                
                @schemas.classproperty
                def CHILD(cls):
                    return cls("Child")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
            
            
            class contactType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DEP(cls):
                    return cls("DEP")
                
                @schemas.classproperty
                def ECON(cls):
                    return cls("ECON")
                
                @schemas.classproperty
                def ACCT(cls):
                    return cls("ACCT")
            
            
            class gender(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def M(cls):
                    return cls("M")
                
                @schemas.classproperty
                def F(cls):
                    return cls("F")
                
                @schemas.classproperty
                def H(cls):
                    return cls("H")
            taxNumber = schemas.StrSchema
            dateOfBirth = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AP(cls):
                    return cls("AP")
                
                @schemas.classproperty
                def WA(cls):
                    return cls("WA")
            extAppUID = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "lastName": lastName,
                "relationToUser": relationToUser,
                "contactType": contactType,
                "gender": gender,
                "taxNumber": taxNumber,
                "dateOfBirth": dateOfBirth,
                "status": status,
                "extAppUID": extAppUID,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationToUser"]) -> MetaOapg.properties.relationToUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactType"]) -> MetaOapg.properties.contactType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxNumber"]) -> MetaOapg.properties.taxNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateOfBirth"]) -> MetaOapg.properties.dateOfBirth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extAppUID"]) -> MetaOapg.properties.extAppUID: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "lastName", "relationToUser", "contactType", "gender", "taxNumber", "dateOfBirth", "status", "extAppUID", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationToUser"]) -> typing.Union[MetaOapg.properties.relationToUser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactType"]) -> typing.Union[MetaOapg.properties.contactType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxNumber"]) -> typing.Union[MetaOapg.properties.taxNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateOfBirth"]) -> typing.Union[MetaOapg.properties.dateOfBirth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extAppUID"]) -> typing.Union[MetaOapg.properties.extAppUID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "lastName", "relationToUser", "contactType", "gender", "taxNumber", "dateOfBirth", "status", "extAppUID", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        relationToUser: typing.Union[MetaOapg.properties.relationToUser, str, schemas.Unset] = schemas.unset,
        contactType: typing.Union[MetaOapg.properties.contactType, str, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        taxNumber: typing.Union[MetaOapg.properties.taxNumber, str, schemas.Unset] = schemas.unset,
        dateOfBirth: typing.Union[MetaOapg.properties.dateOfBirth, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        extAppUID: typing.Union[MetaOapg.properties.extAppUID, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactListItem':
        return super().__new__(
            cls,
            *args,
            name=name,
            lastName=lastName,
            relationToUser=relationToUser,
            contactType=contactType,
            gender=gender,
            taxNumber=taxNumber,
            dateOfBirth=dateOfBirth,
            status=status,
            extAppUID=extAppUID,
            _configuration=_configuration,
            **kwargs,
        )
