from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class DoctorAccountSettingPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        print(params)
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

            # return fullName, username, email, phoneNumber, password
            return fullName, username, email, phoneNumber, password, experience, specialization, description, clinic

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        fullName, username, email, phoneNumber, password, experience, specialization, description, clinic = get_user_details()

        def get_clinic_name(clinic_id):
            c = db.cursor()
            c.execute(f"SELECT name FROM clinic WHERE id = {clinic_id}")
            record = c.fetchone()

            clinic_name = record[0]

            return clinic_name

        clinic_name = get_clinic_name(clinic)

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
            dense=True,
            read_only=True
        )

        setTextFieldValue(phoneNumberTextField,phoneNumber)

        # experienceTextField = TextField(
        #     label="Experience",
        #     label_style=TextStyle(font_family="RobotoSlab",
        #                           size=12,
        #                           color=colors.GREY_800),
        #     border_color=blue,
        #     hint_text="Example: 8 years working experience",
        #     hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
        #     text_style=TextStyle(size=12,
        #                          color=colors.GREY_800,
        #                          weight=FontWeight.W_600,
        #                          ),
        #     dense=True
        # )

        experienceTextField = TextField(
            label="Working Experience",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 ),
            # hint_text="Example: 3 years working experience",
            hint_style=TextStyle(size=12, color=colors.BLACK),
            dense=True,
        )

        setTextFieldValue(experienceTextField, experience)

        specializationTextField = Dropdown(
            dense=True,
            label="Specialization",
            border_color=blue,
            height=40,
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            options=[
                dropdown.Option("General Practitioner"),
                dropdown.Option("Cardiologists"),
                dropdown.Option("Pediatrician"),
                dropdown.Option("Obstetrician and Gynecologist"),
            ],
            text_style=TextStyle(color=grey,
                                 size=12,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500),
        )

        setTextFieldValue(specializationTextField, specialization)

        descriptionTextField = TextField(
            label="Description",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: (what you do)",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            multiline=True
        )

        setTextFieldValue(descriptionTextField, description)

        clinicTextField = TextField(
            label="Clinic",
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
            dense=True,
            read_only=True
        )

        setTextFieldValue(clinicTextField, clinic_name)

        success_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have updated your personal information successfully!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg(success_dialog))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Failed", text_align=TextAlign.CENTER),
            content=Text("Something went wrong! Please try again ...",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg(error_dialog))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_dlg(dialog):
            page.dialog = dialog
            dialog.open = True
            page.update()

        def close_dlg(dialog):
            page.dialog = dialog
            dialog.open = False
            page.update()

        def updateProfile(e):
            c = db.cursor()
            if fullNameTextField.value != "" and emailTextField.value != "" and phoneNumberTextField.value != "" and experienceTextField.value != "" and specializationTextField.value != "" and descriptionTextField.value != "":
                c.execute(
                    f"UPDATE doctors SET fullName = ?, email = ?, experience = ?, specialization = ?, description = ? "
                    f"WHERE id = {user_id}",
                    (fullNameTextField.value, emailTextField.value, experienceTextField.value, specializationTextField.value, descriptionTextField.value))
                open_dlg(success_dialog)
                db.commit()
                fullName, username, email, phoneNumber, password, experience, specialization, description, clinic = get_user_details()
                clinic_name = get_clinic_name(clinic)
                setTextFieldValue(fullNameTextField, fullName)
                setTextFieldValue(emailTextField, email)
                setTextFieldValue(phoneNumberTextField,phoneNumber)
                setTextFieldValue(experienceTextField, experience)
                setTextFieldValue(specializationTextField, specialization)
                setTextFieldValue(descriptionTextField, description)
                setTextFieldValue(clinicTextField, clinic_name)
            else:
                open_dlg(error_dialog)

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

                    experienceTextField,
                    container_padding,

                    specializationTextField,
                    container_padding,

                    descriptionTextField,
                    container_padding,

                    clinicTextField,

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
            "/doctorAccountSetting/:user_id",
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
                                                    on_click=lambda _: page.go(f"/doctorSettingPage/{user_id}")
                                                    ),

                                          Container(padding=padding.only(left=90, top=25),
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