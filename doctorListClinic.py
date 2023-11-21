import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class DoctorListBasedOnClinic:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
        user_id = int(params.user_id)
        clinic_id = int(params.clinic_id)
        # print(page.route)

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

        def get_doctor_details():
            c = db.cursor()
            c.execute("SELECT doctors.*, clinic.* FROM doctors INNER JOIN clinic ON doctors.clinicID = clinic.id"
                      " WHERE clinic.id = ?", (clinic_id,))
            record = c.fetchall()
            return record

        doctor = get_doctor_details()

        split_current_route = page.route.split("/")
        previous_route = split_current_route[1]

        def displayDoctor(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewDoctor/{user_id}{record_id}{previous_route}")

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
                                        src=f"{record[12]}",
                                        width=80,
                                        height=80,

                                    )
                                ),

                                Container(
                                    margin=margin.only(top=10),
                                    content=Column(
                                        controls=[
                                            Text(
                                                value=f"Dr. {record[1]}",
                                                size=14,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_600,
                                                color=colors.BLACK
                                            ),

                                            Row(
                                                controls=[
                                                    Text(
                                                        value="🩺",
                                                        size=10
                                                    ),

                                                    Container(
                                                        width=185,
                                                        content=Text(
                                                            value=f"{record[7]}",
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
                                                            value="🥼",
                                                            size=10
                                                        ),

                                                        Container(
                                                            content=Text(
                                                                value=f"{record[6]}",
                                                                size=10,
                                                                font_family="RobotoSlab",
                                                                color=grey,
                                                                text_align=TextAlign.JUSTIFY

                                                            )
                                                        )
                                                    ]
                                                )
                                            ),

                                            Container(
                                                margin=margin.only(top=-3),
                                                content=Row(
                                                    controls=[
                                                        Text(
                                                            value="📝",
                                                            size=10
                                                        ),

                                                        Container(
                                                            width=185,
                                                            margin=margin.only(right=90),
                                                            content=Text(
                                                                value=f"{record[8]}",
                                                                size=10,
                                                                font_family="RobotoSlab",
                                                                color=grey,
                                                                text_align=TextAlign.JUSTIFY

                                                            )
                                                        ),

                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                        on_click=on_more_button_click()
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

            else:
                return Container(
                    padding=padding.only(top=250),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="There is no any doctor in the selected clinic currently.",
                                    text_align=TextAlign.CENTER,
                                    size=12,
                                    color=colors.BLACK,
                                    font_family="RobotoSlab"
                                )
                            ),

                        ]
                    )
                )

        return View(
            "/doctorListBasedOnClinic/:user_id:clinic_id",
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
                                                              on_click=lambda _: page.go(f"/viewClinic/{user_id}{clinic_id}")
                                                              ),

                                                    Container(padding=padding.only(left=110, top=25),
                                                              content=Text(
                                                                  value="Doctor",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),

                                                ]
                                            )
                                            ),

                                  displayDoctor(doctor),

                              ]
                          )
                          )
            ]
        )
