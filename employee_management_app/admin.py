from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, LeaveReportStaff,  FeedBackStaffs

# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)

admin.site.register(AdminHOD)
admin.site.register(Staffs)

admin.site.register(LeaveReportStaff)
# admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
# admin.site.register(NotificationStudent)
# admin.site.register(NotificationStaffs)
