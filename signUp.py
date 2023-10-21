import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)
c = db.cursor()


# def CreateTable():
#     c = db.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS admin(
#                  id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  fullName TEXT NOT NULL,
#                  username TEXT NOT NULL,
#                  email TEXT NOT NULL,
#                  phoneNumber TEXT NOT NULL,
#                  password TEXT NOT NULL)""")
#     db.commit()

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


#
# def UpdateTable():
#     c = db.cursor()
#     c.execute("""ALTER TABLE users
#                  ADD dob TEXT,
#                  ADD gender TEXT,
#                  ADD address TEXT,
#                  ADD emergencyContact TEXT
#                  """)
#     db.commit()
#

def ReadTable():
    c = db.cursor()
    c.execute('SELECT * FROM users ORDER BY id ASC')
    # c.execute('SELECT id,fullName,username,email,phoneNumber,password,userType FROM users ORDER BY id ASC')
    record = c.fetchall()
    return record


# def DeleteTable():
#     c = db.cursor()
#     c.execute('DELETE FROM users ')
#     db.commit()
#
#
# def DropTable():
#     c = db.cursor()
#     c.execute('DROP TABLE users')
#     db.commit()


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

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Successful!", text_align=TextAlign.CENTER),
            content=Text("You have created your account successfully. Log in to your account to enjoy our service now!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/"))],
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

        def open_dlg():
            page.dialog = alert_dialog
            alert_dialog.open = True
            page.update()

        def addToDatabase(e):
            # DropTable()
            # DeleteTable()
            CreateTable()
            # print(ReadTable())
            try:
                if fullName.value != "" and username.value != "" and email.value != "" and phoneNumber.value != "" and password.value != "":
                    c = db.cursor()
                    c.execute('INSERT INTO users (fullName, username, email, phoneNumber, password) '
                              'VALUES (?, ?, ?, ?, ?)',
                              (
                                  fullName.value, username.value, email.value, phoneNumber.value, password.value))
                    db.commit()
                    page.update()
                    open_dlg()
                    print("success")
                    print(ReadTable())
            except Exception as e:
                print(e)


            # try:
            #     if fullName.value != "" and username.value != "" and email.value != "" and phoneNumber.value != "" and password.value != "":
            #         c = db.cursor()
            #         c.execute('INSERT INTO admin (fullName, username, email, phoneNumber, password) '
            #                   'VALUES (?, ?, ?, ?, ?)',
            #                   (
            #                       fullName.value, username.value, email.value, phoneNumber.value, password.value))
            #         db.commit()
            #         page.update()
            #         open_dlg()
            #         print("success")
            #         print(ReadTable())
            # except Exception as e:
            #     print(e)

            # try:
            #     if fullName.value != "" and username.value != "" and email.value != "" and phoneNumber.value != "" and password.value != "":
            #         c = db.cursor()
            #         c.execute('INSERT INTO doctors (fullName, username, email, phoneNumber, password) '
            #                   'VALUES (?, ?, ?, ?, ?)',
            #                   (
            #                       fullName.value, username.value, email.value, phoneNumber.value, password.value))
            #         db.commit()
            #         page.update()
            #         open_dlg()
            #         print("success")
            #         print(ReadTable())
            # except Exception as e:
            #     print(e)


        return View(
            "/signUp",
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
