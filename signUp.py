import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)
c = db.cursor()

def CreateTable():
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 fullName TEXT NOT NULL,
                 username TEXT NOT NULL,
                 email TEXT NOT NULL,
                 phoneNumber TEXT NOT NULL,
                 password TEXT NOT NULL,
                 dob TEXT,
                 gender TEXT,
                 address TEXT,
                 emergencyContact TEXT)""")
    db.commit()

class SignUpPage:
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

        def get_exist_user():
            c = db.cursor()
            c.execute("SELECT email FROM users")
            record = c.fetchall()

            return record

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Successful", text_align=TextAlign.CENTER),
            content=Text("You have created your account successfully. Log in to your account to enjoy our service now!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/"))],
            actions_alignment=MainAxisAlignment.CENTER
        )

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Failed", text_align=TextAlign.CENTER),
            content=Text("Something went wrong! Please try again...",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Try Again", on_click=lambda _: close_dlg(error_dialog))],
            actions_alignment=MainAxisAlignment.CENTER
        )

        exist_dialog = AlertDialog(
            modal=True,
            title=Text("Failed", text_align=TextAlign.CENTER),
            content=Text("The email has been registered!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Try Again", on_click=lambda _: close_dlg(exist_dialog))],
            actions_alignment=MainAxisAlignment.CENTER
        )

        paddingBottom = Container(padding=padding.only(bottom=5))

        fullName = TextField(
            label="Enter Full Name",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=14,
                                  color=colors.GREY_800),
            height=50,
            border_color=colors.BLACK,
            text_style=TextStyle(size=14,
                                 color=colors.BLACK))

        username = TextField(
            label="Enter Username",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=14,
                                  color=colors.GREY_800),
            height=50,
            border_color=colors.BLACK,
            text_style=TextStyle(size=14,
                                 color=colors.BLACK))

        email = TextField(
            label="Enter Email",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=14,
                                  color=colors.GREY_800),
            height=50,
            border_color=colors.BLACK,
            text_style=TextStyle(size=14,
                                 color=colors.BLACK))

        phoneNumber = TextField(
            label="Enter Phone Number",
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

        def open_dlg(dialog):
            page.dialog = dialog
            dialog.open = True
            page.update()

        def close_dlg(dialog):
            page.dialog = dialog
            dialog.open = False
            page.update()

        def addToDatabase(e):
            CreateTable()
            try:
                if fullName.value != "" and username.value != "" and email.value != "" and phoneNumber.value != "" and password.value != "":
                    c = db.cursor()

                    existing_user = get_exist_user()
                    existing = False

                    for exist in existing_user:
                        if email.value == exist[0]:
                            existing = True
                            break
                        else:
                            existing = False
                            continue

                    if not existing:
                        c.execute('INSERT INTO users (fullName, username, email, phoneNumber, password) '
                                  'VALUES (?, ?, ?, ?, ?)',
                                  (
                                      fullName.value, username.value, email.value, phoneNumber.value, password.value))
                        db.commit()
                        page.update()
                        open_dlg(alert_dialog)
                    else:
                        open_dlg(exist_dialog)
                else:
                    open_dlg(error_dialog)
            except Exception as e:
                print(e)

        return View(
            "/signUp",
            controls=[
                Container(padding=padding.only(left=20, right=20, top=20),
                          width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
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

                                  Container(padding=padding.only(top=20, bottom=20),
                                            content=Row(
                                                alignment=MainAxisAlignment.START,
                                                controls=[
                                                    Image(src="pic/logo.png",
                                                          width=80,
                                                          height=80),

                                                    Text(value="Create an account",
                                                         size=18,
                                                         color="#3386C5",
                                                         font_family="RobotoSlab",
                                                         weight=FontWeight.W_500)
                                                ]
                                            )

                                            ),

                                  fullName,
                                  paddingBottom,

                                  username,
                                  paddingBottom,

                                  email,
                                  paddingBottom,

                                  phoneNumber,
                                  paddingBottom,

                                  password,
                                  paddingBottom,

                                  Container(padding=padding.only(top=30),
                                            content=IconButton(content=Text("Sign Up",
                                                                            size=16,
                                                                            font_family="RobotoSlab",
                                                                            color="WHITE",
                                                                            text_align=TextAlign.CENTER),
                                                               width=300,
                                                               height=50,
                                                               style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                                 shape={"": RoundedRectangleBorder(
                                                                                     radius=7)}
                                                                                 ),
                                                               on_click=addToDatabase)
                                            )

                              ]
                          )
                          )
            ]
        )
