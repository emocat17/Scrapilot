from django.conf.urls import url
from rest_framework.authtoken import views as auth
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/user/auth', auth.obtain_auth_token),
    url(r'^api/index/status$', views.index_status, name='index_status'),
    url(r'^api/client$', views.client_index, name='client_index'),
    url(r'^api/client/create', views.client_create, name='client_create'),
    url(r'^api/client/(\d+)$', views.client_info, name='client_info'),
    url(r'^api/client/(\d+)/status', views.client_status, name='client_status'),
    url(r'^api/client/(\d+)/update', views.client_update, name='client_update'),
    url(r'^api/client/(\d+)/remove', views.client_remove, name='client_remove'),
    url(r'^api/client/(\d+)/projects', views.project_list, name='project_list'),
    url(r'^api/client/(\d+)/project/(\S+)/spiders', views.spider_list, name='spider_list'),
    url(r'^api/client/(\d+)/project/(\S+)/spider/(\S+)/job/(\S+)/log', views.job_log, name='job_log'),
    url(r'^api/client/(\d+)/project/(\S+)/spider/(\S+)$', views.spider_start, name='spider_start'),
    url(r'^api/client/(\d+)/project/(\S+)/jobs', views.job_list, name='job_list'),
    url(r'^api/client/(\d+)/project/(\S+)/version', views.project_version, name='project_version'),
    url(r'^api/client/(\d+)/project/(\S+)/deploy', views.project_deploy, name='project_deploy'),
    url(r'^api/client/(\d+)/project/(\S+)/job/(\S+)/cancel', views.job_cancel, name='job_cancel'),
    url(r'^api/project/index', views.project_index, name='project_index'),
    url(r'^api/project/create', views.project_create, name='project_create'),
    url(r'^api/project/upload', views.project_upload, name='project_upload'),
    url(r'^api/project/clone', views.project_clone, name='project_clone'),
    url(r'^api/project/(\S+)/configure', views.project_configure, name='project_configure'),
    url(r'^api/project/(\S+)/build', views.project_build, name='project_build'),
    url(r'^api/project/(\S+)/tree', views.project_tree, name='project_tree'),
    url(r'^api/project/(\S+)/remove', views.project_remove, name='project_remove'),
    url(r'^api/project/(\S+)/parse', views.project_parse, name='project_parse'),
    url(r'^api/project/file/rename', views.project_file_rename, name='project_file_rename'),
    url(r'^api/project/file/delete', views.project_file_delete, name='project_file_delete'),
    url(r'^api/project/file/create', views.project_file_create, name='project_file_create'),
    url(r'^api/project/file/update', views.project_file_update, name='project_file_update'),
    url(r'^api/project/file/read', views.project_file_read, name='project_file_read'),
    url(r'^api/monitor/create', views.monitor_create, name='monitor_create'),
    url(r'^api/monitor/db/list', views.monitor_db_list, name='monitor_db_list'),
    url(r'^api/monitor/collection/list', views.monitor_collection_list, name='monitor_collection_list'),
    url(r'^api/task$', views.task_index, name='task_index'),
    url(r'^api/task/create', views.task_create, name='task_create'),
    url(r'^api/task/(\d+)/update', views.task_update, name='task_update'),
    url(r'^api/task/(\d+)/info', views.task_info, name='task_info'),
    url(r'^api/task/(\d+)/remove', views.task_remove, name='task_remove'),
    url(r'^api/task/(\d+)/status', views.task_status, name='task_status'),
    url(r'^api/render', views.render_html, name='render_html'),
    # 资源可视化
    url(r'^api/index/host/infos', views.index_host_infos, name='index_host_infos'),

    # 用户管理
    url(r'^api/account/list', views.account_list, name='account_list'),
    url(r'^api/account/(\d+)/remove', views.account_remove, name='account_remove'),

    # 用户管理按钮功能
    url(r'^api/account/create', views.account_create, name='account_create'),
    url(r'^api/account/(\d+)/info', views.account_info, name='account_info'),
    url(r'^api/account/(\d+)/update', views.account_update, name='account_update'),

]
