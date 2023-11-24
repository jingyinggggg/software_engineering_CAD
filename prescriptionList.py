import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class PrescriptionList:
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

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        self.db = sqlite3.connect("cad.db", check_same_thread=False)

        def get_prescription_list():
            c = db.cursor()
            c.execute("SELECT * FROM prescriptions INNER JOIN booking ON prescriptions.bookingID = booking.bookingID "
                      "WHERE booking.doctorID = ? AND booking.bookingID = ?",
                      (user_id, booking_id,))
            record = c.fetchall()
            return record

        prescription = get_prescription_list()

        def displayPrescriptionList(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/prescription/{user_id}{record_id}")

                    record_container = Container(
                        margin=margin.only(left=15, right=15, top=20),
                        border_radius=10,
                        border=border.all(1, colors.BLACK),
                        padding=padding.only(left=20, right=20, top=20, bottom=20),
                        content=Row(
                            controls=[
                                Container(
                                    padding=padding.only(top=-10),
                                    content=Image(
                                        src="pic/prescription_icon.png",
                                        width=50,
                                        height=50,
                                    )

                                ),

                                Column(
                                    controls=[
                                        Container(
                                            margin=margin.only(bottom=-3),
                                            width=220,
                                            content=Text(
                                                value=f"Appointment Date: {record[0]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Appointment Time: {record[1]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Clinic Name: {record[2]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=235,
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        value="Appointment Status: ",
                                                        color=colors.BLACK,
                                                        size=11,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                    ),

                                                    Container(
                                                        margin=margin.only(left=-8),
                                                        content=Text(
                                                            value=record[3],
                                                            color=colors.GREEN,  # Set the text color to red
                                                            size=11,
                                                            font_family="RobotoSlab",
                                                            weight=FontWeight.W_600,  # Set the text to bold
                                                            text_align=TextAlign.JUSTIFY,
                                                        )
                                                    ),

                                                ]
                                            )
                                        )
                                    ]
                                )
                            ]
                        ), on_click=on_more_button_click()
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

            else:
                return Container(
                    padding=padding.only(top=140),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Image(
                                src="pic/appointment_icon.png",
                                width=120,
                                height=120
                            ),

                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="You do not have any approved status yet.",
                                    text_align=TextAlign.CENTER,
                                    size=12,
                                    color=colors.BLACK,
                                    font_family="RobotoSlab",
                                    weight=FontWeight.W_500
                                )
                            ),

                        ]
                    )
                )

        def get_requested_booking():
            c = db.cursor()
            c.execute("SELECT appointmentDate, appointmentTime, clinic.name, appointmentStatus FROM booking INNER JOIN clinic ON booking.clinicID = clinic.id WHERE "
                      "doctorID = ? AND proofStatus = ? ORDER BY bookingID DESC",
                      (user_id, 0,))
            record = c.fetchall()
            return record

        requested_booking = get_requested_booking()

        def displayRequestedBooking(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/prescription/{user_id}{record_id}")

                    record_container = Container(
                        margin=margin.only(left=15, right=15, top=20),
                        border_radius=10,
                        border=border.all(1, colors.BLACK),
                        padding=padding.only(left=20, right=20, top=20, bottom=20),
                        content=Row(
                            controls=[
                                Container(
                                    padding=padding.only(top=-10),
                                    content=Image(
                                        src="pic/prescription_icon.png",
                                        width=50,
                                        height=50,
                                    )

                                ),

                                Column(
                                    controls=[
                                        Container(
                                            margin=margin.only(bottom=-3),
                                            width=220,
                                            content=Text(
                                                value=f"Appointment Date: {record[0]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Appointment Time: {record[1]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Clinic Name: {record[2]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=235,
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        value="Appointment Status: ",
                                                        color=colors.BLACK,
                                                        size=11,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                    ),

                                                    Container(
                                                        margin=margin.only(left=-8),
                                                        content=Text(
                                                            value=record[3],
                                                            color=colors.GREEN,  # Set the text color to red
                                                            size=11,
                                                            font_family="RobotoSlab",
                                                            weight=FontWeight.W_600,  # Set the text to bold
                                                            text_align=TextAlign.JUSTIFY,
                                                        )
                                                    ),

                                                ]
                                            )
                                        )
                                    ]
                                )
                            ]
                        ), on_click=on_more_button_click()
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

            else:
                return Container(
                    padding=padding.only(top=140),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Image(
                                src="pic/prescription_icon.png",
                                width=120,
                                height=120
                            ),

                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="You do not have any requested appointment yet.",
                                    text_align=TextAlign.CENTER,
                                    size=12,
                                    color=colors.BLACK,
                                    font_family="RobotoSlab",
                                    weight=FontWeight.W_500
                                )
                            ),

                        ]
                    )
                )

        def get_rejected_booking():
            c = db.cursor()
            c.execute("SELECT appointmentDate, appointmentTime, clinic.name, appointmentStatus FROM booking INNER JOIN clinic ON booking.clinicID = clinic.id WHERE "
                      "doctorID = ? AND proofStatus = ? ORDER BY bookingID DESC",
                      (user_id, -1,))
            record = c.fetchall()
            return record

        rejected_booking = get_rejected_booking()

        def displayRejectedBooking(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/prescription/{user_id}{record_id}")

                    record_container = Container(
                        margin=margin.only(left=15, right=15, top=20),
                        border_radius=10,
                        border=border.all(1, colors.BLACK),
                        padding=padding.only(left=20, right=20, top=20, bottom=20),
                        content=Row(
                            controls=[
                                Container(
                                    padding=padding.only(top=-10),
                                    content=Image(
                                        src="pic/prescription_icon.png",
                                        width=50,
                                        height=50,
                                    )

                                ),

                                Column(
                                    controls=[
                                        Container(
                                            margin=margin.only(bottom=-3),
                                            width=220,
                                            content=Text(
                                                value=f"Appointment Date: {record[0]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Appointment Time: {record[1]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Clinic Name: {record[2]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=235,
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        value="Appointment Status: ",
                                                        color=colors.BLACK,
                                                        size=11,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                    ),

                                                    Container(
                                                        margin=margin.only(left=-8),
                                                        content=Text(
                                                            value=record[3],
                                                            color=colors.RED,
                                                            size=11,
                                                            font_family="RobotoSlab",
                                                            weight=FontWeight.W_600,  # Set the text to bold
                                                            text_align=TextAlign.JUSTIFY,
                                                        )
                                                    ),

                                                ]
                                            )
                                        )
                                    ]
                                )
                            ]
                        ), on_click=on_more_button_click()
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

            else:
                return Container(
                    padding=padding.only(top=140),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Image(
                                src="pic/prescription_icon.png",
                                width=120,
                                height=120
                            ),

                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="You do not have any rejected request yet.",
                                    text_align=TextAlign.CENTER,
                                    size=12,
                                    color=colors.BLACK,
                                    font_family="RobotoSlab",
                                    weight=FontWeight.W_500
                                )
                            ),

                        ]
                    )
                )

        return View(
            "/prescriptionList/:user_id:booking_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Column(
                        # alignment=MainAxisAlignment.CENTER,
                                   controls=[
                                       Row(
                                           alignment=MainAxisAlignment.CENTER,
                                           controls=[
                                               Container(
                                                   padding=padding.only(right=120),
                                                   width=350,
                                                   height=80,
                                                   bgcolor="#3386C5",
                                                   content=Row(controls=[
                                                                   Container(padding=padding.only(left=10, top=5),
                                                                             content=Image(
                                                                                 src="pic/back.png",
                                                                                 color=colors.WHITE,
                                                                                 width=20,
                                                                                 height=20
                                                                             ),
                                                                             on_click=lambda _: page.go(
                                                                                 f"/login/homepage/{user_id}")),
                                                                   Container(padding=padding.only(left=75),
                                                                             content=Text("Prescription",
                                                                                          color="WHITE",
                                                                                          text_align=TextAlign.CENTER,
                                                                                          size=20,
                                                                                          font_family="RobotoSlab"
                                                                                          ))
                                                               ]),

                                               ), get_prescription_list()
                                           ])
                                   ])
                )
            ])
