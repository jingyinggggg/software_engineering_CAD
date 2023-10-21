import flet
from flet import *
from flet_route import Routing, path

from login import LoginPage
from signUp import SignUpPage
from homepage import Homepage
from resetPassword import ResetPasswordPage
from welcome import WelcomePage
from doctorHomepage import DoctorHomepage
from profile import ProfilePage
from medicalRecord import MedicalRecordPage
from addMedicalRecord import AddMedicalRecordPage
from viewMedicalRecord import ViewMedicalRecordPage
from clinic import ClinicPage
from viewClinic import ViewClinicPage
from clinicSignUp import ClinicSignUpPage
from notification import Notification
from history import HistoryPage
from schedule import Schedule
from appointmentDetail import AppointmentDetail
from chat import Chat
from prescription import Prescription
from addDoctorDetails import AddDoctorDetailsPage
from doctor import DoctorPage
from viewDoctor import ViewDoctorPage
from healthTips import HealthTipsPage


def main(mainPage: Page):
    mainPage.theme_mode = "light"
    app_routes = [
        path(url="/", clear=True, view=WelcomePage().view),
        path(url="/loginUser", clear=False, view=LoginPage().view),
        path(url="/signUp", clear=False, view=SignUpPage().view),
        path(url="/homepage/:user_id", clear=False, view=Homepage().view),
        path(url="/resetPassword", clear=False, view=ResetPasswordPage().view),
        path(url="/profile/:user_id", clear=False, view=ProfilePage().view),
        path(url="/medicalRecord/:user_id", clear=False, view=MedicalRecordPage().view),
        path(url="/addMedicalRecord/:user_id", clear=False, view=AddMedicalRecordPage().view),
        path(url="/viewMedicalRecord/:medicalRecord_id", clear=False, view=ViewMedicalRecordPage().view),
        path(url="/clinic/:user_id", clear=False, view=ClinicPage().view),
        path(url="/viewClinic/:user_id:clinic_id", clear=False, view=ViewClinicPage().view),
        path(url="/doctor/:user_id", clear=False, view=DoctorPage().view),
        path(url="/viewDoctor/:user_id:doctor_id", clear=False, view=ViewDoctorPage().view),
        path(url="/healthTips/:user_id", clear=False, view=HealthTipsPage().view),
        path(url="/login/homepage", clear=False, view=DoctorHomepage().view),
        path(url="/clinicSignUp", clear=False, view=ClinicSignUpPage().view),
        path(url="/notification",clear=False,view=Notification().view),
        path(url="/history",clear=False,view=HistoryPage().view),
        path(url="/schedule",clear=False,view=Schedule().view),
        path(url="/appointmentDetail",clear=False,view=AppointmentDetail().view),
        path(url="/chat",clear=False,view=Chat().view),
        path(url="/prescription",clear=False,view=Prescription().view),
        path(url="/addDoctorDetails", clear=False, view=AddDoctorDetailsPage().view),
    ]

    Routing(page=mainPage, app_routes=app_routes)
    mainPage.go(mainPage.route)


if __name__ == "__main__":
    flet.app(target=main, upload_dir="pic")