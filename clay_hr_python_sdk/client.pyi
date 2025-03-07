# coding: utf-8
"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from clay_hr_python_sdk.client_custom import ClientCustom
from clay_hr_python_sdk.configuration import Configuration
from clay_hr_python_sdk.api_client import ApiClient
from clay_hr_python_sdk.type_util import copy_signature
from clay_hr_python_sdk.apis.tags.announcement_api import AnnouncementApi
from clay_hr_python_sdk.apis.tags.authentication_api import AuthenticationApi
from clay_hr_python_sdk.apis.tags.candidates_api import CandidatesApi
from clay_hr_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from clay_hr_python_sdk.apis.tags.dependents_api import DependentsApi
from clay_hr_python_sdk.apis.tags.document_library_api import DocumentLibraryApi
from clay_hr_python_sdk.apis.tags.expense_reports_api import ExpenseReportsApi
from clay_hr_python_sdk.apis.tags.feedback_api import FeedbackApi
from clay_hr_python_sdk.apis.tags.forms_api import FormsApi
from clay_hr_python_sdk.apis.tags.goals_api import GoalsApi
from clay_hr_python_sdk.apis.tags.invoice_api import InvoiceApi
from clay_hr_python_sdk.apis.tags.job_profiles_api import JobProfilesApi
from clay_hr_python_sdk.apis.tags.leaves_api import LeavesApi
from clay_hr_python_sdk.apis.tags.objective_api import ObjectiveApi
from clay_hr_python_sdk.apis.tags.org_units_api import OrgUnitsApi
from clay_hr_python_sdk.apis.tags.org_relation_api import OrgRelationApi
from clay_hr_python_sdk.apis.tags.pay_stubs_api import PayStubsApi
from clay_hr_python_sdk.apis.tags.people_and_permissions_api import PeopleAndPermissionsApi
from clay_hr_python_sdk.apis.tags.performance_review_api import PerformanceReviewApi
from clay_hr_python_sdk.apis.tags.performance_review_assignment_api import PerformanceReviewAssignmentApi
from clay_hr_python_sdk.apis.tags.positions_api import PositionsApi
from clay_hr_python_sdk.apis.tags.project_api import ProjectApi
from clay_hr_python_sdk.apis.tags.reports_api import ReportsApi
from clay_hr_python_sdk.apis.tags.shifts_api import ShiftsApi
from clay_hr_python_sdk.apis.tags.skills_api import SkillsApi
from clay_hr_python_sdk.apis.tags.survey_api import SurveyApi
from clay_hr_python_sdk.apis.tags.test_api import TestApi
from clay_hr_python_sdk.apis.tags.timecards_api import TimecardsApi
from clay_hr_python_sdk.apis.tags.timesheets_api import TimesheetsApi
from clay_hr_python_sdk.apis.tags.trainings_api import TrainingsApi
from clay_hr_python_sdk.apis.tags.user_pto_policies_api import UserPTOPoliciesApi
from clay_hr_python_sdk.apis.tags.user_workflow_api import UserWorkflowApi
from clay_hr_python_sdk.apis.tags.workflows_api import WorkflowsApi



class ClayHr(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.announcement: AnnouncementApi = AnnouncementApi(api_client)
        self.authentication: AuthenticationApi = AuthenticationApi(api_client)
        self.candidates: CandidatesApi = CandidatesApi(api_client)
        self.custom_fields: CustomFieldsApi = CustomFieldsApi(api_client)
        self.dependents: DependentsApi = DependentsApi(api_client)
        self.document_library: DocumentLibraryApi = DocumentLibraryApi(api_client)
        self.expense_reports: ExpenseReportsApi = ExpenseReportsApi(api_client)
        self.feedback: FeedbackApi = FeedbackApi(api_client)
        self.forms: FormsApi = FormsApi(api_client)
        self.goals: GoalsApi = GoalsApi(api_client)
        self.invoice: InvoiceApi = InvoiceApi(api_client)
        self.job_profiles: JobProfilesApi = JobProfilesApi(api_client)
        self.leaves: LeavesApi = LeavesApi(api_client)
        self.objective: ObjectiveApi = ObjectiveApi(api_client)
        self.org_units: OrgUnitsApi = OrgUnitsApi(api_client)
        self.org_relation: OrgRelationApi = OrgRelationApi(api_client)
        self.pay_stubs: PayStubsApi = PayStubsApi(api_client)
        self.people_and_permissions: PeopleAndPermissionsApi = PeopleAndPermissionsApi(api_client)
        self.performance_review: PerformanceReviewApi = PerformanceReviewApi(api_client)
        self.performance_review_assignment: PerformanceReviewAssignmentApi = PerformanceReviewAssignmentApi(api_client)
        self.positions: PositionsApi = PositionsApi(api_client)
        self.project: ProjectApi = ProjectApi(api_client)
        self.reports: ReportsApi = ReportsApi(api_client)
        self.shifts: ShiftsApi = ShiftsApi(api_client)
        self.skills: SkillsApi = SkillsApi(api_client)
        self.survey: SurveyApi = SurveyApi(api_client)
        self.test: TestApi = TestApi(api_client)
        self.timecards: TimecardsApi = TimecardsApi(api_client)
        self.timesheets: TimesheetsApi = TimesheetsApi(api_client)
        self.trainings: TrainingsApi = TrainingsApi(api_client)
        self.user_pto_policies: UserPTOPoliciesApi = UserPTOPoliciesApi(api_client)
        self.user_workflow: UserWorkflowApi = UserWorkflowApi(api_client)
        self.workflows: WorkflowsApi = WorkflowsApi(api_client)
