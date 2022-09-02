# WCE22_Assassins

FE and WCE 2022 project on attendance and payroll app

## Description

An in-depth paragraph about your project, the tools and methods used, design approach, and overview of use.


![WCE22 Diagrams-Payroll App Schematic drawio](https://user-images.githubusercontent.com/91695658/188133032-d267424c-96be-4fa9-8ce7-1e3d540b34eb.png)


## Project Structure

Django - MySQL 

User module is already there in ver 1.0  www.feweather.com

All other modules have to be added as pert of ver 2.0.  
 - Shift Management, Leave and  Advance Request, Payroll Reports and Scorecard report, Attendance Device Management, Missing Punch Report and Updation, Manual Punch 



### Directory Structure

### following tables already exist in fedbmiraj database 
  employee
  site 
  team
 
### following new tables are required :
 attendance_mc ( Proton Team will be creating this)
 holiday
 leave
 shift_Rate_Default
 shift_Rate_Actual
 app_attendance 
 

Explain the project structure including which folders contain what.

Shift Rate Default is a team wise - day wise Salary Rate / Day.  Shift Rate Actual is the rate updated by site manager at the end of each day. If Shift Rate Actual is not updated then the default Shift Rate is used for calculation of salary .


### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

## Usage

### Installing

* All steps to install your project
* Any modifications needed to be made to files/folders

### Executing

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Here's a link to the presentation about coding practices and guide to git and GitHub: [link](https://drive.google.com/file/d/1_Xi1FKCGCzO1_1x3FQt5Na09HfqZmm2g/view?usp=sharing)

### Screen Layout Template

![FirstScreen Layout](https://user-images.githubusercontent.com/91695658/184523458-e53e2626-8f09-4e21-a7ed-2b2bbcb0fc9d.png)



Add any additional documentation.

Any advise for common problems or issues.
```
command to run if program contains helper info
```
### Contacts for tech 'champions'

[Flutter](https://flutter.dev/): Brijesh Kumar 9541346955

[MySQL](https://www.mysql.com/): Aman Agrawal 8766468554

[Django](https://www.djangoproject.com/): Saurabh Patil 7083204629

[PHP](https://www.php.net/): Parshwa Onil Shah 8796200905

[Git](https://git-scm.com/): Vyankatesh Sanjay Bura 8850426459

## Authors

Contributors names and contact info

ex. John Doe [@JDoe](https://github.com/)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release
