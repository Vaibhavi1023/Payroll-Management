from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, LeaveReportStaff,  FeedBackStaffs, NotificationStaffs, Group, Site, AttendanceReportStaff

# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)

admin.site.register(AdminHOD)
admin.site.register(Staffs)

admin.site.register(Group)
admin.site.register(Site)
admin.site.register(AttendanceReportStaff)

admin.site.register(LeaveReportStaff)
# admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
# admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
