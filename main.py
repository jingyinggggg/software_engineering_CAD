import flet
from flet import *
from flet_route import Routing, path

# Shared interface
from welcome import WelcomePage
from login import LoginPage
from signUp import SignUpPage
from resetPassword import ResetPasswordPage

# Patient's interface
from homepage import Homepage
from medicalRecord import MedicalRecordPage
from addMedicalRecord import AddMedicalRecordPage
from viewMedicalRecord import ViewMedicalRecordPage
from setting import SettingPage
from password import PasswordPage
from accountSetting import AccountSettingPage
from clinic import ClinicPage
from viewClinic import ViewClinicPage
from doctorListClinic import DoctorListBasedOnClinic
from doctor import DoctorPage
from viewDoctor import ViewDoctorPage
from makeAppointment import MakeAppointmentPage
from patientPrescription import PatientPrescriptionPage
from viewPrescription import ViewPrescriptionPage
from healthTips import HealthTipsPage
from bookingPage import BookingPage
from viewBooking import ViewBookingPage
from profile import ProfilePage
from patientNotification import PatientNotificationPage
from patientChatViewDoctor import PatientChatViewDoctorPage
from patientChat import PatientChatPage
from patientCallDoctor import PatientCallDoctorPage

# Doctor's interface
from doctorHomepage import DoctorHomepage
from doctorNotification import DoctorNotification
from history import HistoryPage
from historyDetail import HistoryDetail
from schedule import Schedule
from appointmentDetail import AppointmentDetail
from chat import Chat
from chat_info import ChatInfo
from prescription import Prescription
from doctorSetting import DoctorSettingPage
from doctorPassword import DoctorPasswordPage
from doctorAccountSetting import DoctorAccountSettingPage
from doctorProfile import DoctorProfilePage
from prescriptionList import PrescriptionList
from appointment import Appointment
from doctorViewMedicalRecord import DoctorViewMedicalRecord
from doctorViewMedicalRecordList import DoctorViewMedicalRecordList
from doctorCallInterface import DoctorCallInterface
from doctorGeneratePrescription import DoctorGeneratePrescription
from editPrescription import EditPrescription
from proofStatus import ProofStatus
from viewProof import ViewProofPage

# Clinic's interface
from clinicSignUp import ClinicSignUpPage
from addDoctorDetails import AddDoctorDetailsPage
from clinicHomepage import ClinicHomepage
from clinicProfile import ClinicProfile
from clinicViewDoctorDetails import ClinicViewDoctorDetails
from clinicModifyDeclineDetails import ClinicModifyDeclineDetails
from clinicViewAppointment import ClinicViewAppointment
from clinicViewPatient import ClinicViewPatient
from createAdminAccount import CreateAdminAccount
from appointmentChart import ClinicViewAppointmentChart

# Clinic admin interface
from clinicAdminHomepage import AdminHomepage
from clinicAdminPatientRequestList import AdminPatientRequestList
from clinicAdminPatientAppointmentList import ClinicAdminPatientAppointmentList
from clinicAdminPatientAppointmentDetails import ClinicAdminPatientAppointmentDetails
from clinicAdminUpdateAppointment import ClinicAdminUpdateAppointmentPage
from clinicAdminUpdateAppointmentDetails import ClinicAdminUpdateAppointmentDetailsPage
from clinicAdminSetting import ClinicAdminSettingPage
from clinicAdminAccountPage import ClinicAdminAccountPage
from clinicAdminPasswordPage import ClinicAdminPasswordPage
from clinicAdminManageDoctor import ClinicAdminManageDoctorPage
from clinicAdminAddNewDoctorList import ClinicAdminAddNewDoctorList
from clinicAdminAddNewDoctorPage import ClinicAdminAddNewDoctorPage
from clinicAdminEditDoctorPage import ClinicAdminEditDoctorPage
from clinicAdminDeleteDoctorPage import ClinicAdminDeleteDoctorPage

# Project admin interface
from projectAdminHomepage import ProjectAdminHomepage
from projectAdminViewClinicDetail import ProjectAdminViewClinicDetail

