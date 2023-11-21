from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminUpdateAppointmentDetailsPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        booking_id = int(params.booking_id)

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

        def get_patient_details():
            c = db.cursor()
            c.execute(
                f"SELECT fullName, dob, gender FROM users INNER JOIN booking ON users.id = booking.patientID WHERE booking.bookingID = {booking_id}")
            patient_details = c.fetchall()

            patient_fullName = patient_details[0][0]
            patient_dob = patient_details[0][1]
            patient_gender = patient_details[0][2]

            return patient_fullName, patient_dob, patient_gender

        patient_fullName, patient_dob, patient_gender = get_patient_details()

        def get_booking_detail():
            c = db.cursor()
            c.execute(
                f"SELECT appointmentdate, appointmentTime, appointmentType, reasonVisit, proof FROM booking WHERE bookingID = {booking_id}")
            booking_details = c.fetchall()

            appointmentDate = booking_details[0][0]
            appointmentTime = booking_details[0][1]
            appointmentType = booking_details[0][2]
            reasonVisit = booking_details[0][3]
            proof_image = booking_details[0][4]

            return appointmentDate, appointmentTime, appointmentType, reasonVisit, proof_image

        appointmentDate, appointmentTime, appointmentType, reasonVisit, proof_image = get_booking_detail()

        success_dialog = AlertDialog(
            modal=True,
            title=Text("Successful!", text_align=TextAlign.CENTER),
            content=Text("You have updated the appointment status for current booking successfully.",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/admin/clinicAdminUpdateAppointment/{user_id}"))],
            actions_alignment=MainAxisAlignment.CENTER
        )

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Failed!", text_align=TextAlign.CENTER),
            content=Text("Something went wrong. Please try again...",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_error_dlg())],
            actions_alignment=MainAxisAlignment.CENTER
        )

        reject_dialog = AlertDialog(
            modal=True,
            title=Text("Successful!", text_align=TextAlign.CENTER),
            content=Text("You have rejected current booking successfully.",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/admin/clinicAdminUpdateAppointment/{user_id}"))],
            actions_alignment=MainAxisAlignment.CENTER
        )

        def open_reject_dialog():
            page.dialog = reject_dialog
            reject_dialog.open = True
            page.update()

        def close_reject_dlg():
            page.dialog = reject_dialog
            reject_dialog.open = False
            page.update()

        def open_dlg():
            page.dialog = success_dialog
            success_dialog.open = True
            page.update()

        def open_error_dlg():
            page.dialog = error_dialog
            error_dialog.open = True
            page.update()

        def close_error_dlg():
            page.dialog = error_dialog
            error_dialog.open = False
            page.update()

        def update_appointment_status(e):
            c = db.cursor()
            c.execute(
                f"UPDATE booking SET appointmentStatus = ?, bookingStatus = ?, proofStatus = ? WHERE bookingID = {booking_id}",
                ("Completed", 2, 1))
            db.commit()
            updated = True
            if updated:
                open_dlg()
            else:
                open_error_dlg()

        def update_appointment_status_to_reject(e):
            c = db.cursor()
            if reject_reason.value != "":
                c.execute(
                    f"UPDATE booking SET proofStatus = ? AND proofRejectReason = ? WHERE bookingID = {booking_id}",
                    (2,reject_reason.value))
                db.commit()
                updated = True
                if updated:
                    open_reject_dialog()
                else:
                    open_error_dlg()
            else:
                open_error_dlg()


        reject_reason = TextField(
            label="Enter the reject reason",
            label_style=TextStyle(size=14,
                                  color=colors.BLACK),
            border_color=colors.BLACK,
            text_style=TextStyle(size=14,
                                 color=colors.BLACK),
            autofocus=True,
            multiline=True
        )

        reject_reason_container = Container(
            margin=margin.only(left=10, right=10, bottom=20),
            visible=False,
            content=Column(
                controls=[
                    Container(
                        margin=margin.only(left=10, bottom=10),
                        alignment=alignment.top_left,
                        content=
                        Text(
                            "Reject Reason",
                            weight=FontWeight.BOLD,
                            size=14,
                            color=colors.BLACK)
                    ),

                    Container(
                        margin=margin.only(bottom=20),
                        content=reject_reason
                    ),

                    Container(
                        alignment=alignment.bottom_right,
                        content=IconButton(content=Text("Submit",
                                                        size=12,
                                                        color=colors.BLACK,
                                                        text_align=TextAlign.CENTER,
                                                        weight=FontWeight.W_700),
                                           width=100,
                                           height=40,
                                           style=ButtonStyle(bgcolor={"": colors.BLUE_400},
                                                             shape={
                                                                 "": RoundedRectangleBorder(
                                                                     radius=7)}
                                                             ),
                                           on_click=update_appointment_status_to_reject
                                           )
                    )
                ]
            )
        )

        def show_reject_reason_field(e):
            if not reject_reason_container.visible:
                reject_reason_container.visible = True
            else:
                reject_reason_container.visible = False

            page.update()

        return View(
            "/admin/clinicAdminUpdateAppointmentDetails/:user_id:booking_id",
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
                                padding=padding.only(top=25, left=10, bottom=10),
                                content=Row(
                                    controls=[
                                        Container(
                                            content=Image(
                                                src="pic/back.png",
                                                color="#3386C5",
                                                width=20,
                                                height=20
                                            ),
                                            on_click=lambda _: page.go(f"/admin/clinicAdminUpdateAppointment/{user_id}")
                                        ),
                                        Text(
                                            value=" Update Appointment Status",
                                            color="#3386C5",
                                            weight=FontWeight.W_600,
                                            size=18,
                                        )
                                    ]
                                ),
                            ),

                            Container(
                                alignment=alignment.center,
                                padding=padding.only(left=10, bottom=20),
                                margin=margin.only(left=10, top=10, right=10),
                                border=border.all(color="#D3D3D3"),
                                content=Column(
                                    controls=[
                                        Container(
                                            margin=margin.only(top=10),
                                            content=Text(
                                                value="Patient Details",
                                                size=14,
                                                color=colors.BLACK,
                                                weight=FontWeight.BOLD
                                            )
                                        ),

                                        Row(
                                            controls=[
                                                Container(
                                                    margin=margin.only(right=10),
                                                    content=Image(
                                                        src="pic/medicalRecord.png",
                                                        width=60,
                                                        height=60,
                                                        color=grey
                                                    )
                                                ),

                                                Column(
                                                    controls=[
                                                        Row(
                                                            alignment="spaceBetween",
                                                            controls=[
                                                                Text("Full Name",
                                                                     color="BLACK",
                                                                     size=12,
                                                                     width=90,
                                                                     weight=FontWeight.W_600),

                                                                Text(": ",
                                                                     color="BLACK",
                                                                     size=12),

                                                                Text(patient_fullName,
                                                                     text_align=TextAlign.JUSTIFY,
                                                                     color="BLACK",
                                                                     size=12,
                                                                     weight=FontWeight.W_600,
                                                                     width=100)
                                                            ]
                                                        ),

                                                        Row(
                                                            alignment="spaceBetween",
                                                            controls=[
                                                                Text("Date of Birth",
                                                                     color="BLACK",
                                                                     size=12,
                                                                     width=90,
                                                                     weight=FontWeight.W_600),

                                                                Text(": ",
                                                                     color="BLACK",
                                                                     size=12),

                                                                Text(patient_dob,
                                                                     text_align=TextAlign.JUSTIFY,
                                                                     color="BLACK",
                                                                     size=12,
                                                                     weight=FontWeight.W_600,
                                                                     width=100)
                                                            ]
                                                        ),

                                                        Row(
                                                            alignment="spaceBetween",
                                                            controls=[
                                                                Text("Gender",
                                                                     color="BLACK",
                                                                     size=12,
                                                                     width=90,
                                                                     weight=FontWeight.W_600),

                                                                Text(": ",
                                                                     color="BLACK",
                                                                     size=12),

                                                                Text(patient_gender,
                                                                     text_align=TextAlign.JUSTIFY,
                                                                     color="BLACK",
                                                                     size=12,
                                                                     weight=FontWeight.W_600,
                                                                     width=100)
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                    ]
                                )
                            ),

                            Container(
                                margin=margin.only(left=10, top=10),
                                alignment=alignment.top_left,
                                content=
                                Text(
                                    "Appointment Details",
                                    weight=FontWeight.BOLD,
                                    size=14,
                                    color=colors.BLACK)
                            ),

                            Container(
                                padding=padding.only(left=10, top=5, right=20),
                                # Add padding to the entire container
                                content=Row(
                                    alignment="spaceBetween",
                                    controls=[
                                        Text("Appointment Date",
                                             color="BLACK",
                                             size=12,
                                             weight=FontWeight.W_600,
                                             width=130),

                                        Text(":",
                                             color="BLACK",
                                             size=12),

                                        Text(appointmentDate,
                                             color="BLACK",
                                             size=12,
                                             text_align=TextAlign.JUSTIFY,
                                             weight=FontWeight.W_600,
                                             width=160)
                                    ]
                                )
                            ),

                            Container(
                                padding=padding.only(left=10, top=5, right=20),
                                # Add padding to the entire container
                                content=Row(
                                    alignment="spaceBetween",
                                    controls=[
                                        Text("Appointment Time",
                                             color="BLACK",
                                             size=12,
                                             weight=FontWeight.W_600,
                                             width=130),

                                        Text(":",
                                             color="BLACK",
                                             size=12),

                                        Text(appointmentTime,
                                             color="BLACK",
                                             size=12,
                                             text_align=TextAlign.JUSTIFY,
                                             weight=FontWeight.W_600,
                                             width=160)
                                    ]
                                )
                            ),

                            Container(
                                padding=padding.only(left=10, top=5, right=20),
                                # Add padding to the entire container
                                content=Row(
                                    alignment="spaceBetween",
                                    controls=[
                                        Text("Appointment Type",
                                             color="BLACK",
                                             size=12,
                                             weight=FontWeight.W_600,
                                             width=130),

                                        Text(":",
                                             color="BLACK",
                                             size=12),

                                        Text(appointmentType,
                                             color="BLACK",
                                             size=12,
                                             text_align=TextAlign.JUSTIFY,
                                             weight=FontWeight.W_600,
                                             width=160)
                                    ]
                                )
                            ),

                            Container(
                                padding=padding.only(left=10, top=5, right=20),
                                # Add padding to the entire container
                                content=Row(
                                    alignment="spaceBetween",
                                    controls=[
                                        Text("Reason Visit",
                                             color="BLACK",
                                             size=12,
                                             weight=FontWeight.W_600,
                                             width=130),

                                        Text(":",
                                             color="BLACK",
                                             size=12),

                                        Text(reasonVisit,
                                             color="BLACK",
                                             size=12,
                                             text_align=TextAlign.JUSTIFY,
                                             weight=FontWeight.W_600,
                                             width=160)
                                    ]
                                )
                            ),

                            Container(
                                margin=margin.only(left=10, top=20),
                                alignment=alignment.top_left,
                                content=
                                Text(
                                    "Proof Image",
                                    weight=FontWeight.BOLD,
                                    size=14,
                                    color=colors.BLACK)
                            ),

                            Container(
                                margin=margin.only(left=10, right=10, bottom=20),
                                padding=padding.only(left=10, right=10, top=10, bottom=10),
                                border_radius=0,
                                # width=320,
                                border=border.all(2, "#D3D3D3"),
                                content=Column(
                                    controls=[
                                        Text(
                                            value="Evidence about doctor have visited their patient",
                                            size=12,
                                            height=25,
                                            weight=FontWeight.W_600,
                                            color=colors.BLACK
                                        ),

                                        Image(
                                            src=f"{proof_image}"
                                        )
                                    ]
                                )
                            ),

                            Container(
                                margin=margin.only(left=10, right=10, bottom=20),
                                alignment=alignment.center,
                                content=Row(
                                    controls=[
                                        Container(margin=margin.only(right=5),
                                                  content=IconButton(content=Text("Accept",
                                                                                  size=12,
                                                                                  color=colors.BLACK,
                                                                                  text_align=TextAlign.CENTER,
                                                                                  weight=FontWeight.W_700),
                                                                     width=155,
                                                                     height=40,
                                                                     style=ButtonStyle(bgcolor={"": "#7DEB6B"},
                                                                                       shape={
                                                                                           "": RoundedRectangleBorder(
                                                                                               radius=7)}
                                                                                       ),
                                                                     on_click=update_appointment_status
                                                                     )
                                                  ),

                                        Container(content=IconButton(content=Text("Reject",
                                                                                  size=12,
                                                                                  color=colors.BLACK,
                                                                                  text_align=TextAlign.CENTER,
                                                                                  weight=FontWeight.W_700),
                                                                     width=155,
                                                                     height=40,
                                                                     style=ButtonStyle(bgcolor={"": "#F25757"},
                                                                                       shape={
                                                                                           "": RoundedRectangleBorder(
                                                                                               radius=7)}
                                                                                       ),
                                                                     on_click=show_reject_reason_field
                                                                     )
                                                  )
                                    ]
                                )
                            ),

                            reject_reason_container

                        ]
                    )
                )
            ]

        )
