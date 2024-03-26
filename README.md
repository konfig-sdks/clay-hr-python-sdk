<div align="center">

[![Visit Clayhr](./header.png)](https://clayhr.com)

# Clayhr<a id="clayhr"></a>

API Documentation


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`clayhr.announcement.create_new_announcement`](#clayhrannouncementcreate_new_announcement)
  * [`clayhr.announcement.get_attachments_by_id`](#clayhrannouncementget_attachments_by_id)
  * [`clayhr.announcement.get_by_id`](#clayhrannouncementget_by_id)
  * [`clayhr.announcement.update_announcement`](#clayhrannouncementupdate_announcement)
  * [`clayhr.authentication.get_access_token`](#clayhrauthenticationget_access_token)
  * [`clayhr.candidates.extract_pdf_resume`](#clayhrcandidatesextract_pdf_resume)
  * [`clayhr.candidates.get`](#clayhrcandidatesget)
  * [`clayhr.candidates.get_basic_details`](#clayhrcandidatesget_basic_details)
  * [`clayhr.candidates.get_candidate_detail_by_recruitid`](#clayhrcandidatesget_candidate_detail_by_recruitid)
  * [`clayhr.candidates.submit_new_candidate`](#clayhrcandidatessubmit_new_candidate)
  * [`clayhr.custom_fields.get_by_id`](#clayhrcustom_fieldsget_by_id)
  * [`clayhr.custom_fields.get_custom_fields`](#clayhrcustom_fieldsget_custom_fields)
  * [`clayhr.custom_fields.get_custom_lists`](#clayhrcustom_fieldsget_custom_lists)
  * [`clayhr.custom_fields.get_value`](#clayhrcustom_fieldsget_value)
  * [`clayhr.custom_fields.update_value`](#clayhrcustom_fieldsupdate_value)
  * [`clayhr.dependents.delete_by_contact_id`](#clayhrdependentsdelete_by_contact_id)
  * [`clayhr.document_library.get_attachments`](#clayhrdocument_libraryget_attachments)
  * [`clayhr.document_library.get_document_as_byte_array`](#clayhrdocument_libraryget_document_as_byte_array)
  * [`clayhr.expense_reports.create_new`](#clayhrexpense_reportscreate_new)
  * [`clayhr.expense_reports.create_new_expense_item`](#clayhrexpense_reportscreate_new_expense_item)
  * [`clayhr.expense_reports.delete_expense_report`](#clayhrexpense_reportsdelete_expense_report)
  * [`clayhr.expense_reports.get_by_user_id`](#clayhrexpense_reportsget_by_user_id)
  * [`clayhr.expense_reports.get_currencies`](#clayhrexpense_reportsget_currencies)
  * [`clayhr.expense_reports.get_expense_types`](#clayhrexpense_reportsget_expense_types)
  * [`clayhr.expense_reports.get_report_details`](#clayhrexpense_reportsget_report_details)
  * [`clayhr.expense_reports.submit_expense_report`](#clayhrexpense_reportssubmit_expense_report)
  * [`clayhr.feedback.list_feedback`](#clayhrfeedbacklist_feedback)
  * [`clayhr.forms.get_assigned_forms`](#clayhrformsget_assigned_forms)
  * [`clayhr.forms.get_details`](#clayhrformsget_details)
  * [`clayhr.forms.get_dyna_form`](#clayhrformsget_dyna_form)
  * [`clayhr.forms.get_form_response`](#clayhrformsget_form_response)
  * [`clayhr.forms.get_form_responses`](#clayhrformsget_form_responses)
  * [`clayhr.forms.save_form_response`](#clayhrformssave_form_response)
  * [`clayhr.forms.submit_item_response`](#clayhrformssubmit_item_response)
  * [`clayhr.goals.create_new_goal`](#clayhrgoalscreate_new_goal)
  * [`clayhr.goals.delete_goal`](#clayhrgoalsdelete_goal)
  * [`clayhr.goals.get_all_goals`](#clayhrgoalsget_all_goals)
  * [`clayhr.goals.get_goal`](#clayhrgoalsget_goal)
  * [`clayhr.goals.get_user_goals`](#clayhrgoalsget_user_goals)
  * [`clayhr.invoice.get_by_project_id`](#clayhrinvoiceget_by_project_id)
  * [`clayhr.job_profiles.get_job_profiles`](#clayhrjob_profilesget_job_profiles)
  * [`clayhr.leaves.add_pto_balance`](#clayhrleavesadd_pto_balance)
  * [`clayhr.leaves.create_new_leave`](#clayhrleavescreate_new_leave)
  * [`clayhr.leaves.get_leave_requests_within_date_range`](#clayhrleavesget_leave_requests_within_date_range)
  * [`clayhr.leaves.get_leaves_based_on_role`](#clayhrleavesget_leaves_based_on_role)
  * [`clayhr.leaves.get_remaining_hours_credit`](#clayhrleavesget_remaining_hours_credit)
  * [`clayhr.leaves.process_leave_by_id`](#clayhrleavesprocess_leave_by_id)
  * [`clayhr.objective.get_by_user_id_or_specific_objective_by_id`](#clayhrobjectiveget_by_user_id_or_specific_objective_by_id)
  * [`clayhr.org_units.create_new_org_unit`](#clayhrorg_unitscreate_new_org_unit)
  * [`clayhr.org_units.get_org_units`](#clayhrorg_unitsget_org_units)
  * [`clayhr.org_relation.get_all_active`](#clayhrorg_relationget_all_active)
  * [`clayhr.org_relation.get_org_relations_by_user`](#clayhrorg_relationget_org_relations_by_user)
  * [`clayhr.org_relation.save_user`](#clayhrorg_relationsave_user)
  * [`clayhr.pay_stubs.get_details`](#clayhrpay_stubsget_details)
  * [`clayhr.people_and_permissions.add_reports_to`](#clayhrpeople_and_permissionsadd_reports_to)
  * [`clayhr.people_and_permissions.create_or_update_user_details`](#clayhrpeople_and_permissionscreate_or_update_user_details)
  * [`clayhr.people_and_permissions.create_user`](#clayhrpeople_and_permissionscreate_user)
  * [`clayhr.people_and_permissions.create_user_compensation`](#clayhrpeople_and_permissionscreate_user_compensation)
  * [`clayhr.people_and_permissions.delete_user_address`](#clayhrpeople_and_permissionsdelete_user_address)
  * [`clayhr.people_and_permissions.delete_user_education`](#clayhrpeople_and_permissionsdelete_user_education)
  * [`clayhr.people_and_permissions.delete_user_employment`](#clayhrpeople_and_permissionsdelete_user_employment)
  * [`clayhr.people_and_permissions.get_all_users_details`](#clayhrpeople_and_permissionsget_all_users_details)
  * [`clayhr.people_and_permissions.get_basic_user_details`](#clayhrpeople_and_permissionsget_basic_user_details)
  * [`clayhr.people_and_permissions.get_financial_record`](#clayhrpeople_and_permissionsget_financial_record)
  * [`clayhr.people_and_permissions.get_financial_status`](#clayhrpeople_and_permissionsget_financial_status)
  * [`clayhr.people_and_permissions.get_user_basic_information`](#clayhrpeople_and_permissionsget_user_basic_information)
  * [`clayhr.people_and_permissions.get_user_details`](#clayhrpeople_and_permissionsget_user_details)
  * [`clayhr.people_and_permissions.get_user_list`](#clayhrpeople_and_permissionsget_user_list)
  * [`clayhr.people_and_permissions.get_user_permissions_and_menu_configurations`](#clayhrpeople_and_permissionsget_user_permissions_and_menu_configurations)
  * [`clayhr.people_and_permissions.get_users`](#clayhrpeople_and_permissionsget_users)
  * [`clayhr.people_and_permissions.save_custom_field_values`](#clayhrpeople_and_permissionssave_custom_field_values)
  * [`clayhr.people_and_permissions.save_user_address`](#clayhrpeople_and_permissionssave_user_address)
  * [`clayhr.people_and_permissions.save_user_education`](#clayhrpeople_and_permissionssave_user_education)
  * [`clayhr.people_and_permissions.save_user_employment`](#clayhrpeople_and_permissionssave_user_employment)
  * [`clayhr.people_and_permissions.update_financial_record`](#clayhrpeople_and_permissionsupdate_financial_record)
  * [`clayhr.people_and_permissions.update_user`](#clayhrpeople_and_permissionsupdate_user)
  * [`clayhr.people_and_permissions.upload_user_profile_picture`](#clayhrpeople_and_permissionsupload_user_profile_picture)
  * [`clayhr.performance_review.create_performance_review`](#clayhrperformance_reviewcreate_performance_review)
  * [`clayhr.performance_review.get_completed_reviews_based_on_user_id`](#clayhrperformance_reviewget_completed_reviews_based_on_user_id)
  * [`clayhr.performance_review.get_performance_reviews`](#clayhrperformance_reviewget_performance_reviews)
  * [`clayhr.performance_review.get_templates`](#clayhrperformance_reviewget_templates)
  * [`clayhr.performance_review.launch_performance_reviews_in_bulk`](#clayhrperformance_reviewlaunch_performance_reviews_in_bulk)
  * [`clayhr.performance_review_assignment.get_assignments`](#clayhrperformance_review_assignmentget_assignments)
  * [`clayhr.positions.create_position`](#clayhrpositionscreate_position)
  * [`clayhr.positions.get_position`](#clayhrpositionsget_position)
  * [`clayhr.positions.get_positions_list`](#clayhrpositionsget_positions_list)
  * [`clayhr.project.assign_user_allocation`](#clayhrprojectassign_user_allocation)
  * [`clayhr.project.create_new`](#clayhrprojectcreate_new)
  * [`clayhr.project.details_by_id`](#clayhrprojectdetails_by_id)
  * [`clayhr.project.list_allocations`](#clayhrprojectlist_allocations)
  * [`clayhr.project.list_projects`](#clayhrprojectlist_projects)
  * [`clayhr.reports.get_content_by_analytic_id`](#clayhrreportsget_content_by_analytic_id)
  * [`clayhr.reports.get_content_for_report`](#clayhrreportsget_content_for_report)
  * [`clayhr.reports.get_report_details`](#clayhrreportsget_report_details)
  * [`clayhr.shifts.list_shifts_using_get`](#clayhrshiftslist_shifts_using_get)
  * [`clayhr.shifts.save_shift`](#clayhrshiftssave_shift)
  * [`clayhr.skills.create_new_skill`](#clayhrskillscreate_new_skill)
  * [`clayhr.skills.get_skills`](#clayhrskillsget_skills)
  * [`clayhr.skills.get_user_assigned_skills`](#clayhrskillsget_user_assigned_skills)
  * [`clayhr.survey.create_item_response`](#clayhrsurveycreate_item_response)
  * [`clayhr.survey.create_response_by_assignment_id`](#clayhrsurveycreate_response_by_assignment_id)
  * [`clayhr.survey.details_by_form_id`](#clayhrsurveydetails_by_form_id)
  * [`clayhr.survey.get_all_survey_responses`](#clayhrsurveyget_all_survey_responses)
  * [`clayhr.survey.get_list`](#clayhrsurveyget_list)
  * [`clayhr.test.get_test`](#clayhrtestget_test)
  * [`clayhr.timecards.clock_out`](#clayhrtimecardsclock_out)
  * [`clayhr.timecards.create_past_timecard`](#clayhrtimecardscreate_past_timecard)
  * [`clayhr.timecards.create_timecard`](#clayhrtimecardscreate_timecard)
  * [`clayhr.timecards.get_by_user_id`](#clayhrtimecardsget_by_user_id)
  * [`clayhr.timecards.get_by_user_id_0`](#clayhrtimecardsget_by_user_id_0)
  * [`clayhr.timecards.get_details_by_timecard_id`](#clayhrtimecardsget_details_by_timecard_id)
  * [`clayhr.timecards.get_tvc_for_clockin_with_qr_code_using_cid`](#clayhrtimecardsget_tvc_for_clockin_with_qr_code_using_cid)
  * [`clayhr.timecards.get_user_by_id`](#clayhrtimecardsget_user_by_id)
  * [`clayhr.timecards.register_device_for_clock_in_with_asset_model`](#clayhrtimecardsregister_device_for_clock_in_with_asset_model)
  * [`clayhr.timecards.verify_device_with_device_uuid`](#clayhrtimecardsverify_device_with_device_uuid)
  * [`clayhr.timecards.verify_user_with_userid`](#clayhrtimecardsverify_user_with_userid)
  * [`clayhr.timesheets.clock_in`](#clayhrtimesheetsclock_in)
  * [`clayhr.timesheets.clock_out`](#clayhrtimesheetsclock_out)
  * [`clayhr.timesheets.create_or_update_timesheet`](#clayhrtimesheetscreate_or_update_timesheet)
  * [`clayhr.timesheets.delete_by_timesheet_id`](#clayhrtimesheetsdelete_by_timesheet_id)
  * [`clayhr.timesheets.get_active_allocations`](#clayhrtimesheetsget_active_allocations)
  * [`clayhr.timesheets.get_approval_list`](#clayhrtimesheetsget_approval_list)
  * [`clayhr.timesheets.get_by_timesheet_id`](#clayhrtimesheetsget_by_timesheet_id)
  * [`clayhr.timesheets.get_by_user_id`](#clayhrtimesheetsget_by_user_id)
  * [`clayhr.timesheets.get_details_by_timesheet_id`](#clayhrtimesheetsget_details_by_timesheet_id)
  * [`clayhr.timesheets.get_preferences_by_cid`](#clayhrtimesheetsget_preferences_by_cid)
  * [`clayhr.timesheets.get_timecards_by_timesheet_id`](#clayhrtimesheetsget_timecards_by_timesheet_id)
  * [`clayhr.timesheets.list_activity_types_by_cid`](#clayhrtimesheetslist_activity_types_by_cid)
  * [`clayhr.timesheets.update_status_by_timesheet_id`](#clayhrtimesheetsupdate_status_by_timesheet_id)
  * [`clayhr.trainings.get_by_user_id`](#clayhrtrainingsget_by_user_id)
  * [`clayhr.trainings.get_training_content_by_training_id`](#clayhrtrainingsget_training_content_by_training_id)
  * [`clayhr.trainings.synchronize_with_talent_lms`](#clayhrtrainingssynchronize_with_talent_lms)
  * [`clayhr.trainings.update_user_status`](#clayhrtrainingsupdate_user_status)
  * [`clayhr.user_pto_policies.get_policies`](#clayhruser_pto_policiesget_policies)
  * [`clayhr.user_pto_policies.list_pto_policies`](#clayhruser_pto_policieslist_pto_policies)
  * [`clayhr.user_workflow.assign_workflow_to_user`](#clayhruser_workflowassign_workflow_to_user)
  * [`clayhr.workflows.create_new_task`](#clayhrworkflowscreate_new_task)
  * [`clayhr.workflows.get_task_details_by_task_id`](#clayhrworkflowsget_task_details_by_task_id)
  * [`clayhr.workflows.get_tasks_by_user_id`](#clayhrworkflowsget_tasks_by_user_id)
  * [`clayhr.workflows.get_user_workflows`](#clayhrworkflowsget_user_workflows)
  * [`clayhr.workflows.get_workflows`](#clayhrworkflowsget_workflows)
  * [`clayhr.workflows.list_tasks_by_userworkflow_id`](#clayhrworkflowslist_tasks_by_userworkflow_id)
  * [`clayhr.workflows.update_status_task`](#clayhrworkflowsupdate_status_task)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=ClayHR&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from clay_hr_python_sdk import ClayHr, ApiException

clayhr = ClayHr(
    sec0="YOUR_API_KEY",
    sec1="YOUR_API_KEY",
)

try:
    # Create Announcement
    create_new_announcement_response = clayhr.announcement.create_new_announcement(
        title="Travel Policies",
        description="There are some amendments done in policy leave.",
        url="https://www.google.com",
        status="A",
    )
except ApiException as e:
    print("Exception when calling AnnouncementApi.create_new_announcement: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from clay_hr_python_sdk import ClayHr, ApiException

clayhr = ClayHr(
    sec0="YOUR_API_KEY",
    sec1="YOUR_API_KEY",
)


async def main():
    try:
        # Create Announcement
        create_new_announcement_response = (
            await clayhr.announcement.acreate_new_announcement(
                title="Travel Policies",
                description="There are some amendments done in policy leave.",
                url="https://www.google.com",
                status="A",
            )
        )
    except ApiException as e:
        print(
            "Exception when calling AnnouncementApi.create_new_announcement: %s\n" % e
        )
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from clay_hr_python_sdk import ClayHr, ApiException

clayhr = ClayHr(
    sec0="YOUR_API_KEY",
    sec1="YOUR_API_KEY",
)

try:
    # Create Announcement
    create_new_announcement_response = clayhr.announcement.raw.create_new_announcement(
        title="Travel Policies",
        description="There are some amendments done in policy leave.",
        url="https://www.google.com",
        status="A",
    )
    pprint(create_new_announcement_response.headers)
    pprint(create_new_announcement_response.status)
    pprint(create_new_announcement_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AnnouncementApi.create_new_announcement: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `clayhr.announcement.create_new_announcement`<a id="clayhrannouncementcreate_new_announcement"></a>

 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_announcement_response = clayhr.announcement.create_new_announcement(
    title="Travel Policies",
    description="There are some amendments done in policy leave.",
    url="https://www.google.com",
    status="A",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Title of the announcement.

##### description: `str`<a id="description-str"></a>

Description of the announcement.

##### url: `str`<a id="url-str"></a>

Any link associated/brief of the announcement.

##### status: `str`<a id="status-str"></a>

Status of Announcement. Choose between [\"A\", \"D\", \"I\"]. Defaults to \"A\".   A - Active, D - In Draft, I - Archive

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/announcement/create` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.announcement.get_attachments_by_id`<a id="clayhrannouncementget_attachments_by_id"></a>

Retrieve Announcement Attachments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attachments_by_id_response = clayhr.announcement.get_attachments_by_id(
    ann_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ann_id: `int`<a id="ann_id-int"></a>

The ID of the announcement.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/attachment/list/{annId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.announcement.get_by_id`<a id="clayhrannouncementget_by_id"></a>

Retrieve Announcement

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = clayhr.announcement.get_by_id(
    ann_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ann_id: `int`<a id="ann_id-int"></a>

The ID of the announcement.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/announcement/{annId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.announcement.update_announcement`<a id="clayhrannouncementupdate_announcement"></a>

Update Announcement

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_announcement_response = clayhr.announcement.update_announcement(
    ann_id=1,
    title="title_example",
    desciption="",
    status="A",
    url="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ann_id: `int`<a id="ann_id-int"></a>

The ID of the announcement.

##### title: `str`<a id="title-str"></a>

Title of the announcement.

##### desciption: `str`<a id="desciption-str"></a>

Description of the announcement.

##### status: `str`<a id="status-str"></a>

Status of Announcement. Choose between [\"A\", \"D\", \"I\"]. Defaults to \"A\".   A - Active, D - In Draft, I - Archive

##### url: `str`<a id="url-str"></a>

Link associated with the announcement.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/announcement/edit` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.authentication.get_access_token`<a id="clayhrauthenticationget_access_token"></a>

Get Access Token for Authentication using x-api-key and userId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_access_token_response = clayhr.authentication.get_access_token()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationGetAccessTokenResponse`](./clay_hr_python_sdk/pydantic/authentication_get_access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.candidates.extract_pdf_resume`<a id="clayhrcandidatesextract_pdf_resume"></a>

Create a candidate from pdf resume

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
extract_pdf_resume_response = clayhr.candidates.extract_pdf_resume(
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

The pdf resume of the candidate.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CandidatesExtractPdfResumeRequest`](./clay_hr_python_sdk/type/candidates_extract_pdf_resume_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CandidatesExtractPdfResumeResponse`](./clay_hr_python_sdk/pydantic/candidates_extract_pdf_resume_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resume` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.candidates.get`<a id="clayhrcandidatesget"></a>

Retrieve candidates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = clayhr.candidates.get()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CandidatesGetResponse`](./clay_hr_python_sdk/pydantic/candidates_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.candidates.get_basic_details`<a id="clayhrcandidatesget_basic_details"></a>

Retrieve candidates with basic details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_basic_details_response = clayhr.candidates.get_basic_details(
    page=0,
    page_size=20,
    search="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Page number.

##### page_size: `int`<a id="page_size-int"></a>

Number of candidates per page.

##### search: `str`<a id="search-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CandidatesGetBasicDetailsResponse`](./clay_hr_python_sdk/pydantic/candidates_get_basic_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.candidates.get_candidate_detail_by_recruitid`<a id="clayhrcandidatesget_candidate_detail_by_recruitid"></a>

Retrieve the candidate detail by recruitid

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_candidate_detail_by_recruitid_response = (
    clayhr.candidates.get_candidate_detail_by_recruitid(
        recruitid=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recruitid: `int`<a id="recruitid-int"></a>

The ID of the recruiter.

#### 🔄 Return<a id="🔄-return"></a>

[`CandidatesGetCandidateDetailByRecruitidResponse`](./clay_hr_python_sdk/pydantic/candidates_get_candidate_detail_by_recruitid_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/detail/{recruitid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.candidates.submit_new_candidate`<a id="clayhrcandidatessubmit_new_candidate"></a>

Create new candidate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_new_candidate_response = clayhr.candidates.submit_new_candidate(
    name="string_example",
    email="string_example",
    is_new_cand="true",
    phone=1,
    source="API",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the candidate.

##### email: `str`<a id="email-str"></a>

Email ID of the candidate.

##### is_new_cand: `str`<a id="is_new_cand-str"></a>

Is this new candidate?

##### phone: `int`<a id="phone-int"></a>

Phone number of the candidate.

##### source: `str`<a id="source-str"></a>

The source from which the candidate is being created.

#### 🔄 Return<a id="🔄-return"></a>

[`CandidatesSubmitNewCandidateResponse`](./clay_hr_python_sdk/pydantic/candidates_submit_new_candidate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.custom_fields.get_by_id`<a id="clayhrcustom_fieldsget_by_id"></a>

Retrieve Custom Field by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = clayhr.custom_fields.get_by_id(
    custom_field_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_id: `int`<a id="custom_field_id-int"></a>

The ID of the custom field.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsGetByIdResponse`](./clay_hr_python_sdk/pydantic/custom_fields_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customfield` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.custom_fields.get_custom_fields`<a id="clayhrcustom_fieldsget_custom_fields"></a>

Retrieve Custom Fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_response = clayhr.custom_fields.get_custom_fields(
    object_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### object_type: `str`<a id="object_type-str"></a>

The object type of custom field.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsGetCustomFieldsResponse`](./clay_hr_python_sdk/pydantic/custom_fields_get_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customfields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.custom_fields.get_custom_lists`<a id="clayhrcustom_fieldsget_custom_lists"></a>

Retrieve Custom Lists

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_lists_response = clayhr.custom_fields.get_custom_lists()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsGetCustomListsResponse`](./clay_hr_python_sdk/pydantic/custom_fields_get_custom_lists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customlist` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.custom_fields.get_value`<a id="clayhrcustom_fieldsget_value"></a>

Retrieve Custom Field Value

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_value_response = clayhr.custom_fields.get_value(
    custom_field_id=1,
    custom_field_code="string_example",
    user_email="string_example",
    emp_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_id: `int`<a id="custom_field_id-int"></a>

customFieldId

##### custom_field_code: `str`<a id="custom_field_code-str"></a>

customFieldCode

##### user_email: `str`<a id="user_email-str"></a>

userEmail

##### emp_id: `str`<a id="emp_id-str"></a>

empId

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsGetValueResponse`](./clay_hr_python_sdk/pydantic/custom_fields_get_value_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customfieldvalues` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.custom_fields.update_value`<a id="clayhrcustom_fieldsupdate_value"></a>

Update Custom Field Value

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_value_response = clayhr.custom_fields.update_value(
    custom_field_id=1,
    value="value_example",
    custom_field_code="string_example",
    user_email="string_example",
    emp_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_id: `int`<a id="custom_field_id-int"></a>

##### value: `str`<a id="value-str"></a>

##### custom_field_code: `str`<a id="custom_field_code-str"></a>

##### user_email: `str`<a id="user_email-str"></a>

##### emp_id: `str`<a id="emp_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsUpdateValueResponse`](./clay_hr_python_sdk/pydantic/custom_fields_update_value_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customfieldvalues` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.dependents.delete_by_contact_id`<a id="clayhrdependentsdelete_by_contact_id"></a>

Delete dependent by contactId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_contact_id_response = clayhr.dependents.delete_by_contact_id(
    contact_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_id: `int`<a id="contact_id-int"></a>

Contact ID of Dependent

#### 🔄 Return<a id="🔄-return"></a>

[`DependentsDeleteByContactIdResponse`](./clay_hr_python_sdk/pydantic/dependents_delete_by_contact_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.document_library.get_attachments`<a id="clayhrdocument_libraryget_attachments"></a>

Retrieve attachments within document library

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attachments_response = clayhr.document_library.get_attachments()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/documentLibrary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.document_library.get_document_as_byte_array`<a id="clayhrdocument_libraryget_document_as_byte_array"></a>

Retrieve document as byte array

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_document_as_byte_array_response = (
    clayhr.document_library.get_document_as_byte_array(
        file_name="fileName_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_name: `str`<a id="file_name-str"></a>

File ID from the server

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentLibraryGetDocumentAsByteArrayResponse`](./clay_hr_python_sdk/pydantic/document_library_get_document_as_byte_array_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attachment/download` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.expense_reports.create_new`<a id="clayhrexpense_reportscreate_new"></a>

Create expense report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = clayhr.expense_reports.create_new(
    name="Travel expense report.",
    amount=300,
    description="This expene report is regarding the travelling.",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the expense report.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount to be added in expense report.

##### description: `str`<a id="description-str"></a>

Description of the expense report.

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseReportsCreateNewResponse`](./clay_hr_python_sdk/pydantic/expense_reports_create_new_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expensereport` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.expense_reports.create_new_expense_item`<a id="clayhrexpense_reportscreate_new_expense_item"></a>

Create expense item

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_expense_item_response = clayhr.expense_reports.create_new_expense_item(
    amount=3.14,
    billable="Y",
    cid=1,
    currency_code="$(USD)",
    date="1970-01-01",
    expense_item_id=1,
    expense_type="expenseType_example",
    expense_type_id=1,
    project_id=1,
    reimbursible="Y",
    remarks="remarks_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount of the expense item.

##### billable: `str`<a id="billable-str"></a>

Y for \"Yes\" and N for \"No\".

##### cid: `int`<a id="cid-int"></a>

The unique ID of the customer.

##### currency_code: `str`<a id="currency_code-str"></a>

Code of the currency.

##### date: `date`<a id="date-date"></a>

Date of creating expense item.

##### expense_item_id: `int`<a id="expense_item_id-int"></a>

The ID of the expense item.

##### expense_type: `str`<a id="expense_type-str"></a>

The type of expense.

##### expense_type_id: `int`<a id="expense_type_id-int"></a>

The ID of the expense type.

##### project_id: `int`<a id="project_id-int"></a>

The ID of the project.

##### reimbursible: `str`<a id="reimbursible-str"></a>

Y for \"Yes\" and N for \"No\".

##### remarks: `str`<a id="remarks-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseReportsCreateNewExpenseItemResponse`](./clay_hr_python_sdk/pydantic/expense_reports_create_new_expense_item_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expenseitem` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.expense_reports.delete_expense_report`<a id="clayhrexpense_reportsdelete_expense_report"></a>

Delete expense report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_expense_report_response = clayhr.expense_reports.delete_expense_report(
    expense_report_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_report_id: `int`<a id="expense_report_id-int"></a>

The ID of the expense report.

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseReportsDeleteExpenseReportResponse`](./clay_hr_python_sdk/pydantic/expense_reports_delete_expense_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expensereport/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.expense_reports.get_by_user_id`<a id="clayhrexpense_reportsget_by_user_id"></a>

Retrieve expense reports by User ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_user_id_response = clayhr.expense_reports.get_by_user_id(
    guid="string_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### guid: `str`<a id="guid-str"></a>

The unique system generated ID of the user.

##### email: `str`<a id="email-str"></a>

Email of the user.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expensereports` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.expense_reports.get_currencies`<a id="clayhrexpense_reportsget_currencies"></a>

Retrieve currencies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_currencies_response = clayhr.expense_reports.get_currencies()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseReportsGetCurrenciesResponse`](./clay_hr_python_sdk/pydantic/expense_reports_get_currencies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/currencylist` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.expense_reports.get_expense_types`<a id="clayhrexpense_reportsget_expense_types"></a>

Retrieve expense types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_expense_types_response = clayhr.expense_reports.get_expense_types()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expensetypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.expense_reports.get_report_details`<a id="clayhrexpense_reportsget_report_details"></a>

Retrieve the details of expense report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_details_response = clayhr.expense_reports.get_report_details(
    expense_report_id=1,
    guid="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_report_id: `int`<a id="expense_report_id-int"></a>

The ID of the expense report.

##### guid: `str`<a id="guid-str"></a>

The unique system generated ID of the user.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expensereport` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.expense_reports.submit_expense_report`<a id="clayhrexpense_reportssubmit_expense_report"></a>

Submit expense report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_expense_report_response = clayhr.expense_reports.submit_expense_report(
    expense_report_id=1,
    status="DRFT",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_report_id: `int`<a id="expense_report_id-int"></a>

The ID of the expense report.

##### status: `str`<a id="status-str"></a>

Status of the expense report.

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseReportsSubmitExpenseReportResponse`](./clay_hr_python_sdk/pydantic/expense_reports_submit_expense_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expensereport/submit/{expenseReportId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.feedback.list_feedback`<a id="clayhrfeedbacklist_feedback"></a>

Retrieve feedback

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_feedback_response = clayhr.feedback.list_feedback(
    type="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of feedback to retrieve.  Choose between [\"all\", \"my\", \"team\"]. all - All Feedback, my - My Feedback, team - Team's feedback

#### 🔄 Return<a id="🔄-return"></a>

[`FeedbackListFeedbackResponse`](./clay_hr_python_sdk/pydantic/feedback_list_feedback_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rm/api/feedback` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.forms.get_assigned_forms`<a id="clayhrformsget_assigned_forms"></a>

Retrieve completed forms assigned to me  

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_assigned_forms_response = clayhr.forms.get_assigned_forms()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/my` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.forms.get_details`<a id="clayhrformsget_details"></a>

Retrieve form details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = clayhr.forms.get_details(
    dynamic_form_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dynamic_form_id: `int`<a id="dynamic_form_id-int"></a>

The ID of Form.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/view` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.forms.get_dyna_form`<a id="clayhrformsget_dyna_form"></a>

Retrieve forms

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_dyna_form_response = clayhr.forms.get_dyna_form()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/getdynaforms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.forms.get_form_response`<a id="clayhrformsget_form_response"></a>

Retrieve form response 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_form_response_response = clayhr.forms.get_form_response(
    dynamic_form_id=1,
    assign_user_id=1,
    assignment_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dynamic_form_id: `int`<a id="dynamic_form_id-int"></a>

The ID of Form.

##### assign_user_id: `int`<a id="assign_user_id-int"></a>

The ID of User.

##### assignment_id: `int`<a id="assignment_id-int"></a>

The Assignment ID of the User.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/response/{dynamicFormId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.forms.get_form_responses`<a id="clayhrformsget_form_responses"></a>

Retrieve form responses

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_form_responses_response = clayhr.forms.get_form_responses(
    dynamic_form_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dynamic_form_id: `int`<a id="dynamic_form_id-int"></a>

The ID of Form.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/responselist` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.forms.save_form_response`<a id="clayhrformssave_form_response"></a>

Save form repsonse 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_form_response_response = clayhr.forms.save_form_response(
    assignment_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assignment_id: `int`<a id="assignment_id-int"></a>

The Assignment ID of the User.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/saveFormResponse` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.forms.submit_item_response`<a id="clayhrformssubmit_item_response"></a>

Save item response

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_item_response_response = clayhr.forms.submit_item_response(
    assignment_id=1,
    item_id=1,
    response_value="responseValue_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assignment_id: `int`<a id="assignment_id-int"></a>

The Assignment ID of the User.

##### item_id: `int`<a id="item_id-int"></a>

The ID of the form Item.

##### response_value: `str`<a id="response_value-str"></a>

Response Value to save in Form.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/saveItemResponse` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.goals.create_new_goal`<a id="clayhrgoalscreate_new_goal"></a>

Create new goal

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_goal_response = clayhr.goals.create_new_goal(
    additive=1,
    begindate="1970-01-01",
    cid=1,
    comment_crediteatets="string_example",
    comment_description="string_example",
    company_goal=1,
    completion_ratio=3.14,
    create_user_id=1,
    createts_date=1,
    createts_day=1,
    createts_hours=1,
    createts_minutes=1,
    createts_month=1,
    createts_nanos=1,
    createts_seconds=1,
    createts_time=1,
    createts_timezone_offset=1,
    createts_year=1,
    crediteatets="1970-01-01T00:00:00.00Z",
    current_value=3.14,
    description="string_example",
    disposition="string_example",
    elapsed_time_ratio=3.14,
    goal_id=1,
    goal_value=3.14,
    goal_weightage=3.14,
    has_goal_approval_permission=True,
    id=1,
    initialvalue=3.14,
    is_forward=True,
    last_update_user_id=1,
    objective_id=1,
    parent_goal_id=1,
    progress_ratio=3.14,
    projectid=1,
    review_user_id=0,
    state="string_example",
    status="string_example",
    summary="string_example",
    target_date="1970-01-01",
    typecode="string_example",
    uname="string_example",
    units="string_example",
    visible_to_direct_reports=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### additive: `int`<a id="additive-int"></a>

##### begindate: `date`<a id="begindate-date"></a>

##### cid: `int`<a id="cid-int"></a>

##### comment_crediteatets: `str`<a id="comment_crediteatets-str"></a>

##### comment_description: `str`<a id="comment_description-str"></a>

##### company_goal: `int`<a id="company_goal-int"></a>

##### completion_ratio: `Union[int, float]`<a id="completion_ratio-unionint-float"></a>

##### create_user_id: `int`<a id="create_user_id-int"></a>

##### createts_date: `int`<a id="createts_date-int"></a>

##### createts_day: `int`<a id="createts_day-int"></a>

##### createts_hours: `int`<a id="createts_hours-int"></a>

##### createts_minutes: `int`<a id="createts_minutes-int"></a>

##### createts_month: `int`<a id="createts_month-int"></a>

##### createts_nanos: `int`<a id="createts_nanos-int"></a>

##### createts_seconds: `int`<a id="createts_seconds-int"></a>

##### createts_time: `int`<a id="createts_time-int"></a>

##### createts_timezone_offset: `int`<a id="createts_timezone_offset-int"></a>

##### createts_year: `int`<a id="createts_year-int"></a>

##### crediteatets: `datetime`<a id="crediteatets-datetime"></a>

##### current_value: `Union[int, float]`<a id="current_value-unionint-float"></a>

##### description: `str`<a id="description-str"></a>

##### disposition: `str`<a id="disposition-str"></a>

##### elapsed_time_ratio: `Union[int, float]`<a id="elapsed_time_ratio-unionint-float"></a>

##### goal_id: `int`<a id="goal_id-int"></a>

##### goal_value: `Union[int, float]`<a id="goal_value-unionint-float"></a>

##### goal_weightage: `Union[int, float]`<a id="goal_weightage-unionint-float"></a>

##### has_goal_approval_permission: `bool`<a id="has_goal_approval_permission-bool"></a>

##### id: `int`<a id="id-int"></a>

##### initialvalue: `Union[int, float]`<a id="initialvalue-unionint-float"></a>

##### is_forward: `bool`<a id="is_forward-bool"></a>

##### last_update_user_id: `int`<a id="last_update_user_id-int"></a>

##### objective_id: `int`<a id="objective_id-int"></a>

##### parent_goal_id: `int`<a id="parent_goal_id-int"></a>

##### progress_ratio: `Union[int, float]`<a id="progress_ratio-unionint-float"></a>

##### projectid: `int`<a id="projectid-int"></a>

##### review_user_id: `int`<a id="review_user_id-int"></a>

reviewUserId

##### state: `str`<a id="state-str"></a>

##### status: `str`<a id="status-str"></a>

##### summary: `str`<a id="summary-str"></a>

##### target_date: `date`<a id="target_date-date"></a>

##### typecode: `str`<a id="typecode-str"></a>

##### uname: `str`<a id="uname-str"></a>

##### units: `str`<a id="units-str"></a>

##### visible_to_direct_reports: `int`<a id="visible_to_direct_reports-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goal` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.goals.delete_goal`<a id="clayhrgoalsdelete_goal"></a>

Delete Goal

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_goal_response = clayhr.goals.delete_goal(
    goal_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_id: `int`<a id="goal_id-int"></a>

GoalId to delete a goal

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsDeleteGoalResponse`](./clay_hr_python_sdk/pydantic/goals_delete_goal_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/deletegoal` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.goals.get_all_goals`<a id="clayhrgoalsget_all_goals"></a>

Retrieve all goals

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_goals_response = clayhr.goals.get_all_goals()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goal` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.goals.get_goal`<a id="clayhrgoalsget_goal"></a>

Retrieve Goal

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_goal_response = clayhr.goals.get_goal(
    goalid=1,
    review_user_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goalid: `int`<a id="goalid-int"></a>

ID to get a goal.

##### review_user_id: `int`<a id="review_user_id-int"></a>

The ID of the user who is reviewee.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetGoalResponse`](./clay_hr_python_sdk/pydantic/goals_get_goal_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/getgoal` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.goals.get_user_goals`<a id="clayhrgoalsget_user_goals"></a>

Retrieve goals of user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_goals_response = clayhr.goals.get_user_goals()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetUserGoalsResponse`](./clay_hr_python_sdk/pydantic/goals_get_user_goals_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goal/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.invoice.get_by_project_id`<a id="clayhrinvoiceget_by_project_id"></a>

Retrieve invoices by Project Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_project_id_response = clayhr.invoice.get_by_project_id(
    project_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `int`<a id="project_id-int"></a>

The ID of the project

#### 🔄 Return<a id="🔄-return"></a>

[`InvoiceGetByProjectIdResponse`](./clay_hr_python_sdk/pydantic/invoice_get_by_project_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoice` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.job_profiles.get_job_profiles`<a id="clayhrjob_profilesget_job_profiles"></a>

Retrieve job profiles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_profiles_response = clayhr.job_profiles.get_job_profiles(
    status="A",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

Status of the job profile A- Active, OPEN- Open, ARCHV- Archive

#### 🔄 Return<a id="🔄-return"></a>

[`JobProfilesGetJobProfilesResponse`](./clay_hr_python_sdk/pydantic/job_profiles_get_job_profiles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/jobprofiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.leaves.add_pto_balance`<a id="clayhrleavesadd_pto_balance"></a>

Add PTO balance.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_pto_balance_response = clayhr.leaves.add_pto_balance(
    ptobalances="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ptobalances: `str`<a id="ptobalances-str"></a>

PTO Balance of user.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeavesAddPtoBalanceRequest`](./clay_hr_python_sdk/type/leaves_add_pto_balance_request.py)
ptoBalances

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/userpto/balance/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.leaves.create_new_leave`<a id="clayhrleavescreate_new_leave"></a>

Create a new leave.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_leave_response = clayhr.leaves.create_new_leave(
    date="1970-01-01",
    description="string_example",
    create_user_view_model={},
    end_date_meridiem="string_example",
    meridiem="string_example",
    number_of_days=1,
    pto_policy_model={
        "pto_policy_id": 1,
    },
    total_leave_days=3.14,
    total_leave_hours=3.14,
    user_model={
        "user_id": 1,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `date`<a id="date-date"></a>

Date of the leave.

##### description: `str`<a id="description-str"></a>

Description for the leave.

##### create_user_view_model: [`UserViewModel`](./clay_hr_python_sdk/type/user_view_model.py)<a id="create_user_view_model-userviewmodelclay_hr_python_sdktypeuser_view_modelpy"></a>


##### end_date_meridiem: `str`<a id="end_date_meridiem-str"></a>

##### meridiem: `str`<a id="meridiem-str"></a>

##### number_of_days: `int`<a id="number_of_days-int"></a>

Number of days for which leave is requested.

##### pto_policy_model: [`PtoPolicyModel`](./clay_hr_python_sdk/type/pto_policy_model.py)<a id="pto_policy_model-ptopolicymodelclay_hr_python_sdktypepto_policy_modelpy"></a>


##### total_leave_days: `Union[int, float]`<a id="total_leave_days-unionint-float"></a>

Total days of leave.

##### total_leave_hours: `Union[int, float]`<a id="total_leave_hours-unionint-float"></a>

Total hours of leave.

##### user_model: [`UserModel`](./clay_hr_python_sdk/type/user_model.py)<a id="user_model-usermodelclay_hr_python_sdktypeuser_modelpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveModel`](./clay_hr_python_sdk/type/leave_model.py)
leaveModel

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/leaverequest` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.leaves.get_leave_requests_within_date_range`<a id="clayhrleavesget_leave_requests_within_date_range"></a>

Retrieve leave requests within a date range

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_leave_requests_within_date_range_response = (
    clayhr.leaves.get_leave_requests_within_date_range(
        end_date="1970-01-01",
        start_date="1970-01-01",
        leave_userid=0,
        status="AP",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### end_date: `date`<a id="end_date-date"></a>

End date of the leave.

##### start_date: `date`<a id="start_date-date"></a>

Start date of the leave.

##### leave_userid: `int`<a id="leave_userid-int"></a>

The userId for that leave.

##### status: `str`<a id="status-str"></a>

The status of leave.   AP: Leave approved   WA: Leave is waiting for approval   RJ: Leave has been rejected   PAP: Leave is in a muti layer approval flow and has been partially approved   RCAL:  Leave was approved, taken, computed and then recalled 

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/leaverequests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.leaves.get_leaves_based_on_role`<a id="clayhrleavesget_leaves_based_on_role"></a>

Retrieve leaves for approval/rejection by filtering on basis of Role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_leaves_based_on_role_response = clayhr.leaves.get_leaves_based_on_role()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/manage/leaves` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.leaves.get_remaining_hours_credit`<a id="clayhrleavesget_remaining_hours_credit"></a>

Retrieve remaining hours credit for leave policy

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_remaining_hours_credit_response = clayhr.leaves.get_remaining_hours_credit(
    leave_date="1970-01-01",
    leave_id=1,
    leave_user_id=1,
    pto_policy_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leave_date: `date`<a id="leave_date-date"></a>

The date of the leave.

##### leave_id: `int`<a id="leave_id-int"></a>

The Id of the leave.

##### leave_user_id: `int`<a id="leave_user_id-int"></a>

The userId for that leave.

##### pto_policy_id: `int`<a id="pto_policy_id-int"></a>

The Id of the ptoPolicy

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/leave/hours/credit` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.leaves.process_leave_by_id`<a id="clayhrleavesprocess_leave_by_id"></a>

Process the leave of a user by leave Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
process_leave_by_id_response = clayhr.leaves.process_leave_by_id(
    leave_id=1,
    status="AP",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leave_id: `int`<a id="leave_id-int"></a>

The Id for the leave.

##### status: `str`<a id="status-str"></a>

The status of leave.   AP: Leave approved   WA: Leave is waiting for approval   RJ: Leave has been rejected   PAP: Leave is in a muti layer approval flow and has been partially approved   RCAL:  Leave was approved, taken, computed and then recalled 

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/process/leave` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.objective.get_by_user_id_or_specific_objective_by_id`<a id="clayhrobjectiveget_by_user_id_or_specific_objective_by_id"></a>

Retrieve objectives by user ID or specific objective by objective ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_user_id_or_specific_objective_by_id_response = (
    clayhr.objective.get_by_user_id_or_specific_objective_by_id(
        objective_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### objective_id: `str`<a id="objective_id-str"></a>

ID of Objective

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/objective` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.org_units.create_new_org_unit`<a id="clayhrorg_unitscreate_new_org_unit"></a>

Create new org unit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_org_unit_response = clayhr.org_units.create_new_org_unit(
    name="name_example",
    description="description_example",
    dept_head=1,
    dept_head_name="string_example",
    department_code="string_example",
    department_id=1,
    department_label="string_example",
    no_of_employees=1,
    parent_department_id=1,
    parent_department_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the org unit.

##### description: `str`<a id="description-str"></a>

Description of the org unit.

##### dept_head: `int`<a id="dept_head-int"></a>

The ID of the department head.

##### dept_head_name: `str`<a id="dept_head_name-str"></a>

Name of the department head.

##### department_code: `str`<a id="department_code-str"></a>

The code of the department.

##### department_id: `int`<a id="department_id-int"></a>

The ID of the department.

##### department_label: `str`<a id="department_label-str"></a>

Label for the department.

##### no_of_employees: `int`<a id="no_of_employees-int"></a>

Number of employees.

##### parent_department_id: `int`<a id="parent_department_id-int"></a>

The ID of the parent department.

##### parent_department_name: `str`<a id="parent_department_name-str"></a>

Name of the parent department.

#### 🔄 Return<a id="🔄-return"></a>

[`OrgUnitsCreateNewOrgUnitResponse`](./clay_hr_python_sdk/pydantic/org_units_create_new_org_unit_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/orgunits/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.org_units.get_org_units`<a id="clayhrorg_unitsget_org_units"></a>

Retrieve org units

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_org_units_response = clayhr.org_units.get_org_units()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/orgunits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.org_relation.get_all_active`<a id="clayhrorg_relationget_all_active"></a>

Retrieve all active OrgRelations for entire organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_active_response = clayhr.org_relation.get_all_active()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/orgrelation/allactive` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.org_relation.get_org_relations_by_user`<a id="clayhrorg_relationget_org_relations_by_user"></a>

Retrieve all the OrgRelations for the given user including Active, Archive and Future OrgRelations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_org_relations_by_user_response = clayhr.org_relation.get_org_relations_by_user(
    email="email_example",
    employee_user_id=1,
    emp_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Email for which org relation will be fetched.

##### employee_user_id: `int`<a id="employee_user_id-int"></a>

User Id for which org relation will be fetched.

##### emp_id: `str`<a id="emp_id-str"></a>

Employee Id for which org relation will be fetched.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/orgrelation/orgRelationsByUser` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.org_relation.save_user`<a id="clayhrorg_relationsave_user"></a>

Saves the OrgRelation for the User.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_user_response = clayhr.org_relation.save_user(
    org_relation_id=1,
    manager_user_id=1,
    manager_email="managerEmail_example",
    user_email="string_example",
    other_user_id=1,
    relation_type="string_example",
    start_date="1970-01-01",
    enddate="1970-01-01",
    cid=1,
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_relation_id: `int`<a id="org_relation_id-int"></a>

ID of OrgRelation for which data will be saved.

##### manager_user_id: `int`<a id="manager_user_id-int"></a>

User Id of the manager.

##### manager_email: `str`<a id="manager_email-str"></a>

Email of manager.

##### user_email: `str`<a id="user_email-str"></a>

User's email.

##### other_user_id: `int`<a id="other_user_id-int"></a>

User Id of the reporter.

##### relation_type: `str`<a id="relation_type-str"></a>

Type of relation w.r.t manager.

##### start_date: `date`<a id="start_date-date"></a>

Date of start in that org unit.

##### enddate: `date`<a id="enddate-date"></a>

Ending date in that org unit.

##### cid: `int`<a id="cid-int"></a>

Company ID.

##### status: `str`<a id="status-str"></a>

User is active or not active.

#### 🔄 Return<a id="🔄-return"></a>

[`OrgRelationSaveUserResponse`](./clay_hr_python_sdk/pydantic/org_relation_save_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/orgrelation/save` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.pay_stubs.get_details`<a id="clayhrpay_stubsget_details"></a>

Retrieve my pay stubs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = clayhr.pay_stubs.get_details()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/paystub` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.add_reports_to`<a id="clayhrpeople_and_permissionsadd_reports_to"></a>

Add reports to

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_reports_to_response = clayhr.people_and_permissions.add_reports_to(
    add_objects=[{}],
    emp_id="string_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### add_objects: [`PeopleAndPermissionsAddReportsToRequestAddObjects`](./clay_hr_python_sdk/type/people_and_permissions_add_reports_to_request_add_objects.py)<a id="add_objects-peopleandpermissionsaddreportstorequestaddobjectsclay_hr_python_sdktypepeople_and_permissions_add_reports_to_request_add_objectspy"></a>

##### emp_id: `str`<a id="emp_id-str"></a>

The unique identity of the employee. 

##### email: `str`<a id="email-str"></a>

Email address of the user.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleAndPermissionsAddReportsToRequest`](./clay_hr_python_sdk/type/people_and_permissions_add_reports_to_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PeopleAndPermissionsAddReportsToResponse`](./clay_hr_python_sdk/pydantic/people_and_permissions_add_reports_to_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/orgrelation/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.create_or_update_user_details`<a id="clayhrpeople_and_permissionscreate_or_update_user_details"></a>

Create or Update user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_or_update_user_details_response = (
    clayhr.people_and_permissions.create_or_update_user_details(
        first_name="string_example",
        email="string_example",
        last_name="string_example",
        emp_id="string_example",
        gender="string_example",
        guid="string_example",
        status="A",
        display_full_name="string_example",
        middle_name="string_example",
        second_last_name="string_example",
        short_name="string_example",
        name_pronunciation="string_example",
        family_suffix="string_example",
        worker_type="string_example",
        user_date_of_birth="string_example",
        phone="string_example",
        cell_phone="string_example",
        position=1,
        department_id=1,
        location_id=1,
        location_name="string_example",
        user_start_date="string_example",
        reports_to_email=["string_example"],
        address_list=[
            {
                "address_type": "Billing",
            }
        ],
        education_list=[{}],
        contact_list=[
            {
                "relation_to_user": "Spouse",
                "contact_type": "DEP",
                "gender": "M",
                "status": "AP",
            }
        ],
        financial_list=[
            {
                "period": "HRLY",
                "financial_type": "COMP",
                "compensation_type": "sal",
                "status": "ACTV",
            }
        ],
        custom_field_values="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

First name of user.

##### email: `str`<a id="email-str"></a>

Mail ID of user.

##### last_name: `str`<a id="last_name-str"></a>

Last name of user.

##### emp_id: `str`<a id="emp_id-str"></a>

Employee ID of the user.

##### gender: `str`<a id="gender-str"></a>

Gender of the user.

##### guid: `str`<a id="guid-str"></a>

The unique system generated ID of the user.

##### status: `str`<a id="status-str"></a>

Status of the user. A - Active, I - Inactive, F - Future Joiner

##### display_full_name: `str`<a id="display_full_name-str"></a>

Display name of the user.

##### middle_name: `str`<a id="middle_name-str"></a>

Middle name of user.

##### second_last_name: `str`<a id="second_last_name-str"></a>

Second Last name of user.

##### short_name: `str`<a id="short_name-str"></a>

Short name of user.

##### name_pronunciation: `str`<a id="name_pronunciation-str"></a>

Name Pronunciation

##### family_suffix: `str`<a id="family_suffix-str"></a>

Family Suffix

##### worker_type: `str`<a id="worker_type-str"></a>

Worker type of the user.

##### user_date_of_birth: `str`<a id="user_date_of_birth-str"></a>

Birth date of user.

##### phone: `str`<a id="phone-str"></a>

Phone number of the user.

##### cell_phone: `str`<a id="cell_phone-str"></a>

Cell phone of the user.

##### position: `int`<a id="position-int"></a>

Profile ID of the user.

##### department_id: `int`<a id="department_id-int"></a>

Org Unit ID of the user.

##### location_id: `int`<a id="location_id-int"></a>

Location ID of the user.

##### location_name: `str`<a id="location_name-str"></a>

Location of user.

##### user_start_date: `str`<a id="user_start_date-str"></a>

Start Date of user.

##### reports_to_email: [`PeopleAndPermissionsCreateOrUpdateUserDetailsRequestReportsToEmail`](./clay_hr_python_sdk/type/people_and_permissions_create_or_update_user_details_request_reports_to_email.py)<a id="reports_to_email-peopleandpermissionscreateorupdateuserdetailsrequestreportstoemailclay_hr_python_sdktypepeople_and_permissions_create_or_update_user_details_request_reports_to_emailpy"></a>

##### address_list: [`PeopleAndPermissionsCreateOrUpdateUserDetailsRequestAddressList`](./clay_hr_python_sdk/type/people_and_permissions_create_or_update_user_details_request_address_list.py)<a id="address_list-peopleandpermissionscreateorupdateuserdetailsrequestaddresslistclay_hr_python_sdktypepeople_and_permissions_create_or_update_user_details_request_address_listpy"></a>

##### education_list: [`PeopleAndPermissionsCreateOrUpdateUserDetailsRequestEducationList`](./clay_hr_python_sdk/type/people_and_permissions_create_or_update_user_details_request_education_list.py)<a id="education_list-peopleandpermissionscreateorupdateuserdetailsrequesteducationlistclay_hr_python_sdktypepeople_and_permissions_create_or_update_user_details_request_education_listpy"></a>

##### contact_list: [`PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactList`](./clay_hr_python_sdk/type/people_and_permissions_create_or_update_user_details_request_contact_list.py)<a id="contact_list-peopleandpermissionscreateorupdateuserdetailsrequestcontactlistclay_hr_python_sdktypepeople_and_permissions_create_or_update_user_details_request_contact_listpy"></a>

##### financial_list: [`PeopleAndPermissionsCreateOrUpdateUserDetailsRequestFinancialList`](./clay_hr_python_sdk/type/people_and_permissions_create_or_update_user_details_request_financial_list.py)<a id="financial_list-peopleandpermissionscreateorupdateuserdetailsrequestfinanciallistclay_hr_python_sdktypepeople_and_permissions_create_or_update_user_details_request_financial_listpy"></a>

##### custom_field_values: `str`<a id="custom_field_values-str"></a>

key - cfcode , value - cfvalue

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleAndPermissionsCreateOrUpdateUserDetailsRequest`](./clay_hr_python_sdk/type/people_and_permissions_create_or_update_user_details_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/completeUserDetails` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.create_user`<a id="clayhrpeople_and_permissionscreate_user"></a>

Create user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_user_response = clayhr.people_and_permissions.create_user(
    first_name="firstName_example",
    email="email_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

First name of user.

##### email: `str`<a id="email-str"></a>

Mail ID of user.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.create_user_compensation`<a id="clayhrpeople_and_permissionscreate_user_compensation"></a>

Create compensation for user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_user_compensation_response = (
    clayhr.people_and_permissions.create_user_compensation(
        value="value_example",
        compensation_type="sal",
        currency_code="currencyCode_example",
        period="HRLY",
        effectivedate="effectivedate_example",
        status="ACTV",
        enddate="string_example",
        notes="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### value: `str`<a id="value-str"></a>

Value of compensation

##### compensation_type: `str`<a id="compensation_type-str"></a>

Type of compensation.   sal - Salary, pay - , INCTV - Incentive, SVCR - Severance

##### currency_code: `str`<a id="currency_code-str"></a>

##### period: `str`<a id="period-str"></a>

Time period for compensation.   HRLY - Hourly, DLY - Daily, WKLY - Weekly,  BWKLY - Bi-Weekly, MTHLY - Monthly, BMTH - Bi-Monthly, QTRLY - Quarterly, BYRLY - Bi-Yearly, YRLY - Yearly,   ONEF - OneOff

##### effectivedate: `str`<a id="effectivedate-str"></a>

##### status: `str`<a id="status-str"></a>

Status of compensation.   ACTV - Active, ARCHV - Archive, PVNL - Provisional

##### enddate: `str`<a id="enddate-str"></a>

##### notes: `str`<a id="notes-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/compensation/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.delete_user_address`<a id="clayhrpeople_and_permissionsdelete_user_address"></a>

Delete User Address

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_user_address_response = clayhr.people_and_permissions.delete_user_address(
    address_id="addressId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### address_id: `str`<a id="address_id-str"></a>

The unique ID of the address.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleAndPermissionsDeleteUserAddressResponse`](./clay_hr_python_sdk/pydantic/people_and_permissions_delete_user_address_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/address/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.delete_user_education`<a id="clayhrpeople_and_permissionsdelete_user_education"></a>

Delete User Education

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_user_education_response = clayhr.people_and_permissions.delete_user_education(
    education_id="educationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### education_id: `str`<a id="education_id-str"></a>

Education ID the user

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/education/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.delete_user_employment`<a id="clayhrpeople_and_permissionsdelete_user_employment"></a>

Deletes User Employment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_user_employment_response = clayhr.people_and_permissions.delete_user_employment(
    empid=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### empid: `int`<a id="empid-int"></a>

The unique identity of the employee. 

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleAndPermissionsDeleteUserEmploymentResponse`](./clay_hr_python_sdk/pydantic/people_and_permissions_delete_user_employment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/employment/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.get_all_users_details`<a id="clayhrpeople_and_permissionsget_all_users_details"></a>

Retrieve all users details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_users_details_response = clayhr.people_and_permissions.get_all_users_details(
    name="string_example",
    page=1,
    page_size=20,
    search="string_example",
    start_date_before="1970-01-01",
    start_date_after="1970-01-01",
    end_date_before="1970-01-01",
    end_date_after="1970-01-01",
    status="A",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the user.

##### page: `int`<a id="page-int"></a>

Page number.

##### page_size: `int`<a id="page_size-int"></a>

Number of users per page.

##### search: `str`<a id="search-str"></a>

##### start_date_before: `date`<a id="start_date_before-date"></a>

The date before the assigned Start Date.

##### start_date_after: `date`<a id="start_date_after-date"></a>

The date after the assigned Start Date.

##### end_date_before: `date`<a id="end_date_before-date"></a>

The date before the assigned End Date.

##### end_date_after: `date`<a id="end_date_after-date"></a>

The date after the assigned End Date.

##### status: `str`<a id="status-str"></a>

Status of the user.    A- Active User   I- Inactive User   F- Future Joiner 

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleAndPermissionsGetAllUsersDetailsResponse`](./clay_hr_python_sdk/pydantic/people_and_permissions_get_all_users_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.get_basic_user_details`<a id="clayhrpeople_and_permissionsget_basic_user_details"></a>

Retrieve basic user details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_basic_user_details_response = clayhr.people_and_permissions.get_basic_user_details(
    name="string_example",
    page=1,
    page_size=20,
    search="string_example",
    start_date_before="1970-01-01",
    start_date_after="1970-01-01",
    end_date_before="1970-01-01",
    end_date_after="1970-01-01",
    status="A",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the user.

##### page: `int`<a id="page-int"></a>

Page number.

##### page_size: `int`<a id="page_size-int"></a>

Number of users per page.

##### search: `str`<a id="search-str"></a>

##### start_date_before: `date`<a id="start_date_before-date"></a>

The date before the assigned Start Date.

##### start_date_after: `date`<a id="start_date_after-date"></a>

The date after the assigned Start Date.

##### end_date_before: `date`<a id="end_date_before-date"></a>

The date before the assigned End Date.

##### end_date_after: `date`<a id="end_date_after-date"></a>

The date after the assigned End Date.

##### status: `str`<a id="status-str"></a>

Status of the user.    A- Active User   I- Inactive User   F- Future Joiner 

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleAndPermissionsGetBasicUserDetailsResponse`](./clay_hr_python_sdk/pydantic/people_and_permissions_get_basic_user_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/basic` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.get_financial_record`<a id="clayhrpeople_and_permissionsget_financial_record"></a>

Retrieve user financial record

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_financial_record_response = clayhr.people_and_permissions.get_financial_record(
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Email address of the user.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/compensation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.get_financial_status`<a id="clayhrpeople_and_permissionsget_financial_status"></a>

Retrieve user financial status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_financial_status_response = clayhr.people_and_permissions.get_financial_status()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/update/status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.get_user_basic_information`<a id="clayhrpeople_and_permissionsget_user_basic_information"></a>

Retrieve user basic information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_basic_information_response = (
    clayhr.people_and_permissions.get_user_basic_information(
        email="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Email of user

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/basic` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.get_user_details`<a id="clayhrpeople_and_permissionsget_user_details"></a>

Retrieve user details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_details_response = clayhr.people_and_permissions.get_user_details()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.get_user_list`<a id="clayhrpeople_and_permissionsget_user_list"></a>

Retrieve a user or list of users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_list_response = clayhr.people_and_permissions.get_user_list(
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.get_user_permissions_and_menu_configurations`<a id="clayhrpeople_and_permissionsget_user_permissions_and_menu_configurations"></a>

Retrieve user permissions and menu configurations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_permissions_and_menu_configurations_response = (
    clayhr.people_and_permissions.get_user_permissions_and_menu_configurations()
)
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/permissions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.get_users`<a id="clayhrpeople_and_permissionsget_users"></a>

Retrieve users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_users_response = clayhr.people_and_permissions.get_users(
    name="string_example",
    page=1,
    page_size=20,
    sort_by="string_example",
    sort_order="asc",
    status="A",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the user.

##### page: `int`<a id="page-int"></a>

Page number.

##### page_size: `int`<a id="page_size-int"></a>

Number of users per page.

##### sort_by: `str`<a id="sort_by-str"></a>

##### sort_order: `str`<a id="sort_order-str"></a>

Order to sort the users.   asc- Ascending Order   desc- Descending Order 

##### status: `str`<a id="status-str"></a>

Status of the user.    A- Active User   I- Inactive User   F- Future Joiner 

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleAndPermissionsGetUsersResponse`](./clay_hr_python_sdk/pydantic/people_and_permissions_get_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resource` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.save_custom_field_values`<a id="clayhrpeople_and_permissionssave_custom_field_values"></a>

Save Custom Field values

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_custom_field_values_response = (
    clayhr.people_and_permissions.save_custom_field_values(
        body=[None],
        emp_id="string_example",
        guid="string_example",
        email="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### emp_id: `str`<a id="emp_id-str"></a>

The unique identity of the employee.

##### guid: `str`<a id="guid-str"></a>

The unique system generated ID of the user.

##### email: `str`<a id="email-str"></a>

Email address of the user.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ArrayCustomFields`](./clay_hr_python_sdk/type/array_custom_fields.py)
Custom fields

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleAndPermissionsSaveCustomFieldValuesResponse`](./clay_hr_python_sdk/pydantic/people_and_permissions_save_custom_field_values_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/saveCustomFieldValues` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.save_user_address`<a id="clayhrpeople_and_permissionssave_user_address"></a>

Save User Address

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_user_address_response = clayhr.people_and_permissions.save_user_address(
    raw_body=[
        {
            "zip_code": "121121",
        }
    ],
    emp_id="string_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### raw_body: [`PeopleAndPermissionsSaveUserAddressRequestRawBody`](./clay_hr_python_sdk/type/people_and_permissions_save_user_address_request_raw_body.py)<a id="raw_body-peopleandpermissionssaveuseraddressrequestrawbodyclay_hr_python_sdktypepeople_and_permissions_save_user_address_request_raw_bodypy"></a>

##### emp_id: `str`<a id="emp_id-str"></a>

The unique identity of the employee. 

##### email: `str`<a id="email-str"></a>

Email address of the user.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleAndPermissionsSaveUserAddressRequest`](./clay_hr_python_sdk/type/people_and_permissions_save_user_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PeopleAndPermissionsSaveUserAddressResponse`](./clay_hr_python_sdk/pydantic/people_and_permissions_save_user_address_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/address/save` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.save_user_education`<a id="clayhrpeople_and_permissionssave_user_education"></a>

Save User Education

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_user_education_response = clayhr.people_and_permissions.save_user_education(
    raw_body=[
        {
            "course": "Business Administration and Management",
            "degree": "Bachelor of Liberal Arts (A.L.B.)",
            "institution": "Harvard University",
            "gpa": "98.5",
            "state": "Massachusetts",
            "city": "Cambridge",
        }
    ],
    emp_id="string_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### raw_body: [`PeopleAndPermissionsSaveUserEducationRequestRawBody`](./clay_hr_python_sdk/type/people_and_permissions_save_user_education_request_raw_body.py)<a id="raw_body-peopleandpermissionssaveusereducationrequestrawbodyclay_hr_python_sdktypepeople_and_permissions_save_user_education_request_raw_bodypy"></a>

##### emp_id: `str`<a id="emp_id-str"></a>

The unique identity of the employee. 

##### email: `str`<a id="email-str"></a>

Email address of the user.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleAndPermissionsSaveUserEducationRequest`](./clay_hr_python_sdk/type/people_and_permissions_save_user_education_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/education/save` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.save_user_employment`<a id="clayhrpeople_and_permissionssave_user_employment"></a>

Save User Employment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_user_employment_response = clayhr.people_and_permissions.save_user_employment(
    raw_body=[{}],
    emp_id="string_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### raw_body: [`PeopleAndPermissionsSaveUserEmploymentRequestRawBody`](./clay_hr_python_sdk/type/people_and_permissions_save_user_employment_request_raw_body.py)<a id="raw_body-peopleandpermissionssaveuseremploymentrequestrawbodyclay_hr_python_sdktypepeople_and_permissions_save_user_employment_request_raw_bodypy"></a>

##### emp_id: `str`<a id="emp_id-str"></a>

The unique identity of the employee. 

##### email: `str`<a id="email-str"></a>

Email address of the user.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleAndPermissionsSaveUserEmploymentRequest`](./clay_hr_python_sdk/type/people_and_permissions_save_user_employment_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/employment/save` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.update_financial_record`<a id="clayhrpeople_and_permissionsupdate_financial_record"></a>

Update financial record of User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_financial_record_response = (
    clayhr.people_and_permissions.update_financial_record(
        guid="guid_example",
        value="value_example",
        compensation_type="sal",
        currency_code="currencyCode_example",
        period="HRLY",
        status="ACTV",
        effectivedate="yyyy-mm-dd",
        enddate="yyyy-mm-dd",
        notes="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### guid: `str`<a id="guid-str"></a>

##### value: `str`<a id="value-str"></a>

##### compensation_type: `str`<a id="compensation_type-str"></a>

Type of compensation.   sal - Salary, pay - , INCTV - Incentive, SVCR - Severance

##### currency_code: `str`<a id="currency_code-str"></a>

##### period: `str`<a id="period-str"></a>

Time period for compensation.   HRLY - Hourly, DLY - Daily, WKLY - Weekly,  BWKLY - Bi-Weekly, MTHLY - Monthly, BMTH - Bi-Monthly, QTRLY - Quarterly, BYRLY - Bi-Yearly, YRLY - Yearly,   ONEF - OneOff

##### status: `str`<a id="status-str"></a>

Status of compensation.   ACTV - Active, ARCHV - Archive, PVNL - Provisional

##### effectivedate: `date`<a id="effectivedate-date"></a>

##### enddate: `date`<a id="enddate-date"></a>

##### notes: `str`<a id="notes-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/compensation/update` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.update_user`<a id="clayhrpeople_and_permissionsupdate_user"></a>

Update user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_response = clayhr.people_and_permissions.update_user(
    guid="string_example",
    email="string_example",
    emp_id="string_example",
    first_name="string_example",
    middle_name="string_example",
    last_name="string_example",
    second_last_name="string_example",
    display_full_name="string_example",
    cell_phone="string_example",
    phone="string_example",
    family_suffix="string_example",
    user_date_of_birth="1970-01-01",
    job_grade="string_example",
    user_start_date="1970-01-01",
    user_end_date="1970-01-01",
    gender="string_example",
    position="string_example",
    profile_id="string_example",
    short_name="string_example",
    status="A",
    location_name="string_example",
    location_id="string_example",
    notes="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### guid: `str`<a id="guid-str"></a>

The unique system generated ID of the user.

##### email: `str`<a id="email-str"></a>

Email address of the user.

##### emp_id: `str`<a id="emp_id-str"></a>

Employee ID of the user.   To update the employee ID, you need admin access.

##### first_name: `str`<a id="first_name-str"></a>

First name of the user.

##### middle_name: `str`<a id="middle_name-str"></a>

Last name of the user.

##### last_name: `str`<a id="last_name-str"></a>

Last name of the user.

##### second_last_name: `str`<a id="second_last_name-str"></a>

Second last name of the user.

##### display_full_name: `str`<a id="display_full_name-str"></a>

Display name of the user.

##### cell_phone: `str`<a id="cell_phone-str"></a>

Cell phone of the user.

##### phone: `str`<a id="phone-str"></a>

Phone number of the user.

##### family_suffix: `str`<a id="family_suffix-str"></a>

Family suffix of the user.

##### user_date_of_birth: `date`<a id="user_date_of_birth-date"></a>

Date of birth of the user.

##### job_grade: `str`<a id="job_grade-str"></a>

Job grade of the user.

##### user_start_date: `date`<a id="user_start_date-date"></a>

Starting date of the user.

##### user_end_date: `date`<a id="user_end_date-date"></a>

End date of the user.

##### gender: `str`<a id="gender-str"></a>

Gender of the user.

##### position: `str`<a id="position-str"></a>

Position of the user.

##### profile_id: `str`<a id="profile_id-str"></a>

Profile ID of the user.

##### short_name: `str`<a id="short_name-str"></a>

Short name of the user.

##### status: `str`<a id="status-str"></a>

Status of the user.

##### location_name: `str`<a id="location_name-str"></a>

Location of the user.

##### location_id: `str`<a id="location_id-str"></a>

Location ID of user location.

##### notes: `str`<a id="notes-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/update` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.people_and_permissions.upload_user_profile_picture`<a id="clayhrpeople_and_permissionsupload_user_profile_picture"></a>

 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_user_profile_picture_response = (
    clayhr.people_and_permissions.upload_user_profile_picture(
        file=open("/path/to/file", "rb"),
        userid="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

Upload the profile picture here.

##### userid: `str`<a id="userid-str"></a>

The ID of the user whose profile picture has to be updated.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PeopleAndPermissionsUploadUserProfilePictureRequest`](./clay_hr_python_sdk/type/people_and_permissions_upload_user_profile_picture_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PeopleAndPermissionsUploadUserProfilePictureResponse`](./clay_hr_python_sdk/pydantic/people_and_permissions_upload_user_profile_picture_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/uploadpicture` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.performance_review.create_performance_review`<a id="clayhrperformance_reviewcreate_performance_review"></a>

Create Performance Review

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_performance_review_response = (
    clayhr.performance_review.create_performance_review(
        template_id=1,
        start_date="2022-10-02",
        end_date="2022-10-02",
        appraisal_type="Annual",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `int`<a id="template_id-int"></a>

The ID of the performance review template.

##### start_date: `date`<a id="start_date-date"></a>

Start Date of the performance review.

##### end_date: `date`<a id="end_date-date"></a>

End Date of the performance review.

##### appraisal_type: `str`<a id="appraisal_type-str"></a>

Review Period

#### 🔄 Return<a id="🔄-return"></a>

[`PerformanceReviewCreatePerformanceReviewResponse`](./clay_hr_python_sdk/pydantic/performance_review_create_performance_review_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/appraisal/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.performance_review.get_completed_reviews_based_on_user_id`<a id="clayhrperformance_reviewget_completed_reviews_based_on_user_id"></a>

Retrieve Completed Performance Reviews

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_completed_reviews_based_on_user_id_response = (
    clayhr.performance_review.get_completed_reviews_based_on_user_id(
        target_user_id=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### target_user_id: `int`<a id="target_user_id-int"></a>

The ID of the user.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/appraisal/getCompletedReviews` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.performance_review.get_performance_reviews`<a id="clayhrperformance_reviewget_performance_reviews"></a>

Retrieve Performance Reviews

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_performance_reviews_response = clayhr.performance_review.get_performance_reviews()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/appraisal/user` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.performance_review.get_templates`<a id="clayhrperformance_reviewget_templates"></a>

Retrieve Performance Review Templates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_templates_response = clayhr.performance_review.get_templates()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/appraisal/template/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.performance_review.launch_performance_reviews_in_bulk`<a id="clayhrperformance_reviewlaunch_performance_reviews_in_bulk"></a>

Launch Performance Reviews In Bulk

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
launch_performance_reviews_in_bulk_response = (
    clayhr.performance_review.launch_performance_reviews_in_bulk(
        template_id="string_example",
        review_type="string_example",
        start_date="string_example",
        end_date="string_example",
        import_goals="string_example",
        import_job_profile_skills="string_example",
        import_skills="string_example",
        user_id_list="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

##### review_type: `str`<a id="review_type-str"></a>

##### start_date: `str`<a id="start_date-str"></a>

##### end_date: `str`<a id="end_date-str"></a>

##### import_goals: `str`<a id="import_goals-str"></a>

##### import_job_profile_skills: `str`<a id="import_job_profile_skills-str"></a>

##### import_skills: `str`<a id="import_skills-str"></a>

##### user_id_list: `str`<a id="user_id_list-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/appraisal/bulkLaunch` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.performance_review_assignment.get_assignments`<a id="clayhrperformance_review_assignmentget_assignments"></a>

Retrieve Performance Review Assignments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_assignments_response = clayhr.performance_review_assignment.get_assignments()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/appraisal/assignment` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.positions.create_position`<a id="clayhrpositionscreate_position"></a>

Save Position

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_position_response = clayhr.positions.create_position(
    name="name_example",
    count=1,
    status="OPEN",
    access_level="pvt",
    date_open="dateOpen_example",
    date_close="dateClose_example",
    position_uid="positionUID_example",
    funnel_id=1,
    description="string_example",
    requirements="string_example",
    responsibilities="string_example",
    projectid=1,
    approval_flow_id=1,
    locationid=1,
    department_id="string_example",
    profileid=1,
    recruiter_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of Position

##### count: `int`<a id="count-int"></a>

Number of openings

##### status: `str`<a id="status-str"></a>

Status of Position

##### access_level: `str`<a id="access_level-str"></a>

Access level of Position   'pvt' - Private, 'ijp' - Publish Internally, 'pub' - Public

##### date_open: `str`<a id="date_open-str"></a>

Date of Opening

##### date_close: `str`<a id="date_close-str"></a>

Date of Closing

##### position_uid: `str`<a id="position_uid-str"></a>

Unique Identity of Position

##### funnel_id: `int`<a id="funnel_id-int"></a>

Candidate Funnel ID of Position

##### description: `str`<a id="description-str"></a>

Description of Position

##### requirements: `str`<a id="requirements-str"></a>

Requirements of Position

##### responsibilities: `str`<a id="responsibilities-str"></a>

Responsibilities of Position

##### projectid: `int`<a id="projectid-int"></a>

Project ID of Position

##### approval_flow_id: `int`<a id="approval_flow_id-int"></a>

Position Approval Flow ID of Position

##### locationid: `int`<a id="locationid-int"></a>

Location ID of Position

##### department_id: `str`<a id="department_id-str"></a>

Department ID of Position

##### profileid: `int`<a id="profileid-int"></a>

Profile ID of Position

##### recruiter_id: `int`<a id="recruiter_id-int"></a>

ID of Recruiter

#### 🔄 Return<a id="🔄-return"></a>

[`PositionsCreatePositionResponse`](./clay_hr_python_sdk/pydantic/positions_create_position_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/position/save` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.positions.get_position`<a id="clayhrpositionsget_position"></a>

Retrieve position

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_position_response = clayhr.positions.get_position(
    positionid=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### positionid: `int`<a id="positionid-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/position/view` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.positions.get_positions_list`<a id="clayhrpositionsget_positions_list"></a>

Retrieve positions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_positions_list_response = clayhr.positions.get_positions_list(
    search="string_example",
    page=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### search: `str`<a id="search-str"></a>

##### page: `int`<a id="page-int"></a>

Page number

##### page_size: `int`<a id="page_size-int"></a>

Number of users per page

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/position/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.project.assign_user_allocation`<a id="clayhrprojectassign_user_allocation"></a>

Assigns the project to the user based on the project ID and user ID and returns the userProjectId, which is the ID of the assignment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_user_allocation_response = clayhr.project.assign_user_allocation(
    project_id=1,
    user_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `int`<a id="project_id-int"></a>

The ID of the project.

##### user_id: `int`<a id="user_id-int"></a>

The ID of the user to whom the project should be assigned.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectAssignUserAllocationRequest`](./clay_hr_python_sdk/type/project_assign_user_allocation_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/projects/allocation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.project.create_new`<a id="clayhrprojectcreate_new"></a>

Create a new project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = clayhr.project.create_new(
    project_name="Machine Learning",
    project_desc="The project relates to the machine learning services.",
    short_code="ML_007",
    start_date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_name: `str`<a id="project_name-str"></a>

Name of the project.

##### project_desc: `str`<a id="project_desc-str"></a>

Description of the project.

##### short_code: `str`<a id="short_code-str"></a>

A unique short code to identify the project.

##### start_date: `date`<a id="start_date-date"></a>

Start date of the project.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectCreateNewRequest`](./clay_hr_python_sdk/type/project_create_new_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/projects` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.project.details_by_id`<a id="clayhrprojectdetails_by_id"></a>

Retrieve the details of the Project by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
details_by_id_response = clayhr.project.details_by_id(
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

The ID of the project.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/projects/{projectId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.project.list_allocations`<a id="clayhrprojectlist_allocations"></a>

Returns all user allocations for the project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_allocations_response = clayhr.project.list_allocations(
    project_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `int`<a id="project_id-int"></a>

The ID of the project.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/projects/allocation/{projectId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.project.list_projects`<a id="clayhrprojectlist_projects"></a>

Returns a list of projects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_projects_response = clayhr.project.list_projects()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.reports.get_content_by_analytic_id`<a id="clayhrreportsget_content_by_analytic_id"></a>

Get content for report by analytic Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_by_analytic_id_response = clayhr.reports.get_content_by_analytic_id(
    analytic_id="analyticId_example",
    authorization="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### analytic_id: `str`<a id="analytic_id-str"></a>

analyticId

##### authorization: `str`<a id="authorization-str"></a>

Authorization

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/report/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.reports.get_content_for_report`<a id="clayhrreportsget_content_for_report"></a>

Retrieve report content

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_for_report_response = clayhr.reports.get_content_for_report(
    analytic_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### analytic_id: `int`<a id="analytic_id-int"></a>

The ID of the report.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetContentForReportResponse`](./clay_hr_python_sdk/pydantic/reports_get_content_for_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.reports.get_report_details`<a id="clayhrreportsget_report_details"></a>

Get report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_details_response = clayhr.reports.get_report_details(
    analytic_id="analyticId_example",
    authorization="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### analytic_id: `str`<a id="analytic_id-str"></a>

analyticId

##### authorization: `str`<a id="authorization-str"></a>

Authorization

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.shifts.list_shifts_using_get`<a id="clayhrshiftslist_shifts_using_get"></a>

Get Shifts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_shifts_using_get_response = clayhr.shifts.list_shifts_using_get(
    project_id=1,
    start_date="string_example",
    end_date="string_example",
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `int`<a id="project_id-int"></a>

projectId

##### start_date: `str`<a id="start_date-str"></a>

startDate

##### end_date: `str`<a id="end_date-str"></a>

endDate

##### status: `str`<a id="status-str"></a>

status

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/shifts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.shifts.save_shift`<a id="clayhrshiftssave_shift"></a>

Save Shift

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_shift_response = clayhr.shifts.save_shift(
    body="body_example",
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`str`
shiftBody

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/shifts/save` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.skills.create_new_skill`<a id="clayhrskillscreate_new_skill"></a>

Create a new skill

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_skill_response = clayhr.skills.create_new_skill(
    description="string_example",
    skill_code="string_example",
    assessment_model={
        "scoretemplateid": 1,
        "status": "A",
    },
    skill_type_model={
        "skill_type_id": 1,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description of the skill.

##### skill_code: `str`<a id="skill_code-str"></a>

The title of the skill.

##### assessment_model: [`SkillsCreateNewSkillRequestAssessmentModel`](./clay_hr_python_sdk/type/skills_create_new_skill_request_assessment_model.py)<a id="assessment_model-skillscreatenewskillrequestassessmentmodelclay_hr_python_sdktypeskills_create_new_skill_request_assessment_modelpy"></a>


##### skill_type_model: [`SkillsCreateNewSkillRequestSkillTypeModel`](./clay_hr_python_sdk/type/skills_create_new_skill_request_skill_type_model.py)<a id="skill_type_model-skillscreatenewskillrequestskilltypemodelclay_hr_python_sdktypeskills_create_new_skill_request_skill_type_modelpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SkillsCreateNewSkillRequest`](./clay_hr_python_sdk/type/skills_create_new_skill_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SkillsCreateNewSkillResponse`](./clay_hr_python_sdk/pydantic/skills_create_new_skill_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skill/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.skills.get_skills`<a id="clayhrskillsget_skills"></a>

Retrieve skills

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_skills_response = clayhr.skills.get_skills()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SkillsGetSkillsResponse`](./clay_hr_python_sdk/pydantic/skills_get_skills_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skills` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.skills.get_user_assigned_skills`<a id="clayhrskillsget_user_assigned_skills"></a>

Retrieve skills assigned to a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_assigned_skills_response = clayhr.skills.get_user_assigned_skills(
    assigned_user_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assigned_user_id: `int`<a id="assigned_user_id-int"></a>

The ID of the user whose skills should be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`SkillsGetUserAssignedSkillsResponse`](./clay_hr_python_sdk/pydantic/skills_get_user_assigned_skills_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/userSkill` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.survey.create_item_response`<a id="clayhrsurveycreate_item_response"></a>

Create the item's response for a survey

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_item_response_response = clayhr.survey.create_item_response(
    assignment_id=1,
    item_id=1,
    response_value="responseValue_example",
    authorization="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assignment_id: `int`<a id="assignment_id-int"></a>

assignmentId

##### item_id: `int`<a id="item_id-int"></a>

itemId

##### response_value: `str`<a id="response_value-str"></a>

responseValue

##### authorization: `str`<a id="authorization-str"></a>

Authorization

#### 🔄 Return<a id="🔄-return"></a>

[`SurveyCreateItemResponseResponse`](./clay_hr_python_sdk/pydantic/survey_create_item_response_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/survey/item/save` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.survey.create_response_by_assignment_id`<a id="clayhrsurveycreate_response_by_assignment_id"></a>

Create a survey response by assignment id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response_by_assignment_id_response = (
    clayhr.survey.create_response_by_assignment_id(
        assignment_id=1,
        authorization="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assignment_id: `int`<a id="assignment_id-int"></a>

assignmentId

##### authorization: `str`<a id="authorization-str"></a>

Authorization

#### 🔄 Return<a id="🔄-return"></a>

[`SurveyCreateResponseByAssignmentIdResponse`](./clay_hr_python_sdk/pydantic/survey_create_response_by_assignment_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/survey/save` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.survey.details_by_form_id`<a id="clayhrsurveydetails_by_form_id"></a>

Get the details of a survey form by form id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
details_by_form_id_response = clayhr.survey.details_by_form_id(
    authorization="string_example",
    dynamic_form_id=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

Authorization

##### dynamic_form_id: `int`<a id="dynamic_form_id-int"></a>

dynamicFormId

#### 🔄 Return<a id="🔄-return"></a>

[`SurveyDetailsByFormIdResponse`](./clay_hr_python_sdk/pydantic/survey_details_by_form_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/survey/view` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.survey.get_all_survey_responses`<a id="clayhrsurveyget_all_survey_responses"></a>

This page will help you get started with Surveys.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_survey_responses_response = clayhr.survey.get_all_survey_responses(
    survey_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### survey_id: `int`<a id="survey_id-int"></a>

The ID of the survey.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/survey/allresponses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.survey.get_list`<a id="clayhrsurveyget_list"></a>

Get a list of surveys

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = clayhr.survey.get_list(
    authorization="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

Authorization

#### 🔄 Return<a id="🔄-return"></a>

[`SurveyGetListResponse`](./clay_hr_python_sdk/pydantic/survey_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/survey/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.test.get_test`<a id="clayhrtestget_test"></a>

Retrieve test

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_test_response = clayhr.test.get_test(
    status="A",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

The status of test - Choose between [\"A-Active\", \"ARCHV-Archive\", \"DRAFT-Draft\"].

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/test` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.clock_out`<a id="clayhrtimecardsclock_out"></a>

Clock Out

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
clock_out_response = clayhr.timecards.clock_out(
    authorization="Authorization_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

Authorization

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timecard/clock/out` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.create_past_timecard`<a id="clayhrtimecardscreate_past_timecard"></a>

Create a past timecard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_past_timecard_response = clayhr.timecards.create_past_timecard(
    authorization="Authorization_example",
    activity="string_example",
    amount=3.14,
    approval_rejection_reason="string_example",
    billable="string_example",
    card_id=1,
    case_num="string_example",
    case_url="string_example",
    category_code="string_example",
    charge_type="string_example",
    cid=1,
    create_user_id=1,
    createts_date=1,
    createts_day=1,
    createts_hours=1,
    createts_minutes=1,
    createts_month=1,
    createts_nanos=1,
    createts_seconds=1,
    createts_time=1,
    createts_timezone_offset=1,
    createts_year=1,
    custom_hours="string_example",
    date="1970-01-01",
    description="string_example",
    elapsed_time_date=1,
    elapsed_time_day=1,
    elapsed_time_hours=1,
    elapsed_time_minutes=1,
    elapsed_time_month=1,
    elapsed_time_seconds=1,
    elapsed_time_time=1,
    elapsed_time_timezone_offset=1,
    elapsed_time_year=1,
    end_date_time_date=1,
    end_date_time_day=1,
    end_date_time_hours=1,
    end_date_time_minutes=1,
    end_date_time_month=1,
    end_date_time_nanos=1,
    end_date_time_seconds=1,
    end_date_time_time=1,
    end_date_time_timezone_offset=1,
    end_date_time_year=1,
    end_date_time_str="string_example",
    id=1,
    invoice_id=1,
    notes="string_example",
    number_of_days=1,
    payment_date="1970-01-01",
    project_id=1,
    project_manager="string_example",
    project_model_account=1,
    pto_computed="string_example",
    source="string_example",
    start_date_time_date=1,
    start_date_time_day=1,
    start_date_time_hours=1,
    start_date_time_minutes=1,
    start_date_time_month=1,
    start_date_time_nanos=1,
    start_date_time_seconds=1,
    start_date_time_time=1,
    start_date_time_timezone_offset=1,
    start_date_time_year=1,
    start_date_time_str="string_example",
    status="string_example",
    sum_of_elapsed_time="string_example",
    timesheet_id=1,
    timezone="string_example",
    used_time=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

Authorization

##### activity: `str`<a id="activity-str"></a>

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

##### approval_rejection_reason: `str`<a id="approval_rejection_reason-str"></a>

##### billable: `str`<a id="billable-str"></a>

##### card_id: `int`<a id="card_id-int"></a>

##### case_num: `str`<a id="case_num-str"></a>

##### case_url: `str`<a id="case_url-str"></a>

##### category_code: `str`<a id="category_code-str"></a>

##### charge_type: `str`<a id="charge_type-str"></a>

##### cid: `int`<a id="cid-int"></a>

##### create_user_id: `int`<a id="create_user_id-int"></a>

##### createts_date: `int`<a id="createts_date-int"></a>

##### createts_day: `int`<a id="createts_day-int"></a>

##### createts_hours: `int`<a id="createts_hours-int"></a>

##### createts_minutes: `int`<a id="createts_minutes-int"></a>

##### createts_month: `int`<a id="createts_month-int"></a>

##### createts_nanos: `int`<a id="createts_nanos-int"></a>

##### createts_seconds: `int`<a id="createts_seconds-int"></a>

##### createts_time: `int`<a id="createts_time-int"></a>

##### createts_timezone_offset: `int`<a id="createts_timezone_offset-int"></a>

##### createts_year: `int`<a id="createts_year-int"></a>

##### custom_hours: `str`<a id="custom_hours-str"></a>

##### date: `date`<a id="date-date"></a>

##### description: `str`<a id="description-str"></a>

##### elapsed_time_date: `int`<a id="elapsed_time_date-int"></a>

##### elapsed_time_day: `int`<a id="elapsed_time_day-int"></a>

##### elapsed_time_hours: `int`<a id="elapsed_time_hours-int"></a>

##### elapsed_time_minutes: `int`<a id="elapsed_time_minutes-int"></a>

##### elapsed_time_month: `int`<a id="elapsed_time_month-int"></a>

##### elapsed_time_seconds: `int`<a id="elapsed_time_seconds-int"></a>

##### elapsed_time_time: `int`<a id="elapsed_time_time-int"></a>

##### elapsed_time_timezone_offset: `int`<a id="elapsed_time_timezone_offset-int"></a>

##### elapsed_time_year: `int`<a id="elapsed_time_year-int"></a>

##### end_date_time_date: `int`<a id="end_date_time_date-int"></a>

##### end_date_time_day: `int`<a id="end_date_time_day-int"></a>

##### end_date_time_hours: `int`<a id="end_date_time_hours-int"></a>

##### end_date_time_minutes: `int`<a id="end_date_time_minutes-int"></a>

##### end_date_time_month: `int`<a id="end_date_time_month-int"></a>

##### end_date_time_nanos: `int`<a id="end_date_time_nanos-int"></a>

##### end_date_time_seconds: `int`<a id="end_date_time_seconds-int"></a>

##### end_date_time_time: `int`<a id="end_date_time_time-int"></a>

##### end_date_time_timezone_offset: `int`<a id="end_date_time_timezone_offset-int"></a>

##### end_date_time_year: `int`<a id="end_date_time_year-int"></a>

##### end_date_time_str: `str`<a id="end_date_time_str-str"></a>

##### id: `int`<a id="id-int"></a>

##### invoice_id: `int`<a id="invoice_id-int"></a>

##### notes: `str`<a id="notes-str"></a>

##### number_of_days: `int`<a id="number_of_days-int"></a>

##### payment_date: `date`<a id="payment_date-date"></a>

##### project_id: `int`<a id="project_id-int"></a>

##### project_manager: `str`<a id="project_manager-str"></a>

##### project_model_account: `int`<a id="project_model_account-int"></a>

##### pto_computed: `str`<a id="pto_computed-str"></a>

##### source: `str`<a id="source-str"></a>

##### start_date_time_date: `int`<a id="start_date_time_date-int"></a>

##### start_date_time_day: `int`<a id="start_date_time_day-int"></a>

##### start_date_time_hours: `int`<a id="start_date_time_hours-int"></a>

##### start_date_time_minutes: `int`<a id="start_date_time_minutes-int"></a>

##### start_date_time_month: `int`<a id="start_date_time_month-int"></a>

##### start_date_time_nanos: `int`<a id="start_date_time_nanos-int"></a>

##### start_date_time_seconds: `int`<a id="start_date_time_seconds-int"></a>

##### start_date_time_time: `int`<a id="start_date_time_time-int"></a>

##### start_date_time_timezone_offset: `int`<a id="start_date_time_timezone_offset-int"></a>

##### start_date_time_year: `int`<a id="start_date_time_year-int"></a>

##### start_date_time_str: `str`<a id="start_date_time_str-str"></a>

##### status: `str`<a id="status-str"></a>

##### sum_of_elapsed_time: `str`<a id="sum_of_elapsed_time-str"></a>

##### timesheet_id: `int`<a id="timesheet_id-int"></a>

##### timezone: `str`<a id="timezone-str"></a>

##### used_time: `int`<a id="used_time-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timecard/clockin` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.create_timecard`<a id="clayhrtimecardscreate_timecard"></a>

Create a new timecard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_timecard_response = clayhr.timecards.create_timecard(
    createts_date=1,
    createts_day=1,
    createts_hours=1,
    createts_minutes=1,
    createts_month=1,
    createts_nanos=1,
    createts_seconds=1,
    createts_time=1,
    createts_timezone_offset=1,
    createts_year=1,
    custom_hours="string_example",
    date="1970-01-01",
    description="string_example",
    elapsed_time_date=1,
    elapsed_time_day=1,
    elapsed_time_hours=1,
    elapsed_time_minutes=1,
    elapsed_time_month=1,
    elapsed_time_seconds=1,
    elapsed_time_time=1,
    elapsed_time_timezone_offset=1,
    elapsed_time_year=1,
    end_date_time_date=1,
    end_date_time_day=1,
    end_date_time_hours=1,
    end_date_time_minutes=1,
    end_date_time_month=1,
    end_date_time_nanos=1,
    end_date_time_seconds=1,
    end_date_time_time=1,
    end_date_time_timezone_offset=1,
    end_date_time_year=1,
    end_date_time_str="string_example",
    id=1,
    invoice_id=1,
    notes="string_example",
    number_of_days=1,
    payment_date="1970-01-01",
    project_id=1,
    project_manager="string_example",
    project_model_account=1,
    timesheet_id=1,
    timezone="string_example",
    used_time=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### createts_date: `int`<a id="createts_date-int"></a>

##### createts_day: `int`<a id="createts_day-int"></a>

##### createts_hours: `int`<a id="createts_hours-int"></a>

##### createts_minutes: `int`<a id="createts_minutes-int"></a>

##### createts_month: `int`<a id="createts_month-int"></a>

##### createts_nanos: `int`<a id="createts_nanos-int"></a>

##### createts_seconds: `int`<a id="createts_seconds-int"></a>

##### createts_time: `int`<a id="createts_time-int"></a>

##### createts_timezone_offset: `int`<a id="createts_timezone_offset-int"></a>

##### createts_year: `int`<a id="createts_year-int"></a>

##### custom_hours: `str`<a id="custom_hours-str"></a>

##### date: `date`<a id="date-date"></a>

##### description: `str`<a id="description-str"></a>

##### elapsed_time_date: `int`<a id="elapsed_time_date-int"></a>

##### elapsed_time_day: `int`<a id="elapsed_time_day-int"></a>

##### elapsed_time_hours: `int`<a id="elapsed_time_hours-int"></a>

##### elapsed_time_minutes: `int`<a id="elapsed_time_minutes-int"></a>

##### elapsed_time_month: `int`<a id="elapsed_time_month-int"></a>

##### elapsed_time_seconds: `int`<a id="elapsed_time_seconds-int"></a>

##### elapsed_time_time: `int`<a id="elapsed_time_time-int"></a>

##### elapsed_time_timezone_offset: `int`<a id="elapsed_time_timezone_offset-int"></a>

##### elapsed_time_year: `int`<a id="elapsed_time_year-int"></a>

##### end_date_time_date: `int`<a id="end_date_time_date-int"></a>

##### end_date_time_day: `int`<a id="end_date_time_day-int"></a>

##### end_date_time_hours: `int`<a id="end_date_time_hours-int"></a>

##### end_date_time_minutes: `int`<a id="end_date_time_minutes-int"></a>

##### end_date_time_month: `int`<a id="end_date_time_month-int"></a>

##### end_date_time_nanos: `int`<a id="end_date_time_nanos-int"></a>

##### end_date_time_seconds: `int`<a id="end_date_time_seconds-int"></a>

##### end_date_time_time: `int`<a id="end_date_time_time-int"></a>

##### end_date_time_timezone_offset: `int`<a id="end_date_time_timezone_offset-int"></a>

##### end_date_time_year: `int`<a id="end_date_time_year-int"></a>

##### end_date_time_str: `str`<a id="end_date_time_str-str"></a>

##### id: `int`<a id="id-int"></a>

##### invoice_id: `int`<a id="invoice_id-int"></a>

##### notes: `str`<a id="notes-str"></a>

##### number_of_days: `int`<a id="number_of_days-int"></a>

##### payment_date: `date`<a id="payment_date-date"></a>

##### project_id: `int`<a id="project_id-int"></a>

##### project_manager: `str`<a id="project_manager-str"></a>

##### project_model_account: `int`<a id="project_model_account-int"></a>

##### timesheet_id: `int`<a id="timesheet_id-int"></a>

##### timezone: `str`<a id="timezone-str"></a>

##### used_time: `int`<a id="used_time-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timecard/addtimecard` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.get_by_user_id`<a id="clayhrtimecardsget_by_user_id"></a>

Retrieve timecard details based on User ID with Add Time Cards For Other permission.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_user_id_response = clayhr.timecards.get_by_user_id(
    email="string_example",
    guid="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

email of the user.

##### guid: `str`<a id="guid-str"></a>

Graphical user ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/timecard` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.get_by_user_id_0`<a id="clayhrtimecardsget_by_user_id_0"></a>

Retrieve timecard basic details based on User ID with Add Time Cards For Other permission.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_user_id_0_response = clayhr.timecards.get_by_user_id_0(
    email="string_example",
    guid="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

email of the user.

##### guid: `str`<a id="guid-str"></a>

Graphical user ID.

#### 🔄 Return<a id="🔄-return"></a>

[`TimecardsGetByUserId200Response`](./clay_hr_python_sdk/pydantic/timecards_get_by_user_id200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/user/timecards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.get_details_by_timecard_id`<a id="clayhrtimecardsget_details_by_timecard_id"></a>

Retrieve timecard details based on timecard ID with Add Time Cards For Other permission.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_by_timecard_id_response = clayhr.timecards.get_details_by_timecard_id(
    timecard_id=1,
    flatcustomfields=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timecard_id: `int`<a id="timecard_id-int"></a>

Timecard ID of the timecard.

##### flatcustomfields: `bool`<a id="flatcustomfields-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timecards/details/{timecardId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.get_tvc_for_clockin_with_qr_code_using_cid`<a id="clayhrtimecardsget_tvc_for_clockin_with_qr_code_using_cid"></a>

TVC code for clockin with QR Code using cid.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tvc_for_clockin_with_qr_code_using_cid_response = (
    clayhr.timecards.get_tvc_for_clockin_with_qr_code_using_cid(
        cid=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cid: `int`<a id="cid-int"></a>

cid

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/verify/tvc` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.get_user_by_id`<a id="clayhrtimecardsget_user_by_id"></a>

Get timecards by user id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_id_response = clayhr.timecards.get_user_by_id(
    authorization="Authorization_example",
    type="leave",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

Authorization

##### type: `str`<a id="type-str"></a>

type

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timecard` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.register_device_for_clock_in_with_asset_model`<a id="clayhrtimecardsregister_device_for_clock_in_with_asset_model"></a>

Register device for ClockIn with AssetModel.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
register_device_for_clock_in_with_asset_model_response = (
    clayhr.timecards.register_device_for_clock_in_with_asset_model(
        accessories="string_example",
        acknowledge=1,
        asset_id=1,
        assetno="string_example",
        assetstatus="string_example",
        assettype="string_example",
        purchase_date="1970-01-01",
        self_assign=1,
        serialno="string_example",
        service="string_example",
        source="string_example",
        specs="string_example",
        supplier="string_example",
        use_status_code="string_example",
        user_domain="string_example",
        user_mail="string_example",
        user_password="string_example",
        uuid="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### accessories: `str`<a id="accessories-str"></a>

##### acknowledge: `int`<a id="acknowledge-int"></a>

##### asset_id: `int`<a id="asset_id-int"></a>

##### assetno: `str`<a id="assetno-str"></a>

##### assetstatus: `str`<a id="assetstatus-str"></a>

##### assettype: `str`<a id="assettype-str"></a>

##### purchase_date: `date`<a id="purchase_date-date"></a>

##### self_assign: `int`<a id="self_assign-int"></a>

##### serialno: `str`<a id="serialno-str"></a>

##### service: `str`<a id="service-str"></a>

##### source: `str`<a id="source-str"></a>

##### specs: `str`<a id="specs-str"></a>

##### supplier: `str`<a id="supplier-str"></a>

##### use_status_code: `str`<a id="use_status_code-str"></a>

##### user_domain: `str`<a id="user_domain-str"></a>

##### user_mail: `str`<a id="user_mail-str"></a>

##### user_password: `str`<a id="user_password-str"></a>

##### uuid: `str`<a id="uuid-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/register` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.verify_device_with_device_uuid`<a id="clayhrtimecardsverify_device_with_device_uuid"></a>

Device verification with DeviceUUID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_device_with_device_uuid_response = (
    clayhr.timecards.verify_device_with_device_uuid(
        device_uuid="deviceUUID_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_uuid: `str`<a id="device_uuid-str"></a>

deviceUUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/verify/device` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timecards.verify_user_with_userid`<a id="clayhrtimecardsverify_user_with_userid"></a>

User verification with userid.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_user_with_userid_response = clayhr.timecards.verify_user_with_userid(
    adp_associate_oid="string_example",
    allocation=3.14,
    apple_user_identifier="string_example",
    assignments="string_example",
    auth_token="string_example",
    cal_week_pref="string_example",
    calendar_id=1,
    candidate_id=1,
    career_pathway_id=1,
    cell_phone="string_example",
    cid=1,
    country_id=1,
    createts_date=1,
    createts_day=1,
    createts_hours=1,
    createts_minutes=1,
    createts_month=1,
    createts_nanos=1,
    createts_seconds=1,
    createts_time=1,
    createts_timezone_offset=1,
    createts_year=1,
    createuserid=1,
    thumbnail="string_example",
    timecard_period_pref="string_example",
    timezone="string_example",
    tos_version="string_example",
    user_country="string_example",
    user_date_format="string_example",
    user_date_of_birth="1970-01-01",
    user_display_name="string_example",
    user_end_date="1970-01-01",
    user_name="string_example",
    user_name_format="string_example",
    user_type="string_example",
    view=True,
    worker_type="string_example",
    working_days="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### adp_associate_oid: `str`<a id="adp_associate_oid-str"></a>

##### allocation: `Union[int, float]`<a id="allocation-unionint-float"></a>

##### apple_user_identifier: `str`<a id="apple_user_identifier-str"></a>

##### assignments: `str`<a id="assignments-str"></a>

##### auth_token: `str`<a id="auth_token-str"></a>

##### cal_week_pref: `str`<a id="cal_week_pref-str"></a>

##### calendar_id: `int`<a id="calendar_id-int"></a>

##### candidate_id: `int`<a id="candidate_id-int"></a>

##### career_pathway_id: `int`<a id="career_pathway_id-int"></a>

##### cell_phone: `str`<a id="cell_phone-str"></a>

##### cid: `int`<a id="cid-int"></a>

##### country_id: `int`<a id="country_id-int"></a>

##### createts_date: `int`<a id="createts_date-int"></a>

##### createts_day: `int`<a id="createts_day-int"></a>

##### createts_hours: `int`<a id="createts_hours-int"></a>

##### createts_minutes: `int`<a id="createts_minutes-int"></a>

##### createts_month: `int`<a id="createts_month-int"></a>

##### createts_nanos: `int`<a id="createts_nanos-int"></a>

##### createts_seconds: `int`<a id="createts_seconds-int"></a>

##### createts_time: `int`<a id="createts_time-int"></a>

##### createts_timezone_offset: `int`<a id="createts_timezone_offset-int"></a>

##### createts_year: `int`<a id="createts_year-int"></a>

##### createuserid: `int`<a id="createuserid-int"></a>

##### thumbnail: `str`<a id="thumbnail-str"></a>

##### timecard_period_pref: `str`<a id="timecard_period_pref-str"></a>

##### timezone: `str`<a id="timezone-str"></a>

##### tos_version: `str`<a id="tos_version-str"></a>

##### user_country: `str`<a id="user_country-str"></a>

##### user_date_format: `str`<a id="user_date_format-str"></a>

##### user_date_of_birth: `date`<a id="user_date_of_birth-date"></a>

##### user_display_name: `str`<a id="user_display_name-str"></a>

##### user_end_date: `date`<a id="user_end_date-date"></a>

##### user_name: `str`<a id="user_name-str"></a>

##### user_name_format: `str`<a id="user_name_format-str"></a>

##### user_type: `str`<a id="user_type-str"></a>

##### view: `bool`<a id="view-bool"></a>

##### worker_type: `str`<a id="worker_type-str"></a>

##### working_days: `str`<a id="working_days-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/verify/user` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.clock_in`<a id="clayhrtimesheetsclock_in"></a>

Allows to clock in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
clock_in_response = clayhr.timesheets.clock_in(
    proceed_outside_geo_fence=0,
    description="string_example",
    project_id=1,
    project_manager="string_example",
    category_code="RG",
    notes="string_example",
    billable="Y",
    activity="string_example",
    approval_rejection_reason="string_example",
    clock_in_longitude=3.14,
    clock_in_latitude=3.14,
    clock_out_longitude=3.14,
    clock_out_latitude=3.14,
    project_area_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### proceed_outside_geo_fence: `int`<a id="proceed_outside_geo_fence-int"></a>

To clockin outside geofence

##### description: `str`<a id="description-str"></a>

Description of timecard.

##### project_id: `int`<a id="project_id-int"></a>

Project ID of project.

##### project_manager: `str`<a id="project_manager-str"></a>

Project Manager corresponding user.

##### category_code: `str`<a id="category_code-str"></a>

Category of timecard. Choose between [\"Regular\", \"Overtime\"].

##### notes: `str`<a id="notes-str"></a>

Notes.

##### billable: `str`<a id="billable-str"></a>

Billable or non- billable timecard. Select 'Y' for billable and 'N' for non-billable

##### activity: `str`<a id="activity-str"></a>

Activity type of timecard.

##### approval_rejection_reason: `str`<a id="approval_rejection_reason-str"></a>

Reason for approval rejection.

##### clock_in_longitude: `Union[int, float]`<a id="clock_in_longitude-unionint-float"></a>

Longitude value while clocking in.

##### clock_in_latitude: `Union[int, float]`<a id="clock_in_latitude-unionint-float"></a>

Latitude value while clocking in.

##### clock_out_longitude: `Union[int, float]`<a id="clock_out_longitude-unionint-float"></a>

Longitude value while clocking out.

##### clock_out_latitude: `Union[int, float]`<a id="clock_out_latitude-unionint-float"></a>

Latitude value while clocking out.

##### project_area_id: `int`<a id="project_area_id-int"></a>

Project area ID of project area.

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsClockInResponse`](./clay_hr_python_sdk/pydantic/timesheets_clock_in_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet/clockin` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.clock_out`<a id="clayhrtimesheetsclock_out"></a>

Allows user to clock out.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
clock_out_response = clayhr.timesheets.clock_out(
    proceed_outside_geo_fence=0,
    description="string_example",
    project_id=1,
    project_manager="string_example",
    category_code="RG",
    notes="string_example",
    billable="Y",
    activity="string_example",
    approval_rejection_reason="string_example",
    clock_in_longitude=3.14,
    clock_in_latitude=3.14,
    clock_out_longitude=3.14,
    clock_out_latitude=3.14,
    project_area_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### proceed_outside_geo_fence: `int`<a id="proceed_outside_geo_fence-int"></a>

clock out outside geofence

##### description: `str`<a id="description-str"></a>

Description of timecard.

##### project_id: `int`<a id="project_id-int"></a>

Project ID of project.

##### project_manager: `str`<a id="project_manager-str"></a>

Project Manager corresponding user.

##### category_code: `str`<a id="category_code-str"></a>

Category of timecard. Choose between [\"Regular\", \"Overtime\"].

##### notes: `str`<a id="notes-str"></a>

Notes.

##### billable: `str`<a id="billable-str"></a>

Billable or non- billable timecard. Select 'Y' for billable and 'N' for non-billable

##### activity: `str`<a id="activity-str"></a>

Activity type of timecard.

##### approval_rejection_reason: `str`<a id="approval_rejection_reason-str"></a>

Reason for approval rejection.

##### clock_in_longitude: `Union[int, float]`<a id="clock_in_longitude-unionint-float"></a>

Longitude value while clocking in.

##### clock_in_latitude: `Union[int, float]`<a id="clock_in_latitude-unionint-float"></a>

Latitude value while clocking in.

##### clock_out_longitude: `Union[int, float]`<a id="clock_out_longitude-unionint-float"></a>

Longitude value while clocking out.

##### clock_out_latitude: `Union[int, float]`<a id="clock_out_latitude-unionint-float"></a>

Latitude value while clocking out.

##### project_area_id: `int`<a id="project_area_id-int"></a>

Project area ID of project area.

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsClockOutResponse`](./clay_hr_python_sdk/pydantic/timesheets_clock_out_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet/clockout` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.create_or_update_timesheet`<a id="clayhrtimesheetscreate_or_update_timesheet"></a>

Creates a new timesheet and update existing timesheet.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_or_update_timesheet_response = clayhr.timesheets.create_or_update_timesheet(
    date="1970-01-01",
    project_id=1,
    elapsed_time="1970-01-01T00:00:00.00Z",
    card_id=1,
    description="string_example",
    clocked_outside_geofence=1,
    project_manager="string_example",
    category_code="RG",
    notes="string_example",
    billable="Y",
    activity="string_example",
    approval_rejection_reason="string_example",
    clock_in_longitude=3.14,
    clock_in_latitude=3.14,
    clock_out_longitude=3.14,
    clock_out_latitude=3.14,
    project_area_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `date`<a id="date-date"></a>

Timesheet date.

##### project_id: `int`<a id="project_id-int"></a>

Project ID of project.

##### elapsed_time: `datetime`<a id="elapsed_time-datetime"></a>

Elapsed Time of timecard.

##### card_id: `int`<a id="card_id-int"></a>

Timecard Id of timecard.

##### description: `str`<a id="description-str"></a>

Description of timecard.

##### clocked_outside_geofence: `int`<a id="clocked_outside_geofence-int"></a>

Clocked in or clocked out outside geofence.

##### project_manager: `str`<a id="project_manager-str"></a>

Project Manager corresponding user.

##### category_code: `str`<a id="category_code-str"></a>

Category of timecard. Choose between [\"Regular\", \"Overtime\"].

##### notes: `str`<a id="notes-str"></a>

Notes.

##### billable: `str`<a id="billable-str"></a>

Billable or non- billable timecard. Select 'Y' for billable and 'N' for non-billable

##### activity: `str`<a id="activity-str"></a>

Activity type of timecard.

##### approval_rejection_reason: `str`<a id="approval_rejection_reason-str"></a>

Reason for approval rejection.

##### clock_in_longitude: `Union[int, float]`<a id="clock_in_longitude-unionint-float"></a>

Longitude value while clocking in.

##### clock_in_latitude: `Union[int, float]`<a id="clock_in_latitude-unionint-float"></a>

Latitude value while clocking in.

##### clock_out_longitude: `Union[int, float]`<a id="clock_out_longitude-unionint-float"></a>

Longitude value while clocking out.

##### clock_out_latitude: `Union[int, float]`<a id="clock_out_latitude-unionint-float"></a>

Latitude value while clocking out.

##### project_area_id: `int`<a id="project_area_id-int"></a>

Project area ID of project area.

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsCreateOrUpdateTimesheetResponse`](./clay_hr_python_sdk/pydantic/timesheets_create_or_update_timesheet_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet/save` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.delete_by_timesheet_id`<a id="clayhrtimesheetsdelete_by_timesheet_id"></a>

Deletes a timesheet by Timesheet ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_timesheet_id_response = clayhr.timesheets.delete_by_timesheet_id(
    timesheet_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheet_id: `int`<a id="timesheet_id-int"></a>

Timesheet ID of timesheet.

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsDeleteByTimesheetIdResponse`](./clay_hr_python_sdk/pydantic/timesheets_delete_by_timesheet_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet/delete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.get_active_allocations`<a id="clayhrtimesheetsget_active_allocations"></a>

Retrieve list of active allocations of user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_active_allocations_response = clayhr.timesheets.get_active_allocations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsGetActiveAllocationsResponse`](./clay_hr_python_sdk/pydantic/timesheets_get_active_allocations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet/allocations/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.get_approval_list`<a id="clayhrtimesheetsget_approval_list"></a>

Retrieve list of timesheet approvals on the basis of permission.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_approval_list_response = clayhr.timesheets.get_approval_list(
    start_date="startDate_example",
    end_date="endDate_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `str`<a id="start_date-str"></a>

Start date of the timesheet.

##### end_date: `str`<a id="end_date-str"></a>

End date of the timesheet.

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsGetApprovalListResponse`](./clay_hr_python_sdk/pydantic/timesheets_get_approval_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet/approvals/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.get_by_timesheet_id`<a id="clayhrtimesheetsget_by_timesheet_id"></a>

Retrieve a timesheet by timesheet ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_timesheet_id_response = clayhr.timesheets.get_by_timesheet_id(
    timesheet_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheet_id: `int`<a id="timesheet_id-int"></a>

Tmesheet ID of timesheet.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.get_by_user_id`<a id="clayhrtimesheetsget_by_user_id"></a>

Retrieve a list of timesheets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_user_id_response = clayhr.timesheets.get_by_user_id(
    start_date="string_example",
    end_date="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `str`<a id="start_date-str"></a>

Start date of the timesheet.

##### end_date: `str`<a id="end_date-str"></a>

End date of the timesheet.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.get_details_by_timesheet_id`<a id="clayhrtimesheetsget_details_by_timesheet_id"></a>

Retrieve timesheet details by Timesheet ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_by_timesheet_id_response = clayhr.timesheets.get_details_by_timesheet_id(
    time_sheet_id=1,
    flatcustomfields=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_sheet_id: `int`<a id="time_sheet_id-int"></a>

Timesheet ID of timesheet.

##### flatcustomfields: `bool`<a id="flatcustomfields-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheets/details/{timeSheetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.get_preferences_by_cid`<a id="clayhrtimesheetsget_preferences_by_cid"></a>

Retrieve list of timesheet preferences based in cid.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_preferences_by_cid_response = clayhr.timesheets.get_preferences_by_cid()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsGetPreferencesByCidResponse`](./clay_hr_python_sdk/pydantic/timesheets_get_preferences_by_cid_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet/preferences/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.get_timecards_by_timesheet_id`<a id="clayhrtimesheetsget_timecards_by_timesheet_id"></a>

Retrieve a list of timecards.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_timecards_by_timesheet_id_response = (
    clayhr.timesheets.get_timecards_by_timesheet_id(
        start_date="",
        end_date="",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `date`<a id="start_date-date"></a>

Start date of the timesheet.

##### end_date: `date`<a id="end_date-date"></a>

End date of the timesheet.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timecards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.list_activity_types_by_cid`<a id="clayhrtimesheetslist_activity_types_by_cid"></a>

Retrieve list of activity types based on cid.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_activity_types_by_cid_response = clayhr.timesheets.list_activity_types_by_cid()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsListActivityTypesByCidResponse`](./clay_hr_python_sdk/pydantic/timesheets_list_activity_types_by_cid_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet/activitytype/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.timesheets.update_status_by_timesheet_id`<a id="clayhrtimesheetsupdate_status_by_timesheet_id"></a>

Update the timesheet status (submit, approve, reject) corresponding to supplied Timesheet ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_status_by_timesheet_id_response = (
    clayhr.timesheets.update_status_by_timesheet_id(
        timesheet_id=1,
        status="AP",
        comments="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheet_id: `int`<a id="timesheet_id-int"></a>

Timesheet ID of the timesheet.

##### status: `str`<a id="status-str"></a>

Status of timecard. Choose between [\"PD-Pending for Approval\", \"PAP-Partially Approved\", \"AP-Fully Approved\",\"NEW-New Timesheet\",\"RJ-Rejected\"].

##### comments: `str`<a id="comments-str"></a>

Comments

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsUpdateStatusByTimesheetIdResponse`](./clay_hr_python_sdk/pydantic/timesheets_update_status_by_timesheet_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/timesheet/update` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.trainings.get_by_user_id`<a id="clayhrtrainingsget_by_user_id"></a>

Retrieve trainings by user ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_user_id_response = clayhr.trainings.get_by_user_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/trainings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.trainings.get_training_content_by_training_id`<a id="clayhrtrainingsget_training_content_by_training_id"></a>

Retrieve training content by training ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_training_content_by_training_id_response = (
    clayhr.trainings.get_training_content_by_training_id(
        training_id=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### training_id: `int`<a id="training_id-int"></a>

trainingId

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/training/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.trainings.synchronize_with_talent_lms`<a id="clayhrtrainingssynchronize_with_talent_lms"></a>

Sync with talent LMS

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
synchronize_with_talent_lms_response = clayhr.trainings.synchronize_with_talent_lms(
    redirect_url="redirectUrl_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### redirect_url: `str`<a id="redirect_url-str"></a>

redirectUrl

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/training/talentlms/sync` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.trainings.update_user_status`<a id="clayhrtrainingsupdate_user_status"></a>

Update training status for user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_status_response = clayhr.trainings.update_user_status(
    status="status_example",
    user_training_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

Status of the user training.

##### user_training_id: `int`<a id="user_training_id-int"></a>

The ID of the user training.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/training/status/update` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.user_pto_policies.get_policies`<a id="clayhruser_pto_policiesget_policies"></a>

Retrieve your PTO Policies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policies_response = clayhr.user_pto_policies.get_policies()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserPtoPoliciesGetPoliciesResponse`](./clay_hr_python_sdk/pydantic/user_pto_policies_get_policies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v3/user/pto` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.user_pto_policies.list_pto_policies`<a id="clayhruser_pto_policieslist_pto_policies"></a>

Retrieve list of PTO policies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_pto_policies_response = clayhr.user_pto_policies.list_pto_policies()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserPtoPoliciesListPtoPoliciesResponse`](./clay_hr_python_sdk/pydantic/user_pto_policies_list_pto_policies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ptopolicies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.user_workflow.assign_workflow_to_user`<a id="clayhruser_workflowassign_workflow_to_user"></a>

This page will help you get started with Assign Workflow to User.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_workflow_to_user_response = clayhr.user_workflow.assign_workflow_to_user(
    workflow_id=1,
    assignee_user_id=1,
    coordinator_user_id=1,
    comment="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workflow_id: `int`<a id="workflow_id-int"></a>

The ID of the workflow.

##### assignee_user_id: `int`<a id="assignee_user_id-int"></a>

The ID of Workflow Assignee.

##### coordinator_user_id: `int`<a id="coordinator_user_id-int"></a>

The ID of Workflow Coordinator.

##### comment: `str`<a id="comment-str"></a>

Comment of the workflow.

#### 🔄 Return<a id="🔄-return"></a>

[`UserWorkflowAssignWorkflowToUserResponse`](./clay_hr_python_sdk/pydantic/user_workflow_assign_workflow_to_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/userworkflow/assign/{workflowId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.workflows.create_new_task`<a id="clayhrworkflowscreate_new_task"></a>

Create a new task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_task_response = clayhr.workflows.create_new_task(
    body=[{}],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ArrayTaskModel`](./clay_hr_python_sdk/type/array_task_model.py)
task object to create a new task

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/task/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.workflows.get_task_details_by_task_id`<a id="clayhrworkflowsget_task_details_by_task_id"></a>

Get the details of a workflow task by task id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_details_by_task_id_response = clayhr.workflows.get_task_details_by_task_id(
    taskid=1,
    authorization="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### taskid: `int`<a id="taskid-int"></a>

taskid

##### authorization: `str`<a id="authorization-str"></a>

Authorization

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/task/{taskid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.workflows.get_tasks_by_user_id`<a id="clayhrworkflowsget_tasks_by_user_id"></a>

Get tasks by user id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tasks_by_user_id_response = clayhr.workflows.get_tasks_by_user_id()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.workflows.get_user_workflows`<a id="clayhrworkflowsget_user_workflows"></a>

Get workflows by user id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_workflows_response = clayhr.workflows.get_user_workflows(
    authorization="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

Authorization

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/userworkflows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.workflows.get_workflows`<a id="clayhrworkflowsget_workflows"></a>

Get workflows.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workflows_response = clayhr.workflows.get_workflows(
    status="A",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

status

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/workflows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.workflows.list_tasks_by_userworkflow_id`<a id="clayhrworkflowslist_tasks_by_userworkflow_id"></a>

Get tasks by userworkflowid.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_tasks_by_userworkflow_id_response = clayhr.workflows.list_tasks_by_userworkflow_id(
    userworkflowid=1,
    authorization="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### userworkflowid: `int`<a id="userworkflowid-int"></a>

userworkflowid

##### authorization: `str`<a id="authorization-str"></a>

Authorization

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/userworkflows/{userworkflowid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clayhr.workflows.update_status_task`<a id="clayhrworkflowsupdate_status_task"></a>

Update status workflow task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_status_task_response = clayhr.workflows.update_status_task(
    authorization="string_example",
    appraisal_id=1,
    assigned_user_id=1,
    ci=True,
    cid=1,
    create_user_id=1,
    createts="1970-01-01",
    description="string_example",
    due_date="1970-01-01",
    last_edit="string_example",
    launchts_date=1,
    launchts_day=1,
    launchts_hours=1,
    launchts_minutes=1,
    launchts_month=1,
    launchts_nanos=1,
    launchts_seconds=1,
    launchts_time=1,
    launchts_timezone_offset=1,
    launchts_year=1,
    phasename="string_example",
    project_id=1,
    recruit_id=1,
    status_code="string_example",
    system_task=1,
    task_id=1,
    task_uid=1,
    title="string_example",
    transition_name="string_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

Authorization

##### appraisal_id: `int`<a id="appraisal_id-int"></a>

##### assigned_user_id: `int`<a id="assigned_user_id-int"></a>

##### ci: `bool`<a id="ci-bool"></a>

##### cid: `int`<a id="cid-int"></a>

##### create_user_id: `int`<a id="create_user_id-int"></a>

##### createts: `date`<a id="createts-date"></a>

##### description: `str`<a id="description-str"></a>

##### due_date: `date`<a id="due_date-date"></a>

##### last_edit: `str`<a id="last_edit-str"></a>

##### launchts_date: `int`<a id="launchts_date-int"></a>

##### launchts_day: `int`<a id="launchts_day-int"></a>

##### launchts_hours: `int`<a id="launchts_hours-int"></a>

##### launchts_minutes: `int`<a id="launchts_minutes-int"></a>

##### launchts_month: `int`<a id="launchts_month-int"></a>

##### launchts_nanos: `int`<a id="launchts_nanos-int"></a>

##### launchts_seconds: `int`<a id="launchts_seconds-int"></a>

##### launchts_time: `int`<a id="launchts_time-int"></a>

##### launchts_timezone_offset: `int`<a id="launchts_timezone_offset-int"></a>

##### launchts_year: `int`<a id="launchts_year-int"></a>

##### phasename: `str`<a id="phasename-str"></a>

##### project_id: `int`<a id="project_id-int"></a>

##### recruit_id: `int`<a id="recruit_id-int"></a>

##### status_code: `str`<a id="status_code-str"></a>

##### system_task: `int`<a id="system_task-int"></a>

##### task_id: `int`<a id="task_id-int"></a>

##### task_uid: `int`<a id="task_uid-int"></a>

##### title: `str`<a id="title-str"></a>

##### transition_name: `str`<a id="transition_name-str"></a>

##### type: `str`<a id="type-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/task/update/status` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
