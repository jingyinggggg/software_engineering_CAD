import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class BookingPage:
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

        def get_clinic_name(clinic_id):
            c = db.cursor()
            c.execute(f"SELECT name FROM clinic WHERE id = {clinic_id}")
            record = c.fetchone()
            clinic_name = record[0]
            return clinic_name

        def get_request_booking():
            c = db.cursor()
            c.execute("SELECT * FROM booking WHERE patientID = ? AND bookingStatus = ? ORDER BY bookingID DESC", (user_id,0,))
            record = c.fetchall()
            return record

        requested_booking = get_request_booking()

        def displayRequestBooking(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewBooking/{user_id}{record_id}")

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
                                        src="pic/appointment_icon.png",
                                        # color=grey,
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
                                                value=f"Appointment Date: {record[3]}",
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
                                                value=f"Appointment Time: {record[4]}",
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
                                                # value=f"Clinic Name: {record[6]}",
                                                value=f"Clinic Name: {get_clinic_name(record[6])}",
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
                                                            value=record[8],
                                                            color=colors.INDIGO_700,
                                                            size=11,
                                                            font_family="RobotoSlab",
                                                            weight=FontWeight.W_600,
                                                            text_align=TextAlign.JUSTIFY,
                                                        )
                                                    )

                                                ]
                                            )
                                        )
                                    ]
                                )
                            ]
                        ),
                        on_click=on_more_button_click()

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

        def get_schedule_booking():
            c = db.cursor()
            c.execute("SELECT * FROM booking WHERE patientID = ? AND bookingStatus = ? ORDER BY bookingID DESC", (user_id,1,))
            record = c.fetchall()
            return record

        schedule_booking = get_schedule_booking()

        def displayScheduleBooking(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewBooking/{user_id}{record_id}")

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
                                        src="pic/appointment_icon.png",
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
                                                value=f"Appointment Date: {record[3]}",
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
                                                value=f"Appointment Time: {record[4]}",
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
                                                value=f"Clinic Name: {get_clinic_name(record[6])}",
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
                                                            value=record[8],
                                                            color=blue,  # Set the text color to red
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
                        ),

                        on_click=on_more_button_click()
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
                                    value="You do not have any scheduled appointment yet.",
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

        def get_completed_booking():
            c = db.cursor()
            c.execute("SELECT * FROM booking WHERE patientID = ? AND bookingStatus = ? ORDER BY bookingID DESC", (user_id,2,))
            record = c.fetchall()
            return record

        completed_booking = get_completed_booking()

        def displayCompletedBooking(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewBooking/{user_id}{record_id}")

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
                                        src="pic/appointment_icon.png",
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
                                                value=f"Appointment Date: {record[3]}",
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
                                                value=f"Appointment Time: {record[4]}",
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
                                                value=f"Clinic Name: {get_clinic_name(record[6])}",
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
                                                            value=record[8],
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
                        ),

                        on_click=on_more_button_click()
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
                                    value="You do not have any completed appointment yet.",
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
            c.execute("SELECT * FROM booking WHERE patientID = ? AND bookingStatus = ? ORDER BY bookingID DESC", (user_id,-1,))
            record = c.fetchall()
            return record

        rejected_booking = get_rejected_booking()

        def displayRejectedBooking(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewBooking/{user_id}{record_id}")

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
                                        src="pic/appointment_icon.png",
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
                                                value=f"Appointment Date: {record[3]}",
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
                                                value=f"Appointment Time: {record[4]}",
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
                                                value=f"Clinic Name: {get_clinic_name(record[6])}",
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
                                                            value=record[8],
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
                        ),

                        on_click=on_more_button_click()
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
                                    value="You do not have any rejected appointment yet.",
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
                    text="Requested",
                    content=Container(
                        content=displayRequestBooking(requested_booking)
                    ),
                ),
                Tab(
                    text="Scheduled",
                    content=Container(
                        content=displayScheduleBooking(schedule_booking)
                    ),
                ),
                Tab(
                    text="Completed",
                    content=Container(
                        width=340,
                        content=displayCompletedBooking(completed_booking)
                    ),
                ),
                Tab(
                    text="Rejected",
                    content=Container(
                        width=340,
                        content=displayRejectedBooking(rejected_booking)
                    ),
                ),
            ],
            expand=1,
        )

        return View(
            "/booking/:user_id",
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
                                                              on_click=lambda _: page.go(f"/homepage/{user_id}")
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

                                  tab
                              ]
                          )
                          )
            ]
        )