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


class CustomFieldsGetCustomListsResponseItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            listId = schemas.StrSchema
        
            @staticmethod
            def customListEntryModel() -> typing.Type['CustomFieldsGetCustomListsResponseItemCustomListEntryModel']:
                return CustomFieldsGetCustomListsResponseItemCustomListEntryModel
            listName = schemas.StrSchema
            cid = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "listId": listId,
                "customListEntryModel": customListEntryModel,
                "listName": listName,
                "cid": cid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["listId"]) -> MetaOapg.properties.listId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customListEntryModel"]) -> 'CustomFieldsGetCustomListsResponseItemCustomListEntryModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["listName"]) -> MetaOapg.properties.listName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "listId", "customListEntryModel", "listName", "cid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["listId"]) -> typing.Union[MetaOapg.properties.listId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customListEntryModel"]) -> typing.Union['CustomFieldsGetCustomListsResponseItemCustomListEntryModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["listName"]) -> typing.Union[MetaOapg.properties.listName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "listId", "customListEntryModel", "listName", "cid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        listId: typing.Union[MetaOapg.properties.listId, str, schemas.Unset] = schemas.unset,
        customListEntryModel: typing.Union['CustomFieldsGetCustomListsResponseItemCustomListEntryModel', schemas.Unset] = schemas.unset,
        listName: typing.Union[MetaOapg.properties.listName, str, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldsGetCustomListsResponseItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            listId=listId,
            customListEntryModel=customListEntryModel,
            listName=listName,
            cid=cid,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.custom_fields_get_custom_lists_response_item_custom_list_entry_model import CustomFieldsGetCustomListsResponseItemCustomListEntryModel
