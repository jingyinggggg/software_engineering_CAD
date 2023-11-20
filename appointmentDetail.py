from flet import *
from flet_route import Params, Basket
import sqlite3
import os
import shutil

db = sqlite3.connect("cad.db", check_same_thread=False)


class AppointmentDetail:
    def get_patient_appointment_data(self, user_id):
        c = db.cursor()
        sql = '''
        SELECT fullName, dob, gender
        FROM users
        INNER JOIN booking
        ON users.id = booking.patientID
        WHERE users.id = ?;
        '''
        c.execute(sql, (user_id,))
        result = c.fetchall()

        if result:
            fullName, dob, gender = result[0]
            return fullName, dob, gender
        else:
            return None

    def get_appointment_detail(self, user_id):
        c = db.cursor()
        sql = '''
        SELECT appointmentDate, appointmentTime, appointmentType, reasonVisit, bookingID
        FROM booking
        INNER JOIN users
        ON booking.patientID = users.id
        WHERE users.id = ?;
        '''
        c.execute(sql, (user_id,))
        result = c.fetchall()

        if result:
            appointmentDate, appointmentTime, appointmentType, reasonVisit, bookingID = result[0]
            return appointmentDate, appointmentTime, appointmentType, reasonVisit, bookingID
        else:
            return None

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)

        # Retrieve patient and appointment data
        patient_data = self.get_patient_appointment_data(user_id)
        appointment_data = self.get_appointment_detail(user_id)

        if patient_data and appointment_data:
            fullName, dob, gender = patient_data
            appointmentDate, appointmentTime, appointmentType, reasonVisit, bookingID = appointment_data

            # Update the relevant parts of your view with the retrieved data
            page.title = "Call A Doctor"
            page.window_width = 380
            page.window_height = 900
            page.horizontal_alignment = "center"
            page.vertical_alignment = "center"
            page.theme_mode = "dark"

            page.fonts = {
                "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
            }

            def setTextFieldValue(textField, value):
                if value != "":
                    textField.value = value

            lightBlue = "#D0DCEE"
            blue = "#3386C5"
            grey = "#71839B"

            def display_patient_details(patient_details):
                fullName, dob, gender = patient_details

                return Column(
                    controls=[
                        Row(
                            alignment="spaceBetween",
                            controls=[
                                Text("Full Name", color="BLACK", size=12, weight=FontWeight.BOLD, width=90),
                                Text(": ", color="BLACK", size=12),
                                Text(fullName, text_align=TextAlign.JUSTIFY, color="BLACK", size=12,
                                     weight=FontWeight.W_600, width=100)
                            ]
                        ),
                        Row(
                            alignment="spaceBetween",
                            controls=[
                                Text("Date of Birth", color="BLACK", size=12, weight=FontWeight.BOLD, width=90),
                                Text(": ", color="BLACK", size=12),
                                Text(dob, color="BLACK", text_align=TextAlign.JUSTIFY, size=12, weight=FontWeight.W_600,
                                     width=100)
                            ]
                        ),
                        Row(
                            alignment="spaceBetween",
                            controls=[
                                Text("Gender", color="BLACK", size=12, weight=FontWeight.BOLD, width=90),
                                Text(": ", color="BLACK", size=12),
                                Text(gender, text_align=TextAlign.JUSTIFY, color="BLACK", size=12,
                                     weight=FontWeight.W_600, width=100)
                            ]
                        )
                    ]
                )

            proof_of_status_picker = TextField(
                label="Upload Proof of Status",
                height=50,
                width=230,
                label_style=TextStyle(font_family="RobotoSlab",
                                      size=12,
                                      color=colors.GREY_800),
                value="Filename: doctor_name_patient_name",
                border_color=blue,
                text_style=TextStyle(size=10,
                                     color=grey,
                                     font_family="RobotoSlab"
                                     ),
                dense=True,
                read_only=True
            )

            image_file = Text("")

            def saveUpload(e: FilePickerResultEvent):
                # Get path of the image
                for x in e.files:
                    image_file.value = f"pic/{x.name}"
                    setTextFieldValue(proof_of_status_picker, x.name)

                    # This is to get current location
                    copy = os.path.join(os.getcwd(), "pic")
                    shutil.copy(x.path, copy)
                    page.update()

            file_picker = FilePicker(on_result=saveUpload)
            page.overlay.append(file_picker)

            proof_status = Container(
                margin=margin.only(top=10),
                content=Row(
                    controls=[
                        proof_of_status_picker,

                        Container(
                            margin=margin.only(left=-8, top=-10),
                            content=TextButton(content=Text("📂 Insert file",
                                                            size=12,
                                                            font_family="RobotoSlab",
                                                            color=colors.BLACK,
                                                            text_align=TextAlign.CENTER),
                                               on_click=lambda _: file_picker.pick_files()
                                               )
                        )
                    ]
                )
            )

            alert_dialog = AlertDialog(
                modal=True,
                title=Text("Success", text_align=TextAlign.CENTER),
                content=Text(
                    "You have upload the evidence to proof that the patient has visited you. Please wait for "
                    "admin to review it then only generate the prescription for this patient.",
                    text_align=TextAlign.CENTER),
                actions=[TextButton("Done", on_click=lambda _: close_dlg())],
                actions_alignment=MainAxisAlignment.CENTER,
                open=False
            )

            error_dialog = AlertDialog(
                modal=True,
                title=Text("Fail", text_align=TextAlign.CENTER),
                content=Text(
                    "Please upload the proof image.",
                    text_align=TextAlign.CENTER),
                actions=[TextButton("Try Again", on_click=lambda _: close_dlg1())],
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

            def open_dlg1():
                page.dialog = error_dialog
                error_dialog.open = True
                page.update()

            def close_dlg1():
                page.dialog = error_dialog
                error_dialog.open = False
                page.update()

            def addToDatabase(e):
                c = db.cursor()
                if image_file.value != "":
                    c.execute("UPDATE booking SET proof = ? WHERE bookingID = ?",
                              (image_file.value, bookingID))
                    db.commit()
                    open_dlg()
                else:
                    open_dlg1()


            patient_details_control = display_patient_details(patient_data)

            def display_appointment_details(appointment_details):
                appointmentDate, appointmentTime, appointmentType, reasonVisit, bookingID = appointment_details

                return Column(
                    controls=[
                        Container(
                            padding=padding.only(left=10, top=5, right=20),  # Add padding to the entire container
                            content=Row(
                                alignment="spaceBetween",
                                controls=[
                                    Text("Appointment Date", color="BLACK", size=12, weight=FontWeight.BOLD, width=130),
                                    Text(":", color="BLACK", size=12),
                                    Text(f"{appointmentDate}", color="BLACK", size=12, text_align=TextAlign.JUSTIFY,
                                         weight=FontWeight.W_600, width=160)
                                ]
                            )
                        ),
                        Container(
                            padding=padding.only(left=10, right=20, top=10),  # Add padding to the entire container
                            content=Row(
                                alignment="spaceBetween",
                                controls=[
                                    Text("Appointment Time", color="BLACK", size=12, weight=FontWeight.BOLD, width=130),
                                    Text(":", color="BLACK", size=12),
                                    Text(f"{appointmentTime}", color="BLACK", size=12, text_align=TextAlign.JUSTIFY,
                                         weight=FontWeight.W_600, width=160)
                                ]
                            )
                        ),
                        Container(
                            padding=padding.only(left=10, right=20, top=10),  # Add padding to the entire container
                            # margin=margin.only(right=10),
                            content=Row(
                                alignment="spaceBetween",
                                controls=[
                                    Text("Type of appointment", color="BLACK", size=12, weight=FontWeight.BOLD,
                                         width=130),
                                    Text(":", color="BLACK", size=12),
                                    Text(f"{appointmentType}", color="BLACK", size=12, text_align=TextAlign.JUSTIFY,
                                         weight=FontWeight.W_600, width=160)
                                ]
                            )
                        ),
                        Container(
                            padding=padding.only(left=10, right=20, top=10),  # Add padding to the entire container
                            content=Row(
                                alignment="spaceBetween",
                                controls=[
                                    Text("Reason for visit", color="BLACK", size=12, weight=FontWeight.BOLD, width=130),
                                    Text(":", color="BLACK", size=12),
                                    Text(reasonVisit, color="BLACK", size=12, text_align=TextAlign.JUSTIFY,
                                         weight=FontWeight.W_600, width=160)
                                ]
                            )
                        ),

                        Container(
                            margin=margin.only(left=10, top=20),
                            alignment=alignment.top_left,
                            content=Column(
                                controls=[
                                    Text("Proof of Status",
                                         font_family="RobotoSlab",
                                         weight=FontWeight.BOLD,
                                         size=14,
                                         color="#71839B"),

                                    proof_status
                                ]
                            )
                        )

                    ]
                )

            appointment_details_control = display_appointment_details(appointment_data)

            return View(
                "/appointmentDetail/:user_id",
                controls=[Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Container(
                                        padding=padding.only(right=120),
                                        width=350,
                                        height=80,
                                        alignment=alignment.center,
                                        bgcolor="#3386C5",
                                        content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        IconButton(icons.ARROW_BACK_ROUNDED,
                                                                   icon_size=30,
                                                                   icon_color="WHITE",
                                                                   on_click=lambda _: page.go(
                                                                       f"/login/homepage/{user_id}")),
                                                        Text("Appointment",
                                                             color="WHITE",
                                                             text_align=TextAlign.CENTER,
                                                             size=20,
                                                             font_family="RobotoSlab",
                                                             weight=FontWeight.BOLD)
                                                    ]
                                                    )
                                    )
                                ]),

                            Container(alignment=alignment.center,
                                      border_radius=8,
                                      padding=padding.only(left=10),
                                      margin=margin.only(left=10, top=10),
                                      border=border.all(color="BLACK"),
                                      width=320,
                                      height=150,
                                      content=Column(
                                          controls=[
                                              Container(
                                                  margin=margin.only(top=10),
                                                  content=Text(
                                                      value="Patient Details",
                                                      size=14,
                                                      font_family="RobotoSlab",
                                                      color="#71839B",
                                                      weight=FontWeight.BOLD
                                                  )
                                              ),

                                              Row(
                                                  controls=[
                                                      Container(
                                                          margin=margin.only(left=10, right=10),
                                                          content=Image(
                                                              src="pic/medicalRecord.png",
                                                              width=60,
                                                              height=60,
                                                          )
                                                      ),
                                                      patient_details_control
                                                  ]
                                              ),
                                          ]
                                      )),
                            Container(
                                margin=margin.only(left=10, top=10),
                                alignment=alignment.top_left,
                                content=
                                Text("Appointment Details",
                                     font_family="RobotoSlab",
                                     weight=FontWeight.BOLD,
                                     size=14,
                                     color="#71839B")),
                            appointment_details_control,

                            Container(alignment=alignment.center,
                                      margin=margin.only(top=10, bottom=20),
                                      content=TextButton(content=Text("Submit",
                                                                      size=16,
                                                                      font_family="RobotoSlab",
                                                                      color=colors.WHITE,
                                                                      text_align=TextAlign.CENTER),
                                                         width=325,
                                                         height=45,
                                                         style=ButtonStyle(bgcolor={"": blue},
                                                                           shape={
                                                                               "": RoundedRectangleBorder(
                                                                                   radius=10)}),
                                                         on_click=addToDatabase
                                                         )
                                      ),
                        ]
                    )
                )
                ]
            )
