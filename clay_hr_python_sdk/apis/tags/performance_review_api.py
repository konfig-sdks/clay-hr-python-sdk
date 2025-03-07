# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.appraisal_add.post import CreatePerformanceReview
from clay_hr_python_sdk.paths.appraisal_get_completed_reviews.get import GetCompletedReviewsBasedOnUserId
from clay_hr_python_sdk.paths.appraisal_user.get import GetPerformanceReviews
from clay_hr_python_sdk.paths.appraisal_template_list.get import GetTemplates
from clay_hr_python_sdk.paths.appraisal_bulk_launch.post import LaunchPerformanceReviewsInBulk
from clay_hr_python_sdk.apis.tags.performance_review_api_raw import PerformanceReviewApiRaw


class PerformanceReviewApi(
    CreatePerformanceReview,
    GetCompletedReviewsBasedOnUserId,
    GetPerformanceReviews,
    GetTemplates,
    LaunchPerformanceReviewsInBulk,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PerformanceReviewApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PerformanceReviewApiRaw(api_client)
