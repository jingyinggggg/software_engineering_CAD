import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class DoctorProfilePage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
        user_id = int(params.user_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 800
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        def get_user_details():
            c = db.cursor()
            c.execute("SELECT * FROM doctors WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]
            username = record[0][2]
            email = record[0][3]
            phoneNumber = record[0][4]
            password = record[0][5]
            experience = record[0][6]
            specialization = record[0][7]
            description = record[0][8]
            clinic = record[0][9]
            workingTime = record[0][10]
            workingDate = record[0][11]

            # return fullName, username, email, phoneNumber, password
            return fullName, username, email, phoneNumber, password, experience, specialization, description, clinic, workingTime, workingDate

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        fullName, username, email, phoneNumber, password, experience, specialization, description, clinic, workingTime, workingDate = get_user_details()

        fullNameTextField = TextField(
            label="Full Name",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            read_only=True,
            border_color=grey,
            # value=fullName,
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(fullNameTextField,fullName)

        emailTextField = TextField(
            label="Email",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            read_only=True,
            border_color=grey,
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(emailTextField,email)

        phoneNumberTextField = TextField(
            label="Phone Number",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            read_only=True,
            border_color=grey,
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(phoneNumberTextField,phoneNumber)

        experienceTextField = TextField(
            label="Experience",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            read_only=True,
            border_color=grey,
            hint_text="Example: 8 Years",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(experienceTextField, experience)

        specializationTextField = TextField(
            label="Specialization",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            read_only=True,
            border_color=grey,
            hint_text="Example: Emergency",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(specializationTextField, specialization)

        descriptionTextField = TextField(
            label="Description",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            # height=40,
            read_only=True,
            multiline=True,
            border_color=grey,
            hint_text="Example: Treat...",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600
                                 ),
            dense=True
        )

        setTextFieldValue(descriptionTextField, description)

        clinicTextField = TextField(
            label="Clinic",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            read_only=True,
            border_color=grey,
            hint_text="*** Clinic xxx ***",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(clinicTextField, clinic)

        return View(
            "/doctorProfile/:user_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              scroll=True,
                              horizontal_alignment="center",
                              controls=[
                                  Container(width=350,
                                            height=70,
                                            bgcolor=blue,
                                            alignment=alignment.top_center,
                                            content=Row(
                                                controls=[
                                                    Container(padding=padding.only(left=20, top=25),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ),
                                                              on_click=lambda _: page.go(f"/login/homepage/{user_id}")
                                                              ),

                                                    Container(padding=padding.only(left=100, top=25),
                                                              content=Text(
                                                                  value="Profile",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),
                                                ]
                                            )
                                            ),

                                  Container(
                                      padding=padding.only(top=10),
                                      content=Column(
                                          horizontal_alignment="center",
                                          controls=[
                                              Image(
                                                  src="pic/avatar.png",
                                                  width=75,
                                                  height=75
                                              ),

                                              Text(
                                                  value=username,
                                                  size=14,
                                                  text_align=TextAlign.CENTER,
                                                  color=colors.BLACK,
                                                  font_family="RobotoSlab",
                                                  weight=FontWeight.W_500
                                              )
                                          ]
                                      )
                                  ),

                                  Container(
                                      padding=padding.only(left=20, right=20, top=10),
                                      alignment=alignment.center_left,
                                      content=Column(
                                          controls=[
                                              Text(
                                                  value="Personal Information",
                                                  size=12,
                                                  color=colors.BLACK,
                                                  weight=FontWeight.W_600,
                                                  font_family="RobotoSlab",
                                                  text_align=TextAlign.LEFT
                                              ),

                                              fullNameTextField,

                                              emailTextField,

                                              phoneNumberTextField,

                                              experienceTextField,

                                              specializationTextField,

                                              descriptionTextField,

                                              clinicTextField,

                                          ]

                                      )
                                  )

                              ]
                          )
                          )
            ]
        )
