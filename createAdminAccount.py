import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


def CreateTable():
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS clinicAdmin(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 fullName TEXT NOT NULL,
                 username INTEGER NOT NULL,
                 email TEXT NOT NULL,
                 password TEXT NOT NULL,
                 clinicID TEXT NOT NULL)""")
    db.commit()


class CreateAdminAccount:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        clinic_id = int(params.clinic_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        def get_clinic_details():
            c = db.cursor()
            c.execute("SELECT id,name FROM clinic WHERE id = ?", (clinic_id,))
            record = c.fetchall()

            clinic_name = record[0][1]

            return clinic_id, clinic_name

        clinic_id, clinicName = get_clinic_details()

        fullnameTextField = TextField(
            width=320,
            label="Fullname",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: Jovin Pang",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        usernameTextField = TextField(
            width=320,
            label="Username",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: jovin",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        emailTextField = TextField(
            width=320,
            label="Email",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: jovin@gmail.com",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        passwordTextField = TextField(
            width=320,
            label="Password",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: 123",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have created an admin account!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Ok", on_click=lambda _: page.go(f"/clinicHomepage/{clinic_id}"))],
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

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Fail", text_align=TextAlign.CENTER),
            content=Text("Please fill in all the field!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Try Again", on_click=lambda _: close_error_dlg())],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_error_dlg():
            page.dialog = error_dialog
            error_dialog.open = True
            page.update()

        def close_error_dlg():
            page.dialog = error_dialog
            error_dialog.open = False
            page.update()

        def addToDatabase(e):
            CreateTable()
            if (fullnameTextField.value != "" and usernameTextField.value != "" and emailTextField.value != "" and
                    passwordTextField.value != ""):
                c = db.cursor()
                c.execute('INSERT INTO clinicAdmin (fullName, username, email, password, clinicID)'
                          'VALUES (?, ?, ?, ?, ?)',
                          (fullnameTextField.value, usernameTextField.value, emailTextField.value,
                           passwordTextField.value, clinic_id))
                db.commit()
                page.update()
                open_dlg()
                print("success")
            else:
                open_error_dlg()

        return View(
            "/createAdminAccount/:clinic_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Column(
                        # alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        padding=padding.only(right=120),
                                        width=350,
                                        height=80,
                                        bgcolor="#3386C5",
                                        content=Row(controls=[
                                            Container(padding=padding.only(left=10, top=5),
                                                      content=Image(
                                                          src="pic/back.png",
                                                          color=colors.WHITE,
                                                          width=20,
                                                          height=20
                                                      ),
                                                      on_click=lambda _: page.go(f"/clinicHomepage/{clinic_id}")),
                                            Container(padding=padding.only(left=75),
                                                      content=Text("Create Account",
                                                                   color="WHITE",
                                                                   text_align=TextAlign.CENTER,
                                                                   size=20,
                                                                   font_family="RobotoSlab"
                                                                   ))
                                        ])

                                    )
                                ]),

                            Container(padding=padding.only(left=10),
                                      content=fullnameTextField),
                            Container(padding=padding.only(left=10),
                                      content=usernameTextField),
                            Container(padding=padding.only(left=10),
                                      content=emailTextField),
                            Container(padding=padding.only(left=10),
                                      content=passwordTextField),

                            Container(padding=padding.only(left=10, top=10),
                                      content=TextButton(content=Text("Create",
                                                                      size=16,
                                                                      font_family="RobotoSlab",
                                                                      color="WHITE",
                                                                      text_align=TextAlign.CENTER),
                                                         width=320,
                                                         height=45,
                                                         style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                           shape={
                                                                               "": RoundedRectangleBorder(
                                                                                   radius=7)}
                                                                           ),
                                                         on_click=addToDatabase

                                                         ),

                                      ),
                        ])
                )
            ])
