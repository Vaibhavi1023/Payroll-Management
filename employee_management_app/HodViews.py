from dataclasses import fields
from datetime import datetime
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import csv
from employee_management_app.models import CustomUser,  Staffs,  FeedBackStaffs,  LeaveReportStaff, AttendanceReportStaff, Group, Site

from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django import forms

def admin_home(request):
   
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    print("................")
    print(request.user.id)
    return render(request, "hod_template/home_content.html", context)


def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")


def add_staff_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_staff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        group_id=request.POST.get('group_id')
        site_id=request.POST.get('site_id')
        # staff_id=Staffs.objects.get(group_id=group_id)
        address = request.POST.get('address')
        try:
            print(group_id)
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, group_id_id=group_id,site_id_id=site_id, user_type=2 )
            # user2 = customuser_groups.objects.create_user(group_id=group_id)
            user.staffs.address = address
            user.staffs.group_id_id=group_id
            user.staffs.site_id_id = site_id
            # user.staffs.admin_id=request.user.id
            
            print('2')
            user.save()
            # user2.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_staff')



def manage_staff(request):
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    return render(request, "hod_template/manage_staff_template.html", context)





def add_group(request):
    return render(request, "hod_template/add_group.html")



def add_group_save(request):
    
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_group')
    else:
        gname = request.POST.get('gname')
        try:
            user = Group.objects.create( gname=gname)
            # print(user)
            user.save()
            messages.success(request, "Group Added Successfully!")
            return redirect('add_group')
        except:
            messages.error(request, "Failed to Add Group!")
            return redirect('add_group')

def manage_group(request):
    groups = Group.objects.all()
    context = {
        "groups": groups
    }
    return render(request, "hod_template/manage_group.html", context)



def add_site(request):
    return render(request, "hod_template/add_site.html")



def add_site_save(request):
    
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_site')
    else:
        sname = request.POST.get('sname')
        try:
            user = Site.objects.create( sname=sname)
            # print(user)
            user.save()
            messages.success(request, "Site Added Successfully!")
            return redirect('add_site')
        except:
            messages.error(request, "Failed to Add Site!")
            return redirect('add_site')

def manage_site(request):
    sites = Site.objects.all()
    context = {
        "sites": sites
    }
    return render(request, "hod_template/manage_site.html", context)




def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)

    context = {
        "staff": staff,
        "id": staff_id
    }
    return render(request, "hod_template/edit_staff_template.html", context)


def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()

            # INSERTING into Staff Model
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Staff Updated Successfully.")
            return redirect('/edit_staff/'+staff_id)

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_staff/'+staff_id)



def delete_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request, "Staff Deleted Successfully.")
        return redirect('manage_staff')
    except:
        messages.error(request, "Failed to Delete Staff.")
        return redirect('manage_staff')






@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)





def staff_feedback_message(request):
    feedbacks = FeedBackStaffs.objects.all()
    context = {
        "feedbacks": feedbacks
    }
    return render(request, 'hod_template/staff_feedback_template.html', context)


@csrf_exempt
def staff_feedback_message_reply(request):
    feedback_id = request.POST.get('id')
    feedback_reply = request.POST.get('reply')

    try:
        feedback = FeedBackStaffs.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        return HttpResponse("True")

    except:
        return HttpResponse("False")




def staff_leave_view(request):
    leaves = LeaveReportStaff.objects.all()
    context = {
        "leaves": leaves
    }
    return render(request, 'hod_template/staff_leave_view.html', context)


def staff_leave_approve(request, leave_id):
    leave = LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status = 1
    leave.save()
    return redirect('staff_leave_view')


def staff_leave_reject(request, leave_id):
    leave = LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status = 2
    leave.save()
    return redirect('staff_leave_view')



def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context={
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)


def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')



def staff_profile(request):
    pass


def student_profile(request):
    pass




def add_attendance(request):
    return render(request, "hod_template/add_attendance_template.html")



def add_attendance_save(request):
   
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_attendance')
    else:
    
        staff_id_id=request.POST.get('staff_id')
        # staff_id=Staffs.objects.get(admin=x)
        # print(staff_id.id)
        attendance_date=request.POST.get('attendance_date')
        # payroll_date =request.POST.get('attendance_date')
       
        # if PayrollReportStaff.objects.filter(staff_id=Staffs.objects.get(admin=x)).exists():
        #     y=PayrollReportStaff.objects.filter(staff_id=Staffs.objects.get(admin=x))
        #     print(y)
        #     for i in y : 
                
        #         z= i.payroll_money
        #         payroll_money=z+100
        # else:
        #     payroll_money= 100

        # attendance_message = request.POST.get('attendance_message')
        # attendance_status = request.POST.get('attendance_status')
        intime= request.POST.get('intime')
        outtime= request.POST.get('outtime')
        # class Meta:
        #     model= AttendanceReportStaff
        #     fields= "__all__"
        #     widgets={
        #         "attendance_date": AdminDateWidget(),
        #         "intime": AdminTimeWidget(),
        #         "outtime": AdminTimeWidget(),
        #     }

        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # address = request.POST.get('address')

        try:
            user = AttendanceReportStaff.objects.create(staff_id_id=staff_id_id,attendance_date=attendance_date, intime=intime, outtime=outtime)
            # user2 = PayrollReportStaff.objects.create(staff_id=staff_id,payroll_date=attendance_date,payroll_money=payroll_money)

            #user.save()
            messages.success(request, "Attendance Added Successfully!")
            return redirect('add_attendance')
        except:
            messages.error(request, "Failed to Add Attendance!")
            return redirect('add_attendance')

