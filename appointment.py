import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class Appointment:
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

        def get_booking_detail(user_id):
            c = db.cursor()
            c.execute(
                "SELECT doctorID, bookingID, patientID, appointmentDate, appointmentTime, appointmentType, users.fullName, users.id FROM booking "
                "INNER JOIN users ON users.id = booking.patientID WHERE doctorID = ?", (user_id,))
            record = c.fetchall()
            return record

        booking = get_booking_detail(user_id)

        def displayAppointment(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[1]):
                        return lambda _: page.go(f"/appointmentDetail/{user_id}{record_id}")

                    record_container = Container(
                        margin=margin.only(left=10, right=10, top=10),
                        padding=padding.only(left=10, right=10, top=10, bottom=10),
                        border_radius=10,
                        border=border.all(1, blue),
                        content=Row(
                            controls=[
                                Container(
                                    margin=margin.only(top=10, bottom=10),
                                    # padding=padding.only(top=10, bottom=10),
                                    bgcolor=lightBlue,
                                    border_radius=10,
                                    content=Image(
                                        src="pic/medicalRecord.png",
                                        width=80,
                                        height=80,

                                    )
                                ),

                                Container(
                                    margin=margin.only(top=10),
                                    content=Column(
                                        controls=[
                                            Text(
                                                value=f"{record[6]}",
                                                size=14,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_600,
                                                color=colors.BLACK
                                            ),

                                            Row(
                                                controls=[
                                                    Text(
                                                        value="Appointment Date:",
                                                        size=10,
                                                        color="BLACK"
                                                    ),

                                                    Container(
                                                        width=185,
                                                        content=Text(
                                                            value=f"{record[3]}",
                                                            size=10,
                                                            font_family="RobotoSlab",
                                                            color=grey,
                                                            text_align=TextAlign.JUSTIFY

                                                        )
                                                    )

                                                ]

                                            ),

                                            Container(
                                                margin=margin.only(top=-3),
                                                content=Row(
                                                    controls=[
                                                        Text(
                                                            value="Appointment Time:",
                                                            size=10,
                                                            color="BLACK"
                                                        ),

                                                        Container(
                                                            content=Text(
                                                                width=200,
                                                                value=f"{record[4]}",
                                                                overflow=TextOverflow.VISIBLE,
                                                                size=10,
                                                                font_family="RobotoSlab",
                                                                color=grey,
                                                                text_align=TextAlign.JUSTIFY

                                                            )
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        ), on_click=on_more_button_click()
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

        def get_schedule_appointment():
            c = db.cursor()
            c.execute("SELECT bookingID, appointmentDate, appointmentTime, users.fullName, appointmentStatus "
                      "FROM booking INNER JOIN users ON booking.patientID = users.id WHERE "
                      "doctorID = ? AND bookingStatus = ? ORDER BY bookingID DESC",
                      (user_id, 1,))
            record = c.fetchall()
            return record

        scheduled_appointment = get_schedule_appointment()

        def displayScheduleAppointment(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/appointmentDetail/{user_id}{record_id}")

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
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Patient Name: {record[3]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            margin=margin.only(bottom=-3),
                                            width=220,
                                            content=Text(
                                                value=f"Appointment Date: {record[1]}",
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
                                                value=f"Appointment Time: {record[2]}",
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
                                                            value=record[4],
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

        def get_completed_appointment():
            c = db.cursor()
            c.execute("SELECT bookingID, appointmentDate, appointmentTime, users.fullName, appointmentStatus "
                      "FROM booking INNER JOIN users ON booking.patientID = users.id WHERE "
                      "doctorID = ? AND bookingStatus = ? ORDER BY bookingID DESC",
                      (user_id, 2,))
            record = c.fetchall()
            return record

        completed_appointment = get_completed_appointment()

        def displayCompletedAppointment(records):
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
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Patient Name: {record[3]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            margin=margin.only(bottom=-3),
                                            width=220,
                                            content=Text(
                                                value=f"Appointment Date: {record[1]}",
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
                                                value=f"Appointment Time: {record[2]}",
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
                                                            value=record[4],
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

        def get_rejected_appointment():
            c = db.cursor()
            c.execute("SELECT bookingID, appointmentDate, appointmentTime, users.fullName, appointmentStatus "
                      "FROM booking INNER JOIN users ON booking.patientID = users.id WHERE "
                      "doctorID = ? AND bookingStatus = ? ORDER BY bookingID DESC",
                      (user_id, -1,))
            record = c.fetchall()
            return record

        rejected_appointment = get_rejected_appointment()

        def displayRejectedAppointment(records):
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
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Patient Name: {record[3]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            margin=margin.only(bottom=-3),
                                            width=220,
                                            content=Text(
                                                value=f"Appointment Date: {record[1]}",
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
                                                value=f"Appointment Time: {record[2]}",
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
                                                            value=record[4],
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

        tab = Tabs(
            width=350,
            selected_index=0,
            animation_duration=300,
            label_color=blue,
            unselected_label_color=grey,
            indicator_tab_size=True,
            indicator_color=blue,
            divider_color=grey,
            tabs=[
                Tab(
                    text="\t\t\tScheduled\t\t",
                    content=Container(
                        width=340,
                        content=displayScheduleAppointment(scheduled_appointment)
                    ),
                ),
                Tab(
                    text="\t\t\tCompleted\t\t",
                    content=Container(
                        width=340,
                        content=displayCompletedAppointment(completed_appointment)
                    ),
                ),
                Tab(
                    text="\t\t\tRejected\t\t",
                    content=Container(
                        width=340,
                        content=displayRejectedAppointment(rejected_appointment)
                    ),
                )
            ],
            expand=1,
        )

        return View(
            "/appointment/:user_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              horizontal_alignment="center",
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
                                                              on_click=lambda _: page.go(f"/login/homepage/{user_id}")
                                                              ),

                                                    Container(padding=padding.only(left=70, top=25),
                                                              content=Text(
                                                                  value="Appointment",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),

                                                ]
                                            )
                                            ),

                                  tab,
                                  # displayAppointment(booking)
                              ]
                          )
                          ),
            ]
        )
