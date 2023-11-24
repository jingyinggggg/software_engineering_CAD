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

        def get_notification_details():
            c = db.cursor()
            c.execute("SELECT booking.*, doctors.* FROM booking INNER JOIN doctors ON booking.doctorID = doctors.id "
                      "WHERE booking.patientID = ? AND booking.bookingStatus = ? ORDER BY appointmentDate DESC", (user_id,1,))
            record = c.fetchall()
            return record

        notification_details = get_notification_details()

        def displayRecord(records):
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
                                                value=f"You have an appointment with Dr. {record[12]} on {record[3]} at {record[4]}.",
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

                if not record_containers:
                    return Container(
                        padding=padding.only(top=170),
                        content=Column(
                            horizontal_alignment="center",
                            controls=[
                                Image(
                                    src="pic/notification_icon.png",
                                    width=100,
                                    height=100
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

                                  displayRecord(notification_details)


                              ]
                          )
                          )
            ]
        )

# import flet
# from flet import *
# from flet_route import Params, Basket
# import sqlite3
# from datetime import datetime
#
# db = sqlite3.connect("cad.db", check_same_thread=False)
#
#
# class PatientNotificationPage:
#     def __init__(self):
#         self.show_sidebar = False
#
#     def view(self, page: Page, params: Params, basket: Basket):
#         user_id = int(params.user_id)
#
#         page.title = "Call A Doctor"
#         page.window_width = 380
#         page.window_height = 800
#         page.horizontal_alignment = "center"
#         page.vertical_alignment = "center"
#         page.theme_mode = "dark"
#
#         page.fonts = {
#             "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
#         }
#
#         lightBlue = "#D0DCEE"
#         blue = "#3386C5"
#         grey = "#71839B"
#
#         def get_notification_details():
#             c = db.cursor()
#             c.execute("SELECT booking.*, doctors.* FROM booking INNER JOIN doctors ON booking.doctorID = doctors.id "
#                       "WHERE booking.patientID = ? AND booking.bookingStatus = ? ORDER BY appointmentDate DESC",
#                       (user_id, 0,))
#             record = c.fetchall()
#             return record
#
#         notification_details = get_notification_details()
#
#         def displayRecord(records):
#             current_datetime = datetime.now()
#             record_containers = []
#             notification_count = 0
#
#             if records:
#                 for record in records:
#                     appointment_datetime = datetime.strptime(f"{record[3]} {record[4]}", "%d %B %Y %I:%M %p")
#
#                     if appointment_datetime.date() < current_datetime.date() or (
#                             appointment_datetime.date() == current_datetime.date() and appointment_datetime.time() < current_datetime.time()):
#                         # Skip notifications for appointments in the past
#                         continue
#
#                     record_container = Container(
#                         width=350,
#                         bgcolor=lightBlue,
#                         margin=margin.only(top=-10, bottom=1),
#                         padding=padding.only(left=10, right=10, top=10, bottom=20),
#                         alignment=alignment.center,
#                         content=Row(
#                             controls=[
#                                 Container(
#                                     padding=padding.only(top=10, right=10),
#                                     alignment=alignment.center,
#                                     content=Column(
#                                         horizontal_alignment="center",
#                                         controls=[
#                                             Icon(
#                                                 icons.TIPS_AND_UPDATES_OUTLINED,
#                                                 size=35,
#                                                 color=blue,
#                                             )
#                                         ]
#                                     )
#                                 ),
#
#                                 Column(
#                                     controls=[
#                                         Container(
#                                             padding=padding.only(top=10),
#                                             width=260,
#                                             content=Text(
#                                                 value=f"You have an appointment with Dr. {record[12]} on {record[3]} at {record[4]}.",
#                                                 color=colors.BLACK,
#                                                 size=12,
#                                                 font_family="RobotoSlab",
#                                                 weight=FontWeight.W_500,
#                                                 text_align=TextAlign.JUSTIFY
#                                             )
#                                         )
#                                     ]
#                                 )
#                             ]
#                         )
#                     )
#                     record_containers.append(record_container)
#                     notification_count += 1  # Increment the count for each notification
#
#                 if not record_containers:
#                     return {
#                         "count": 0,
#                         "content": Container(
#                             padding=padding.only(top=170),
#                             content=Column(
#                                 horizontal_alignment="center",
#                                 controls=[
#                                     Image(
#                                         src="pic/notification_icon.png",
#                                         width=100,
#                                         height=100
#                                     ),
#
#                                     Container(
#                                         padding=padding.only(left=30, right=30),
#                                         content=Text(
#                                             width=250,
#                                             value="You do not have any notification yet.",
#                                             text_align=TextAlign.CENTER,
#                                             size=12,
#                                             color=grey,
#                                             font_family="RobotoSlab"
#                                         )
#                                     ),
#                                 ]
#                             )
#                         )
#                     }
#                 else:
#                     return {"count": len(record_containers), "content": Column(controls=record_containers)}
#
#         def get_notification_count():
#             notification_details1 = get_notification_details()
#             notification_data1 = displayRecord(notification_details1)
#             notification_count = notification_data1["count"]
#             return {"count": notification_count, "content": notification_data1["content"]}
#
#             # else:
#             #     return {
#             #         "count": 0,
#             #         "content": Container(
#             #             padding=padding.only(top=120),
#             #             content=Column(
#             #                 horizontal_alignment="center",
#             #                 controls=[
#             #                     Image(
#             #                         src="pic/notification_icon.png",
#             #                         width=150,
#             #                         height=150
#             #                     ),
#             #
#             #                     Container(
#             #                         padding=padding.only(left=30, right=30),
#             #                         content=Text(
#             #                             width=250,
#             #                             value="You do not have any notification yet.",
#             #                             text_align=TextAlign.CENTER,
#             #                             size=12,
#             #                             color=grey,
#             #                             font_family="RobotoSlab"
#             #                         )
#             #                     ),
#             #                 ]
#             #             )
#             #         )
#             #     }
#
#         notification_data = displayRecord(notification_details)
#
#         return View(
#             "/patientNotification/:user_id",
#             controls=[
#                 Container(width=350,
#                           height=700,
#                           bgcolor=colors.WHITE,
#                           border_radius=30,
#                           content=Column(
#                               horizontal_alignment="center",
#                               controls=[
#                                   Container(width=350,
#                                             height=70,
#                                             bgcolor=blue,
#                                             alignment=alignment.top_center,
#                                             padding=padding.only(left=10, right=10, bottom=0),
#                                             content=Row(
#                                                 controls=[
#                                                     Container(padding=padding.only(top=25),
#                                                               content=Image(
#                                                                   src="pic/back.png",
#                                                                   color=colors.WHITE,
#                                                                   width=20,
#                                                                   height=20
#                                                               ),
#                                                               on_click=lambda _: page.go(f"/homepage/{user_id}")
#                                                               ),
#
#                                                     Container(padding=padding.only(left=85, top=25),
#                                                               content=Text(
#                                                                   value="Notification",
#                                                                   size=20,
#                                                                   font_family="RobotoSlab",
#                                                                   color=colors.WHITE,
#                                                                   text_align=TextAlign.CENTER)
#                                                               ),
#
#                                                 ]
#                                             )
#                                             ),
#
#                                   notification_data["content"]
#
#                               ]
#                           )
#                           )
#             ]
#         )
#
#
# def get_notification_count():
#     return None