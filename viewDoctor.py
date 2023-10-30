import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ViewDoctorPage:
    def __init__(self):
        self.previous_page_route = ""

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        doctor_id = int(params.doctor_id)
        previous_page_route = params.previous_page

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
            c.execute("SELECT fullName, email, phoneNumber, experience, specialization, description, clinic, "
                      "workingTime, workingDay, image  FROM doctors WHERE id = ?", (doctor_id,))
            record = c.fetchall()
            return record

        doctor = get_doctor_details()

        def get_clinic_id():
            c = db.cursor()
            c.execute("SELECT id FROM clinic WHERE name = ?", (doctor[0][6],))
            record = c.fetchone()

            clinic_id = record[0]

            return clinic_id

        clinic_id = get_clinic_id()

        def displayDoctor(records):
            if records:
                record_containers = []
                for record in records:
                    record_container = Column(
                        horizontal_alignment="center",
                        controls=[
                            Container(
                                margin=margin.only(top=20, bottom=10),
                                # padding=padding.only(top=10, bottom=10),
                                bgcolor=lightBlue,
                                border_radius=10,
                                content=Image(
                                    src=f"{record[9]}",
                                    width=130,
                                    height=130,

                                )
                            ),

                            Text(
                                value=f"Dr. {record[0]}",
                                size=14,
                                color=colors.BLACK,
                                font_family="RobotoSlab",
                                text_align=TextAlign.CENTER.CENTER,
                                weight=FontWeight.W_600
                            ),

                            Container(
                                width=350,
                                bgcolor=lightBlue,
                                margin=margin.only(top=10),
                                padding=padding.only(left=10, right=10, top=20, bottom=20),
                                content=Row(
                                    controls=[
                                        Container(
                                            padding=padding.only(left=10),
                                            content=Column(
                                                controls=[
                                                    Text(
                                                        value=f"About",
                                                        size=14,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_600,
                                                        color=colors.BLACK
                                                    ),

                                                    Row(
                                                        controls=[
                                                            Text(
                                                                value="📍",
                                                                size=12
                                                            ),

                                                            Container(
                                                                width=230,
                                                                content=Text(
                                                                    value=f"{record[6]}",
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
                                                                value="🩺",
                                                                size=12
                                                            ),

                                                            Container(
                                                                width=300,
                                                                content=Text(
                                                                    value=f"{record[4]}",
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
                                                                content=Text(
                                                                    value=f"{record[3]}",
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
                                                                value="📝",
                                                                size=12
                                                            ),

                                                            Container(
                                                                width=280,
                                                                content=Text(
                                                                    value=f"{record[5]}",
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
                                                                value="⏳",
                                                                size=12
                                                            ),

                                                            Container(
                                                                content=Text(
                                                                    value=f"{record[8]}",
                                                                    size=12,
                                                                    font_family="RobotoSlab",
                                                                    color=grey,
                                                                    text_align=TextAlign.JUSTIFY

                                                                )
                                                            ),
                                                        ]
                                                    ),

                                                    Row(
                                                        controls=[
                                                            Text(
                                                                value="🕛",
                                                                size=12
                                                            ),

                                                            Container(
                                                                width=230,
                                                                content=Text(
                                                                    value=f"{record[7]}",
                                                                    size=12,
                                                                    font_family="RobotoSlab",
                                                                    color=grey,
                                                                    text_align=TextAlign.JUSTIFY

                                                                )
                                                            )
                                                        ]
                                                    ),

                                                    Container(
                                                        margin=margin.only(top=10),
                                                        content=Text(
                                                            value="Contact Details:",
                                                            size=12,
                                                            color=colors.BLACK,
                                                            font_family="RobotoSlab",
                                                            weight=FontWeight.W_600,
                                                        )
                                                    ),

                                                    Row(
                                                        controls=[
                                                            Text(
                                                                value="📨",
                                                                size=12
                                                            ),

                                                            Container(
                                                                width=230,
                                                                content=Text(
                                                                    value=f"{record[1]}",
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
                                                                value="📞",
                                                                size=12
                                                            ),

                                                            Container(
                                                                width=230,
                                                                content=Text(
                                                                    value=f"{record[2]}",
                                                                    size=12,
                                                                    font_family="RobotoSlab",
                                                                    color=grey,
                                                                    text_align=TextAlign.JUSTIFY

                                                                )
                                                            )
                                                        ]
                                                    ),

                                                    Container(padding=padding.only(top=20),
                                                              content=IconButton(content=Text("Make Appointment",
                                                                                              size=16,
                                                                                              font_family="RobotoSlab",
                                                                                              color=blue,
                                                                                              text_align=TextAlign.CENTER),
                                                                                 width=300,
                                                                                 height=50,
                                                                                 style=ButtonStyle(
                                                                                     bgcolor={"": colors.WHITE},
                                                                                     side={"": BorderSide(1, blue)},
                                                                                     shape={"": RoundedRectangleBorder(
                                                                                         radius=7)}
                                                                                 ),

                                                                                 on_click=lambda _: page.go(
                                                                                     f"/makeAppointment/{user_id}{doctor_id}{previous_page_route}")
                                                                                 )
                                                              )

                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),

                        ]
                    )

                    record_containers.append(record_container)

                return Column(controls=record_containers)

        def back_previous_page(e):
            if previous_page_route == "doctorListBasedOnClinic":
                page.go(f"/{previous_page_route}/{user_id}{clinic_id}")
            elif previous_page_route == "doctor":
                page.go(f"/{previous_page_route}/{user_id}")

        return View(
            "/viewDoctor/:user_id:doctor_id:previous_page",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              horizontal_alignment="center",
                              scroll=True,
                              controls=[
                                  Container(width=350,
                                            height=70,
                                            bgcolor=blue,
                                            alignment=alignment.top_center,
                                            padding=padding.only(left=10, right=10, bottom=0),
                                            content=Row(
                                                controls=[
                                                    Container(padding=padding.only(top=25),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ),
                                                              on_click=back_previous_page
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

                                  displayDoctor(doctor)

                              ]
                          )
                          )
            ]
        )