def staff_attendance_view(request):
    attendance = AttendanceReportStaff.objects.all()
    context = {

        "attendance": attendance
    }
    return render(request, 'hod_template/staff_attendance_view.html', context)




def edit_attendance(request, staff_id):
    attendance = AttendanceReportStaff.objects.all()

    context = {
        "attendance": attendance,
        "id": staff_id
    }
    return render(request, "hod_template/edit_attendance.html", context)


def edit_attendance_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        attendance_date=request.POST.get('attendance_date')
        intime=request.POST.get('intime')
        outtime=request.POST.get('outtime')
        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.attendance_date=attendance_date
            user.intime=intime
            user.outtime=outtime
            user.save()

            # INSERTING into Staff Model
            attendance_model = AttendanceReportStaff.objects.get(admin=staff_id)
            attendance_model.attendance_date = attendance_date
            attendance_model.intime = intime
            attendance_model.outtime = outtime
            attendance_model.save()

            messages.success(request, "Attendance Updated Successfully.")
            return redirect('/edit_staff/'+staff_id)

        except:
            messages.error(request, "Failed to Update Attendance.")
            return redirect('/edit_attendance/'+staff_id)

# def staff_attendance_view(request):
#     staffs = Staffs.objects.all()
#     context = {
#         "staffs": staffs
#     }
#     return render(request, "hod_template/staff_attendance_view.html", context)   
# def add_payroll_save(request):
   
#     if request.method != "POST":
#         messages.error(request, "Invalid Method ")
#         return redirect('add_attendance')
#     else:
    
#         x=request.POST.get('staff_id')
#         staff_id=Staffs.objects.get(admin=x)
#         print(staff_id.id)


        # payroll_date =request.POST.get('attendance_date')
        # attendance_message = request.POST.get('attendance_message')
        # attendance_status = request.POST.get('attendance_status')
        # intime= request.POST.get('intime')
        # outtime= request.POST.get('outtime')
        # class Meta:
        #     model= AttendanceReportStaff
        #     fields= "__all__"
        #     widgets={
        #         "attendance_date": AdminDateWidget(),
        #         "intime": AdminTimeWidget(),
        #         "outtime": AdminTimeWidget(),
        #     }

        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # address = request.POST.get('address')

        # try:
        #     # user = PayrollReportStaff.objects.create(staff_id=staff_id,payroll_date=payroll_date)
        #     #user.save()
        #     messages.success(request, "Attendance Added Successfully!")
        #     return redirect('add_attendance')
        # except:
        #     messages.error(request, "Failed to Add Attendance!")
        #     return redirect('add_attendance')

# def staff_payroll_views(request):
#     payroll= PayrollReportStaff.objects.all()
#     context = {

#         "payroll": payroll
#     }

#     print(payroll)


#     return render(request, 'hod_template/staff_payroll_template.html', context)


def export_csv(request):

    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; fileName=Attendance'+ '.csv'
    writer=csv.writer(response)
    writer.writerow(['Staff ID','Attendance Date','In Time','Out Time'])


    attendances = AttendanceReportStaff.objects.all()
    for attendance in attendances:

        writer.writerow([attendance.staff_id.id+1, attendance.attendance_date,attendance.intime,attendance.outtime])
    return response



def attendance_report(request):
    return render(request, 'hod_template/attendance_report.html')



def payroll_report(request):
    return render(request, 'hod_template/payrollreport.html')



def unapprovedleave_report(request):
    return render(request, 'hod_template/unapprovedleave.html')






from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework import viewsets,status


from rest_framework.response import Response
import pandas as pd           
# remember to import the File model
# remember to import the FileUploadSerializer and SaveFileSerializer

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file, on_bad_lines='skip', encoding='latin-1')
        ct=0
        sp=-1
        
        for _, row in reader.iterrows():
            sp=row['id']
            import math
            # print("//////////////////////")
            ct=ct+1
            if sp==-1:
                print("......errror solved>>>")
                break
            new_file = AttendanceReportStaff(
                      
                       id=row['id'],
                       staff_id_id = row["staff_id_id"],
                       attendance_date= row["attendance_date"],
                       intime= row["intime"],
                       outtime= row["outtime"],
                       )
            # print(sp)
            
            # print(ct)
            # print("....................")
            new_file.save()
        print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb......")
        return Response({"status": "success"},   status.HTTP_201_CREATED)

