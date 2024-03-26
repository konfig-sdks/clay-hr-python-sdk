import typing_extensions

from clay_hr_python_sdk.paths import PathValues
from clay_hr_python_sdk.apis.paths.api_token import ApiToken
from clay_hr_python_sdk.apis.paths.api_announcement_create import ApiAnnouncementCreate
from clay_hr_python_sdk.apis.paths.api_announcement_ann_id import ApiAnnouncementAnnId
from clay_hr_python_sdk.apis.paths.api_announcement_edit import ApiAnnouncementEdit
from clay_hr_python_sdk.apis.paths.api_attachment_list_ann_id import ApiAttachmentListAnnId
from clay_hr_python_sdk.apis.paths.root import Root
from clay_hr_python_sdk.apis.paths.detail_recruitid import DetailRecruitid
from clay_hr_python_sdk.apis.paths._list import ModelList
from clay_hr_python_sdk.apis.paths.customfield import Customfield
from clay_hr_python_sdk.apis.paths.customfields import Customfields
from clay_hr_python_sdk.apis.paths.customfieldvalues import Customfieldvalues
from clay_hr_python_sdk.apis.paths.customlist import Customlist
from clay_hr_python_sdk.apis.paths.delete import Delete
from clay_hr_python_sdk.apis.paths.attachment_download import AttachmentDownload
from clay_hr_python_sdk.apis.paths.document_library import DocumentLibrary
from clay_hr_python_sdk.apis.paths.currencylist import Currencylist
from clay_hr_python_sdk.apis.paths.expensereport import Expensereport
from clay_hr_python_sdk.apis.paths.expensetypes import Expensetypes
from clay_hr_python_sdk.apis.paths.expensereports import Expensereports
from clay_hr_python_sdk.apis.paths.expensereport_submit_expense_report_id import ExpensereportSubmitExpenseReportId
from clay_hr_python_sdk.apis.paths.expensereport_delete import ExpensereportDelete
from clay_hr_python_sdk.apis.paths.expenseitem import Expenseitem
from clay_hr_python_sdk.apis.paths.api_getdynaforms import ApiGetdynaforms
from clay_hr_python_sdk.apis.paths.api_my import ApiMy
from clay_hr_python_sdk.apis.paths.api_response_dynamic_form_id import ApiResponseDynamicFormId
from clay_hr_python_sdk.apis.paths.api_responselist import ApiResponselist
from clay_hr_python_sdk.apis.paths.api_save_form_response import ApiSaveFormResponse
from clay_hr_python_sdk.apis.paths.api_save_item_response import ApiSaveItemResponse
from clay_hr_python_sdk.apis.paths.api_view import ApiView
from clay_hr_python_sdk.apis.paths.goal_list import GoalList
from clay_hr_python_sdk.apis.paths.api_jobprofiles import ApiJobprofiles
from clay_hr_python_sdk.apis.paths.api_leave_hours_credit import ApiLeaveHoursCredit
from clay_hr_python_sdk.apis.paths.api_leaverequest import ApiLeaverequest
from clay_hr_python_sdk.apis.paths.api_leaverequests import ApiLeaverequests
from clay_hr_python_sdk.apis.paths.api_manage_leaves import ApiManageLeaves
from clay_hr_python_sdk.apis.paths.api_process_leave import ApiProcessLeave
from clay_hr_python_sdk.apis.paths.api_userpto_balance_add import ApiUserptoBalanceAdd
from clay_hr_python_sdk.apis.paths.api_orgrelation_org_relations_by_user import ApiOrgrelationOrgRelationsByUser
from clay_hr_python_sdk.apis.paths.api_orgrelation_allactive import ApiOrgrelationAllactive
from clay_hr_python_sdk.apis.paths.api_orgrelation_save import ApiOrgrelationSave
from clay_hr_python_sdk.apis.paths.api_orgunits import ApiOrgunits
from clay_hr_python_sdk.apis.paths.api_orgunits_add import ApiOrgunitsAdd
from clay_hr_python_sdk.apis.paths.paystub import Paystub
from clay_hr_python_sdk.apis.paths.api_user_complete_user_details import ApiUserCompleteUserDetails
from clay_hr_python_sdk.apis.paths.api_user_add import ApiUserAdd
from clay_hr_python_sdk.apis.paths.api_user_update import ApiUserUpdate
from clay_hr_python_sdk.apis.paths.api_user_basic import ApiUserBasic
from clay_hr_python_sdk.apis.paths.api_user_compensation_add import ApiUserCompensationAdd
from clay_hr_python_sdk.apis.paths.api_user_compensation_update import ApiUserCompensationUpdate
from clay_hr_python_sdk.apis.paths.api_user_list import ApiUserList
from clay_hr_python_sdk.apis.paths.api_user_permissions import ApiUserPermissions
from clay_hr_python_sdk.apis.paths.api_user_update_status import ApiUserUpdateStatus
from clay_hr_python_sdk.apis.paths.api_user_uploadpicture import ApiUserUploadpicture
from clay_hr_python_sdk.apis.paths.api_users import ApiUsers
from clay_hr_python_sdk.apis.paths.api_users_basic import ApiUsersBasic
from clay_hr_python_sdk.apis.paths.api_address_save import ApiAddressSave
from clay_hr_python_sdk.apis.paths.api_education_save import ApiEducationSave
from clay_hr_python_sdk.apis.paths.api_employment_save import ApiEmploymentSave
from clay_hr_python_sdk.apis.paths.api_user_orgrelation_add import ApiUserOrgrelationAdd
from clay_hr_python_sdk.apis.paths.api_user_save_custom_field_values import ApiUserSaveCustomFieldValues
from clay_hr_python_sdk.apis.paths.api_user_address_delete import ApiUserAddressDelete
from clay_hr_python_sdk.apis.paths.api_user_employment_delete import ApiUserEmploymentDelete
from clay_hr_python_sdk.apis.paths.user_education_delete import UserEducationDelete
from clay_hr_python_sdk.apis.paths.appraisal_user import AppraisalUser
from clay_hr_python_sdk.apis.paths.appraisal_template_list import AppraisalTemplateList
from clay_hr_python_sdk.apis.paths.appraisal_add import AppraisalAdd
from clay_hr_python_sdk.apis.paths.appraisal_get_completed_reviews import AppraisalGetCompletedReviews
from clay_hr_python_sdk.apis.paths.appraisal_bulk_launch import AppraisalBulkLaunch
from clay_hr_python_sdk.apis.paths.appraisal_assignment import AppraisalAssignment
from clay_hr_python_sdk.apis.paths.position_save import PositionSave
from clay_hr_python_sdk.apis.paths.position_view import PositionView
from clay_hr_python_sdk.apis.paths.position_list import PositionList
from clay_hr_python_sdk.apis.paths.api_projects_allocation_project_id import ApiProjectsAllocationProjectId
from clay_hr_python_sdk.apis.paths.api_projects_allocation import ApiProjectsAllocation
from clay_hr_python_sdk.apis.paths.api_projects_project_id import ApiProjectsProjectId
from clay_hr_python_sdk.apis.paths.api_projects import ApiProjects
from clay_hr_python_sdk.apis.paths.api_report import ApiReport
from clay_hr_python_sdk.apis.paths.api_report_content import ApiReportContent
from clay_hr_python_sdk.apis.paths.report_content import ReportContent
from clay_hr_python_sdk.apis.paths.skill_add import SkillAdd
from clay_hr_python_sdk.apis.paths.skills import Skills
from clay_hr_python_sdk.apis.paths.user_skill import UserSkill
from clay_hr_python_sdk.apis.paths.api_survey_allresponses import ApiSurveyAllresponses
from clay_hr_python_sdk.apis.paths.api_survey_item_save import ApiSurveyItemSave
from clay_hr_python_sdk.apis.paths.api_survey_list import ApiSurveyList
from clay_hr_python_sdk.apis.paths.api_survey_save import ApiSurveySave
from clay_hr_python_sdk.apis.paths.api_survey_view import ApiSurveyView
from clay_hr_python_sdk.apis.paths.api_user_timecard import ApiUserTimecard
from clay_hr_python_sdk.apis.paths.api_user_timecards import ApiUserTimecards
from clay_hr_python_sdk.apis.paths.timecard_clock_out import TimecardClockOut
from clay_hr_python_sdk.apis.paths.verify_device import VerifyDevice
from clay_hr_python_sdk.apis.paths.verify_tvc import VerifyTvc
from clay_hr_python_sdk.apis.paths.verify_user import VerifyUser
from clay_hr_python_sdk.apis.paths.register import Register
from clay_hr_python_sdk.apis.paths.api_timecards_details_timecard_id import ApiTimecardsDetailsTimecardId
from clay_hr_python_sdk.apis.paths.api_timecards import ApiTimecards
from clay_hr_python_sdk.apis.paths.api_timesheet_activitytype_list import ApiTimesheetActivitytypeList
from clay_hr_python_sdk.apis.paths.api_timesheet_allocations_list import ApiTimesheetAllocationsList
from clay_hr_python_sdk.apis.paths.api_timesheet_clockin import ApiTimesheetClockin
from clay_hr_python_sdk.apis.paths.api_timesheet_clockout import ApiTimesheetClockout
from clay_hr_python_sdk.apis.paths.api_timesheet_delete import ApiTimesheetDelete
from clay_hr_python_sdk.apis.paths.api_timesheet_preferences_list import ApiTimesheetPreferencesList
from clay_hr_python_sdk.apis.paths.api_timesheet_save import ApiTimesheetSave
from clay_hr_python_sdk.apis.paths.api_timesheet_update import ApiTimesheetUpdate
from clay_hr_python_sdk.apis.paths.api_timesheets import ApiTimesheets
from clay_hr_python_sdk.apis.paths.api_timesheet_approvals_list import ApiTimesheetApprovalsList
from clay_hr_python_sdk.apis.paths.api_timesheet import ApiTimesheet
from clay_hr_python_sdk.apis.paths.api_timesheets_details_time_sheet_id import ApiTimesheetsDetailsTimeSheetId
from clay_hr_python_sdk.apis.paths.api_training_content import ApiTrainingContent
from clay_hr_python_sdk.apis.paths.api_training_status_update import ApiTrainingStatusUpdate
from clay_hr_python_sdk.apis.paths.api_training_talentlms_sync import ApiTrainingTalentlmsSync
from clay_hr_python_sdk.apis.paths.api_trainings import ApiTrainings
from clay_hr_python_sdk.apis.paths.ptopolicies import Ptopolicies
from clay_hr_python_sdk.apis.paths.v3_user_pto import V3UserPto
from clay_hr_python_sdk.apis.paths.api_v3_userworkflow_assign_workflow_id import ApiV3UserworkflowAssignWorkflowId
from clay_hr_python_sdk.apis.paths.api_v3_userworkflows import ApiV3Userworkflows
from clay_hr_python_sdk.apis.paths.api_v3_userworkflows_userworkflowid import ApiV3UserworkflowsUserworkflowid
from clay_hr_python_sdk.apis.paths.api_v3_task_add import ApiV3TaskAdd
from clay_hr_python_sdk.apis.paths.api_v3_task_update_status import ApiV3TaskUpdateStatus
from clay_hr_python_sdk.apis.paths.api_v3_task_taskid import ApiV3TaskTaskid
from clay_hr_python_sdk.apis.paths.api_v3_tasks import ApiV3Tasks
from clay_hr_python_sdk.apis.paths.api_workflows import ApiWorkflows
from clay_hr_python_sdk.apis.paths.api_test import ApiTest
from clay_hr_python_sdk.apis.paths.api_shifts import ApiShifts
from clay_hr_python_sdk.apis.paths.api_shifts_save import ApiShiftsSave
from clay_hr_python_sdk.apis.paths.resume import Resume
from clay_hr_python_sdk.apis.paths.rm_api_feedback import RmApiFeedback
from clay_hr_python_sdk.apis.paths.getgoal import Getgoal
from clay_hr_python_sdk.apis.paths.goal import Goal
from clay_hr_python_sdk.apis.paths.deletegoal import Deletegoal
from clay_hr_python_sdk.apis.paths.invoice import Invoice
from clay_hr_python_sdk.apis.paths.objective import Objective
from clay_hr_python_sdk.apis.paths.api_user import ApiUser
from clay_hr_python_sdk.apis.paths.api_user_compensation import ApiUserCompensation
from clay_hr_python_sdk.apis.paths.resource import Resource
from clay_hr_python_sdk.apis.paths.timecard import Timecard
from clay_hr_python_sdk.apis.paths.timecard_addtimecard import TimecardAddtimecard
from clay_hr_python_sdk.apis.paths.timecard_clockin import TimecardClockin

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_TOKEN: ApiToken,
        PathValues.API_ANNOUNCEMENT_CREATE: ApiAnnouncementCreate,
        PathValues.API_ANNOUNCEMENT_ANN_ID: ApiAnnouncementAnnId,
        PathValues.API_ANNOUNCEMENT_EDIT: ApiAnnouncementEdit,
        PathValues.API_ATTACHMENT_LIST_ANN_ID: ApiAttachmentListAnnId,
        PathValues._: Root,
        PathValues.DETAIL_RECRUITID: DetailRecruitid,
        PathValues.LIST: ModelList,
        PathValues.CUSTOMFIELD: Customfield,
        PathValues.CUSTOMFIELDS: Customfields,
        PathValues.CUSTOMFIELDVALUES: Customfieldvalues,
        PathValues.CUSTOMLIST: Customlist,
        PathValues.DELETE: Delete,
        PathValues.ATTACHMENT_DOWNLOAD: AttachmentDownload,
        PathValues.DOCUMENT_LIBRARY: DocumentLibrary,
        PathValues.CURRENCYLIST: Currencylist,
        PathValues.EXPENSEREPORT: Expensereport,
        PathValues.EXPENSETYPES: Expensetypes,
        PathValues.EXPENSEREPORTS: Expensereports,
        PathValues.EXPENSEREPORT_SUBMIT_EXPENSE_REPORT_ID: ExpensereportSubmitExpenseReportId,
        PathValues.EXPENSEREPORT_DELETE: ExpensereportDelete,
        PathValues.EXPENSEITEM: Expenseitem,
        PathValues.API_GETDYNAFORMS: ApiGetdynaforms,
        PathValues.API_MY: ApiMy,
        PathValues.API_RESPONSE_DYNAMIC_FORM_ID: ApiResponseDynamicFormId,
        PathValues.API_RESPONSELIST: ApiResponselist,
        PathValues.API_SAVE_FORM_RESPONSE: ApiSaveFormResponse,
        PathValues.API_SAVE_ITEM_RESPONSE: ApiSaveItemResponse,
        PathValues.API_VIEW: ApiView,
        PathValues.GOAL_LIST: GoalList,
        PathValues.API_JOBPROFILES: ApiJobprofiles,
        PathValues.API_LEAVE_HOURS_CREDIT: ApiLeaveHoursCredit,
        PathValues.API_LEAVEREQUEST: ApiLeaverequest,
        PathValues.API_LEAVEREQUESTS: ApiLeaverequests,
        PathValues.API_MANAGE_LEAVES: ApiManageLeaves,
        PathValues.API_PROCESS_LEAVE: ApiProcessLeave,
        PathValues.API_USERPTO_BALANCE_ADD: ApiUserptoBalanceAdd,
        PathValues.API_ORGRELATION_ORG_RELATIONS_BY_USER: ApiOrgrelationOrgRelationsByUser,
        PathValues.API_ORGRELATION_ALLACTIVE: ApiOrgrelationAllactive,
        PathValues.API_ORGRELATION_SAVE: ApiOrgrelationSave,
        PathValues.API_ORGUNITS: ApiOrgunits,
        PathValues.API_ORGUNITS_ADD: ApiOrgunitsAdd,
        PathValues.PAYSTUB: Paystub,
        PathValues.API_USER_COMPLETE_USER_DETAILS: ApiUserCompleteUserDetails,
        PathValues.API_USER_ADD: ApiUserAdd,
        PathValues.API_USER_UPDATE: ApiUserUpdate,
        PathValues.API_USER_BASIC: ApiUserBasic,
        PathValues.API_USER_COMPENSATION_ADD: ApiUserCompensationAdd,
        PathValues.API_USER_COMPENSATION_UPDATE: ApiUserCompensationUpdate,
        PathValues.API_USER_LIST: ApiUserList,
        PathValues.API_USER_PERMISSIONS: ApiUserPermissions,
        PathValues.API_USER_UPDATE_STATUS: ApiUserUpdateStatus,
        PathValues.API_USER_UPLOADPICTURE: ApiUserUploadpicture,
        PathValues.API_USERS: ApiUsers,
        PathValues.API_USERS_BASIC: ApiUsersBasic,
        PathValues.API_ADDRESS_SAVE: ApiAddressSave,
        PathValues.API_EDUCATION_SAVE: ApiEducationSave,
        PathValues.API_EMPLOYMENT_SAVE: ApiEmploymentSave,
        PathValues.API_USER_ORGRELATION_ADD: ApiUserOrgrelationAdd,
        PathValues.API_USER_SAVE_CUSTOM_FIELD_VALUES: ApiUserSaveCustomFieldValues,
        PathValues.API_USER_ADDRESS_DELETE: ApiUserAddressDelete,
        PathValues.API_USER_EMPLOYMENT_DELETE: ApiUserEmploymentDelete,
        PathValues.USER_EDUCATION_DELETE: UserEducationDelete,
        PathValues.APPRAISAL_USER: AppraisalUser,
        PathValues.APPRAISAL_TEMPLATE_LIST: AppraisalTemplateList,
        PathValues.APPRAISAL_ADD: AppraisalAdd,
        PathValues.APPRAISAL_GET_COMPLETED_REVIEWS: AppraisalGetCompletedReviews,
        PathValues.APPRAISAL_BULK_LAUNCH: AppraisalBulkLaunch,
        PathValues.APPRAISAL_ASSIGNMENT: AppraisalAssignment,
        PathValues.POSITION_SAVE: PositionSave,
        PathValues.POSITION_VIEW: PositionView,
        PathValues.POSITION_LIST: PositionList,
        PathValues.API_PROJECTS_ALLOCATION_PROJECT_ID: ApiProjectsAllocationProjectId,
        PathValues.API_PROJECTS_ALLOCATION: ApiProjectsAllocation,
        PathValues.API_PROJECTS_PROJECT_ID: ApiProjectsProjectId,
        PathValues.API_PROJECTS: ApiProjects,
        PathValues.API_REPORT: ApiReport,
        PathValues.API_REPORT_CONTENT: ApiReportContent,
        PathValues.REPORT_CONTENT: ReportContent,
        PathValues.SKILL_ADD: SkillAdd,
        PathValues.SKILLS: Skills,
        PathValues.USER_SKILL: UserSkill,
        PathValues.API_SURVEY_ALLRESPONSES: ApiSurveyAllresponses,
        PathValues.API_SURVEY_ITEM_SAVE: ApiSurveyItemSave,
        PathValues.API_SURVEY_LIST: ApiSurveyList,
        PathValues.API_SURVEY_SAVE: ApiSurveySave,
        PathValues.API_SURVEY_VIEW: ApiSurveyView,
        PathValues.API_USER_TIMECARD: ApiUserTimecard,
        PathValues.API_USER_TIMECARDS: ApiUserTimecards,
        PathValues.TIMECARD_CLOCK_OUT: TimecardClockOut,
        PathValues.VERIFY_DEVICE: VerifyDevice,
        PathValues.VERIFY_TVC: VerifyTvc,
        PathValues.VERIFY_USER: VerifyUser,
        PathValues.REGISTER: Register,
        PathValues.API_TIMECARDS_DETAILS_TIMECARD_ID: ApiTimecardsDetailsTimecardId,
        PathValues.API_TIMECARDS: ApiTimecards,
        PathValues.API_TIMESHEET_ACTIVITYTYPE_LIST: ApiTimesheetActivitytypeList,
        PathValues.API_TIMESHEET_ALLOCATIONS_LIST: ApiTimesheetAllocationsList,
        PathValues.API_TIMESHEET_CLOCKIN: ApiTimesheetClockin,
        PathValues.API_TIMESHEET_CLOCKOUT: ApiTimesheetClockout,
        PathValues.API_TIMESHEET_DELETE: ApiTimesheetDelete,
        PathValues.API_TIMESHEET_PREFERENCES_LIST: ApiTimesheetPreferencesList,
        PathValues.API_TIMESHEET_SAVE: ApiTimesheetSave,
        PathValues.API_TIMESHEET_UPDATE: ApiTimesheetUpdate,
        PathValues.API_TIMESHEETS: ApiTimesheets,
        PathValues.API_TIMESHEET_APPROVALS_LIST: ApiTimesheetApprovalsList,
        PathValues.API_TIMESHEET: ApiTimesheet,
        PathValues.API_TIMESHEETS_DETAILS_TIME_SHEET_ID: ApiTimesheetsDetailsTimeSheetId,
        PathValues.API_TRAINING_CONTENT: ApiTrainingContent,
        PathValues.API_TRAINING_STATUS_UPDATE: ApiTrainingStatusUpdate,
        PathValues.API_TRAINING_TALENTLMS_SYNC: ApiTrainingTalentlmsSync,
        PathValues.API_TRAININGS: ApiTrainings,
        PathValues.PTOPOLICIES: Ptopolicies,
        PathValues.V3_USER_PTO: V3UserPto,
        PathValues.API_V3_USERWORKFLOW_ASSIGN_WORKFLOW_ID: ApiV3UserworkflowAssignWorkflowId,
        PathValues.API_V3_USERWORKFLOWS: ApiV3Userworkflows,
        PathValues.API_V3_USERWORKFLOWS_USERWORKFLOWID: ApiV3UserworkflowsUserworkflowid,
        PathValues.API_V3_TASK_ADD: ApiV3TaskAdd,
        PathValues.API_V3_TASK_UPDATE_STATUS: ApiV3TaskUpdateStatus,
        PathValues.API_V3_TASK_TASKID: ApiV3TaskTaskid,
        PathValues.API_V3_TASKS: ApiV3Tasks,
        PathValues.API_WORKFLOWS: ApiWorkflows,
        PathValues.API_TEST: ApiTest,
        PathValues.API_SHIFTS: ApiShifts,
        PathValues.API_SHIFTS_SAVE: ApiShiftsSave,
        PathValues.RESUME: Resume,
        PathValues.RM_API_FEEDBACK: RmApiFeedback,
        PathValues.GETGOAL: Getgoal,
        PathValues.GOAL: Goal,
        PathValues.DELETEGOAL: Deletegoal,
        PathValues.INVOICE: Invoice,
        PathValues.OBJECTIVE: Objective,
        PathValues.API_USER: ApiUser,
        PathValues.API_USER_COMPENSATION: ApiUserCompensation,
        PathValues.RESOURCE: Resource,
        PathValues.TIMECARD: Timecard,
        PathValues.TIMECARD_ADDTIMECARD: TimecardAddtimecard,
        PathValues.TIMECARD_CLOCKIN: TimecardClockin,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_TOKEN: ApiToken,
        PathValues.API_ANNOUNCEMENT_CREATE: ApiAnnouncementCreate,
        PathValues.API_ANNOUNCEMENT_ANN_ID: ApiAnnouncementAnnId,
        PathValues.API_ANNOUNCEMENT_EDIT: ApiAnnouncementEdit,
        PathValues.API_ATTACHMENT_LIST_ANN_ID: ApiAttachmentListAnnId,
        PathValues._: Root,
        PathValues.DETAIL_RECRUITID: DetailRecruitid,
        PathValues.LIST: ModelList,
        PathValues.CUSTOMFIELD: Customfield,
        PathValues.CUSTOMFIELDS: Customfields,
        PathValues.CUSTOMFIELDVALUES: Customfieldvalues,
        PathValues.CUSTOMLIST: Customlist,
        PathValues.DELETE: Delete,
        PathValues.ATTACHMENT_DOWNLOAD: AttachmentDownload,
        PathValues.DOCUMENT_LIBRARY: DocumentLibrary,
        PathValues.CURRENCYLIST: Currencylist,
        PathValues.EXPENSEREPORT: Expensereport,
        PathValues.EXPENSETYPES: Expensetypes,
        PathValues.EXPENSEREPORTS: Expensereports,
        PathValues.EXPENSEREPORT_SUBMIT_EXPENSE_REPORT_ID: ExpensereportSubmitExpenseReportId,
        PathValues.EXPENSEREPORT_DELETE: ExpensereportDelete,
        PathValues.EXPENSEITEM: Expenseitem,
        PathValues.API_GETDYNAFORMS: ApiGetdynaforms,
        PathValues.API_MY: ApiMy,
        PathValues.API_RESPONSE_DYNAMIC_FORM_ID: ApiResponseDynamicFormId,
        PathValues.API_RESPONSELIST: ApiResponselist,
        PathValues.API_SAVE_FORM_RESPONSE: ApiSaveFormResponse,
        PathValues.API_SAVE_ITEM_RESPONSE: ApiSaveItemResponse,
        PathValues.API_VIEW: ApiView,
        PathValues.GOAL_LIST: GoalList,
        PathValues.API_JOBPROFILES: ApiJobprofiles,
        PathValues.API_LEAVE_HOURS_CREDIT: ApiLeaveHoursCredit,
        PathValues.API_LEAVEREQUEST: ApiLeaverequest,
        PathValues.API_LEAVEREQUESTS: ApiLeaverequests,
        PathValues.API_MANAGE_LEAVES: ApiManageLeaves,
        PathValues.API_PROCESS_LEAVE: ApiProcessLeave,
        PathValues.API_USERPTO_BALANCE_ADD: ApiUserptoBalanceAdd,
        PathValues.API_ORGRELATION_ORG_RELATIONS_BY_USER: ApiOrgrelationOrgRelationsByUser,
        PathValues.API_ORGRELATION_ALLACTIVE: ApiOrgrelationAllactive,
        PathValues.API_ORGRELATION_SAVE: ApiOrgrelationSave,
        PathValues.API_ORGUNITS: ApiOrgunits,
        PathValues.API_ORGUNITS_ADD: ApiOrgunitsAdd,
        PathValues.PAYSTUB: Paystub,
        PathValues.API_USER_COMPLETE_USER_DETAILS: ApiUserCompleteUserDetails,
        PathValues.API_USER_ADD: ApiUserAdd,
        PathValues.API_USER_UPDATE: ApiUserUpdate,
        PathValues.API_USER_BASIC: ApiUserBasic,
        PathValues.API_USER_COMPENSATION_ADD: ApiUserCompensationAdd,
        PathValues.API_USER_COMPENSATION_UPDATE: ApiUserCompensationUpdate,
        PathValues.API_USER_LIST: ApiUserList,
        PathValues.API_USER_PERMISSIONS: ApiUserPermissions,
        PathValues.API_USER_UPDATE_STATUS: ApiUserUpdateStatus,
        PathValues.API_USER_UPLOADPICTURE: ApiUserUploadpicture,
        PathValues.API_USERS: ApiUsers,
        PathValues.API_USERS_BASIC: ApiUsersBasic,
        PathValues.API_ADDRESS_SAVE: ApiAddressSave,
        PathValues.API_EDUCATION_SAVE: ApiEducationSave,
        PathValues.API_EMPLOYMENT_SAVE: ApiEmploymentSave,
        PathValues.API_USER_ORGRELATION_ADD: ApiUserOrgrelationAdd,
        PathValues.API_USER_SAVE_CUSTOM_FIELD_VALUES: ApiUserSaveCustomFieldValues,
        PathValues.API_USER_ADDRESS_DELETE: ApiUserAddressDelete,
        PathValues.API_USER_EMPLOYMENT_DELETE: ApiUserEmploymentDelete,
        PathValues.USER_EDUCATION_DELETE: UserEducationDelete,
        PathValues.APPRAISAL_USER: AppraisalUser,
        PathValues.APPRAISAL_TEMPLATE_LIST: AppraisalTemplateList,
        PathValues.APPRAISAL_ADD: AppraisalAdd,
        PathValues.APPRAISAL_GET_COMPLETED_REVIEWS: AppraisalGetCompletedReviews,
        PathValues.APPRAISAL_BULK_LAUNCH: AppraisalBulkLaunch,
        PathValues.APPRAISAL_ASSIGNMENT: AppraisalAssignment,
        PathValues.POSITION_SAVE: PositionSave,
        PathValues.POSITION_VIEW: PositionView,
        PathValues.POSITION_LIST: PositionList,
        PathValues.API_PROJECTS_ALLOCATION_PROJECT_ID: ApiProjectsAllocationProjectId,
        PathValues.API_PROJECTS_ALLOCATION: ApiProjectsAllocation,
        PathValues.API_PROJECTS_PROJECT_ID: ApiProjectsProjectId,
        PathValues.API_PROJECTS: ApiProjects,
        PathValues.API_REPORT: ApiReport,
        PathValues.API_REPORT_CONTENT: ApiReportContent,
        PathValues.REPORT_CONTENT: ReportContent,
        PathValues.SKILL_ADD: SkillAdd,
        PathValues.SKILLS: Skills,
        PathValues.USER_SKILL: UserSkill,
        PathValues.API_SURVEY_ALLRESPONSES: ApiSurveyAllresponses,
        PathValues.API_SURVEY_ITEM_SAVE: ApiSurveyItemSave,
        PathValues.API_SURVEY_LIST: ApiSurveyList,
        PathValues.API_SURVEY_SAVE: ApiSurveySave,
        PathValues.API_SURVEY_VIEW: ApiSurveyView,
        PathValues.API_USER_TIMECARD: ApiUserTimecard,
        PathValues.API_USER_TIMECARDS: ApiUserTimecards,
        PathValues.TIMECARD_CLOCK_OUT: TimecardClockOut,
        PathValues.VERIFY_DEVICE: VerifyDevice,
        PathValues.VERIFY_TVC: VerifyTvc,
        PathValues.VERIFY_USER: VerifyUser,
        PathValues.REGISTER: Register,
        PathValues.API_TIMECARDS_DETAILS_TIMECARD_ID: ApiTimecardsDetailsTimecardId,
        PathValues.API_TIMECARDS: ApiTimecards,
        PathValues.API_TIMESHEET_ACTIVITYTYPE_LIST: ApiTimesheetActivitytypeList,
        PathValues.API_TIMESHEET_ALLOCATIONS_LIST: ApiTimesheetAllocationsList,
        PathValues.API_TIMESHEET_CLOCKIN: ApiTimesheetClockin,
        PathValues.API_TIMESHEET_CLOCKOUT: ApiTimesheetClockout,
        PathValues.API_TIMESHEET_DELETE: ApiTimesheetDelete,
        PathValues.API_TIMESHEET_PREFERENCES_LIST: ApiTimesheetPreferencesList,
        PathValues.API_TIMESHEET_SAVE: ApiTimesheetSave,
        PathValues.API_TIMESHEET_UPDATE: ApiTimesheetUpdate,
        PathValues.API_TIMESHEETS: ApiTimesheets,
        PathValues.API_TIMESHEET_APPROVALS_LIST: ApiTimesheetApprovalsList,
        PathValues.API_TIMESHEET: ApiTimesheet,
        PathValues.API_TIMESHEETS_DETAILS_TIME_SHEET_ID: ApiTimesheetsDetailsTimeSheetId,
        PathValues.API_TRAINING_CONTENT: ApiTrainingContent,
        PathValues.API_TRAINING_STATUS_UPDATE: ApiTrainingStatusUpdate,
        PathValues.API_TRAINING_TALENTLMS_SYNC: ApiTrainingTalentlmsSync,
        PathValues.API_TRAININGS: ApiTrainings,
        PathValues.PTOPOLICIES: Ptopolicies,
        PathValues.V3_USER_PTO: V3UserPto,
        PathValues.API_V3_USERWORKFLOW_ASSIGN_WORKFLOW_ID: ApiV3UserworkflowAssignWorkflowId,
        PathValues.API_V3_USERWORKFLOWS: ApiV3Userworkflows,
        PathValues.API_V3_USERWORKFLOWS_USERWORKFLOWID: ApiV3UserworkflowsUserworkflowid,
        PathValues.API_V3_TASK_ADD: ApiV3TaskAdd,
        PathValues.API_V3_TASK_UPDATE_STATUS: ApiV3TaskUpdateStatus,
        PathValues.API_V3_TASK_TASKID: ApiV3TaskTaskid,
        PathValues.API_V3_TASKS: ApiV3Tasks,
        PathValues.API_WORKFLOWS: ApiWorkflows,
        PathValues.API_TEST: ApiTest,
        PathValues.API_SHIFTS: ApiShifts,
        PathValues.API_SHIFTS_SAVE: ApiShiftsSave,
        PathValues.RESUME: Resume,
        PathValues.RM_API_FEEDBACK: RmApiFeedback,
        PathValues.GETGOAL: Getgoal,
        PathValues.GOAL: Goal,
        PathValues.DELETEGOAL: Deletegoal,
        PathValues.INVOICE: Invoice,
        PathValues.OBJECTIVE: Objective,
        PathValues.API_USER: ApiUser,
        PathValues.API_USER_COMPENSATION: ApiUserCompensation,
        PathValues.RESOURCE: Resource,
        PathValues.TIMECARD: Timecard,
        PathValues.TIMECARD_ADDTIMECARD: TimecardAddtimecard,
        PathValues.TIMECARD_CLOCKIN: TimecardClockin,
    }
)
