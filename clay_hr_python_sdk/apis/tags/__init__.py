# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from clay_hr_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PEOPLE_AND_PERMISSIONS = "People and Permissions"
    TIMESHEETS = "Timesheets"
    TIMECARDS = "Timecards"
    EXPENSE_REPORTS = "Expense Reports"
    FORMS = "Forms"
    WORKFLOWS = "Workflows"
    LEAVES = "Leaves"
    CANDIDATES = "Candidates"
    CUSTOM_FIELDS = "Custom Fields"
    GOALS = "Goals"
    PERFORMANCE_REVIEW = "Performance Review"
    PROJECT = "Project"
    SURVEY = "Survey"
    ANNOUNCEMENT = "Announcement"
    TRAININGS = "Trainings"
    ORG_RELATION = "OrgRelation"
    POSITIONS = "Positions"
    REPORTS = "Reports"
    SKILLS = "Skills"
    DOCUMENT_LIBRARY = "Document Library"
    ORG_UNITS = "Org Units"
    USER_PTO_POLICIES = "User PTO Policies"
    SHIFTS = "Shifts"
    DEPENDENTS = "Dependents"
    FEEDBACK = "Feedback"
    INVOICE = "Invoice"
    JOB_PROFILES = "Job profiles"
    OBJECTIVE = "Objective"
    PAY_STUBS = "Pay Stubs"
    PERFORMANCE_REVIEW_ASSIGNMENT = "Performance Review Assignment"
    TEST = "Test"
    AUTHENTICATION = "Authentication"
    USER_WORKFLOW = "UserWorkflow"
    SWAGGER_SHIFT = "Swagger Shift"
