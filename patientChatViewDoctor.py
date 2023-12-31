import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
db = sqlite3.connect("cad.db", check_same_thread=False)


class PatientChatViewDoctorPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
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

        def get_doctor_details():
            c = db.cursor()
            c.execute("SELECT doctors.id, doctors.fullName, doctors.specialization, doctors.experience, "
                      "doctors.description, doctors.image FROM doctors INNER JOIN clinic ON doctors.clinicID = "
                      "clinic.id WHERE doctors.STATUS = ? AND clinic.approvalStatus = 1", (1,))
            record = c.fetchall()
            return record

        doctor = get_doctor_details()

        def displayDoctor(records):
            if records:
                record_containers = []
                for record in records:
                    def chat_button_click(record_id=record[0]):
                        # print("123")
                        return lambda _: page.go(f"/patientChat/{user_id}{record_id}")

                    record_container = Container(
                        margin=margin.only(left=10, right=10, top=10),
                        padding=padding.only(left=10, right=10, top=10, bottom=10),
                        border_radius=10,
                        border=border.all(1, blue),
                        content=Row(
                            alignment="spaceBetween",
                            controls=[
                                Container(
                                    margin=margin.only(top=10, bottom=10, right=15),
                                    # padding=padding.only(top=10, bottom=10),
                                    bgcolor=lightBlue,
                                    border_radius=10,
                                    content=Image(
                                        src=f"{record[5]}",
                                        width=60,
                                        height=60,

                                    )
                                ),

                                Container(
                                    # margin=margin.only(top=10),
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
                                                        width=170,
                                                        content=Text(
                                                            value=f"{record[2]}",
                                                            size=10,
                                                            font_family="RobotoSlab",
                                                            color=grey,
                                                            text_align=TextAlign.JUSTIFY

                                                        )
                                                    )

                                                ]

                                            ),
                                        ]
                                    )
                                ),

                                IconButton(
                                    icons.CHAT_ROUNDED,
                                    icon_size=25,
                                    icon_color=blue,
                                    on_click=chat_button_click()
                                )
                            ]
                        )
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)
            else:
                return Container(
                    padding=padding.only(top=120),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Icon(
                                icons.CHAT_ROUNDED,
                                size=100,
                                color=blue
                            ),

                            Container(
                                padding=padding.only(top=10),
                                content=Text(
                                    value="There is no doctors in the system currently.",
                                    text_align=TextAlign.CENTER,
                                    size=18,
                                    weight=FontWeight.W_500,
                                    color=colors.BLACK,
                                    font_family="RobotoSlab"
                                )
                            ),

                        ]
                    )
                )

        return View(
            "/patientChatViewDoctor/:user_id",
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
                                                              on_click=lambda _: page.go(f"/homepage/{user_id}")
                                                              ),

                                                    Container(padding=padding.only(left=120, top=25),
                                                              content=Text(
                                                                  value="Chat",
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
