from django.conf import settings
from django.urls import re_path

from .views import *


branch_mode_urls = [
    re_path(
        r"^merge_request/create/$",
        CreateMergeRequest.as_view(),
        name="create_merge_request",
    ),
    re_path(
        r"^merge_request/list/$", MergeRequestList.as_view(), name="merge_requests_list"
    ),
    re_path(
        r"^merge_request/(?P<merge_request_id>\d+)/$",
        MergeRequestDiscussionView.as_view(),
        name="merge_request",
    ),
    re_path(
        r"^merge_request/(?P<merge_request_id>\d+)/$",
        MergeRequestDiscussionView.as_view(),
        name="merge_request_discussion",
    ),
    re_path(
        r"^merge_request/(?P<merge_request_id>\d+)/changes/$",
        MergeRequestChangesView.as_view(),
        name="merge_request_changes",
    ),
    re_path(
        r"^merge_request/(?P<merge_request_id>\d+)/reopen/$",
        MergeRequestReopenView.as_view(),
        name="merge_request_reopen",
    ),
    re_path(
        r"^merge_request/(?P<merge_request_id>\d+)/follow/$",
        FollowMergeRequestView.as_view(),
        name="merge_request_follow",
    ),
    re_path(
        r"^merge_request/(?P<merge_request_id>\d+)/unfollow/$",
        UnfollowMergeRequestView.as_view(),
        name="merge_request_unfollow",
    ),
    re_path(r"^branch/list/$", BranchesListView.as_view(), name="branches_list"),
    re_path(r"^branch/create/$", CreateBranchView.as_view(), name="create_branch"),
    re_path(r"^delete/$", DeleteBranchView.as_view(), name="delete_branch"),
]

