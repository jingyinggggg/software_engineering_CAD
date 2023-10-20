import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ResetPasswordPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        # page.theme_mode = "light"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        paddingBottom = Container(padding=padding.only(bottom=5))

        email = TextField(
            label="Enter Email",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=14,
                                  color=colors.GREY_800),
            height=50,
            border_color=colors.BLACK,
            text_style=TextStyle(size=14,
                                 color=colors.BLACK))
        password = TextField(
            label="Enter Password",
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
            title=Text("Successful!", text_align=TextAlign.CENTER),
            content=Text("You have updated your password successfully!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/loginUser"))],
            actions_alignment=MainAxisAlignment.CENTER
        )

        def open_dlg():
            page.dialog = alert_dialog
            alert_dialog.open = True
            page.update()

        def UpdateTable(e):
            try:
                c = db.cursor()
                c.execute('UPDATE users SET password = ? WHERE email = ?', (password.value, email.value))
                db.commit()
                page.update()
                open_dlg()
            except Exception as e:
                print(e)

        return View(
            "/resetPassword",
            controls=[
                Container(padding=padding.only(left=20, right=20, top=20),
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
                                            on_click=lambda _: page.go(f"/loginUser")),

                                  Container(padding=padding.only(top=120, bottom=20),
                                            content=Row(
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[
                                                    Image(src="pic/logo.png",
                                                          width=80,
                                                          height=80),

                                                    Text(value="Reset Password",
                                                         size=18,
                                                         color="#3386C5",
                                                         font_family="RobotoSlab",
                                                         weight=FontWeight.W_500)
                                                ]
                                            )

                                            ),

                                  email,
                                  paddingBottom,

                                  password,
                                  paddingBottom,

                                  Container(padding=padding.only(top=30),
                                            content=IconButton(content=Text("Update Password",
                                                                            size=16,
                                                                            font_family="RobotoSlab",
                                                                            color="WHITE",
                                                                            text_align=TextAlign.CENTER),
                                                               width=300,
                                                               height=50,
                                                               style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                                 shape={"": RoundedRectangleBorder(
                                                                                     radius=7)}),
                                                               on_click=UpdateTable)
                                            )

                              ]
                          )
                          )
            ]
        )

