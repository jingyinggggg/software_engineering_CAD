import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class LoginPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"
        # page.theme_mode = "light"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        email = TextField(label="Enter Email",
                          label_style=TextStyle(font_family="RobotoSlab",
                                                size=14,
                                                color=colors.GREY_800),
                          height=50,
                          border_color=colors.BLACK,
                          text_style=TextStyle(size=14,
                                               color=colors.BLACK))

        password = TextField(label="Enter Password",
                             password=True,
                             can_reveal_password=True,
                             label_style=TextStyle(font_family="RobotoSlab",
                                                   size=14,
                                                   color=colors.GREY_800),
                             height=50,
                             border_color=colors.BLACK,
                             text_style=TextStyle(size=14,
                                                  color=colors.BLACK))

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Failed!", text_align=TextAlign.CENTER),
            content=Text("Login failed! Please make sure that the email and password that you entered is correct...",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Try Again", on_click=lambda _: close_dlg())],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_dlg():
            page.dialog = alert_dialog
            alert_dialog.open = True
            page.update()

        def close_dlg():
            page.dialog = alert_dialog
            alert_dialog.open = False
            page.update()

        def verifyUser(e):
            c = db.cursor()
            c.execute("SELECT id FROM users WHERE email = ? AND password = ?", (email.value, password.value))
            user = c.fetchone()

            if user:
                page.go(f"/homepage/{user[0]}")

            elif email.value == "" or password.value == "":
                open_dlg()

            else:
                c.execute("SELECT id FROM doctors WHERE email = ? AND password = ?", (email.value, password.value))
                doctor = c.fetchone()

                if doctor is not None:
                    page.go(f"/login/homepage")
                else:
                    c.execute("SELECT id FROM admin WHERE email = ? AND password = ?", (email.value, password.value))
                    admin = c.fetchone()

                    if admin is not None:
                        page.go(f"/")
                    else:
                        open_dlg()

        return View(
            "/loginUser",
            controls=[
                Container(padding=padding.symmetric(horizontal=20, vertical=20),
                          width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # border=border.all(1, "black"),
                          alignment=alignment.center,
                          # child control
                          content=Column(
                              horizontal_alignment="center",
                              controls=[
                                  Container(Image(src="pic/back.png",
                                                  width=20,
                                                  height=20),
                                            alignment=alignment.top_left,
                                            on_click=lambda _: page.go(f"/")),

                                  Container(padding=padding.only(top=70),
                                            content=Image(src="pic/logo.png",
                                                          width=150,
                                                          height=150)),

                                  Container(padding=padding.only(bottom=30),
                                            content=Text("Call A Doctor",
                                                         size=24,
                                                         font_family="RobotoSlab",
                                                         color="#3386C5",
                                                         text_align=TextAlign.CENTER)),

                                  email,

                                  password,

                                  Container(padding=padding.only(top=30),
                                            content=IconButton(content=Text("Login",
                                                                            size=16,
                                                                            font_family="RobotoSlab",
                                                                            color="WHITE",
                                                                            text_align=TextAlign.CENTER),
                                                               width=300,
                                                               height=45,
                                                               style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                                 shape={"": RoundedRectangleBorder(
                                                                                     radius=7)}
                                                                                 ),
                                                               on_click=verifyUser,
                                                               )),

                                  TextButton(content=Text("forget password?",
                                                          size=14,
                                                          italic=True,
                                                          font_family="RobotoSlab",
                                                          color=colors.BLACK,
                                                          text_align=TextAlign.CENTER),
                                             on_click=lambda _: page.go("/resetPassword")
                                             ),

                                  Container(padding=padding.only(top=40),
                                            content=Column(
                                                horizontal_alignment="center",
                                                controls=[

                                                    Container(
                                                        padding=padding.only(bottom=-10),
                                                        content=Text("Don't have an account?",
                                                                     weight=FontWeight.W_500,
                                                                     font_family="RobotoSlab",
                                                                     color="#3386C5",
                                                                     text_align=TextAlign.CENTER)
                                                    ),

                                                    Row(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        controls=[

                                                            TextButton(
                                                                content=Text("Sign up for user",
                                                                             weight=FontWeight.W_500,
                                                                             font_family="RobotoSlab",
                                                                             color=colors.BLACK,
                                                                             italic=True,
                                                                             size=13,
                                                                             text_align=TextAlign.CENTER),
                                                                on_click=lambda _: page.go("/signUp")
                                                            ),

                                                            TextButton(
                                                                content=Text("Sign up for clinic",
                                                                             weight=FontWeight.W_500,
                                                                             font_family="RobotoSlab",
                                                                             color=colors.BLACK,
                                                                             italic=True,
                                                                             size=13,
                                                                             text_align=TextAlign.CENTER),
                                                                # on_click=lambda _: page.go("/clinicSignUp")
                                                            )
                                                        ]
                                                    )
                                                ]
                                            ))

                                  # Container(padding=padding.only(top=50),
                                  #           content=
                                  #               ]
                                  #           )
                                  #           )
                              ]
                          )
                          )
            ]
        )
