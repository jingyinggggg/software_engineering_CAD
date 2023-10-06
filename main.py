import flet
from flet import *
from flet_route import Routing,path
from welcome import WelcomePage
from login import LoginPage
import sqlite3


def main(mainPage: Page):

    mainPage.theme_mode = "light"
    app_routes = [
        path(
            url="/",
            clear=True,
            view=WelcomePage().view
        ),
        path(
            url="/login",
            clear=True,
            view=LoginPage().view
        )

    ]

    Routing(page=mainPage,app_routes=app_routes)
    mainPage.go(mainPage.route)



if __name__ == "__main__":
    flet.app(target=main)
