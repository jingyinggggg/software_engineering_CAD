import time

from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class AdminPatientRequestList:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        def get_request_booking():
            c = db.cursor()
            c.execute("SELECT * FROM booking WHERE bookingStatus = ? ORDER BY bookingID DESC", (0,))
            record = c.fetchall()
            return record

        requested_booking = get_request_booking()

        def showDialog(e):

            list_container.visible = False

            dialog.offset = transform.Offset(0,0)

            page.update()

        dialog = Container(
            border_radius=30,
            margin=margin.only(top=80, left=30, right=30),
            border=border.all(color="#D3D3D3", width=2),
            height=400,
            alignment=alignment.center,
            content=Text(
                value="Testing",
                color=colors.RED,
            ),
            offset=transform.Offset(0,2),
            animate_offset=animation.Animation(duration=300)
        )

        list_container = Container(
            alignment=alignment.center,
            content=Column(
                spacing=0,
                controls=[
                    Container(
                        width=330,
                        height=160,
                        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15),
                        border=border.all(color="#D3D3D3", width=2),
                        content=Row(
                            spacing=0,
                            alignment=alignment.center,
                            height=150,
                            controls=[
                                Column(
                                    width=80,
                                    height=150,
                                    spacing=0,
                                    controls=[
                                        Container(
                                            margin=margin.only(left=5),
                                            alignment=alignment.top_left,
                                            content=Text(
                                                value="02/12/2023",
                                                color="#A9A9A9",
                                                size=11,
                                            )
                                        ),
                                        Container(
                                            height=100,
                                            alignment=alignment.center,
                                            content=Image(
                                                src="pic/male_patient.png",
                                                width=65,
                                            )
                                        ),
                                        Container(
                                            alignment=alignment.bottom_center,
                                            content=Text(
                                                value="Tan Guan Yi",
                                                color=colors.BLACK,
                                                size=13,
                                                weight=FontWeight.W_600,
                                            )
                                        ),
                                    ]
                                ),
                                Column(
                                    alignment=alignment.center,
                                    width=128,
                                    height=150,
                                    spacing=1,
                                    controls=[
                                        Text(
                                            value="Appointment Type",
                                            size=11,
                                            color="#727272",
                                            weight=FontWeight.W_500,
                                        ),
                                        Text(
                                            value="Appointment Date|Time",
                                            size=11,
                                            color="#727272",
                                            weight=FontWeight.W_500,
                                        ),
                                        Text(
                                            value="Reason",
                                            size=11,
                                            color="#727272",
                                            weight=FontWeight.W_500,
                                        ),
                                        Text(
                                            value="Date of birth",
                                            size=11,
                                            color="#727272",
                                            weight=FontWeight.W_500,
                                        ),
                                        Text(
                                            value="Contact",
                                            size=11,
                                            color="#727272",
                                            weight=FontWeight.W_500,
                                        ),
                                        Text(
                                            value="Gender",
                                            size=11,
                                            color="#727272",
                                            weight=FontWeight.W_500,
                                        ),
                                        Text(
                                            value="Address",
                                            size=11,
                                            color="#727272",
                                            weight=FontWeight.W_500,
                                        ),

                                    ]
                                ),
                                Column(
                                    alignment=alignment.center,
                                    width=125,
                                    height=150,
                                    spacing=1,
                                    controls=[
                                        Text(
                                            value=": Offline appointment",
                                            size=11,
                                            color=colors.BLACK,
                                            weight=FontWeight.W_600,
                                        ),
                                        Text(
                                            value=": 2023/10/12 | 10:00am",
                                            size=11,
                                            color=colors.BLACK,
                                            weight=FontWeight.W_600,
                                        ),
                                        Text(
                                            value=": Irregular heartbeat",
                                            size=11,
                                            color=colors.BLACK,
                                            weight=FontWeight.W_600,
                                        ),
                                        Text(
                                            value=": 2003/07/17",
                                            size=11,
                                            color=colors.BLACK,
                                            weight=FontWeight.W_600,
                                        ),
                                        Text(
                                            value=": 012-4807808",
                                            size=11,
                                            color=colors.BLACK,
                                            weight=FontWeight.W_600,
                                        ),
                                        Text(
                                            value=": Male",
                                            size=11,
                                            color=colors.BLACK,
                                            weight=FontWeight.W_600,
                                        ),
                                        Text(
                                            value=": 16, Jalan Mawar, Taman Mawar, 12300 Butterworth",
                                            size=11,
                                            color=colors.BLACK,
                                            weight=FontWeight.W_600,
                                        ),

                                    ]
                                )
                            ]
                        )
                    ),
                    Container(
                        width=330,
                        height=30,
                        alignment=alignment.top_right,
                        content=Row(
                            width=150,
                            spacing=0,
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    width=75,
                                    height=30,
                                    bgcolor="#7DEB6B",
                                    content=Text(
                                        value="Accept",
                                        color=colors.BLACK,
                                        size=12,
                                        weight=FontWeight.W_500,
                                    ),
                                    on_click=showDialog,
                                ),
                                Container(
                                    alignment=alignment.center,
                                    width=75,
                                    height=30,
                                    bgcolor="#F25757",
                                    content=Text(
                                        value="Reject",
                                        color=colors.BLACK,
                                        size=12,
                                        weight=FontWeight.W_500,
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )

        return View(
            "/admin/adminPatientRequestList",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    bgcolor="#F4F4F4",
                    border_radius=30,
                    content=Column(
                        controls=[
                            Container(
                                padding=padding.only(top=45, left=10),
                                content=Column(
                                    controls=[
                                        Text(
                                            value="Patient Request List",
                                            color="#3386C5",
                                            weight=FontWeight.W_600,
                                            size=18,
                                        ),
                                    ]
                                )

                            ),
                            list_container,
                            dialog,
                        ]
                    )
                )
            ]
        )