def main(mainPage: Page):
    mainPage.theme_mode = "dark"

    app_routes = [

        # Shared interface path
        path(url="/", clear=True, view=WelcomePage().view),
        path(url="/loginUser", clear=False, view=LoginPage().view),
        path(url="/signUp", clear=False, view=SignUpPage().view),
        path(url="/resetPassword", clear=False, view=ResetPasswordPage().view),


        # Patient interface path
        path(url="/homepage/:user_id", clear=False, view=Homepage().view),
        path(url="/patientNotification/:user_id", clear=False, view=PatientNotificationPage().view),
        path(url="/medicalRecord/:user_id", clear=False, view=MedicalRecordPage().view),
        path(url="/addMedicalRecord/:user_id", clear=False, view=AddMedicalRecordPage().view),
        path(url="/viewMedicalRecord/:medicalRecord_id", clear=False, view=ViewMedicalRecordPage().view),
        path(url="/setting/:user_id", clear=False, view=SettingPage().view),
        path(url="/accountSetting/:user_id", clear=False, view=AccountSettingPage().view),
        path(url="/password/:user_id", clear=False, view=PasswordPage().view),
        path(url="/clinic/:user_id", clear=False, view=ClinicPage().view),
        path(url="/viewClinic/:user_id:clinic_id", clear=False, view=ViewClinicPage().view),
        path(url="/doctorListBasedOnClinic/:user_id:clinic_id", clear=False, view=DoctorListBasedOnClinic().view),
        path(url="/doctor/:user_id", clear=False, view=DoctorPage().view),
        path(url="/viewDoctor/:user_id:doctor_id:previous_page", clear=False, view=ViewDoctorPage().view),
        path(url="/makeAppointment/:user_id:doctor_id:previous_page", clear=False, view=MakeAppointmentPage().view),
        path(url="/patientPrescription/:user_id", clear=False, view=PatientPrescriptionPage().view),
        path(url="/viewPrescription/:user_id/:prescription_id", clear=False, view=ViewPrescriptionPage().view),
        path(url="/healthTips/:user_id", clear=False, view=HealthTipsPage().view),
        path(url="/patientChatViewDoctor/:user_id", clear=False, view=PatientChatViewDoctorPage().view),
        path(url="/patientChat/:user_id:doctor_id", clear=False, view=PatientChatPage().view),
        path(url="/booking/:user_id", clear=False, view=BookingPage().view),
        path(url="/viewBooking/:user_id:booking_id", clear=False, view=ViewBookingPage().view),
        path(url="/profile/:user_id", clear=False, view=ProfilePage().view),
        path(url="/patientCall/:user_id:doctor_id", clear=False, view=PatientCallDoctorPage().view),


        # Doctor interface path
        path(url="/login/homepage/:user_id", clear=False, view=DoctorHomepage().view),
        path(url="/doctorNotification/:user_id", clear=False, view=DoctorNotification().view),
        path(url="/history/:user_id", clear=False, view=HistoryPage().view),
        path(url="/historyDetail/:user_id:appointment_id", clear=False, view=HistoryDetail().view),
        path(url="/schedule/:user_id", clear=False, view=Schedule().view),
        path(url="/appointmentDetail/:user_id:appointment_id", clear=False, view=AppointmentDetail().view),
        path(url="/chat/:user_id:patient_id", clear=False, view=Chat().view),
        path(url="/chat_info/:user_id:patient_id", clear=False, view=ChatInfo().view),
        path(url="/prescription/:user_id/:prescription_id", clear=False, view=Prescription().view),
        path(url="/doctorSettingPage/:user_id", clear=False, view=DoctorSettingPage().view),
        path(url="/doctorPassword/:user_id", clear=False, view=DoctorPasswordPage().view),
        path(url="/doctorAccountSetting/:user_id", clear=False, view=DoctorAccountSettingPage().view),
        path(url="/doctorPassword/:user_id", clear=False, view=DoctorPasswordPage().view),
        path(url="/doctorProfile/:user_id", clear=False, view=DoctorProfilePage().view),
        path(url="/prescriptionList/:user_id", clear=False, view=PrescriptionList().view),
        path(url="/appointment/:user_id", clear=False, view=Appointment().view),
        path(url="/doctorViewMedicalRecord/:medicalRecord_id:patient_id", clear=False,
             view=DoctorViewMedicalRecord().view),
        path(url="/doctorViewMedicalRecordList/:user_id:patient_id", clear=False,
             view=DoctorViewMedicalRecordList().view),
        path(url="/doctorCallInterface/:user_id:patient_id", clear=False, view=DoctorCallInterface().view),
        path(url="/doctorGeneratePrescription/:user_id/:booking_id", clear=False,
             view=DoctorGeneratePrescription().view),
        path(url="/editPrescription/:user_id/:prescription_id", clear=False, view=EditPrescription().view),
        path(url="/proofStatus/:user_id", clear=False, view=ProofStatus().view),
        path(url="/viewProof/:user_id/:booking_id", clear=False, view=ViewProofPage().view),


        # Clinic interface path
        path(url="/clinicSignUp", clear=False, view=ClinicSignUpPage().view),
        path(url="/addDoctorDetails/:clinic_id", clear=False, view=AddDoctorDetailsPage().view),
        path(url="/clinicHomepage/:user_id", clear=False, view=ClinicHomepage().view),
        path(url="/clinicProfile/:clinic_id", clear=False, view=ClinicProfile().view),
        path(url="/clinicViewDoctorDetails/:doctor_id:clinic_id", clear=False, view=ClinicViewDoctorDetails().view),
        path(url="/clinicModifyDeclineDetails/:clinic_id", clear=False, view=ClinicModifyDeclineDetails().view),
        path(url="/clinicViewAppointment/:clinic_id", clear=False, view=ClinicViewAppointment().view),
        path(url="/clinicViewPatient/:clinic_id", clear=False, view=ClinicViewPatient().view),
        path(url="/createAdminAccount/:clinic_id", clear=False, view=CreateAdminAccount().view),
        path(url="/clinicViewAppointmentChart/:clinic_id", clear=False, view=ClinicViewAppointmentChart().view),


        # Clinic admin interface path
        path(url="/login/adminHomepage/:user_id", clear=False, view=AdminHomepage().view),
        path(url="/admin/adminPatientRequestList/:user_id", clear=False, view=AdminPatientRequestList().view),
        path(url="/admin/clinicAdminPatientAppointmentList/:user_id", clear=False,
             view=ClinicAdminPatientAppointmentList().view),
        path(url="/admin/clinicAdminPatientAppointmentDetails/:user_id:booking_id", clear=False,
             view=ClinicAdminPatientAppointmentDetails().view),
        path(url="/admin/clinicAdminUpdateAppointment/:user_id", clear=False, view=ClinicAdminUpdateAppointmentPage().view),
        path(url="/admin/clinicAdminUpdateAppointmentDetails/:user_id:booking_id", clear=False, view=ClinicAdminUpdateAppointmentDetailsPage().view),
        path(url="/admin/setting/:user_id", clear=False, view=ClinicAdminSettingPage().view),
        path(url="/admin/account/:user_id", clear=False, view=ClinicAdminAccountPage().view),
        path(url="/admin/password/:user_id", clear=False, view=ClinicAdminPasswordPage().view),
        path(url="/admin/clinicAdminManageDoctor/:user_id", clear=False, view=ClinicAdminManageDoctorPage().view),
        path(url="/admin/clinicAdminAddNewDoctorList/:user_id", clear=False, view=ClinicAdminAddNewDoctorList().view),
        path(url="/admin/clinicAdminAddNewDoctorPage/:user_id:doctor_id", clear=False, view=ClinicAdminAddNewDoctorPage().view),
        path(url="/admin/clinicAdminEditDoctorPage/:user_id:doctor_id", clear=False, view=ClinicAdminEditDoctorPage().view),
        path(url="/admin/clinicAdminDeleteDoctorPage/:user_id:doctor_id", clear=False, view=ClinicAdminDeleteDoctorPage().view),


        # Project admin interface path
        path(url="/projectAdminHomepage/:user_id", clear=False, view=ProjectAdminHomepage().view),
        path(url="/projectAdminViewClinicDetail/:user_id:clinic_id", clear=False, view=ProjectAdminViewClinicDetail().view),

    ]
    Routing(page=mainPage, app_routes=app_routes)
    mainPage.go(mainPage.route)


if __name__ == "__main__":
    flet.app(target=main, upload_dir="pic")