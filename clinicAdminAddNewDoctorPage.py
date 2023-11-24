from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminAddNewDoctorPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        doctor_id = int(params.doctor_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        grey = "#71839B"
        blue = "#3386C5"
        lightBlue = "#D0DCEE"

        # Get the appointment details which has updated with the visit proof
        def get_doctor_details():
            c = db.cursor()
            c.execute(f"SELECT id, fullName, email, clinicPhoneNumber, experience, specialization, description, "
                      f"workingTime, workingDay, image, nonWorkingDay FROM doctors WHERE id = {doctor_id}")
            record = c.fetchall()

            retrieve_doctor_id = record[0][0]
            retrieve_fullName = record[0][1]
            retrieve_email = record[0][2]
            retrieve_clinicPhoneNumber = record[0][3]
            retrieve_experience = record[0][4]
            retrieve_specialization = record[0][5]
            retrieve_description = record[0][6]
            retrieve_workingTime = record[0][7]
            retrieve_workingDay = record[0][8]
            retrieve_image = record[0][9]
            retrieve_restDay = record[0][10]

            return retrieve_doctor_id, retrieve_fullName, retrieve_email, retrieve_clinicPhoneNumber, retrieve_experience, retrieve_specialization, retrieve_description, retrieve_workingTime, retrieve_workingDay, retrieve_image, retrieve_image, retrieve_restDay

        retrieve_doctor_id, retrieve_fullName, retrieve_email, retrieve_clinicPhoneNumber, retrieve_experience, retrieve_specialization, retrieve_description, retrieve_workingTime, retrieve_workingDay, retrieve_image, retrieve_image, retrieve_restDay = get_doctor_details()

        def get_clinic_details():
            c = db.cursor()
            c.execute("SELECT name FROM clinic WHERE id = ?", (user_id,))
            record = c.fetchone()

            clinic_name = record[0]
            return clinic_name

        clinic_name = get_clinic_details()

        # def setTextFieldValue(textField, value):
        #     if value != "":
        #         textField.value = value

        success_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have created an account for current doctor!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/admin/clinicAdminAddNewDoctorList/{user_id}"))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Failed", text_align=TextAlign.CENTER),
            content=Text("Something went wrong! Please make sure that you have filled in the details completely.",
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

        name = TextField(
            label="Doctor Name",
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            value=retrieve_fullName,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
        )

        email = TextField(
            label="Email",
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            value=retrieve_email,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            dense=True
        )

        phoneNumber = TextField(
            label="Clinic Phone Number",
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=retrieve_clinicPhoneNumber,
            read_only=True
        )

        experience = TextField(
            label="Working Experience",
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            hint_text="Example: 3 years working experience",
            hint_style=TextStyle(size=12, color=colors.BLACK),
            dense=True,
            value=retrieve_experience
        )

        specialization = Dropdown(
            dense=True,
            label="Specialization",
            border_color=blue,
            height=40,
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            options=[
                dropdown.Option("General Practitioner"),
                dropdown.Option("Cardiologists"),
                dropdown.Option("Pediatrician"),
                dropdown.Option("Obstetrician and Gynecologist"),
            ],
            text_style=TextStyle(color=grey,
                                 size=12,
                                 weight=FontWeight.W_500),
            value=retrieve_specialization
        )

        description = TextField(
            label="Description",
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            hint_text="Please describe that what services can doctor provided...",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True,
            multiline=True,
            value=retrieve_description
        )

        working_clinic = TextField(
            label="Working Clinic",
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            read_only=True,
            value=clinic_name,
            dense=True,
        )

        working_time = TextField(
            label="Working Start Time",
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            hint_text="Example: 7:00 am - 8:00 pm",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True,
            value=retrieve_workingTime
        )

        working_day = TextField(
            label="Working Day",
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            hint_text="E.g. Monday - Sunday",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True,
            width=158,
            value=retrieve_workingDay
        )

        non_working_day = Dropdown(
            dense=True,
            label="Non Working Day",
            border_color=blue,
            height=40,
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            options=[
                dropdown.Option("None"),
                dropdown.Option("Monday"),
                dropdown.Option("Tuesday"),
                dropdown.Option("Wednesday"),
                dropdown.Option("Thursday"),
                dropdown.Option("Friday"),
                dropdown.Option("Saturday"),
                dropdown.Option("Sunday"),
            ],
            text_style=TextStyle(color=grey,
                                 size=12,
                                 weight=FontWeight.W_500),
            width=158,
            value=retrieve_restDay
        )

        username = TextField(
            label="Username",
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
        )

        password = TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            label_style=TextStyle(size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
        )

        def updateDatabase(e):
            c = db.cursor()

            if name.value != "" and email.value != "" and phoneNumber.value != "" and experience.value != "" and specialization.value != "" and description.value != "" and working_clinic.value != "" and working_time.value != "" and working_day.value != "" and non_working_day.value != "" and username.value != "" and password.value != "":
                c.execute(f"UPDATE doctors SET fullName = ?, username = ?, email = ?, password = ?, experience = ?, "
                          f"specialization = ?, description = ?, workingTime = ?, workingDay = ?, STATUS = ?, "
                          f"nonWorkingDay = ? WHERE id = {doctor_id}",
                          (name.value, username.value, email.value, password.value, experience.value, specialization.value, description.value, working_time.value, working_day.value, 1, non_working_day.value))
                db.commit()
                open_dlg(success_dialog)
            else:
                open_dlg(error_dialog)

        return View(
            "/admin/clinicAdminAddNewDoctorPage/:user_id:doctor_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#F4F4F4",
                    border_radius=30,
                    content=Column(
                        scroll=True,
                        controls=[
                            Container(
                                padding=padding.only(top=25, left=10),
                                content=Image(
                                    src="pic/back.png",
                                    color="#3386C5",
                                    width=20,
                                    height=20
                                ),
                                on_click=lambda _: page.go(f"/admin/clinicAdminManageDoctor/{user_id}")
                            ),

                            Container(
                                margin=margin.only(left=10, right=10),
                                content=Text(
                                    value="Add New Doctor",
                                    color="#3386C5",
                                    weight=FontWeight.W_600,
                                    size=18,
                                ),

                            ),

                            Container(
                                margin=margin.only(left=10, right=10, top=10, bottom=10),
                                content=Text(
                                    value="Submitted doctor's details",
                                    color=colors.BLACK,
                                    weight=FontWeight.W_700,
                                    size=14,
                                ),

                            ),

                            Container(
                                margin=margin.only(left=10, right=10),
                                content=Column(
                                    controls=[
                                        name,

                                        email,

                                        phoneNumber,

                                        experience,

                                        specialization,

                                        description,

                                        working_clinic,

                                        working_time,

                                        Row(
                                            width=325,
                                            controls=[
                                                working_day,
                                                non_working_day
                                            ]
                                        ),

                                        # doctor_image,

                                        Container(
                                            margin=margin.only(top=10, bottom=10),
                                            content=Text(
                                                value="Submitted doctor's image",
                                                color=colors.BLACK,
                                                weight=FontWeight.W_700,
                                                size=14,
                                            ),

                                        ),

                                        Container(
                                            margin=margin.only(bottom=20),
                                            padding=padding.only(top=10, bottom=10),
                                            border_radius=0,
                                            border=border.all(2, "#D3D3D3"),
                                            content=Container(
                                                content=Image(
                                                        src=f"{retrieve_image}"
                                                    )
                                            )

                                        ),

                                        Container(
                                            margin=margin.only(top=10, bottom=10),
                                            content=Text(
                                                value="Create account for doctor",
                                                color=colors.BLACK,
                                                weight=FontWeight.W_700,
                                                size=14,
                                            ),

                                        ),

                                        username,

                                        password,

                                        Container(
                                            margin=margin.only(top=10, bottom=20),
                                            content=TextButton(content=Text("Create Account",
                                                                            size=16,
                                                                            color=colors.WHITE,
                                                                            text_align=TextAlign.CENTER),
                                                               width=325,
                                                               height=45,
                                                               style=ButtonStyle(bgcolor={"": blue},
                                                                                 shape={
                                                                                     "": RoundedRectangleBorder(
                                                                                         radius=10)}),

                                                               on_click=updateDatabase
                                                               )
                                        )

                                    ]
                                )
                            )

                        ]
                    )
                )
            ]

        )
