# from flet import *
# from flet_route import Params, Basket
# import sqlite3
#
# db = sqlite3.connect("cad.db", check_same_thread=False)
#
#
# # def update():
# #     c = db.cursor()
# #     c.execute(
# #         "UPDATE booking SET bookingStatus = ? ,appointmentStatus = ? ,rejectReason = ? WHERE bookingID = ?",
# #         (-1, "Rejected", "Dr. Johnson are not available at selected appointment time.", 1))
# #     db.commit()
#
# class ViewBookingPage:
#     def __init__(self):
#         pass
#
#     def view(self, page: Page, params: Params, basket: Basket):
#         user_id = int(params.user_id)
#         booking_id = int(params.booking_id)
#
#         page.title = "Call A Doctor"
#         page.window_width = 380
#         page.window_height = 900
#         page.horizontal_alignment = "center"
#         page.vertical_alignment = "center"
#         page.theme_mode = "dark"
#
#         page.fonts = {
#             "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
#         }
#
#         blue = "#3386C5"
#         grey = "#71839B"
#         lightBlue = "#D0DCEE"
#
#         def getAppointment_details():
#             c = db.cursor()
#             c.execute("SELECT booking.*, doctors.* FROM booking INNER JOIN doctors ON booking.doctorID = doctors.id "
#                       "WHERE bookingID = ? AND patientID = ?", (booking_id, user_id))
#             data = c.fetchall()
#
#             return data
#
#         appointmentData = getAppointment_details()
#
#         def get_doctor_name(reassign_doctor_id):
#             c = db.cursor()
#             c.execute(f"SELECT fullName FROM doctors WHERE id = {reassign_doctor_id}")
#             record = c.fetchone()
#
#             doctor_name = record[0]
#
#             return doctor_name
#
#         def get_clinic_name():
#             c = db.cursor()
#             c.execute(f"SELECT name FROM clinic WHERE id = {appointmentData[0][6]}")
#             record = c.fetchone()
#             clinic_name = record[0]
#             return clinic_name
#
#         clinic_name = get_clinic_name()
#
#         reject_reason = Container(
#             # margin=margin.only(bottom=30),
#             visible=False,
#             content=Column(
#                 controls=[
#                     Text(
#                         value="Rejected Reason",
#                         color=colors.GREY_500,
#                     ),
#                     Text(
#                         value=f"{appointmentData[0][10]}",
#                         color=colors.BLACK,
#                         weight=FontWeight.W_600,
#                         size=17,
#                         width=300,
#                         text_align=TextAlign.JUSTIFY
#                     ),
#                 ]
#             )
#         )
#
#         reassign_doctor = Text(
#                         color=colors.BLACK,
#                         weight=FontWeight.W_600,
#                         size=17,
#                         text_align=TextAlign.JUSTIFY,
#                         width=300,
#                     )
#
#         reassign_doctor_field = Container(
#             # margin=margin.only(bottom=30),
#             visible=False,
#             content=Column(
#                 controls=[
#                     Text(
#                         value="New Assigned Doctor",
#                         color=colors.GREY_500,
#                     ),
#
#                     reassign_doctor,
#                 ]
#             )
#         )
#
#         action_required = Text(
#             color=colors.RED,
#             size=10,
#             visible=False,
#             width=320,
#             text_align=TextAlign.JUSTIFY
#         )
#
#         action = Container(
#             margin=margin.only(right=10, bottom=20),
#             alignment=alignment.center,
#             visible=False,
#             content=Row(
#                 controls=[
#                     Container(margin=margin.only(right=5),
#                               content=IconButton(content=Text("Accept",
#                                                               size=12,
#                                                               color=colors.BLACK,
#                                                               text_align=TextAlign.CENTER,
#                                                               weight=FontWeight.W_700),
#                                                  width=100,
#                                                  height=40,
#                                                  style=ButtonStyle(
#                                                      bgcolor={"": "#7DEB6B"},
#                                                      shape={
#                                                          "": RoundedRectangleBorder(
#                                                              radius=7)}
#                                                  ),
#                                                  # on_click=update_appointment_status
#                                                  )
#                               ),
#
#                     Container(content=IconButton(content=Text("Decline",
#                                                               size=12,
#                                                               color=colors.BLACK,
#                                                               text_align=TextAlign.CENTER,
#                                                               weight=FontWeight.W_700),
#                                                  width=100,
#                                                  height=40,
#                                                  style=ButtonStyle(
#                                                      bgcolor={"": "#F25757"},
#                                                      shape={
#                                                          "": RoundedRectangleBorder(
#                                                              radius=7)}
#                                                  ),
#                                                  # on_click=show_reject_reason_field
#                                                  )
#                               )
#                 ]
#             )
#         )
#
#         def show_reject_reason(records):
#             if records:
#                 for record in records:
#                     if record[9] == -1:
#                         reject_reason.visible = True
#                         if record[14] != "":
#                             reassign_doctor_field.visible = True
#                             reassign_doctor.value = f"Admin have rescheduled your appointment with Dr. {get_doctor_name(record[14])}."
#                             action_required.value = ("*** You may accept or decline the reschedule appointment. Please "
#                                                      "take note that your reschedule appointment will only be "
#                                                      "confirmed after you click on the accept button.")
#                             action_required.visible = True
#                             action.visible = True
#                         else:
#                             action_required.value = ("*** Admin do not rescheduled your appointment because there are "
#                                                      "not any available doctor during the select appointment date and "
#                                                      "time. You may make another appointment in the appointment page.")
#                             action_required.visible = True
#                             action.visible=False
#                     else:
#                         reject_reason.visible = False
#                         action.visible = False
#
#         show_reject_reason(appointmentData)
#
#         return View(
#             "/viewBooking/:user_id:booking_id",
#             controls=[
#                 Container(
#                     width=350,
#                     height=700,
#                     bgcolor="#FFFFFF",
#                     border_radius=30,
#                     content=Column(
#                         scroll=True,
#                         controls=[
#                             Container(width=350,
#                                       height=70,
#                                       bgcolor=blue,
#                                       alignment=alignment.top_center,
#                                       padding=padding.only(left=10, right=10),
#                                       content=Row(
#                                           controls=[
#                                               Container(padding=padding.only(top=25),
#                                                         content=Image(
#                                                             src="pic/back.png",
#                                                             color=colors.WHITE,
#                                                             width=20,
#                                                             height=20,
#                                                         ),
#                                                         on_click=lambda _: page.go(f"/booking/{user_id}")
#                                                         ),
#
#                                               Container(padding=padding.only(left=65, top=25),
#                                                         content=Text(
#                                                             value="My Appointment",
#                                                             size=20,
#                                                             font_family="RobotoSlab",
#                                                             color=colors.WHITE,
#                                                             text_align=TextAlign.CENTER)
#                                                         ),
#
#                                           ]
#                                       )
#                                       ),
#
#                             Container(
#                                 margin=margin.only(left=10),
#                                 content=Row(
#                                     controls=[
#                                         Container(
#                                             border_radius=10,
#                                             bgcolor=lightBlue,
#                                             content=Image(
#                                                 src=f"{appointmentData[0][27]}",
#                                                 width=150,
#                                                 height=150,
#
#                                             )
#                                         ),
#                                         Container(
#                                             width=120,
#                                             padding=padding.only(top=15),
#                                             content=Column(controls=[
#                                                 Row(
#                                                     controls=[
#                                                         Container(
#                                                             alignment=alignment.center,
#                                                             width=170,
#                                                             content=Text(
#                                                                 value=f"DR. {appointmentData[0][16]}",
#                                                                 size=15,
#                                                                 font_family="RobotoSlab",
#                                                                 color=colors.BLACK,
#                                                                 text_align=TextAlign.JUSTIFY,
#                                                                 weight=FontWeight.W_600
#
#                                                             )
#                                                         )
#
#                                                     ]
#
#                                                 ),
#                                                 Row(
#                                                     controls=[
#                                                         Text(
#                                                             value="🩺",
#                                                             size=12
#                                                         ),
#
#                                                         Container(
#                                                             width=300,
#                                                             content=Text(
#                                                                 value=f"{appointmentData[0][22]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                                 text_align=TextAlign.JUSTIFY
#
#                                                             )
#                                                         )
#
#                                                     ]
#
#                                                 ),
#
#                                                 Row(
#                                                     controls=[
#                                                         Text(
#                                                             value="🥼",
#                                                             size=12
#                                                         ),
#
#                                                         Container(
#                                                             width=120,
#                                                             content=Text(
#                                                                 value=f"{appointmentData[0][21]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                             )
#                                                         )
#                                                     ]
#                                                 ),
#
#                                                 Row(
#                                                     controls=[
#                                                         Text(
#                                                             value="📝",
#                                                             size=12
#                                                         ),
#
#                                                         Container(
#                                                             width=130,
#                                                             content=Text(
#                                                                 value=f"{appointmentData[0][23]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                                 text_align=TextAlign.JUSTIFY
#
#                                                             )
#                                                         )
#                                                     ]
#                                                 ),
#                                             ])
#                                         )
#                                     ]
#                                 )
#                             ),
#
#                             Container(
#                                 margin=margin.only(left=10),
#                                 padding=padding.only(right=10),
#                                 content=Column(
#                                     controls=[
#                                         Column(
#                                             controls=[
#                                                 Text(
#
#                                                     value="Appointment On",
#                                                     color=colors.GREY_500,
#                                                 ),
#                                                 Text(
#                                                     value=f"{appointmentData[0][3]} - {appointmentData[0][4]}",
#                                                     color=colors.BLACK,
#                                                     weight=FontWeight.W_600,
#                                                     size=17,
#                                                 ),
#                                             ],
#                                         ),
#
#                                         Column(
#                                             controls=[
#                                                 Text(
#
#                                                     value="Appointment Type",
#                                                     color=colors.GREY_500,
#                                                 ),
#                                                 Text(
#                                                     value=f"{appointmentData[0][5]}",
#                                                     color=colors.BLACK,
#                                                     weight=FontWeight.W_600,
#                                                     size=17,
#                                                 ),
#                                             ],
#                                         ),
#
#                                         Column(
#                                             controls=[
#                                                 Text(
#
#                                                     value="Reason Visit",
#                                                     color=colors.GREY_500,
#                                                 ),
#                                                 Text(
#                                                     width=320,
#                                                     value=f"{appointmentData[0][7]}",
#                                                     color=colors.BLACK,
#                                                     weight=FontWeight.W_600,
#                                                     size=17,
#                                                     text_align=TextAlign.JUSTIFY
#                                                 ),
#                                             ],
#                                         ),
#
#                                         Column(
#                                             controls=[
#                                                 Text(
#
#                                                     value="Location",
#                                                     color=colors.GREY_500,
#                                                 ),
#                                                 Text(
#                                                     value=clinic_name,
#                                                     color=colors.BLACK,
#                                                     weight=FontWeight.W_600,
#                                                     size=17,
#                                                 ),
#                                             ],
#                                         ),
#
#                                         Column(
#                                             controls=[
#                                                 Text(
#
#                                                     value="Appointment Status",
#                                                     color=colors.GREY_500,
#                                                 ),
#                                                 Text(
#                                                     value=f"{appointmentData[0][8]}",
#                                                     color=colors.BLACK,
#                                                     weight=FontWeight.W_600,
#                                                     size=17,
#                                                 ),
#                                             ],
#                                         ),
#
#                                         reject_reason,
#
#                                         reassign_doctor_field,
#
#                                         Container(
#                                             margin=margin.only(bottom=20),
#                                             content=action_required
#                                         ),
#
#                                         action
#
#                                     ]
#                                 )
#                             )
#                         ]
#                     ))
#             ]
#         )

