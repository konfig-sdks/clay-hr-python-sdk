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


class CustomTableModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            candidateAccess = schemas.StrSchema
            cid = schemas.Int32Schema
        
            @staticmethod
            def createUserModel() -> typing.Type['UserModel']:
                return UserModel
        
            @staticmethod
            def createts() -> typing.Type['Timestamp']:
                return Timestamp
            
            
            class ctColumnList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CustomTableColumnModel']:
                        return CustomTableColumnModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CustomTableColumnModel'], typing.List['CustomTableColumnModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ctColumnList':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CustomTableColumnModel':
                    return super().__getitem__(i)
            
            
            class ctValueList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CustomTableValueModel']:
                        return CustomTableValueModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CustomTableValueModel'], typing.List['CustomTableValueModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ctValueList':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CustomTableValueModel':
                    return super().__getitem__(i)
            customTableId = schemas.Int32Schema
            helpText = schemas.StrSchema
            objectType = schemas.StrSchema
            readAccess = schemas.StrSchema
            readUserGroupId = schemas.Int32Schema
        
            @staticmethod
            def readUserGroupModel() -> typing.Type['UserGroupModel']:
                return UserGroupModel
            sequence = schemas.Int32Schema
            tableName = schemas.StrSchema
            userAccess = schemas.StrSchema
            writeAccess = schemas.StrSchema
            writeUserGroupId = schemas.Int32Schema
        
            @staticmethod
            def writeUserGroupModel() -> typing.Type['UserGroupModel']:
                return UserGroupModel
            __annotations__ = {
                "candidateAccess": candidateAccess,
                "cid": cid,
                "createUserModel": createUserModel,
                "createts": createts,
                "ctColumnList": ctColumnList,
                "ctValueList": ctValueList,
                "customTableId": customTableId,
                "helpText": helpText,
                "objectType": objectType,
                "readAccess": readAccess,
                "readUserGroupId": readUserGroupId,
                "readUserGroupModel": readUserGroupModel,
                "sequence": sequence,
                "tableName": tableName,
                "userAccess": userAccess,
                "writeAccess": writeAccess,
                "writeUserGroupId": writeUserGroupId,
                "writeUserGroupModel": writeUserGroupModel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["candidateAccess"]) -> MetaOapg.properties.candidateAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createUserModel"]) -> 'UserModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createts"]) -> 'Timestamp': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ctColumnList"]) -> MetaOapg.properties.ctColumnList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ctValueList"]) -> MetaOapg.properties.ctValueList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customTableId"]) -> MetaOapg.properties.customTableId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["helpText"]) -> MetaOapg.properties.helpText: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectType"]) -> MetaOapg.properties.objectType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readAccess"]) -> MetaOapg.properties.readAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readUserGroupId"]) -> MetaOapg.properties.readUserGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readUserGroupModel"]) -> 'UserGroupModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence"]) -> MetaOapg.properties.sequence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tableName"]) -> MetaOapg.properties.tableName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userAccess"]) -> MetaOapg.properties.userAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["writeAccess"]) -> MetaOapg.properties.writeAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["writeUserGroupId"]) -> MetaOapg.properties.writeUserGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["writeUserGroupModel"]) -> 'UserGroupModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["candidateAccess", "cid", "createUserModel", "createts", "ctColumnList", "ctValueList", "customTableId", "helpText", "objectType", "readAccess", "readUserGroupId", "readUserGroupModel", "sequence", "tableName", "userAccess", "writeAccess", "writeUserGroupId", "writeUserGroupModel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["candidateAccess"]) -> typing.Union[MetaOapg.properties.candidateAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createUserModel"]) -> typing.Union['UserModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createts"]) -> typing.Union['Timestamp', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ctColumnList"]) -> typing.Union[MetaOapg.properties.ctColumnList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ctValueList"]) -> typing.Union[MetaOapg.properties.ctValueList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customTableId"]) -> typing.Union[MetaOapg.properties.customTableId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["helpText"]) -> typing.Union[MetaOapg.properties.helpText, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectType"]) -> typing.Union[MetaOapg.properties.objectType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readAccess"]) -> typing.Union[MetaOapg.properties.readAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readUserGroupId"]) -> typing.Union[MetaOapg.properties.readUserGroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readUserGroupModel"]) -> typing.Union['UserGroupModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence"]) -> typing.Union[MetaOapg.properties.sequence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tableName"]) -> typing.Union[MetaOapg.properties.tableName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userAccess"]) -> typing.Union[MetaOapg.properties.userAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["writeAccess"]) -> typing.Union[MetaOapg.properties.writeAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["writeUserGroupId"]) -> typing.Union[MetaOapg.properties.writeUserGroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["writeUserGroupModel"]) -> typing.Union['UserGroupModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["candidateAccess", "cid", "createUserModel", "createts", "ctColumnList", "ctValueList", "customTableId", "helpText", "objectType", "readAccess", "readUserGroupId", "readUserGroupModel", "sequence", "tableName", "userAccess", "writeAccess", "writeUserGroupId", "writeUserGroupModel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        candidateAccess: typing.Union[MetaOapg.properties.candidateAccess, str, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createUserModel: typing.Union['UserModel', schemas.Unset] = schemas.unset,
        createts: typing.Union['Timestamp', schemas.Unset] = schemas.unset,
        ctColumnList: typing.Union[MetaOapg.properties.ctColumnList, list, tuple, schemas.Unset] = schemas.unset,
        ctValueList: typing.Union[MetaOapg.properties.ctValueList, list, tuple, schemas.Unset] = schemas.unset,
        customTableId: typing.Union[MetaOapg.properties.customTableId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        helpText: typing.Union[MetaOapg.properties.helpText, str, schemas.Unset] = schemas.unset,
        objectType: typing.Union[MetaOapg.properties.objectType, str, schemas.Unset] = schemas.unset,
        readAccess: typing.Union[MetaOapg.properties.readAccess, str, schemas.Unset] = schemas.unset,
        readUserGroupId: typing.Union[MetaOapg.properties.readUserGroupId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        readUserGroupModel: typing.Union['UserGroupModel', schemas.Unset] = schemas.unset,
        sequence: typing.Union[MetaOapg.properties.sequence, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tableName: typing.Union[MetaOapg.properties.tableName, str, schemas.Unset] = schemas.unset,
        userAccess: typing.Union[MetaOapg.properties.userAccess, str, schemas.Unset] = schemas.unset,
        writeAccess: typing.Union[MetaOapg.properties.writeAccess, str, schemas.Unset] = schemas.unset,
        writeUserGroupId: typing.Union[MetaOapg.properties.writeUserGroupId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        writeUserGroupModel: typing.Union['UserGroupModel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomTableModel':
        return super().__new__(
            cls,
            *args,
            candidateAccess=candidateAccess,
            cid=cid,
            createUserModel=createUserModel,
            createts=createts,
            ctColumnList=ctColumnList,
            ctValueList=ctValueList,
            customTableId=customTableId,
            helpText=helpText,
            objectType=objectType,
            readAccess=readAccess,
            readUserGroupId=readUserGroupId,
            readUserGroupModel=readUserGroupModel,
            sequence=sequence,
            tableName=tableName,
            userAccess=userAccess,
            writeAccess=writeAccess,
            writeUserGroupId=writeUserGroupId,
            writeUserGroupModel=writeUserGroupModel,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.custom_table_column_model import CustomTableColumnModel
from clay_hr_python_sdk.model.custom_table_value_model import CustomTableValueModel
from clay_hr_python_sdk.model.timestamp import Timestamp
from clay_hr_python_sdk.model.user_group_model import UserGroupModel
from clay_hr_python_sdk.model.user_model import UserModel
