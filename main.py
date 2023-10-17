import flet
from flet import *
from flet_route import Routing, path
from login import LoginPage
from signUp import SignUpPage
from homepage import Homepage
from resetPassword import ResetPasswordPage
from welcome import WelcomePage
from doctorHomepage import DoctorHomepage
from notification import Notification
from history import HistoryPage
from schedule import Schedule
from appointmentDetail import AppointmentDetail
from chat import Chat
from prescription import Prescription


def main(mainPage: Page):
    mainPage.theme_mode = "light"
    app_routes = [
        path(
            url="/",
            clear=True,
            view=WelcomePage().view
        ),
        path(
            url="/loginUser",
            clear=True,
            view=LoginPage().view
        ),
        path(
            url="/signUp",
            clear=True,
            view=SignUpPage().view
        ),
        path(
            url="/homepage",
            clear=True,
            view=Homepage().view
        ),
        path(
            url="/resetPassword",
            clear=True,
            view=ResetPasswordPage().view
        ),
        path(
            url="/login/homepage",
            clear=True,
            view=DoctorHomepage().view
        ),
        # path(
        #     url="/sidebar",
        #     clear=True,
        #     view=DoctorHomepage().view
        # ),
        path(
            url="/notification",
            clear=True,
            view=Notification().view
        ),
        path(
            url="/history",
            clear=True,
            view=HistoryPage().view
        ),
        path(
            url="/schedule",
            clear=True,
            view=Schedule().view
        ),
        path(
            url="/appointmentDetail",
            clear=True,
            view=AppointmentDetail().view
        ),
        path(
            url="/chat",
            clear=True,
            view=Chat().view
        ),
        path(
            url="/prescription",
            clear=True,
            view=Prescription().view
        ),
    ]

    Routing(page=mainPage, app_routes=app_routes)
    mainPage.go(mainPage.route)


if __name__ == "__main__":
    flet.app(target=main)
