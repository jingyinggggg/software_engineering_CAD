from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class AccountSettingPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        blue = "#3386C5"
        grey = "#71839B"
        lightBlue = "#D0DCEE"

        def get_user_details():
            c = db.cursor()
            c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]
            username = record[0][2]
            email = record[0][3]
            phoneNumber = record[0][4]
            password = record[0][5]
            dob = record[0][6]
            gender = record[0][7]
            address = record[0][8]
            emergencyContact = record[0][9]

            # return fullName, username, email, phoneNumber, password
            return fullName, username, email, phoneNumber, password, dob, gender, address, emergencyContact

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        fullName, username, email, phoneNumber, password, dob, gender, address, emergencyContact = get_user_details()

        container_padding = Container(margin=margin.only(top=3))

        fullNameTextField = TextField(
            label="Full Name",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
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
            border_color=blue,
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
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(phoneNumberTextField,phoneNumber)

        dobTextField = TextField(
            label="Date Of Birth",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: 26 October 2003",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(dobTextField, dob)

        genderTextField = TextField(
            label="Gender",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: Female",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(genderTextField, gender)

        addressTextField = TextField(
            label="Address",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: Golden Triangle",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(addressTextField, address)

        emergencyContactTextField = TextField(
            label="Emergency Contact",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="*** Please enter your family's contact ***",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(emergencyContactTextField, emergencyContact)

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have updated your personal information successfully!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg())],
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

        def updateProfile(e):
            c = db.cursor()
            if fullNameTextField.value != "" and emailTextField.value != "" and phoneNumberTextField.value != "" and dobTextField.value != "" and genderTextField.value != "" and addressTextField.value != "" and emergencyContactTextField != "":
                c.execute(
                    f"UPDATE users SET dob = ?, gender = ?, address = ?, emergencyContact = ? WHERE id = {user_id}",
                    (
                    dobTextField.value, genderTextField.value, addressTextField.value, emergencyContactTextField.value))
                open_dlg()
                db.commit()
                fullName, username, email, phoneNumber, password, dob, gender, address, emergencyContact = get_user_details()
                setTextFieldValue(fullNameTextField, fullName)
                setTextFieldValue(emailTextField, email)
                setTextFieldValue(phoneNumberTextField,phoneNumber)
                setTextFieldValue(dobTextField, dob)
                setTextFieldValue(genderTextField, gender)
                setTextFieldValue(addressTextField, address)
                setTextFieldValue(emergencyContactTextField, emergencyContact)

        password_container = Container(
            padding=padding.only(left=10, right=10),
            content=Column(
                horizontal_alignment="center",
                controls=[
                    Container(
                        margin=margin.only(top=10,bottom=10),
                        content=Text(
                            value="Manage your account. You may edit or update your personal details here.",
                            size=12,
                            color=grey,
                            font_family="RobotoSlab",
                            text_align=TextAlign.JUSTIFY
                        )
                    ),

                    fullNameTextField,
                    container_padding,

                    emailTextField,
                    container_padding,

                    phoneNumberTextField,
                    container_padding,

                    dobTextField,
                    container_padding,

                    genderTextField,
                    container_padding,

                    addressTextField,
                    container_padding,

                    emergencyContactTextField,

                    Container(
                        padding=padding.only(top=20),
                        content=TextButton(content=Text("Update",
                                                        size=16,
                                                        font_family="RobotoSlab",
                                                        color="WHITE",
                                                        text_align=TextAlign.CENTER),
                                           width=323,
                                           height=45,
                                           style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                             shape={
                                                                 "": RoundedRectangleBorder(
                                                                     radius=7)}
                                                             ),
                                           on_click=updateProfile
                                           ),
                    )
                ]
            )
        )

        return View(
            "/accountSetting/:user_id",
            controls=[Container(
                width=350,
                height=700,
                bgcolor="#FFFFFF",
                border_radius=30,
                alignment=alignment.center,
                content=Column(
                    controls=[
                        Container(width=350,
                                  height=70,
                                  bgcolor=blue,
                                  alignment=alignment.top_center,
                                  padding=padding.only(left=10, right=10),
                                  content=Row(
                                      controls=[
                                          Container(padding=padding.only(top=25),
                                                    content=Image(
                                                        src="pic/back.png",
                                                        color=colors.WHITE,
                                                        width=20,
                                                        height=20
                                                    ),
                                                    on_click=lambda _: page.go(f"/setting/{user_id}")
                                                    ),

                                          Container(padding=padding.only(left=110, top=25),
                                                    content=Text(
                                                        value="Account",
                                                        size=20,
                                                        font_family="RobotoSlab",
                                                        color=colors.WHITE,
                                                        text_align=TextAlign.CENTER)
                                                    ),
                                      ]
                                  )
                                  ),

                        password_container


                    ]
                ))
            ]
        )
