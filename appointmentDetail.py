from flet import *
from flet_route import Params, Basket
import sqlite3
import os
import shutil

db = sqlite3.connect("cad.db", check_same_thread=False)


class AppointmentDetail:
    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        booking_id = int(params.appointment_id)

        def get_appointment_detail():
            c = db.cursor()
            c.execute('''SELECT bookingID, appointmentDate, appointmentTime, appointmentType, reasonVisit, users.id,
             users.fullName, users.dob, users.gender, bookingStatus FROM booking INNER JOIN users ON booking.patientID = users.id 
             WHERE booking.doctorID = ? AND booking.bookingID = ? ''', (user_id, booking_id))
            record = c.fetchall()

            return record

        # appointment_detail = get_appointment_detail()

        appointment_detail = get_appointment_detail()

        # Check the length of appointment_detail and rejected_appointment_detail lists
        if appointment_detail and len(appointment_detail) > 0:
            appointment_info = appointment_detail[0]
        else:
            # Handle case when appointment_detail is empty or has no elements
            appointment_info = None  # or any default value you want

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

        def display_patient_details():
            return Column(
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Text("Full Name", color="BLACK", size=12, weight=FontWeight.BOLD, width=100),
                            Text(": ", color="BLACK", size=12),
                            Text(appointment_info[6], text_align=TextAlign.JUSTIFY, color="BLACK", size=12,
                                 weight=FontWeight.W_600, width=100)
                        ]
                    ),
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Text("Date of Birth", color="BLACK", size=12, weight=FontWeight.BOLD, width=100),
                            Text(": ", color="BLACK", size=12),
                            Text(appointment_info[7], color="BLACK", text_align=TextAlign.JUSTIFY, size=12,
                                 weight=FontWeight.W_600,
                                 width=100)
                        ]
                    ),
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Text("Gender", color="BLACK", size=12, weight=FontWeight.BOLD, width=100),
                            Text(": ", color="BLACK", size=12),
                            Text(appointment_info[8], text_align=TextAlign.JUSTIFY, color="BLACK", size=12,
                                 weight=FontWeight.W_600, width=100)
                        ]
                    ),
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Text("Medical Records", color="BLACK", size=12, weight=FontWeight.BOLD, width=100),
                            Text(": ", color="BLACK", size=12),
                            Container(content=Text("view", font_family="RobotoSlab", size=12, color="lightblue"
                                                   ),
                                      on_click=lambda _: page.go(
                                          f"/doctorViewMedicalRecordList/{user_id}{appointment_info[5]}")
                                      )

                        ]
                    )
                ]
            )

        patient_details_control = display_patient_details()

        def display_appointment_details():
            return Column(
                controls=[
                    Container(
                        padding=padding.only(left=10, top=5, right=20),
                        content=Row(
                            alignment="spaceBetween",
                            controls=[
                                Text("Appointment Date", color="BLACK", size=12, weight=FontWeight.BOLD, width=130),
                                Text(" :   ", color="BLACK", size=12),
                                Text(f"{appointment_info[1]}", color="BLACK", size=12,
                                     text_align=TextAlign.JUSTIFY,
                                     weight=FontWeight.W_600, width=160)
                            ]
                        )
                    ),
                    Container(
                        padding=padding.only(left=10, right=20),  # Add padding to the entire container
                        content=Row(
                            alignment="spaceBetween",
                            controls=[
                                Text("Appointment Time", color="BLACK", size=12, weight=FontWeight.BOLD, width=130),
                                Text(" :   ", color="BLACK", size=12),
                                Text(f"{appointment_info[2]}", color="BLACK", size=12, weight=FontWeight.W_600,
                                     text_align=TextAlign.JUSTIFY, width=160)
                            ]
                        )
                    ),
                    Container(
                        padding=padding.only(left=10, right=20),  # Add padding to the entire container
                        # margin=margin.only(right=10),
                        content=Row(
                            alignment="spaceBetween",
                            controls=[
                                Text("Type of appointment", color="BLACK", size=12, weight=FontWeight.BOLD,
                                     width=130),
                                Text(" :   ", color="BLACK", size=12),
                                Text(f"{appointment_info[3]}", color="BLACK", size=12,
                                     text_align=TextAlign.JUSTIFY,
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
                                Text(" :   ", color="BLACK", size=12),
                                Text(appointment_info[4], color="BLACK", size=12, text_align=TextAlign.JUSTIFY,
                                     weight=FontWeight.W_600, width=160)
                            ]
                        )
                    )
                ]
            )

        appointment_details_control = display_appointment_details()

        # Function to get rejected appointment details
        def get_rejected_appointment_detail():
            c = db.cursor()
            c.execute('''SELECT bookingID, appointmentDate, appointmentTime, appointmentType, reasonVisit, users.id,
                     users.fullName, users.dob, users.gender, rejectReason FROM booking INNER JOIN users ON booking.patientID = users.id 
                     WHERE booking.doctorID = ? AND booking.bookingID = ? AND rejectReason IS NOT NULL''',
                      (user_id, booking_id))
            record = c.fetchall()

            return record

        # rejected_appointment_detail = get_rejected_appointment_detail()
        rejected_appointment_detail = get_rejected_appointment_detail()

        if rejected_appointment_detail and len(rejected_appointment_detail) > 0:
            rejected_appointment_info = rejected_appointment_detail[0]
        else:
            # Handle case when rejected_appointment_detail is empty or has no elements
            rejected_appointment_info = None  # or any default value you want


        # Function to display rejected appointment details
        def display_rejected_appointment_details():
            if rejected_appointment_detail:
                return Column(
                    controls=[
                        Container(
                            margin=margin.only(left=10),
                            content=Text(
                                value=f"Rejected Reason",
                                size=14,
                                font_family="RobotoSlab",
                                color="#71839B",
                                weight=FontWeight.BOLD
                            )
                        ),
                        Container(padding=padding.only(left=10, right=10, top=10),
                                  border=border.all(1, color=grey),
                                  border_radius=border_radius.all(10),
                                  width=320,
                                  height=80,
                                  margin=margin.only(left=10),
                                  content=Text(
                                      value=f"{rejected_appointment_info[9]}",
                                      size=12,
                                      font_family="RobotoSlab",
                                      color=colors.RED,
                                      weight=FontWeight.W_600,
                                      text_align=TextAlign.JUSTIFY
                                  )
                                  )
                    ]
                )
            else:
                return None

        rejected_appointment_details_control = display_rejected_appointment_details()

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

                # This is to get the current location
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
                                                        color=grey,
                                                        text_align=TextAlign.CENTER),
                                           on_click=lambda _: file_picker.pick_files()
                                           )
                    )
                ]
            )
        )

        success_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text(
                "You have upload the evidence to proof that the patient has visited you. Please wait for "
                "admin to review it then only generate the prescription for this patient.",
                text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/login/homepage/{user_id}"))],
            actions_alignment=MainAxisAlignment.CENTER,
        )

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Fail", text_align=TextAlign.CENTER),
            content=Text(
                "Please upload the proof image.",
                text_align=TextAlign.CENTER),
            actions=[TextButton("Try Again", on_click=lambda _: close_dlg(error_dialog))],
            actions_alignment=MainAxisAlignment.CENTER,
        )

        def open_dlg(dialog):
            page.dialog = dialog
            dialog.open = True
            page.update()

        def close_dlg(dialog):
            page.dialog = dialog
            dialog.open = False
            page.update()

        def addToDatabase(e):
            c = db.cursor()
            if image_file.value != "":
                c.execute("UPDATE booking SET proof = ?, proofStatus = ? WHERE bookingID = ?",
                          (image_file.value, 0,booking_id))
                db.commit()
                open_dlg(success_dialog)
            else:
                open_dlg(error_dialog)

        submit_button = TextButton(
            content=Text("Submit",
                         size=16,
                         font_family="RobotoSlab",
                         color=colors.WHITE,
                         text_align=TextAlign.CENTER),
            width=325,
            height=45,
            style=ButtonStyle(bgcolor={"": blue},
                              shape={"": RoundedRectangleBorder(radius=10)}),
            on_click=addToDatabase,
            disabled=False  # Set initial disabled state
        )

        return View(
            "/appointmentDetail/:user_id:appointment_id",
            controls=[Container(
                width=350,
                height=700,
                bgcolor="#FFFFFF",
                border_radius=30,
                # alignment=alignment.center,
                content=Column(
                    scroll=True,
                    controls=[
                        Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container(
                                    padding=padding.only(right=120),
                                    width=350,
                                    height=80,
                                    bgcolor="#3386C5",
                                    content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    Container(padding=padding.only(top=5, left=10),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ), on_click=lambda _: page.go(
                                                            f"/appointment/{user_id}")),
                                                    Container(padding=padding.only(left=80),
                                                              content=Text("Appointment",
                                                                           color="WHITE",
                                                                           text_align=TextAlign.CENTER,
                                                                           size=20,
                                                                           font_family="RobotoSlab",
                                                                           ))
                                                ]
                                                )
                                )
                            ]),

                        Container(
                            content=Column(
                                controls=[
                                    Row(
                                        controls=[
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
                                                              )
                                                          ]
                                                      )),
                                            Container(
                                                Row(
                                                    controls=[
                                                        Container(
                                                            content=appointment_details_control)])),
                                            Container(
                                                margin=margin.only(left=10, top=10),
                                                alignment=alignment.top_left,
                                                content=
                                                Text("Appointment Details",
                                                     font_family="RobotoSlab",
                                                     weight=FontWeight.BOLD,
                                                     size=14,
                                                     color="#71839B")),
                                            # appointment_details_control,

                                            Container(
                                                Row(
                                                    controls=[
                                                        Container(
                                                            content=rejected_appointment_details_control)]),
                                            ),
                                        ]
                                    )]
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
                        Container(
                            Row(
                                controls=[
                                    Container(
                                        content=appointment_details_control)
                                ]
                            )
                        ),
                        Container(
                            margin=margin.only(left=10, top=10),
                            alignment=alignment.top_left,
                            content=
                            Text("Upload proof status",
                                 font_family="RobotoSlab",
                                 weight=FontWeight.BOLD,
                                 size=14,
                                 color="#71839B")),
                        Container(padding=padding.only(left=10),
                                  content=proof_status),
                        Container(
                            Row(
                                controls=[
                                    Container(
                                        content=rejected_appointment_details_control)])
                        ),

                        Container(alignment=alignment.center,
                                  margin=margin.only(top=10, bottom=20),
                                  content=submit_button,
                                  )
                    ]))])