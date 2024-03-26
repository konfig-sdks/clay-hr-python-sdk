operation_parameter_map = {
    '/api/announcement/create-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'url'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/attachment/list/{annId}-GET': {
        'parameters': [
            {
                'name': 'annId'
            },
        ]
    },
    '/api/announcement/{annId}-GET': {
        'parameters': [
            {
                'name': 'annId'
            },
        ]
    },
    '/api/announcement/edit-PUT': {
        'parameters': [
            {
                'name': 'annId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'desciption'
            },
            {
                'name': 'status'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/api/token-GET': {
        'parameters': [
        ]
    },
    '/resume-POST': {
        'parameters': [
            {
                'name': 'file'
            },
        ]
    },
    '/-GET': {
        'parameters': [
        ]
    },
    '/list-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/detail/{recruitid}-GET': {
        'parameters': [
            {
                'name': 'recruitid'
            },
        ]
    },
    '/-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'isNewCand'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'source'
            },
        ]
    },
    '/customfield-GET': {
        'parameters': [
            {
                'name': 'customFieldId'
            },
        ]
    },
    '/customfields-GET': {
        'parameters': [
            {
                'name': 'objectType'
            },
        ]
    },
    '/customlist-GET': {
        'parameters': [
        ]
    },
    '/customfieldvalues-GET': {
        'parameters': [
            {
                'name': 'customFieldId'
            },
            {
                'name': 'customFieldCode'
            },
            {
                'name': 'userEmail'
            },
            {
                'name': 'empId'
            },
        ]
    },
    '/customfieldvalues-POST': {
        'parameters': [
            {
                'name': 'customFieldId'
            },
            {
                'name': 'value'
            },
            {
                'name': 'customFieldCode'
            },
            {
                'name': 'userEmail'
            },
            {
                'name': 'empId'
            },
        ]
    },
    '/delete-POST': {
        'parameters': [
            {
                'name': 'contactId'
            },
        ]
    },
    '/documentLibrary-GET': {
        'parameters': [
        ]
    },
    '/attachment/download-GET': {
        'parameters': [
            {
                'name': 'fileName'
            },
        ]
    },
    '/expensereport-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/expenseitem-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'cid'
            },
            {
                'name': 'currencyCode'
            },
            {
                'name': 'date'
            },
            {
                'name': 'expenseItemId'
            },
            {
                'name': 'expenseType'
            },
            {
                'name': 'expenseTypeId'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'reimbursible'
            },
            {
                'name': 'remarks'
            },
        ]
    },
    '/expensereport/delete-POST': {
        'parameters': [
            {
                'name': 'expenseReportId'
            },
        ]
    },
    '/expensereports-GET': {
        'parameters': [
            {
                'name': 'guid'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/currencylist-GET': {
        'parameters': [
        ]
    },
    '/expensetypes-GET': {
        'parameters': [
        ]
    },
    '/expensereport-GET': {
        'parameters': [
            {
                'name': 'expenseReportId'
            },
            {
                'name': 'guid'
            },
        ]
    },
    '/expensereport/submit/{expenseReportId}-POST': {
        'parameters': [
            {
                'name': 'expenseReportId'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/rm/api/feedback-GET': {
        'parameters': [
            {
                'name': 'type'
            },
        ]
    },
    '/api/my-GET': {
        'parameters': [
        ]
    },
    '/api/view-GET': {
        'parameters': [
            {
                'name': 'dynamicFormId'
            },
        ]
    },
    '/api/getdynaforms-GET': {
        'parameters': [
        ]
    },
    '/api/response/{dynamicFormId}-GET': {
        'parameters': [
            {
                'name': 'dynamicFormId'
            },
            {
                'name': 'assignUserId'
            },
            {
                'name': 'assignmentId'
            },
        ]
    },
    '/api/responselist-GET': {
        'parameters': [
            {
                'name': 'dynamicFormId'
            },
        ]
    },
    '/api/saveFormResponse-POST': {
        'parameters': [
            {
                'name': 'assignmentId'
            },
        ]
    },
    '/api/saveItemResponse-POST': {
        'parameters': [
            {
                'name': 'assignmentId'
            },
            {
                'name': 'itemId'
            },
            {
                'name': 'responseValue'
            },
        ]
    },
    '/goal-POST': {
        'parameters': [
            {
                'name': 'additive'
            },
            {
                'name': 'begindate'
            },
            {
                'name': 'cid'
            },
            {
                'name': 'commentCrediteatets'
            },
            {
                'name': 'commentDescription'
            },
            {
                'name': 'companyGoal'
            },
            {
                'name': 'completionRatio'
            },
            {
                'name': 'createUserId'
            },
            {
                'name': 'createts.date'
            },
            {
                'name': 'createts.day'
            },
            {
                'name': 'createts.hours'
            },
            {
                'name': 'createts.minutes'
            },
            {
                'name': 'createts.month'
            },
            {
                'name': 'createts.nanos'
            },
            {
                'name': 'createts.seconds'
            },
            {
                'name': 'createts.time'
            },
            {
                'name': 'createts.timezoneOffset'
            },
            {
                'name': 'createts.year'
            },
            {
                'name': 'crediteatets'
            },
            {
                'name': 'currentValue'
            },
            {
                'name': 'description'
            },
            {
                'name': 'disposition'
            },
            {
                'name': 'elapsedTimeRatio'
            },
            {
                'name': 'goalId'
            },
            {
                'name': 'goalValue'
            },
            {
                'name': 'goalWeightage'
            },
            {
                'name': 'hasGoalApprovalPermission'
            },
            {
                'name': 'id'
            },
            {
                'name': 'initialvalue'
            },
            {
                'name': 'isForward'
            },
            {
                'name': 'lastUpdateUserId'
            },
            {
                'name': 'objectiveId'
            },
            {
                'name': 'parentGoalId'
            },
            {
                'name': 'progressRatio'
            },
            {
                'name': 'projectid'
            },
            {
                'name': 'reviewUserId'
            },
            {
                'name': 'state'
            },
            {
                'name': 'status'
            },
            {
                'name': 'summary'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'typecode'
            },
            {
                'name': 'uname'
            },
            {
                'name': 'units'
            },
            {
                'name': 'visibleToDirectReports'
            },
        ]
    },
    '/deletegoal-DELETE': {
        'parameters': [
            {
                'name': 'goalId'
            },
        ]
    },
    '/goal-GET': {
        'parameters': [
        ]
    },
    '/getgoal-GET': {
        'parameters': [
            {
                'name': 'goalid'
            },
            {
                'name': 'reviewUserId'
            },
        ]
    },
    '/goal/list-GET': {
        'parameters': [
        ]
    },
    '/invoice-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/api/jobprofiles-GET': {
        'parameters': [
            {
                'name': 'status'
            },
        ]
    },
    '/api/userpto/balance/add-POST': {
        'parameters': [
            {
                'name': 'ptobalances'
            },
        ]
    },
    '/api/leaverequest-POST': {
        'parameters': [
            {
                'name': 'date'
            },
            {
                'name': 'description'
            },
            {
                'name': 'createUserViewModel'
            },
            {
                'name': 'endDateMeridiem'
            },
            {
                'name': 'meridiem'
            },
            {
                'name': 'numberOfDays'
            },
            {
                'name': 'ptoPolicyModel'
            },
            {
                'name': 'totalLeaveDays'
            },
            {
                'name': 'totalLeaveHours'
            },
            {
                'name': 'userModel'
            },
        ]
    },
    '/api/leaverequests-GET': {
        'parameters': [
            {
                'name': 'endDate'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'leaveUserid'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/manage/leaves-GET': {
        'parameters': [
        ]
    },
    '/api/leave/hours/credit-GET': {
        'parameters': [
            {
                'name': 'leaveDate'
            },
            {
                'name': 'leaveId'
            },
            {
                'name': 'leaveUserId'
            },
            {
                'name': 'ptoPolicyId'
            },
        ]
    },
    '/api/process/leave-GET': {
        'parameters': [
            {
                'name': 'leaveId'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/objective-GET': {
        'parameters': [
            {
                'name': 'objectiveId'
            },
        ]
    },
    '/api/orgunits/add-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'deptHead'
            },
            {
                'name': 'deptHeadName'
            },
            {
                'name': 'departmentCode'
            },
            {
                'name': 'departmentId'
            },
            {
                'name': 'departmentLabel'
            },
            {
                'name': 'noOfEmployees'
            },
            {
                'name': 'parentDepartmentId'
            },
            {
                'name': 'parentDepartmentName'
            },
        ]
    },
    '/api/orgunits-GET': {
        'parameters': [
        ]
    },
    '/api/orgrelation/allactive-GET': {
        'parameters': [
        ]
    },
    '/api/orgrelation/orgRelationsByUser-GET': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'employeeUserId'
            },
            {
                'name': 'empId'
            },
        ]
    },
    '/api/orgrelation/save-GET': {
        'parameters': [
            {
                'name': 'orgRelationId'
            },
            {
                'name': 'managerUserId'
            },
            {
                'name': 'managerEmail'
            },
            {
                'name': 'userEmail'
            },
            {
                'name': 'otherUserId'
            },
            {
                'name': 'relationType'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'enddate'
            },
            {
                'name': 'cid'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/paystub-GET': {
        'parameters': [
        ]
    },
    '/api/user/orgrelation/add-POST': {
        'parameters': [
            {
                'name': 'Add Objects'
            },
            {
                'name': 'empId'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/api/user/completeUserDetails-POST': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'empId'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'guid'
            },
            {
                'name': 'status'
            },
            {
                'name': 'displayFullName'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'secondLastName'
            },
            {
                'name': 'shortName'
            },
            {
                'name': 'namePronunciation'
            },
            {
                'name': 'familySuffix'
            },
            {
                'name': 'workerType'
            },
            {
                'name': 'userDateOfBirth'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'cellPhone'
            },
            {
                'name': 'position'
            },
            {
                'name': 'departmentID'
            },
            {
                'name': 'locationId'
            },
            {
                'name': 'locationName'
            },
            {
                'name': 'userStartDate'
            },
            {
                'name': 'reportsToEmail'
            },
            {
                'name': 'addressList'
            },
            {
                'name': 'educationList'
            },
            {
                'name': 'contactList'
            },
            {
                'name': 'financialList'
            },
            {
                'name': 'customFieldValues'
            },
        ]
    },
    '/api/user/add-POST': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/api/user/compensation/add-POST': {
        'parameters': [
            {
                'name': 'value'
            },
            {
                'name': 'compensationType'
            },
            {
                'name': 'currencyCode'
            },
            {
                'name': 'period'
            },
            {
                'name': 'effectivedate'
            },
            {
                'name': 'status'
            },
            {
                'name': 'enddate'
            },
            {
                'name': 'notes'
            },
        ]
    },
    '/api/user/address/delete-POST': {
        'parameters': [
            {
                'name': 'addressId'
            },
        ]
    },
    '/user/education/delete-POST': {
        'parameters': [
            {
                'name': 'educationId'
            },
        ]
    },
    '/api/user/employment/delete-POST': {
        'parameters': [
            {
                'name': 'empid'
            },
        ]
    },
    '/api/users-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'search'
            },
            {
                'name': 'startDateBefore'
            },
            {
                'name': 'startDateAfter'
            },
            {
                'name': 'endDateBefore'
            },
            {
                'name': 'endDateAfter'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/users/basic-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'search'
            },
            {
                'name': 'startDateBefore'
            },
            {
                'name': 'startDateAfter'
            },
            {
                'name': 'endDateBefore'
            },
            {
                'name': 'endDateAfter'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/user/compensation-GET': {
        'parameters': [
            {
                'name': 'email'
            },
        ]
    },
    '/api/user/update/status-GET': {
        'parameters': [
        ]
    },
    '/api/user/basic-GET': {
        'parameters': [
            {
                'name': 'email'
            },
        ]
    },
    '/api/user-GET': {
        'parameters': [
        ]
    },
    '/api/user/list-GET': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/api/user/permissions-GET': {
        'parameters': [
        ]
    },
    '/resource-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'sortBy'
            },
            {
                'name': 'sortOrder'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/user/saveCustomFieldValues-POST': {
        'parameters': [
            {
                'name': 'empId'
            },
            {
                'name': 'guid'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/api/address/save-POST': {
        'parameters': [
            {
                'name': 'RAW_BODY'
            },
            {
                'name': 'empId'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/api/education/save-POST': {
        'parameters': [
            {
                'name': 'RAW_BODY'
            },
            {
                'name': 'empId'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/api/employment/save-POST': {
        'parameters': [
            {
                'name': 'RAW_BODY'
            },
            {
                'name': 'empId'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/api/user/compensation/update-POST': {
        'parameters': [
            {
                'name': 'guid'
            },
            {
                'name': 'value'
            },
            {
                'name': 'compensationType'
            },
            {
                'name': 'currencyCode'
            },
            {
                'name': 'period'
            },
            {
                'name': 'status'
            },
            {
                'name': 'effectivedate'
            },
            {
                'name': 'enddate'
            },
            {
                'name': 'notes'
            },
        ]
    },
    '/api/user/update-POST': {
        'parameters': [
            {
                'name': 'guid'
            },
            {
                'name': 'email'
            },
            {
                'name': 'empId'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'secondLastName'
            },
            {
                'name': 'displayFullName'
            },
            {
                'name': 'cellPhone'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'familySuffix'
            },
            {
                'name': 'userDateOfBirth'
            },
            {
                'name': 'jobGrade'
            },
            {
                'name': 'userStartDate'
            },
            {
                'name': 'userEndDate'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'position'
            },
            {
                'name': 'profileId'
            },
            {
                'name': 'shortName'
            },
            {
                'name': 'status'
            },
            {
                'name': 'locationName'
            },
            {
                'name': 'locationId'
            },
            {
                'name': 'notes'
            },
        ]
    },
    '/api/user/uploadpicture-POST': {
        'parameters': [
            {
                'name': 'file'
            },
            {
                'name': 'userid'
            },
        ]
    },
    '/appraisal/add-POST': {
        'parameters': [
            {
                'name': 'templateId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'AppraisalType'
            },
        ]
    },
    '/appraisal/getCompletedReviews-GET': {
        'parameters': [
            {
                'name': 'targetUserId'
            },
        ]
    },
    '/appraisal/user-GET': {
        'parameters': [
        ]
    },
    '/appraisal/template/list-GET': {
        'parameters': [
        ]
    },
    '/appraisal/bulkLaunch-POST': {
        'parameters': [
            {
                'name': 'templateId'
            },
            {
                'name': 'reviewType'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'importGoals'
            },
            {
                'name': 'importJobProfileSkills'
            },
            {
                'name': 'importSkills'
            },
            {
                'name': 'userIdList'
            },
        ]
    },
    '/appraisal/assignment-GET': {
        'parameters': [
        ]
    },
    '/position/save-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'count'
            },
            {
                'name': 'status'
            },
            {
                'name': 'accessLevel'
            },
            {
                'name': 'dateOpen'
            },
            {
                'name': 'dateClose'
            },
            {
                'name': 'positionUID'
            },
            {
                'name': 'funnelId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'requirements'
            },
            {
                'name': 'responsibilities'
            },
            {
                'name': 'projectid'
            },
            {
                'name': 'approvalFlowId'
            },
            {
                'name': 'locationid'
            },
            {
                'name': 'departmentId'
            },
            {
                'name': 'profileid'
            },
            {
                'name': 'recruiterId'
            },
        ]
    },
    '/position/view-GET': {
        'parameters': [
            {
                'name': 'positionid'
            },
        ]
    },
    '/position/list-GET': {
        'parameters': [
            {
                'name': 'search'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/api/projects/allocation-POST': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/api/projects-POST': {
        'parameters': [
            {
                'name': 'projectName'
            },
            {
                'name': 'projectDesc'
            },
            {
                'name': 'shortCode'
            },
            {
                'name': 'startDate'
            },
        ]
    },
    '/api/projects/{projectId}-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/api/projects/allocation/{projectId}-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/api/projects-GET': {
        'parameters': [
        ]
    },
    '/api/report/content-GET': {
        'parameters': [
            {
                'name': 'analyticId'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/report/content-GET': {
        'parameters': [
            {
                'name': 'analyticId'
            },
        ]
    },
    '/api/report-GET': {
        'parameters': [
            {
                'name': 'analyticId'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/api/shifts-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/shifts/save-POST': {
        'parameters': [
        ]
    },
    '/skill/add-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'skillCode'
            },
            {
                'name': 'assessmentModel'
            },
            {
                'name': 'skillTypeModel'
            },
        ]
    },
    '/skills-GET': {
        'parameters': [
        ]
    },
    '/userSkill-GET': {
        'parameters': [
            {
                'name': 'assignedUserID'
            },
        ]
    },
    '/api/survey/item/save-POST': {
        'parameters': [
            {
                'name': 'assignmentId'
            },
            {
                'name': 'itemId'
            },
            {
                'name': 'responseValue'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/api/survey/save-POST': {
        'parameters': [
            {
                'name': 'assignmentId'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/api/survey/view-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'dynamicFormId'
            },
        ]
    },
    '/api/survey/allresponses-GET': {
        'parameters': [
            {
                'name': 'SurveyId'
            },
        ]
    },
    '/api/survey/list-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
        ]
    },
    '/api/test-GET': {
        'parameters': [
            {
                'name': 'status'
            },
        ]
    },
    '/timecard/clock/out-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
        ]
    },
    '/timecard/clockin-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'activity'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'approvalRejectionReason'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'cardId'
            },
            {
                'name': 'caseNum'
            },
            {
                'name': 'caseURL'
            },
            {
                'name': 'categoryCode'
            },
            {
                'name': 'chargeType'
            },
            {
                'name': 'cid'
            },
            {
                'name': 'createUserID'
            },
            {
                'name': 'createts.date'
            },
            {
                'name': 'createts.day'
            },
            {
                'name': 'createts.hours'
            },
            {
                'name': 'createts.minutes'
            },
            {
                'name': 'createts.month'
            },
            {
                'name': 'createts.nanos'
            },
            {
                'name': 'createts.seconds'
            },
            {
                'name': 'createts.time'
            },
            {
                'name': 'createts.timezoneOffset'
            },
            {
                'name': 'createts.year'
            },
            {
                'name': 'customHours'
            },
            {
                'name': 'date'
            },
            {
                'name': 'description'
            },
            {
                'name': 'elapsedTime.date'
            },
            {
                'name': 'elapsedTime.day'
            },
            {
                'name': 'elapsedTime.hours'
            },
            {
                'name': 'elapsedTime.minutes'
            },
            {
                'name': 'elapsedTime.month'
            },
            {
                'name': 'elapsedTime.seconds'
            },
            {
                'name': 'elapsedTime.time'
            },
            {
                'name': 'elapsedTime.timezoneOffset'
            },
            {
                'name': 'elapsedTime.year'
            },
            {
                'name': 'endDateTime.date'
            },
            {
                'name': 'endDateTime.day'
            },
            {
                'name': 'endDateTime.hours'
            },
            {
                'name': 'endDateTime.minutes'
            },
            {
                'name': 'endDateTime.month'
            },
            {
                'name': 'endDateTime.nanos'
            },
            {
                'name': 'endDateTime.seconds'
            },
            {
                'name': 'endDateTime.time'
            },
            {
                'name': 'endDateTime.timezoneOffset'
            },
            {
                'name': 'endDateTime.year'
            },
            {
                'name': 'endDateTimeStr'
            },
            {
                'name': 'id'
            },
            {
                'name': 'invoiceId'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'numberOfDays'
            },
            {
                'name': 'paymentDate'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'projectManager'
            },
            {
                'name': 'projectModel.account'
            },
            {
                'name': 'ptoComputed'
            },
            {
                'name': 'source'
            },
            {
                'name': 'startDateTime.date'
            },
            {
                'name': 'startDateTime.day'
            },
            {
                'name': 'startDateTime.hours'
            },
            {
                'name': 'startDateTime.minutes'
            },
            {
                'name': 'startDateTime.month'
            },
            {
                'name': 'startDateTime.nanos'
            },
            {
                'name': 'startDateTime.seconds'
            },
            {
                'name': 'startDateTime.time'
            },
            {
                'name': 'startDateTime.timezoneOffset'
            },
            {
                'name': 'startDateTime.year'
            },
            {
                'name': 'startDateTimeStr'
            },
            {
                'name': 'status'
            },
            {
                'name': 'sumOfElapsedTime'
            },
            {
                'name': 'timesheetId'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'usedTime'
            },
        ]
    },
    '/timecard/addtimecard-POST': {
        'parameters': [
            {
                'name': 'createts.date'
            },
            {
                'name': 'createts.day'
            },
            {
                'name': 'createts.hours'
            },
            {
                'name': 'createts.minutes'
            },
            {
                'name': 'createts.month'
            },
            {
                'name': 'createts.nanos'
            },
            {
                'name': 'createts.seconds'
            },
            {
                'name': 'createts.time'
            },
            {
                'name': 'createts.timezoneOffset'
            },
            {
                'name': 'createts.year'
            },
            {
                'name': 'customHours'
            },
            {
                'name': 'date'
            },
            {
                'name': 'description'
            },
            {
                'name': 'elapsedTime.date'
            },
            {
                'name': 'elapsedTime.day'
            },
            {
                'name': 'elapsedTime.hours'
            },
            {
                'name': 'elapsedTime.minutes'
            },
            {
                'name': 'elapsedTime.month'
            },
            {
                'name': 'elapsedTime.seconds'
            },
            {
                'name': 'elapsedTime.time'
            },
            {
                'name': 'elapsedTime.timezoneOffset'
            },
            {
                'name': 'elapsedTime.year'
            },
            {
                'name': 'endDateTime.date'
            },
            {
                'name': 'endDateTime.day'
            },
            {
                'name': 'endDateTime.hours'
            },
            {
                'name': 'endDateTime.minutes'
            },
            {
                'name': 'endDateTime.month'
            },
            {
                'name': 'endDateTime.nanos'
            },
            {
                'name': 'endDateTime.seconds'
            },
            {
                'name': 'endDateTime.time'
            },
            {
                'name': 'endDateTime.timezoneOffset'
            },
            {
                'name': 'endDateTime.year'
            },
            {
                'name': 'endDateTimeStr'
            },
            {
                'name': 'id'
            },
            {
                'name': 'invoiceId'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'numberOfDays'
            },
            {
                'name': 'paymentDate'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'projectManager'
            },
            {
                'name': 'projectModel.account'
            },
            {
                'name': 'timesheetId'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'usedTime'
            },
        ]
    },
    '/api/user/timecard-GET': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'guid'
            },
        ]
    },
    '/api/user/timecards-GET': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'guid'
            },
        ]
    },
    '/api/timecards/details/{timecardId}-GET': {
        'parameters': [
            {
                'name': 'timecardId'
            },
            {
                'name': 'flatcustomfields'
            },
        ]
    },
    '/verify/tvc-GET': {
        'parameters': [
            {
                'name': 'cid'
            },
        ]
    },
    '/timecard-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/register-POST': {
        'parameters': [
            {
                'name': 'accessories'
            },
            {
                'name': 'acknowledge'
            },
            {
                'name': 'assetID'
            },
            {
                'name': 'assetno'
            },
            {
                'name': 'assetstatus'
            },
            {
                'name': 'assettype'
            },
            {
                'name': 'purchaseDate'
            },
            {
                'name': 'selfAssign'
            },
            {
                'name': 'serialno'
            },
            {
                'name': 'service'
            },
            {
                'name': 'source'
            },
            {
                'name': 'specs'
            },
            {
                'name': 'supplier'
            },
            {
                'name': 'useStatusCode'
            },
            {
                'name': 'userDomain'
            },
            {
                'name': 'userMail'
            },
            {
                'name': 'userPassword'
            },
            {
                'name': 'uuid'
            },
        ]
    },
    '/verify/device-GET': {
        'parameters': [
            {
                'name': 'deviceUUID'
            },
        ]
    },
    '/verify/user-GET': {
        'parameters': [
            {
                'name': 'adpAssociateOID'
            },
            {
                'name': 'allocation'
            },
            {
                'name': 'appleUserIdentifier'
            },
            {
                'name': 'assignments'
            },
            {
                'name': 'authToken'
            },
            {
                'name': 'calWeekPref'
            },
            {
                'name': 'calendarId'
            },
            {
                'name': 'candidateId'
            },
            {
                'name': 'careerPathwayId'
            },
            {
                'name': 'cellPhone'
            },
            {
                'name': 'cid'
            },
            {
                'name': 'countryId'
            },
            {
                'name': 'createts.date'
            },
            {
                'name': 'createts.day'
            },
            {
                'name': 'createts.hours'
            },
            {
                'name': 'createts.minutes'
            },
            {
                'name': 'createts.month'
            },
            {
                'name': 'createts.nanos'
            },
            {
                'name': 'createts.seconds'
            },
            {
                'name': 'createts.time'
            },
            {
                'name': 'createts.timezoneOffset'
            },
            {
                'name': 'createts.year'
            },
            {
                'name': 'createuserid'
            },
            {
                'name': 'thumbnail'
            },
            {
                'name': 'timecardPeriodPref'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'tosVersion'
            },
            {
                'name': 'userCountry'
            },
            {
                'name': 'userDateFormat'
            },
            {
                'name': 'userDateOfBirth'
            },
            {
                'name': 'userDisplayName'
            },
            {
                'name': 'userEndDate'
            },
            {
                'name': 'userName'
            },
            {
                'name': 'userNameFormat'
            },
            {
                'name': 'userType'
            },
            {
                'name': 'view'
            },
            {
                'name': 'workerType'
            },
            {
                'name': 'workingDays'
            },
        ]
    },
    '/api/timesheet/clockin-POST': {
        'parameters': [
            {
                'name': 'proceedOutsideGeoFence'
            },
            {
                'name': 'description'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'projectManager'
            },
            {
                'name': 'categoryCode'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'activity'
            },
            {
                'name': 'approvalRejectionReason'
            },
            {
                'name': 'clockInLongitude'
            },
            {
                'name': 'clockInLatitude'
            },
            {
                'name': 'clockOutLongitude'
            },
            {
                'name': 'clockOutLatitude'
            },
            {
                'name': 'projectAreaId'
            },
        ]
    },
    '/api/timesheet/clockout-POST': {
        'parameters': [
            {
                'name': 'proceedOutsideGeoFence'
            },
            {
                'name': 'description'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'projectManager'
            },
            {
                'name': 'categoryCode'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'activity'
            },
            {
                'name': 'approvalRejectionReason'
            },
            {
                'name': 'clockInLongitude'
            },
            {
                'name': 'clockInLatitude'
            },
            {
                'name': 'clockOutLongitude'
            },
            {
                'name': 'clockOutLatitude'
            },
            {
                'name': 'projectAreaId'
            },
        ]
    },
    '/api/timesheet/save-POST': {
        'parameters': [
            {
                'name': 'date'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'elapsedTime'
            },
            {
                'name': 'cardId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'clockedOutsideGeofence'
            },
            {
                'name': 'projectManager'
            },
            {
                'name': 'categoryCode'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'activity'
            },
            {
                'name': 'approvalRejectionReason'
            },
            {
                'name': 'clockInLongitude'
            },
            {
                'name': 'clockInLatitude'
            },
            {
                'name': 'clockOutLongitude'
            },
            {
                'name': 'clockOutLatitude'
            },
            {
                'name': 'projectAreaId'
            },
        ]
    },
    '/api/timesheet/delete-POST': {
        'parameters': [
            {
                'name': 'timesheetId'
            },
        ]
    },
    '/api/timesheet/allocations/list-GET': {
        'parameters': [
        ]
    },
    '/api/timesheet/approvals/list-GET': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
        ]
    },
    '/api/timesheet-GET': {
        'parameters': [
            {
                'name': 'timesheetId'
            },
        ]
    },
    '/api/timesheets-GET': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
        ]
    },
    '/api/timesheets/details/{timeSheetId}-GET': {
        'parameters': [
            {
                'name': 'timeSheetId'
            },
            {
                'name': 'flatcustomfields'
            },
        ]
    },
    '/api/timesheet/preferences/list-GET': {
        'parameters': [
        ]
    },
    '/api/timecards-GET': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
        ]
    },
    '/api/timesheet/activitytype/list-GET': {
        'parameters': [
        ]
    },
    '/api/timesheet/update-POST': {
        'parameters': [
            {
                'name': 'timesheetId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'comments'
            },
        ]
    },
    '/api/trainings-GET': {
        'parameters': [
        ]
    },
    '/api/training/content-GET': {
        'parameters': [
            {
                'name': 'trainingId'
            },
        ]
    },
    '/api/training/talentlms/sync-GET': {
        'parameters': [
            {
                'name': 'redirectUrl'
            },
        ]
    },
    '/api/training/status/update-POST': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'userTrainingId'
            },
        ]
    },
    '/v3/user/pto-GET': {
        'parameters': [
        ]
    },
    '/ptopolicies-GET': {
        'parameters': [
        ]
    },
    '/api/v3/userworkflow/assign/{workflowId}-POST': {
        'parameters': [
            {
                'name': 'workflowId'
            },
            {
                'name': 'assigneeUserId'
            },
            {
                'name': 'coordinatorUserId'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/api/v3/task/add-POST': {
        'parameters': [
        ]
    },
    '/api/v3/task/{taskid}-GET': {
        'parameters': [
            {
                'name': 'taskid'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/api/v3/tasks-GET': {
        'parameters': [
        ]
    },
    '/api/v3/userworkflows-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
        ]
    },
    '/api/workflows-GET': {
        'parameters': [
            {
                'name': 'status'
            },
        ]
    },
    '/api/v3/userworkflows/{userworkflowid}-GET': {
        'parameters': [
            {
                'name': 'userworkflowid'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/api/v3/task/update/status-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'appraisalId'
            },
            {
                'name': 'assignedUserId'
            },
            {
                'name': 'ci'
            },
            {
                'name': 'cid'
            },
            {
                'name': 'createUserId'
            },
            {
                'name': 'createts'
            },
            {
                'name': 'description'
            },
            {
                'name': 'dueDate'
            },
            {
                'name': 'lastEdit'
            },
            {
                'name': 'launchts.date'
            },
            {
                'name': 'launchts.day'
            },
            {
                'name': 'launchts.hours'
            },
            {
                'name': 'launchts.minutes'
            },
            {
                'name': 'launchts.month'
            },
            {
                'name': 'launchts.nanos'
            },
            {
                'name': 'launchts.seconds'
            },
            {
                'name': 'launchts.time'
            },
            {
                'name': 'launchts.timezoneOffset'
            },
            {
                'name': 'launchts.year'
            },
            {
                'name': 'phasename'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'recruitId'
            },
            {
                'name': 'statusCode'
            },
            {
                'name': 'systemTask'
            },
            {
                'name': 'taskId'
            },
            {
                'name': 'taskUID'
            },
            {
                'name': 'title'
            },
            {
                'name': 'transitionName'
            },
            {
                'name': 'type'
            },
        ]
    },
};