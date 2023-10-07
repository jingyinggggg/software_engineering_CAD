import flet
from flet import *
from flet_route import Params,Basket

class LoginPage:
    def __int__(self):
        pass

    def view(self,page:Page, params:Params, basket:Basket):
        # print(params)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "light"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        return View(
            "/login",
            controls=[
                Container(padding=padding.symmetric(horizontal=20, vertical=20),
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
                                  Container(Image(src="pic/back.png",
                                                  width=20,
                                                  height=20),
                                            alignment=alignment.top_left,
                                            on_click=lambda _:page.go(f"/")),

                                  Container(padding=padding.only(top=70, bottom=30),
                                            content=Image(src="pic/logo.png",
                                                          width=150,
                                                          height=150)),

                                  TextField(label="Enter Username",
                                            label_style=TextStyle(font_family="RobotoSlab",
                                                                  size=14),
                                            height=50),

                                  TextField(label="Enter Password",
                                            password=True,
                                            can_reveal_password=True,
                                            label_style=TextStyle(font_family="RobotoSlab",
                                                                  size=14),
                                            height=50),

                                  Container(padding=padding.only(top=30),
                                            content=IconButton(content=Text("Login",
                                                               size=16,
                                                               font_family="RobotoSlab",
                                                               color="WHITE",
                                                               text_align=TextAlign.CENTER),
                                                               width=300,
                                                               height=45,
                                                               style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                                 shape={"": RoundedRectangleBorder(radius=7)}
                                                                                 ),
                                                               on_click=lambda _: page.go(f"/homepage")
                                                               )),
                                  Text(
                                      spans=[
                                          TextSpan(
                                              "forget password",
                                              TextStyle(decoration=TextDecoration.UNDERLINE,
                                                        decoration_thickness=1.5,
                                                        decoration_style=TextDecorationStyle.SOLID,
                                                        size=14,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500),

                                          )
                                      ]
                                  ),

                                  Container(padding=padding.only(top=120),
                                            content=Row(
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Text("Don't have an account?",
                                                         weight=FontWeight.W_500,
                                                         font_family="RobotoSlab",
                                                         color="#3386C5",
                                                         text_align=TextAlign.CENTER),

                                                    TextButton(
                                                        content=Text("Sign Up",
                                                                     weight=FontWeight.W_500,
                                                                     font_family="RobotoSlab",
                                                                     color=colors.BLACK,
                                                                     text_align=TextAlign.CENTER),
                                                        on_click=lambda _:page.go("/signUp")
                                                    )
                                                ]
                                            )
                                  )

                              ]
                          )
                )
            ]
        )