import flet
from flet import *
from flet_route import Routing,path
from welcome import WelcomePage
from login import LoginPage
from signUp import SignUpPage
from homepage import Homepage
from resetPassword import ResetPasswordPage
from doctorLogin import DoctorLoginPage
from doctorResetPassword import DoctorResetPassword
from doctorHomepage import DoctorHomepage



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
            url="/login",
            clear=True,
            view=DoctorLoginPage().view
        ),
        path(
            url="/login/resetPassword",
            clear=True,
            view=DoctorResetPassword().view
        ),
        path(
        url="/login/homepage",
        clear=True,
        view=DoctorHomepage().view
        )

    ]

    Routing(page=mainPage,app_routes=app_routes)
    mainPage.go(mainPage.route)



if __name__ == "__main__":
    flet.app(target=main)
