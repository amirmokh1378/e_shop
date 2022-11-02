from django.apps import AppConfig


class MyprojectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_project'


from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = 'my_project.admin.MyAdminSite'
