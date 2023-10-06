import flet
from flet import *
import sqlite3


def main(welcome_page: Page):
    welcome_page.title = "Call A Doctor"
    welcome_page.window_width=420
    welcome_page.window_height=900
    welcome_page.horizontal_alignment = "center"
    welcome_page.vertical_alignment = "center"
    welcome_page.theme_mode = "light"

    welcome_page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    phone: Container = Container(padding=padding.symmetric(horizontal=20, vertical=100),
                                 width=350,
                                 height=700,
                                 bgcolor="#D0DCEE",
                                 border_radius=30,
                                 border=border.all(1, "black"),
                                 alignment=alignment.center,
                                 # child control
                                 content=Column(
                                     horizontal_alignment="center",
                                     controls=[
                                         Text("Welcome",
                                              size=24,
                                              font_family="RobotoSlab",
                                              text_align=TextAlign.CENTER),

                                         Text("Call A Doctor",
                                              size=24,
                                              font_family="RobotoSlab",
                                              color="#3386C5",
                                              text_align=TextAlign.CENTER),

                                         Container(padding=padding.symmetric(vertical=50),
                                                   content=Image(src="pic/welcomePageImage.png",
                                                                 width=250,
                                                                 height=250)),

                                         IconButton(content=Text("Login",
                                                                 size=16,
                                                                 font_family="RobotoSlab",
                                                                 color="WHITE",
                                                                 text_align=TextAlign.CENTER),
                                                    width=300,
                                                    height=45,
                                                    style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                      shape={"": RoundedRectangleBorder(radius=7)}
                                                                      ),
                                                    ),

                                         IconButton(content=Text("Sign Up",
                                                                 size=16,
                                                                 font_family="RobotoSlab",
                                                                 color="#3386C5",
                                                                 text_align=TextAlign.CENTER),
                                                    width=300,
                                                    height=45,
                                                    style=ButtonStyle(bgcolor={"": "WHITE"},
                                                                      shape={"": RoundedRectangleBorder(radius=7)}
                                                                      ),
                                                    )
                                     ]
                                 )
                                 )

    welcome_page.add(
        phone
    )
    pass


if __name__ == "__main__":
    flet.app(target=main)
