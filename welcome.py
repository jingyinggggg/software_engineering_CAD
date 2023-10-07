import flet
from flet import *
from flet_route import Params, Basket


class WelcomePage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 1000
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        page.theme_mode = "light"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        return View(
            "/",
            controls=[
                Container(padding=padding.only(top=100),
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

                                  Container(padding=padding.only(top=50,bottom=30),
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
                                             on_click=lambda _: page.go(f"/login")
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
                                             on_click=lambda _: page.go(f"/signUp")
                                             ),
                              ]
                          )
                          )
            ]
        )
