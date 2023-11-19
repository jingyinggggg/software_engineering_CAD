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

# Doctor's interface
from doctorHomepage import DoctorHomepage
from doctorNotification import DoctorNotification
from history import HistoryPage
from schedule import Schedule
from appointmentDetail import AppointmentDetail
from chat import Chat
from prescription import Prescription

# Clinic's interface
from clinicSignUp import ClinicSignUpPage
from addDoctorDetails import AddDoctorDetailsPage
from clinicHomepage import ClinicHomepage

# Clinic admin interface
from clinicAdminHomepage import AdminHomepage
from clinicAdminPatientRequestList import AdminPatientRequestList
from clinicAdminUpdateAppointment import ClinicAdminUpdateAppointmentPage
from clinicAdminUpdateAppointmentDetails import ClinicAdminUpdateAppointmentDetailsPage

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
        path(url="/viewPrescription/:user_id", clear=False, view=ViewPrescriptionPage().view),
        # path(url="/viewPrescription/:prescription_id", clear=False, view=PatientPrescriptionPage().view),
        path(url="/healthTips/:user_id", clear=False, view=HealthTipsPage().view),
        path(url="/patientChatViewDoctor/:user_id", clear=False, view=PatientChatViewDoctorPage().view),
        path(url="/patientChat/:user_id:doctor_id", clear=False, view=PatientChatPage().view),
        path(url="/booking/:user_id", clear=False, view=BookingPage().view),
        path(url="/viewBooking/:user_id:booking_id", clear=False, view=ViewBookingPage().view),
        path(url="/profile/:user_id", clear=False, view=ProfilePage().view),


        # Doctor interface path
        path(url="/login/homepage/:user_id", clear=False, view=DoctorHomepage().view),
        path(url="/doctorNotification/:user_id", clear=False, view=DoctorNotification().view),
        path(url="/history", clear=False, view=HistoryPage().view),
        path(url="/schedule", clear=False, view=Schedule().view),
        path(url="/appointmentDetail/:user_id", clear=False, view=AppointmentDetail().view),
        path(url="/chat", clear=False, view=Chat().view),
        path(url="/prescription", clear=False, view=Prescription().view),


        # Clinic interface path
        path(url="/clinicSignUp", clear=False, view=ClinicSignUpPage().view),
        path(url="/addDoctorDetails/:clinic_id", clear=False, view=AddDoctorDetailsPage().view),
        path(url="/clinicHomepage/:user_id", clear=False, view=ClinicHomepage().view),


        # Clinic admin interface path
        path(url="/login/adminHomepage/:user_id", clear=False, view=AdminHomepage().view),
        path(url="/admin/adminPatientRequestList", clear=False, view=AdminPatientRequestList().view),
        path(url="/admin/clinicAdminUpdateAppointment/:user_id", clear=False, view=ClinicAdminUpdateAppointmentPage().view),
        path(url="/admin/clinicAdminUpdateAppointmentDetails/:user_id:booking_id", clear=False, view=ClinicAdminUpdateAppointmentDetailsPage().view),

    ]
    Routing(page=mainPage, app_routes=app_routes)
    mainPage.go(mainPage.route)


if __name__ == "__main__":
    flet.app(target=main, upload_dir="pic")