from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


# def update():
#     c = db.cursor()
#     c.execute(
#         "UPDATE booking SET bookingStatus = ? ,appointmentStatus = ? ,rejectReason = ? WHERE bookingID = ?",
#         (-1, "Rejected", "Dr. Johnson are not available at selected appointment time.", 1))
#     db.commit()

class ViewBookingPage:
    def __init__(self):
        pass

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

        blue = "#3386C5"
        grey = "#71839B"
        lightBlue = "#D0DCEE"

        def getAppointment_details():
            c = db.cursor()
            c.execute("SELECT booking.*, doctors.* FROM booking INNER JOIN doctors ON booking.doctorID = doctors.id "
                      "WHERE bookingID = ? AND patientID = ?", (booking_id, user_id))
            data = c.fetchall()

            return data

        appointmentData = getAppointment_details()

        def get_doctor_name(reassign_doctor_id):
            c = db.cursor()
            c.execute(f"SELECT fullName FROM doctors WHERE id = {reassign_doctor_id}")
            record = c.fetchone()

            doctor_name = record[0]

            return doctor_name

        def get_clinic_name():
            c = db.cursor()
            c.execute(f"SELECT name FROM clinic WHERE id = {appointmentData[0][6]}")
            record = c.fetchone()
            clinic_name = record[0]
            return clinic_name

        clinic_name = get_clinic_name()

        accept_dialog = AlertDialog(
            modal=False,
            title=Text("Accepted", text_align=TextAlign.CENTER),
            content=Text(
                f"You have accepted the rescheduled appointment.",
                text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/booking/{user_id}"))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        decline_dialog = AlertDialog(
            modal=False,
            title=Text("Declined", text_align=TextAlign.CENTER),
            content=Text(
                f"You have declined the rescheduled appointment. You may make a new appointment at the appointment page.",
                text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg(decline_dialog))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        error_dialog = AlertDialog(
            modal=False,
            title=Text("Failed", text_align=TextAlign.CENTER),
            content=Text(
                f"Something went wrong! Please try again...",
                text_align=TextAlign.CENTER),
            actions=[TextButton("Try Again", on_click=lambda _: close_dlg(error_dialog))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        noted_dialog = AlertDialog(
            modal=False,
            title=Text("Noted", text_align=TextAlign.CENTER),
            content=Text(
                f"You may make another appointment in the appointment page. Thank you",
                text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg(noted_dialog))],
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

        def update_appointment_status(callfrom, new_doctor_id):
            d = db.cursor()
            if callfrom == "accept":
                # print(new_doctor_id)
                d.execute(f"UPDATE booking SET doctorID = ? , appointmentStatus = ? , bookingStatus = ? , "
                          f"rejectReason = NULL , reassignDoctorID = NULL WHERE bookingID = ?",
                          (new_doctor_id, "Scheduled", 1, booking_id,))
                db.commit()
                updated = True
                if updated:
                    open_dlg(accept_dialog)
                else:
                    open_dlg(error_dialog)
            elif callfrom == "decline":
                d.execute(f"DELETE FROM booking WHERE bookingID = {booking_id}")
                db.commit()
                updated = True
                if updated:
                    open_dlg(decline_dialog)
                else:
                    open_dlg(error_dialog)
            elif callfrom == "noted":
                d.execute(f"DELETE FROM booking WHERE bookingID = {booking_id}")
                db.commit()
                updated = True
                if updated:
                    open_dlg(noted_dialog)
                else:
                    open_dlg(error_dialog)

            # page.go(f"/booking/{user_id}")

        print(appointmentData)
        reject_reason = Container(
            # margin=margin.only(bottom=30),
            visible=False,
            content=Column(
                controls=[
                    Text(
                        value="Rejected Reason",
                        color=colors.GREY_500,
                    ),
                    Text(
                        value=f"{appointmentData[0][10]}",
                        color=colors.BLACK,
                        weight=FontWeight.W_600,
                        size=17,
                        width=300,
                        text_align=TextAlign.JUSTIFY
                    ),
                ]
            )
        )

        reassign_doctor = Text(
            color=colors.BLACK,
            weight=FontWeight.W_600,
            size=17,
            text_align=TextAlign.JUSTIFY,
            width=300,
        )

        reassign_doctor_field = Container(
            # margin=margin.only(bottom=30),
            visible=False,
            content=Column(
                controls=[
                    Text(
                        value="New Assigned Doctor",
                        color=colors.GREY_500,
                    ),

                    reassign_doctor,
                ]
            )
        )

        action_required = Text(
            color=colors.RED,
            size=10,
            visible=False,
            width=320,
            text_align=TextAlign.JUSTIFY
        )

        action = Container(
            margin=margin.only(right=10, bottom=20),
            alignment=alignment.center,
            visible=False,
            content=Row(
                controls=[
                    Container(margin=margin.only(right=5),
                              content=IconButton(content=Text("Accept",
                                                              size=12,
                                                              color=colors.BLACK,
                                                              text_align=TextAlign.CENTER,
                                                              weight=FontWeight.W_700),
                                                 width=100,
                                                 height=40,
                                                 style=ButtonStyle(
                                                     bgcolor={"": "#7DEB6B"},
                                                     shape={
                                                         "": RoundedRectangleBorder(
                                                             radius=7)}
                                                 ),
                                                 on_click=lambda e: update_appointment_status("accept",
                                                                                              appointmentData[0][14])
                                                 )
                              ),

                    Container(content=IconButton(content=Text("Decline",
                                                              size=12,
                                                              color=colors.BLACK,
                                                              text_align=TextAlign.CENTER,
                                                              weight=FontWeight.W_700),
                                                 width=100,
                                                 height=40,
                                                 style=ButtonStyle(
                                                     bgcolor={"": "#F25757"},
                                                     shape={
                                                         "": RoundedRectangleBorder(
                                                             radius=7)}
                                                 ),
                                                 on_click=lambda e: update_appointment_status("decline",
                                                                                              appointmentData[0][14])
                                                 )
                              )
                ]
            )
        )

        noted = Container(
            margin=margin.only(right=10, bottom=20),
            alignment=alignment.center,
            visible=False,
            content=Row(
                controls=[
                    Container(margin=margin.only(right=5),
                              content=IconButton(content=Text("Noted",
                                                              size=12,
                                                              color=colors.WHITE,
                                                              text_align=TextAlign.CENTER,
                                                              weight=FontWeight.W_700),
                                                 width=100,
                                                 height=40,
                                                 style=ButtonStyle(
                                                     bgcolor={"": blue},
                                                     shape={
                                                         "": RoundedRectangleBorder(
                                                             radius=7)}
                                                 ),
                                                 on_click=lambda e: update_appointment_status("noted",
                                                                                              appointmentData[0][14])
                                                 )
                              )
                ]
            )
        )

        def show_reject_reason(records):
            if records:
                for record in records:
                    if record[9] == -1:
                        reject_reason.visible = True
                        if record[14] is not None:
                            reassign_doctor_field.visible = True
                            reassign_doctor.value = f"Admin have rescheduled your appointment with Dr. {get_doctor_name(record[14])}."
                            action_required.value = ("*** You may accept or decline the reschedule appointment. Please "
                                                     "take note that your reschedule appointment will only be "
                                                     "confirmed after you click on the accept button.")
                            action_required.visible = True
                            action.visible = True
                        else:
                            action_required.value = ("*** Admin do not rescheduled your appointment because there are "
                                                     "not any available doctor during the select appointment date and "
                                                     "time. You may make another appointment in the appointment page.")
                            action_required.visible = True
                            action.visible = False
                            noted.visible = True
                    else:
                        reject_reason.visible = False
                        action.visible = False

        show_reject_reason(appointmentData)

        return View(
            "/viewBooking/:user_id:booking_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    content=Column(
                        scroll=True,
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
                                                            height=20,
                                                        ),
                                                        on_click=lambda _: page.go(f"/booking/{user_id}")
                                                        ),

                                              Container(padding=padding.only(left=65, top=25),
                                                        content=Text(
                                                            value="My Appointment",
                                                            size=20,
                                                            font_family="RobotoSlab",
                                                            color=colors.WHITE,
                                                            text_align=TextAlign.CENTER)
                                                        ),

                                          ]
                                      )
                                      ),

                            Container(
                                margin=margin.only(left=10),
                                content=Row(
                                    controls=[
                                        Container(
                                            border_radius=10,
                                            bgcolor=lightBlue,
                                            content=Image(
                                                src=f"{appointmentData[0][28]}",
                                                width=150,
                                                height=150,

                                            )
                                        ),
                                        Container(
                                            width=120,
                                            padding=padding.only(top=15),
                                            content=Column(controls=[
                                                Row(
                                                    controls=[
                                                        Container(
                                                            alignment=alignment.center,
                                                            width=170,
                                                            content=Text(
                                                                value=f"Dr. {appointmentData[0][17]}",
                                                                size=15,
                                                                font_family="RobotoSlab",
                                                                color=colors.BLACK,
                                                                text_align=TextAlign.JUSTIFY,
                                                                weight=FontWeight.W_600

                                                            )
                                                        )

                                                    ]

                                                ),
                                                Row(
                                                    controls=[
                                                        Text(
                                                            value="🩺",
                                                            size=12
                                                        ),

                                                        Container(
                                                            width=130,
                                                            content=Text(
                                                                value=f"{appointmentData[0][23]}",
                                                                size=12,
                                                                font_family="RobotoSlab",
                                                                color=grey,
                                                                text_align=TextAlign.JUSTIFY

                                                            )
                                                        )

                                                    ]

                                                ),

                                                Row(
                                                    controls=[
                                                        Text(
                                                            value="🥼",
                                                            size=12
                                                        ),

                                                        Container(
                                                            width=120,
                                                            content=Text(
                                                                value=f"{appointmentData[0][22]}",
                                                                size=12,
                                                                font_family="RobotoSlab",
                                                                color=grey,
                                                            )
                                                        )
                                                    ]
                                                ),

                                                Row(
                                                    controls=[
                                                        Text(
                                                            value="📝",
                                                            size=12
                                                        ),

                                                        Container(
                                                            width=130,
                                                            content=Text(
                                                                value=f"{appointmentData[0][24]}",
                                                                size=12,
                                                                font_family="RobotoSlab",
                                                                color=grey,
                                                                text_align=TextAlign.JUSTIFY

                                                            )
                                                        )
                                                    ]
                                                ),
                                            ])
                                        )
                                    ]
                                )
                            ),

                            Container(
                                margin=margin.only(left=10),
                                padding=padding.only(right=10),
                                content=Column(
                                    controls=[
                                        Column(
                                            controls=[
                                                Text(

                                                    value="Appointment On",
                                                    color=colors.GREY_500,
                                                ),
                                                Text(
                                                    value=f"{appointmentData[0][3]} - {appointmentData[0][4]}",
                                                    color=colors.BLACK,
                                                    weight=FontWeight.W_600,
                                                    size=17,
                                                ),
                                            ],
                                        ),

                                        Column(
                                            controls=[
                                                Text(

                                                    value="Appointment Type",
                                                    color=colors.GREY_500,
                                                ),
                                                Text(
                                                    value=f"{appointmentData[0][5]}",
                                                    color=colors.BLACK,
                                                    weight=FontWeight.W_600,
                                                    size=17,
                                                ),
                                            ],
                                        ),

                                        Column(
                                            controls=[
                                                Text(

                                                    value="Reason Visit",
                                                    color=colors.GREY_500,
                                                ),
                                                Text(
                                                    width=320,
                                                    value=f"{appointmentData[0][7]}",
                                                    color=colors.BLACK,
                                                    weight=FontWeight.W_600,
                                                    size=17,
                                                    text_align=TextAlign.JUSTIFY
                                                ),
                                            ],
                                        ),

                                        Column(
                                            controls=[
                                                Text(

                                                    value="Location",
                                                    color=colors.GREY_500,
                                                ),
                                                Text(
                                                    value=clinic_name,
                                                    color=colors.BLACK,
                                                    weight=FontWeight.W_600,
                                                    size=17,
                                                ),
                                            ],
                                        ),

                                        Column(
                                            controls=[
                                                Text(

                                                    value="Appointment Status",
                                                    color=colors.GREY_500,
                                                ),
                                                Text(
                                                    value=f"{appointmentData[0][8]}",
                                                    color=colors.BLACK,
                                                    weight=FontWeight.W_600,
                                                    size=17,
                                                ),
                                            ],
                                        ),

                                        reject_reason,

                                        reassign_doctor_field,

                                        Container(
                                            margin=margin.only(bottom=20),
                                            content=action_required
                                        ),

                                        noted,

                                        action,

                                        # noted

                                    ]
                                )
                            )
                        ]
                    ))
            ]
        )
