import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


def CreateTable():
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 fullName TEXT NOT NULL,
                 username TEXT NOT NULL,
                 email TEXT NOT NULL,
                 phoneNumber TEXT NOT NULL,
                 password TEXT NOT NULL,
                 userType TEXT NOT NULL)""")
    db.commit()


def ReadTable():
    c = db.cursor()
    c.execute('SELECT id,fullName,username,email,phoneNumber,password,userType FROM users ORDER BY id ASC')
    record = c.fetchall()
    return record


def DeleteTable():
    c = db.cursor()
    c.execute('DELETE FROM users ')
    db.commit()


class Homepage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
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

        # alert_dialog = AlertDialog(
        #     modal=True,
        #     title=Text("Successful!", text_align=TextAlign.CENTER),
        #     content=Text("You have created your account successfully. Log in to your account to enjoy our service now!",
        #                  text_align=TextAlign.CENTER),
        #     actions=[TextButton("Done", on_click=lambda _: page.go(f"/"))],
        #     actions_alignment=MainAxisAlignment.CENTER
        # )

        paddingBottom = Container(padding=padding.only(bottom=5))

        fullName = TextField(
            label="Enter Full Name",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=14),
            height=50)

        username = TextField(
            label="Enter Username",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=14),
            height=50)

        email = TextField(
            label="Enter Email",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=14),
            height=50)

        phoneNumber = TextField(
            label="Enter Phone Number",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=14),
            height=50)

        password = TextField(
            label="Enter Password",
            password=True,
            can_reveal_password=True,
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=14),
            height=50)

        userType = "patient"

        def open_dlg():
            page.dialog = alert_dialog
            alert_dialog.open = True
            page.update()

        def addToDatabase(e):
            # DeleteTable()
            # ConnectToTable()
            # print(ReadTable())
            try:
                if fullName.value != "" and username.value != "" and email.value != "" and phoneNumber.value != "" and password.value != "":
                    c = db.cursor()
                    c.execute('INSERT INTO users (fullName, username, email, phoneNumber, password, userType) '
                              'VALUES (?, ?, ?, ?, ?, ?)',
                              (fullName.value, username.value, email.value, phoneNumber.value, password.value, userType))
                    db.commit()
                    page.update()
                    open_dlg()
                    print("success")
                    print(ReadTable())
            except Exception as e:
                print(e)

        return View(
            "/homepage",
            controls=[
                Container(padding=padding.only(left=20, right=20, top=20),
                          width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          border=border.all(1, "black"),
                          alignment=alignment.center,
                          # child control
                          content=Column(
                              horizontal_alignment="center",
                              controls=[


                              ]
                          )
                          )
            ]
        )
