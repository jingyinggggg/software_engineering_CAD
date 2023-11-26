from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminDeleteDoctorPage:
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
                      f"workingTime, workingDay, image, nonWorkingDay, username, password FROM doctors WHERE id = {doctor_id}")
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
            retrieve_username = record[0][11]
            retrieve_password = record[0][12]

            return retrieve_doctor_id, retrieve_fullName, retrieve_email, retrieve_clinicPhoneNumber, retrieve_experience, retrieve_specialization, retrieve_description, retrieve_workingTime, retrieve_workingDay, retrieve_image, retrieve_image, retrieve_restDay, retrieve_username, retrieve_password

        retrieve_doctor_id, retrieve_fullName, retrieve_email, retrieve_clinicPhoneNumber, retrieve_experience, retrieve_specialization, retrieve_description, retrieve_workingTime, retrieve_workingDay, retrieve_image, retrieve_image, retrieve_restDay, retrieve_username, retrieve_password = get_doctor_details()

        def get_clinic_details():
            c = db.cursor()
            c.execute("SELECT name FROM clinic WHERE id = ?", (user_id,))
            record = c.fetchone()

            clinic_name = record[0]
            return clinic_name

        clinic_name = get_clinic_details()

        success_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have deleted current doctor account successfully!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/admin/clinicAdminManageDoctor/{user_id}"))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_dlg(dialog):
            page.dialog = dialog
            dialog.open = True
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
            read_only=True
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
            dense=True,
            read_only=True
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
            value=retrieve_experience,
            read_only=True
        )

        specialization = TextField(
            dense=True,
            label="Specialization",
            border_color=blue,
            height=40,
            label_style=TextStyle(size=12,
                                  color=colors.BLACK),
            text_style=TextStyle(color=colors.BLACK,
                                 size=12,
                                 weight=FontWeight.W_500),
            value=retrieve_specialization,
            read_only=True
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
            dense=True,
            multiline=True,
            value=retrieve_description,
            read_only=True
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
            dense=True,
            value=retrieve_workingTime,
            read_only=True
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
            dense=True,
            width=158,
            value=retrieve_workingDay,
            read_only=True
        )

        non_working_day = TextField(
            dense=True,
            label="Non Working Day",
            border_color=blue,
            height=40,
            label_style=TextStyle(size=12,
                                  color=colors.BLACK),
            text_style=TextStyle(color=colors.BLACK,
                                 size=12,
                                 weight=FontWeight.W_500),
            width=158,
            value=retrieve_restDay,
            read_only=True
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
            value=retrieve_username,
            read_only=True
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
            value=retrieve_password,
            read_only=True
        )

        def deleteRecord(e):
            c = db.cursor()
            c.execute(f"DELETE FROM doctors WHERE id = {doctor_id}")
            db.commit()
            open_dlg(success_dialog)

        return View(
            "/admin/clinicAdminDeleteDoctorPage/:user_id:doctor_id",
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
                                margin=margin.only(left=10, right=10, bottom=10),
                                content=Text(
                                    value="Delete Doctor",
                                    color="#3386C5",
                                    weight=FontWeight.W_600,
                                    size=18,
                                ),

                            ),

                            Container(
                                margin=margin.only(left=10, right=10),
                                content=Column(
                                    controls=[
                                        name,

                                        username,

                                        password,

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

                                        Container(
                                            margin=margin.only(top=10, bottom=20),
                                            content=TextButton(content=Text("Delete",
                                                                            size=16,
                                                                            color=colors.WHITE,
                                                                            text_align=TextAlign.CENTER),
                                                               width=325,
                                                               height=45,
                                                               style=ButtonStyle(bgcolor={"": blue},
                                                                                 shape={
                                                                                     "": RoundedRectangleBorder(
                                                                                         radius=10)}),

                                                               on_click=deleteRecord
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
