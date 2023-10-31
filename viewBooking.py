from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


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
            c.execute("SELECT booking.*, doctors.* FROM booking INNER JOIN doctors ON booking.doctorID = doctors.id WHERE bookingID = ? AND patientID = ?",(booking_id,user_id))
            data = c.fetchall()

            return data

        appointmentData = getAppointment_details()

        return View(
            "/viewBooking/:user_id:booking_id",
            controls=[Container(
                width=350,
                height=700,
                bgcolor="#FFFFFF",
                border_radius=30,
                alignment=alignment.center,
                content=Column(
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
                            alignment=alignment.center,
                            content=Stack(
                                [Container(
                                    width=320,
                                    height=205,
                                    border_radius=8,
                                    content=Row(
                                        controls=[
                                            Container(
                                                border_radius=10,
                                                bgcolor=lightBlue,
                                                content=Image(
                                                    src=f"{appointmentData[0][23]}",
                                                    width=150,
                                                    height=150,

                                                )
                                            ),
                                            Container(
                                                width=100,
                                                padding=padding.only(top=15),
                                                content=Column(controls=[

                                                    Row(
                                                        controls=[
                                                            Container(
                                                                alignment=alignment.center,
                                                                width=170,
                                                                content=Text(
                                                                    value=f"DR. {appointmentData[0][12]}",
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
                                                                width=300,
                                                                content=Text(
                                                                    value=f"{appointmentData[0][18]}",
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
                                                                    value=f"{appointmentData[0][17]}",
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
                                                                    value=f"{appointmentData[0][19]}",
                                                                    size=12,
                                                                    font_family="RobotoSlab",
                                                                    color=grey,

                                                                )
                                                            )
                                                        ]
                                                    ),
                                                 ])
                                               )
                                            ]



                                    )
                                )]
                            )

                        ),
                        Container(
                            alignment=alignment.center,
                            content=Stack(
                                [
                                    Container(
                                        width=320,
                                        height=300,
                                        content=(Column([
                                            Container(
                                                content=Column(
                                                    controls=[
                                                        Text(

                                                            value="Appointment On",
                                                            color=colors.GREY_500,
                                                        ),
                                                        Text(
                                                            value=f"{appointmentData[0][3]}|"+f"{appointmentData[0][4]}",
                                                            color=colors.BLACK,
                                                            weight=FontWeight.W_600,
                                                            size=17,
                                                        ),
                                                    ],
                                                )
                                            ),
                                            Container(
                                                content=Column(
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
                                                )
                                            ),
                                            Container(
                                                content=Column(
                                                    controls=[
                                                        Text(

                                                            value="Reason Visit",
                                                            color=colors.GREY_500,
                                                        ),
                                                        Text(
                                                            value=f"{appointmentData[0][7]}",
                                                            color=colors.BLACK,
                                                            weight=FontWeight.W_600,
                                                            size=17,
                                                        ),
                                                    ],
                                                )
                                            ),
                                            Container(
                                                content=Column(
                                                    controls=[
                                                        Text(

                                                            value="Location",
                                                            color=colors.GREY_500,
                                                        ),
                                                        Text(
                                                            value=f"{appointmentData[0][6]}",
                                                            color=colors.BLACK,
                                                            weight=FontWeight.W_600,
                                                            size=17,
                                                        ),
                                                    ],
                                                )
                                            ),
                                            Container(
                                                content=Column(
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
                                                )
                                            )


                                            ])
                                        )
                                    )
                                ]
                            )

                        )

                    ]
                ))
            ]
        )
