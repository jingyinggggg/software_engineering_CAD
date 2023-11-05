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
# from setting import SettingPage
# from password import PasswordPage
# from accountSetting import AccountSettingPage
from clinic import ClinicPage
from viewClinic import ViewClinicPage
from doctor import DoctorPage
from viewDoctor import ViewDoctorPage
# from makeAppointment import MakeAppointmentPage
# from patientPrescription import PatientPrescriptionPage
# from viewPrescription import ViewPrescriptionPage
# from healthTips import HealthTipsPage
# from bookingPage import BookingPage
# from viewBooking import ViewBookingPage
from profile import ProfilePage

# Doctor's interface
from doctorHomepage import DoctorHomepage
from notification import Notification
from history import HistoryPage
from schedule import Schedule
from appointmentDetail import AppointmentDetail
from chat import Chat
from prescription import Prescription

# Clinic's interface
from clinicSignUp import ClinicSignUpPage
from addDoctorDetails import AddDoctorDetailsPage
from clinicHomepage import ClinicHomepage

# Admin interface


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
        path(url="/medicalRecord/:user_id", clear=False, view=MedicalRecordPage().view),
        path(url="/addMedicalRecord/:user_id", clear=False, view=AddMedicalRecordPage().view),
        path(url="/viewMedicalRecord/:medicalRecord_id", clear=False, view=ViewMedicalRecordPage().view),
        # path(url="/setting/:user_id", clear=False, view=SettingPage().view),
        # path(url="/accountSetting/:user_id", clear=False, view=AccountSettingPage().view),
        # path(url="/password/:user_id", clear=False, view=PasswordPage().view),
        path(url="/clinic/:user_id", clear=False, view=ClinicPage().view),
        path(url="/viewClinic/:user_id:clinic_id", clear=False, view=ViewClinicPage().view),
        path(url="/doctor/:user_id", clear=False, view=DoctorPage().view),
        path(url="/viewDoctor/:user_id:doctor_id", clear=False, view=ViewDoctorPage().view),
        # path(url="/makeAppointment/:user_id:doctor_id", clear=False, view=MakeAppointmentPage().view),
        # path(url="/patientPrescription/:user_id", clear=False, view=PatientPrescriptionPage().view),
        # path(url="/viewPrescription/:user_id", clear=False, view=ViewPrescriptionPage().view),
        # # path(url="/viewPrescription/:prescription_id", clear=False, view=PatientPrescriptionPage().view),
        # path(url="/healthTips/:user_id", clear=False, view=HealthTipsPage().view),
        # path(url="/booking/:user_id", clear=False, view=BookingPage().view),
        # path(url="/viewBooking/:user_id:booking_id", clear=False, view=ViewBookingPage().view),
        path(url="/profile/:user_id", clear=False, view=ProfilePage().view),


        # Patient interface path
        path(url="/login/homepage/:user_id", clear=False, view=DoctorHomepage().view),
        path(url="/notification", clear=False, view=Notification().view),
        path(url="/history", clear=False, view=HistoryPage().view),
        path(url="/schedule", clear=False, view=Schedule().view),
        path(url="/appointmentDetail/:user_id", clear=False, view=AppointmentDetail().view),
        path(url="/chat", clear=False, view=Chat().view),
        path(url="/prescription", clear=False, view=Prescription().view),


        # Clinic interface path
        path(url="/clinicSignUp", clear=False, view=ClinicSignUpPage().view),
        path(url="/clinicHomepage/:user_id", clear=False, view=ClinicHomepage().view),
        path(url="/addDoctorDetails/:clinic_id", clear=False, view=AddDoctorDetailsPage().view),


        # Admin interface path
    ]
    Routing(page=mainPage, app_routes=app_routes)
    mainPage.go(mainPage.route)


if __name__ == "__main__":
    flet.app(target=main, upload_dir="pic")