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

        def get_schedule_appointment():
            c = db.cursor()
            c.execute("SELECT bookingID, appointmentDate, appointmentTime, users.fullName, appointmentStatus "
                      "FROM booking INNER JOIN users ON booking.patientID = users.id WHERE "
                      "doctorID = ? AND bookingStatus = ? AND proofStatus is NULL ORDER BY bookingID DESC",
                      (user_id, 1,))
            record = c.fetchall()
            return record

        scheduled_appointment = get_schedule_appointment()

        def displayScheduleAppointment(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        # print(record_id)
                        return lambda _: page.go(f"/appointmentDetail/{user_id}{record_id}")

                    record_container = Container(
                        margin=margin.only(left=15, right=15),
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

                                  Container(
                                      alignment=alignment.top_left,
                                      margin=margin.only(left=20),
                                      content=Text(
                                          "Below are your scheduled appointment:",
                                          color=colors.BLACK,
                                          size=14,
                                          font_family="RobotoSlab"
                                      )
                                  ),
                                  displayScheduleAppointment(scheduled_appointment)
                              ]
                          )
                          ),
            ]
        )