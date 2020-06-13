from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

from . import models
from .models import Profile
from ..common.forms import UserForm, SignUpForm

admin.site.site_header = "MIT RHA Administration"


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class ProfileAdmin(ImportExportModelAdmin):
    inlines = (ProfileInline,)
    list_display = ['first_name', 'last_name', 'username', 'email', 'get_cert_id', 'get_job_location', 'get_job_title']
    list_select_related = ('profile',)
    list_display_links  = ['first_name', 'last_name', 'username']
    search_fields = ['username', 'first_name', 'last_name','profile__cert_id','profile__job_location',]

    def get_cert_id(self, instance):
        return instance.profile.cert_id

    get_cert_id.short_description = 'Cert_ID'

    def get_job_location(self, instance):
        return instance.profile.job_location

    get_job_location.short_description = 'Job_Location'

    def get_job_title(self, instance):
        return instance.profile.job_title

    get_job_title.short_description = 'Job_Title'

    def get_inline_instance(self, request, obj=None):
        if not obj:
            return list()
        return super(ProfileAdmin, self).get_inline_instance(request, obj)



class ProAdmin(ImportExportModelAdmin):

    list_display = ['user','get_first_name','get_last_name','get_email','cert_id','job_location','job_title','phone_number']
    search_fields = ['user__username','cert_id','job_location','job_title','user__first_name','user__last_name']
    list_filter = ['cert_id','job_title','job_location',]
    list_select_related = ('user',)

    def get_first_name(self, instance):
        return  instance.user.first_name
    get_first_name.short_description= 'First Name'

    def get_last_name(self, instance):
        return  instance.user.last_name
    get_last_name.short_description= 'Last Name'

    def get_email(self, instance):
        return  instance.user.email
    get_email.short_description= 'Email'



admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.register(Profile,ProAdmin)
'''@admin.register(Profile,ProAdmin)
class ProfilAdmin1(ImportExportModelAdmin):
    pass
'''