import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
from datetime import datetime

# import datetime
db = sqlite3.connect("cad.db", check_same_thread=False)


class PatientNotificationPage:
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

        rejectedText = Container(
            margin=margin.only(bottom=10, left=10, top=10),
            alignment=alignment.top_left,
            content=Text(
                value="Reminder (Rejected Appointment)",
                size=16,
                font_family="RobotoSlab",
                color=colors.BLACK),
            visible=False

        )

        def get_notification_details():
            c = db.cursor()
            c.execute("SELECT booking.*, doctors.* FROM booking INNER JOIN doctors ON booking.doctorID = doctors.id "
                      "WHERE booking.patientID = ? AND booking.bookingStatus = ? ORDER "
                      "BY appointmentDate DESC", (user_id, 1))
            record = c.fetchall()
            return record

        notification_details = get_notification_details()

        def displayRecord(records):
            current_datetime = datetime.now()

            if records:
                record_containers = []
                for record in records:
                    appointment_datetime = datetime.strptime(f"{record[3]} {record[4]}", "%d %B %Y %I:%M %p")

                    if appointment_datetime.date() < current_datetime.date() or (
                            appointment_datetime.date() == current_datetime.date() and appointment_datetime.time() < current_datetime.time()):
                        # Skip notifications for appointments in the past
                        continue

                    if record:
                        record_container = Container(
                            width=350,
                            bgcolor=lightBlue,
                            margin=margin.only(top=-10, bottom=1),
                            padding=padding.only(left=10, right=10, top=10, bottom=20),
                            alignment=alignment.center,
                            content=Row(
                                controls=[
                                    Container(
                                        padding=padding.only(top=10, right=10),
                                        alignment=alignment.center,
                                        content=Column(
                                            horizontal_alignment="center",
                                            controls=[
                                                Icon(
                                                    icons.TIPS_AND_UPDATES_OUTLINED,
                                                    size=35,
                                                    color=blue,
                                                )
                                            ]
                                        )
                                    ),

                                    Column(
                                        controls=[
                                            Container(
                                                padding=padding.only(top=10),
                                                width=260,
                                                content=Text(
                                                    value=f"You have an appointment with Dr. {record[17]} on {record[3]} at {record[4]}.",
                                                    color=colors.BLACK,
                                                    size=12,
                                                    font_family="RobotoSlab",
                                                    weight=FontWeight.W_500,
                                                    text_align=TextAlign.JUSTIFY
                                                )
                                            )
                                        ]
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
                            Image(
                                src="pic/notification_icon.png",
                                width=150,
                                height=150
                            ),

                            Container(
                                padding=padding.only(left=30, right=30),
                                content=Text(
                                    width=250,
                                    value="You do not have any notification yet.",
                                    text_align=TextAlign.CENTER,
                                    size=12,
                                    color=grey,
                                    font_family="RobotoSlab"
                                )
                            ),
                        ]
                    )
                )

        def get_rejected_notification_details():
            c = db.cursor()
            c.execute("SELECT booking.*, doctors.* FROM booking INNER JOIN doctors ON booking.doctorID = doctors.id "
                      "WHERE booking.patientID = ? AND booking.bookingStatus = ? ORDER "
                      "BY appointmentDate DESC", (user_id, -1))
            record = c.fetchall()
            return record

        reject_notification_details = get_rejected_notification_details()

        def show_reject_text(reject_record):
            return len(reject_record) > 0

        rejectedText.visible = show_reject_text(reject_notification_details)

        def displayRejectedRecord(records):
            current_datetime = datetime.now()
            # current_datetime = datetime(2023, 10, 26, 10, 1)

            if records:
                record_containers = []
                for record in records:
                    appointment_datetime = datetime.strptime(f"{record[3]} {record[4]}", "%d %B %Y %I:%M %p")

                    if appointment_datetime.date() < current_datetime.date() or (
                            appointment_datetime.date() == current_datetime.date() and appointment_datetime.time() < current_datetime.time()):
                        # Skip notifications for appointments in the past
                        continue

                    if record:
                        record_container = Container(
                            width=350,
                            bgcolor=lightBlue,
                            margin=margin.only(top=-10, bottom=1),
                            padding=padding.only(left=10, right=10, top=10, bottom=20),
                            alignment=alignment.center,
                            content=Row(
                                controls=[
                                    Container(
                                        padding=padding.only(top=10, right=10),
                                        alignment=alignment.center,
                                        content=Column(
                                            horizontal_alignment="center",
                                            controls=[
                                                Icon(
                                                    icons.TIPS_AND_UPDATES_OUTLINED,
                                                    size=35,
                                                    color=blue,
                                                )
                                            ]
                                        )
                                    ),

                                    Column(
                                        controls=[
                                            Container(
                                                padding=padding.only(top=10),
                                                width=260,
                                                content=Text(
                                                    value=f"Your appointment with Dr. {record[17]} on {record[3]} at {record[4]} has been rejected by admin.",
                                                    color=colors.BLACK,
                                                    size=12,
                                                    font_family="RobotoSlab",
                                                    weight=FontWeight.W_500,
                                                    text_align=TextAlign.JUSTIFY
                                                )
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
                        record_containers.append(record_container)

                return Column(controls=record_containers)
            else:
                return Container()

        return View(
            "/patientNotification/:user_id",
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

                                                    Container(padding=padding.only(left=85, top=25),
                                                              content=Text(
                                                                  value="Notification",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),

                                                ]
                                            )
                                            ),

                                  Container(
                                      margin=margin.only(bottom=10, left=10),
                                      alignment=alignment.top_left,
                                      content=Text(
                                          value="Reminder (Upcoming Appointment)" if len(notification_details) != 0 else "",
                                          size=16,
                                          font_family="RobotoSlab",
                                          color=colors.BLACK)

                                  ),

                                  displayRecord(notification_details),

                                  rejectedText,

                                  displayRejectedRecord(reject_notification_details)


                              ]
                          )
                          )
            ]
        )
