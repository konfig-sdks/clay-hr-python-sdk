import typing_extensions

from clay_hr_python_sdk.apis.tags import TagValues
from clay_hr_python_sdk.apis.tags.people_and_permissions_api import PeopleAndPermissionsApi
from clay_hr_python_sdk.apis.tags.timesheets_api import TimesheetsApi
from clay_hr_python_sdk.apis.tags.timecards_api import TimecardsApi
from clay_hr_python_sdk.apis.tags.expense_reports_api import ExpenseReportsApi
from clay_hr_python_sdk.apis.tags.forms_api import FormsApi
from clay_hr_python_sdk.apis.tags.workflows_api import WorkflowsApi
from clay_hr_python_sdk.apis.tags.leaves_api import LeavesApi
from clay_hr_python_sdk.apis.tags.candidates_api import CandidatesApi
from clay_hr_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from clay_hr_python_sdk.apis.tags.goals_api import GoalsApi
from clay_hr_python_sdk.apis.tags.performance_review_api import PerformanceReviewApi
from clay_hr_python_sdk.apis.tags.project_api import ProjectApi
from clay_hr_python_sdk.apis.tags.survey_api import SurveyApi
from clay_hr_python_sdk.apis.tags.announcement_api import AnnouncementApi
from clay_hr_python_sdk.apis.tags.trainings_api import TrainingsApi
from clay_hr_python_sdk.apis.tags.org_relation_api import OrgRelationApi
from clay_hr_python_sdk.apis.tags.positions_api import PositionsApi
from clay_hr_python_sdk.apis.tags.reports_api import ReportsApi
from clay_hr_python_sdk.apis.tags.skills_api import SkillsApi
from clay_hr_python_sdk.apis.tags.document_library_api import DocumentLibraryApi
from clay_hr_python_sdk.apis.tags.org_units_api import OrgUnitsApi
from clay_hr_python_sdk.apis.tags.user_pto_policies_api import UserPTOPoliciesApi
from clay_hr_python_sdk.apis.tags.shifts_api import ShiftsApi
from clay_hr_python_sdk.apis.tags.dependents_api import DependentsApi
from clay_hr_python_sdk.apis.tags.feedback_api import FeedbackApi
from clay_hr_python_sdk.apis.tags.invoice_api import InvoiceApi
from clay_hr_python_sdk.apis.tags.job_profiles_api import JobProfilesApi
from clay_hr_python_sdk.apis.tags.objective_api import ObjectiveApi
from clay_hr_python_sdk.apis.tags.pay_stubs_api import PayStubsApi
from clay_hr_python_sdk.apis.tags.performance_review_assignment_api import PerformanceReviewAssignmentApi
from clay_hr_python_sdk.apis.tags.test_api import TestApi
from clay_hr_python_sdk.apis.tags.authentication_api import AuthenticationApi
from clay_hr_python_sdk.apis.tags.user_workflow_api import UserWorkflowApi
from clay_hr_python_sdk.apis.tags.swagger_shift_api import SwaggerShiftApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PEOPLE_AND_PERMISSIONS: PeopleAndPermissionsApi,
        TagValues.TIMESHEETS: TimesheetsApi,
        TagValues.TIMECARDS: TimecardsApi,
        TagValues.EXPENSE_REPORTS: ExpenseReportsApi,
        TagValues.FORMS: FormsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.LEAVES: LeavesApi,
        TagValues.CANDIDATES: CandidatesApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.GOALS: GoalsApi,
        TagValues.PERFORMANCE_REVIEW: PerformanceReviewApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.SURVEY: SurveyApi,
        TagValues.ANNOUNCEMENT: AnnouncementApi,
        TagValues.TRAININGS: TrainingsApi,
        TagValues.ORG_RELATION: OrgRelationApi,
        TagValues.POSITIONS: PositionsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.DOCUMENT_LIBRARY: DocumentLibraryApi,
        TagValues.ORG_UNITS: OrgUnitsApi,
        TagValues.USER_PTO_POLICIES: UserPTOPoliciesApi,
        TagValues.SHIFTS: ShiftsApi,
        TagValues.DEPENDENTS: DependentsApi,
        TagValues.FEEDBACK: FeedbackApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.JOB_PROFILES: JobProfilesApi,
        TagValues.OBJECTIVE: ObjectiveApi,
        TagValues.PAY_STUBS: PayStubsApi,
        TagValues.PERFORMANCE_REVIEW_ASSIGNMENT: PerformanceReviewAssignmentApi,
        TagValues.TEST: TestApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.USER_WORKFLOW: UserWorkflowApi,
        TagValues.SWAGGER_SHIFT: SwaggerShiftApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PEOPLE_AND_PERMISSIONS: PeopleAndPermissionsApi,
        TagValues.TIMESHEETS: TimesheetsApi,
        TagValues.TIMECARDS: TimecardsApi,
        TagValues.EXPENSE_REPORTS: ExpenseReportsApi,
        TagValues.FORMS: FormsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.LEAVES: LeavesApi,
        TagValues.CANDIDATES: CandidatesApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.GOALS: GoalsApi,
        TagValues.PERFORMANCE_REVIEW: PerformanceReviewApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.SURVEY: SurveyApi,
        TagValues.ANNOUNCEMENT: AnnouncementApi,
        TagValues.TRAININGS: TrainingsApi,
        TagValues.ORG_RELATION: OrgRelationApi,
        TagValues.POSITIONS: PositionsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.DOCUMENT_LIBRARY: DocumentLibraryApi,
        TagValues.ORG_UNITS: OrgUnitsApi,
        TagValues.USER_PTO_POLICIES: UserPTOPoliciesApi,
        TagValues.SHIFTS: ShiftsApi,
        TagValues.DEPENDENTS: DependentsApi,
        TagValues.FEEDBACK: FeedbackApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.JOB_PROFILES: JobProfilesApi,
        TagValues.OBJECTIVE: ObjectiveApi,
        TagValues.PAY_STUBS: PayStubsApi,
        TagValues.PERFORMANCE_REVIEW_ASSIGNMENT: PerformanceReviewAssignmentApi,
        TagValues.TEST: TestApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.USER_WORKFLOW: UserWorkflowApi,
        TagValues.SWAGGER_SHIFT: SwaggerShiftApi,
    }
)