problem_urls = (
    [
        re_path(r"^analysis/$", AnalysisView.as_view(), name="analysis"),
        re_path(
            r"^analysis/generate/$",
            AnalysisGenerateView.as_view(),
            name="analysis_generate",
        ),
        re_path(r"^analysis/analyze/$", AnalyzeView.as_view(), name="analyze"),
        re_path(r"^export/$", ExportView.as_view(), name="export"),
        re_path(
            r"export/(?P<export_id>\d+)/download/$",
            ExportDownloadView.as_view(),
            name="export_download",
        ),
        re_path(
            r"export/(?P<export_id>\d+)/start/$",
            ExportPackageStarterView.as_view(),
            name="export_start",
        ),
        re_path(r"statement/$", EditStatement.as_view(), name="statement"),
        re_path(
            r"statement/(?P<attachment_id>.+)$",
            DownloadStatementAttachment.as_view(),
            name="statement",
        ),
        re_path(r"^history/$", HistoryView.as_view(), name="history"),
        re_path(r"^diff/(?P<other_slug>\w{1,40})/$", DiffView.as_view(), name="diff"),
        re_path(r"^$", Overview.as_view(), name="overview"),
        re_path(r"^discussions/$", DiscussionsListView.as_view(), name="discussions"),
        re_path(
            r"^discussion/add/$", DiscussionAddView.as_view(), name="add_discussion"
        ),
        re_path(
            r"^discussion/(?P<discussion_id>\d+)/comments$",
            CommentListView.as_view(),
            name="comments",
        ),
        re_path(r"^invocations/$", InvocationsListView.as_view(), name="invocations"),
        re_path(
            r"^invocation/add/$", InvocationAddView.as_view(), name="add_invocation"
        ),
        re_path(
            r"^invocation/(?P<invocation_id>\d+)/run/$",
            InvocationRunView.as_view(),
            name="run_invocation",
        ),
        re_path(
            r"^invocation/(?P<invocation_id>\d+)/clone/$",
            InvocationCloneView.as_view(),
            name="clone_invocation",
        ),
        re_path(
            r"^invocation/(?P<invocation_id>\d+)/view/$",
            InvocationDetailsView.as_view(),
            name="view_invocation",
        ),
        re_path(
            r"^invocation/(?P<invocation_id>\d+)/invocation_result/(?P<result_id>\d+)/view/$",
            InvocationResultView.as_view(),
            name="view_invocation_result",
        ),
        re_path(
            r"^invocation/(?P<invocation_id>\d+)/invocation_result/(?P<result_id>\d+)/view/download/output/$",
            InvocationOutputDownloadView.as_view(),
            name="download_output",
        ),
        re_path(
            r"^invocation/(?P<invocation_id>\d+)/invocation_result/(?P<result_id>\d+)/view/download/input/$",
            InvocationInputDownloadView.as_view(),
            name="download_input",
        ),
        re_path(
            r"^invocation/(?P<invocation_id>\d+)/invocation_result/(?P<result_id>\d+)/view/download/answer/$",
            InvocationAnswerDownloadView.as_view(),
            name="download_answer",
        ),
        re_path(r"^resource/add/$", ResourceAddView.as_view(), name="add_resource"),
        re_path(
            r"^resource/(?P<resource_id>\d+)/edit/$",
            ResourceEditView.as_view(),
            name="edit_resource",
        ),
        re_path(
            r"^resource/(?P<object_id>\d+)/delete/$",
            ResourceDeleteView.as_view(),
            name="delete_resource",
        ),
        re_path(
            r"^resource/(?P<object_id>\d+)/download/$",
            ResourceDownloadView.as_view(),
            name="download_resource",
        ),
        re_path(r"^solutions/$", SolutionsListView.as_view(), name="solutions"),
        re_path(r"^solution/add/$", SolutionAddView.as_view(), name="add_solution"),
        re_path(
            r"^solution/(?P<solution_id>.+)/edit/$",
            SolutionEditView.as_view(),
            name="edit_solution",
        ),
        re_path(
            r"^solution/(?P<solution_id>.+)/delete/$",
            SolutionDeleteView,
            name="delete_solution",
        ),
        re_path(
            r"^solution/(?P<solution_id>.+)/source/$",
            SolutionShowSourceView.as_view(),
            name="solution_source",
        ),
        re_path(
            r"^solution/(?P<solution_id>.+)/download/$",
            SolutionDownloadView.as_view(),
            name="download_solution",
        ),
        re_path(r"^graders/$", GradersListView.as_view(), name="graders"),
        re_path(r"^grader/add/$", GraderAddView.as_view(), name="add_grader"),
        re_path(
            r"^grader/(?P<grader_id>.+)/edit/$",
            GraderEditView.as_view(),
            name="edit_grader",
        ),
        re_path(
            r"^grader/(?P<grader_id>.+)/delete/$",
            GraderDeleteView,
            name="delete_grader",
        ),
        re_path(
            r"^grader/(?P<grader_id>.+)/source/$",
            GraderShowSourceView.as_view(),
            name="grader_source",
        ),
        re_path(
            r"^grader/(?P<grader_id>.+)/download/$",
            GraderDownloadView.as_view(),
            name="download_grader",
        ),
        re_path(r"^testcases/$", TestCasesListView.as_view(), name="testcases"),
        re_path(r"^testcase/add/$", TestCaseAddView.as_view(), name="add_testcase"),
        re_path(
            r"^testcase/(?P<testcase_id>.+)/edit/$",
            TestCaseEditView.as_view(),
            name="edit_testcase",
        ),
        re_path(
            r"^testcase/(?P<testcase_id>.+)/delete/$",
            TestCaseDeleteView,
            name="delete_testcase",
        ),
        re_path(
            r"^testcase/(?P<testcase_id>.+)/input/$",
            TestCaseInputDownloadView.as_view(),
            name="testcase_input",
        ),
        re_path(
            r"^testcase/(?P<testcase_id>.+)/output/$",
            TestCaseOutputDownloadView.as_view(),
            name="testcase_output",
        ),
        re_path(
            r"^testcase/(?P<testcase_id>.+)/generate/$",
            TestCaseGenerateView.as_view(),
            name="generate_testcase",
        ),
        re_path(
            r"^testcase/generate/all/$",
            TestCaseGenerateView.as_view(),
            name="generate_testcase",
        ),
        re_path(
            r"^testcase/(?P<testcase_id>.+)/details/$",
            TestCaseDetailsView.as_view(),
            name="testcase_details",
        ),
        re_path(r"^subtasks/$", SubtasksListView.as_view(), name="subtasks"),
        re_path(r"^subtask/add/$", SubtaskAddView.as_view(), name="add_subtask"),
        re_path(
            r"^subtask/(?P<subtask_id>.+)/details/$",
            SubtaskDetailsView.as_view(),
            name="subtask_details",
        ),
        re_path(
            r"^subtask/(?P<subtask_id>.+)/delete/$",
            SubtaskDeleteView,
            name="delete_subtask",
        ),
        re_path(
            r"^subtask/(?P<subtask_id>.+)/edit/$",
            SubtaskEditView.as_view(),
            name="edit_subtask",
        ),
        re_path(r"^validators/$", ValidatorsListView.as_view(), name="validators"),
        re_path(
            r"^validator/(?P<validator_id>.+)/edit/$",
            ValidatorEditView.as_view(),
            name="edit_validator",
        ),
        re_path(
            r"^validator/(?P<validator_id>.+)/delete/$",
            ValidatorDeleteView,
            name="delete_validator",
        ),
        re_path(
            r"^validator/(?P<validator_id>.+)/source/$",
            ValidatorShowSourceView.as_view(),
            name="validator_source",
        ),
        re_path(r"^validator/add/$", ValidatorAddView.as_view(), name="add_validator"),
        re_path(
            r"^validator/(?P<validator_id>.+)/download/$",
            ValidatorDownloadView.as_view(),
            name="download_validator",
        ),
        re_path(r"^generators/$", GeneratorsListView.as_view(), name="generators"),
        re_path(
            r"^generator/(?P<generator_id>.+)/edit/$",
            GeneratorEditView.as_view(),
            name="edit_generator",
        ),
        re_path(
            r"^generator/(?P<generator_id>.+)/delete/$",
            GeneratorDeleteView,
            name="delete_generator",
        ),
        re_path(
            r"^generator/(?P<generator_id>.+)/source/$",
            GeneratorShowSourceView.as_view(),
            name="generator_source",
        ),
        re_path(r"^generator/add/$", GeneratorAddView.as_view(), name="add_generator"),
        re_path(
            r"^generator/(?P<generator_id>.+)/generate-testcases/$",
            GeneratorEnableView.as_view(),
            name="enable_generator",
        ),
        re_path(
            r"^generator/(?P<generator_id>.+)/delete-testcases/$",
            GeneratorDisableView.as_view(),
            name="disable_generator",
        ),
        re_path(r"^checkers/$", CheckerListView.as_view(), name="checkers"),
        re_path(r"^checker/add/$$", CheckerAddView.as_view(), name="add_checker"),
        re_path(
            r"^checker/(?P<checker_id>.+)/activate/$$",
            CheckerActivateView.as_view(),
            name="activate_checker",
        ),
        re_path(
            r"^checker/(?P<checker_id>.+)/delete/$$",
            CheckerDeleteView,
            name="delete_checker",
        ),
        re_path(
            r"^checker/(?P<checker_id>.+)/edit/$$",
            CheckerEditView.as_view(),
            name="edit_checker",
        ),
        re_path(
            r"^checker/(?P<checker_id>.+)/source/$$",
            CheckerShowSourceView.as_view(),
            name="checker_source",
        ),
        re_path(
            r"^checker/(?P<checker_id>.+)/download/$$",
            CheckerDownloadView.as_view(),
            name="download_checker",
        ),
        re_path(r"^pull/$", PullBranchView.as_view(), name="pull_branch"),
        re_path(r"^commit/$", CommitWorkingCopy.as_view(), name="commit"),
        re_path(r"^discard/$", DiscardWorkingCopy.as_view(), name="discard"),
        re_path(r"^conflicts/$", ConflictsListView.as_view(), name="conflicts"),
        re_path(
            r"^conflict/(?P<conflict_id>\d+)/$",
            ResolveConflictView.as_view(),
            name="resolve_conflict",
        ),
        re_path(r"files/list/$", ProblemFilesView.as_view(), name="files"),
        re_path(r"files/add/$", ProblemFileAddView.as_view(), name="add_file"),
        re_path(
            r"^files/(?P<file_id>\d+)/edit/$",
            ProblemFileEditView.as_view(),
            name="edit_file",
        ),
        re_path(
            r"^files/(?P<file_id>\d+)/delete/$",
            ProblemFileDeleteView.as_view(),
            name="delete_file",
        ),
        re_path(
            r"^files/(?P<file_id>\d+)/source/$",
            ProblemFileShowSourceView.as_view(),
            name="file_source",
        ),
        re_path(
            r"^files/(?P<file_id>\d+)/download/$",
            ProblemFileDownloadView.as_view(),
            name="download_file",
        ),
    ]
    + (branch_mode_urls if not settings.DISABLE_BRANCHES else []),
    None,
    None,
)

urlpatterns = [
    re_path(r"^$", ProblemsListView.as_view(), name="problems"),
    re_path(
        r"^problem/(?P<problem_code>[^\/]+)/(?P<revision_slug>\w{1,40})/", problem_urls
    ),
    re_path(r"^problem/add/$", ProblemAddView.as_view(), name="add_problem"),
]
