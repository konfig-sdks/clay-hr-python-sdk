# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.api_announcement_create.post import CreateNewAnnouncement
from clay_hr_python_sdk.paths.api_attachment_list_ann_id.get import GetAttachmentsById
from clay_hr_python_sdk.paths.api_announcement_ann_id.get import GetById
from clay_hr_python_sdk.paths.api_announcement_edit.put import UpdateAnnouncement
from clay_hr_python_sdk.apis.tags.announcement_api_raw import AnnouncementApiRaw


class AnnouncementApi(
    CreateNewAnnouncement,
    GetAttachmentsById,
    GetById,
    UpdateAnnouncement,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AnnouncementApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AnnouncementApiRaw(api_client)
