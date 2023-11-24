import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
from datetime import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class Homepage:
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
        # page.theme_mode = "light"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        current_date = datetime.now()
        formatted_date = current_date.strftime("%d %B %Y")

        def show_side_bar(e):
            sidebar.offset = transform.Offset(0, 0)
            page.update()

        def hide_side_bar(e):
            sidebar.offset = transform.Offset(-5, 0)
            page.update()

        for x in range(len(page.views)):
            if x > 3:
                page.views.pop()

        def get_notification_count():
            c = db.cursor()
            c.execute("SELECT COUNT(*) FROM booking WHERE patientID = ? AND bookingStatus = ? AND appointmentDate >= ?",(user_id,1, formatted_date))
            record = c.fetchone()

            count = record[0]

            return count

        notification_count = get_notification_count()

        if notification_count > 0:
            notification_icon = "pic/notification_with_content.png"
        else:
            notification_icon = "pic/notification_without_content.png"

        def get_user_details():
            c = db.cursor()
            c.execute("SELECT username, phoneNumber FROM users WHERE id = ?", (user_id,))
            record = c.fetchall()

            username = record[0][0]
            phoneNumber = record[0][1]

            return username, phoneNumber

        username, phoneNumber = get_user_details()

        def get_clinic_details():
            c = db.cursor()
            c.execute("SELECT id, name, location FROM clinic WHERE approvalStatus = 1")
            record = c.fetchall()
            return record

        clinic = get_clinic_details()

        def displayRecord(records):
            if records:
                record_containers = []
                for record in records[:2]:
                    record_container = Container(
                        padding=padding.only(left=15),
                        content=Container(
                            bgcolor=lightBlue,
                            width=315,
                            padding=padding.only(top=5, bottom=10),
                            border_radius=7,
                            content=Row(
                                controls=[
                                    Container(padding=padding.only(left=10),
                                              content=Icon(icons.LOCATION_PIN,
                                                           color=blue,
                                                           size=25
                                                           )
                                              ),

                                    Column(
                                        controls=[
                                            Container(
                                                padding=padding.only(top=5),
                                                content=Text(value=f"{record[1]}",
                                                             size=12,
                                                             color=colors.BLACK,
                                                             font_family="RobotoSlab",
                                                             weight=FontWeight.W_500
                                                             )
                                            ),

                                            Container(padding=padding.only(top=-8),
                                                      width=260,
                                                      content=Text(
                                                          value=f"{record[2]}",
                                                          size=9,
                                                          color=colors.BLACK,
                                                          font_family="RobotoSlab",
                                                          weight=FontWeight.W_500,
                                                          text_align=TextAlign.JUSTIFY
                                                      )
                                                      )

                                        ]
                                    )

                                ]
                            )
                        ),

                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

            else:
                return Container()

        def get_doctor_details():
            c = db.cursor()
            c.execute("SELECT id, fullName, specialization, image FROM doctors WHERE STATUS = 1")
            record = c.fetchall()
            return record

        doctor = get_doctor_details()

        def displayDoctorRecord(records):
            if records:
                record_containers = []
                for record in records[:2]:
                    record_container = Container(
                        bgcolor=lightBlue,
                        width=155,
                        height=195,
                        border_radius=7,
                        content=Column(
                            horizontal_alignment="center",
                            controls=[
                                Container(padding=padding.only(top=-10, bottom=-8),
                                          border_radius=border_radius.only(top_left=7, top_right=7),
                                          gradient=LinearGradient(begin=alignment.top_center,
                                                                  end=alignment.bottom_center,
                                                                  colors=["#BFD1DA", "#688D9D"]),
                                          content=Image(
                                              src=f"{record[3]}",
                                              width=155,
                                              height=160,
                                              fit=ImageFit,
                                              color_blend_mode=blue,
                                          )
                                          ),

                                Container(padding=padding.only(top=-8),
                                          content=Text(value=f"Dr. {record[1]}",
                                                       size=13,
                                                       color=colors.BLACK,
                                                       text_align=TextAlign.CENTER,
                                                       font_family="RobotoSlab",
                                                       weight=FontWeight.W_500)
                                          ),

                                Container(padding=padding.only(top=-10),
                                          content=Text(
                                              value=f"{record[2]}",
                                              size=8,
                                              color=colors.BLACK,
                                              text_align=TextAlign.CENTER,
                                              font_family="RobotoSlab",
                                              weight=FontWeight.W_500)
                                          ),

                                Container(padding=padding.only(top=-12),
                                          content=Image(
                                              src="pic/star.png",
                                              width=60,
                                              height=20)
                                          )

                            ]
                        )
                    )

                    record_containers.append(record_container)

                return Row(controls=record_containers)

            else:
                return Container()

        sidebar = Container(
            padding=10,
            width=200,
            height=700,
            bgcolor=colors.WHITE,
            content=Column(
                controls=[
                    Container(
                        padding=padding.only(top=60, left=10),
                        content=Column(
                            controls=[
                                Row(
                                    controls=[
                                        Image(
                                            src="pic/avatar.png",
                                            width=50,
                                            height=50
                                        ),

                                        Column(
                                            controls=[
                                                Container(
                                                    padding=padding.only(top=5, bottom=-5),
                                                    content=Text(
                                                        value=username,
                                                        size=14,
                                                        font_family="RobotoSlab",
                                                        color=colors.BLACK
                                                    )
                                                ),
                                                Row(
                                                    controls=[
                                                        Icon(
                                                            icons.PHONE,
                                                            color=colors.BLACK,
                                                            size=10
                                                        ),
                                                        Container(
                                                            padding=padding.only(left=-8),
                                                            content=Text(
                                                                value=phoneNumber,
                                                                size=10,
                                                                font_family="RobotoSlab",
                                                                color=colors.BLACK
                                                            )
                                                        )

                                                    ]
                                                )

                                            ]
                                        ),
                                    ]
                                ),

                                Container(
                                    padding=padding.only(top=40, left=10, right=10),
                                    content=Column(
                                        controls=[
                                            Row(
                                                alignment="SpaceBetween",
                                                controls=[
                                                    Row(
                                                        controls=[
                                                            Image(
                                                                src="pic/medicalRecord.png",
                                                                width=20,
                                                                height=20
                                                            ),

                                                            Text(
                                                                value="Medical Record",
                                                                size=12,
                                                                color=colors.BLACK,
                                                                font_family="RobotoSlab"
                                                            )
                                                        ]
                                                    ),

                                                    Container(

                                                        content=Icon(
                                                            icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                                                            size=14,
                                                            color=grey
                                                        ),
                                                        on_click=lambda _: page.go(f"/medicalRecord/{user_id}")
                                                    )
                                                ]
                                            )

                                        ]
                                    )
                                ),

                                Container(
                                    padding=padding.only(top=20, left=10, right=10),
                                    content=Column(
                                        controls=[
                                            Row(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    Row(
                                                        controls=[
                                                            Icon(
                                                                icons.SETTINGS,
                                                                size=20,
                                                                color=grey
                                                            ),

                                                            Text(
                                                                value="Settings",
                                                                size=12,
                                                                color=colors.BLACK,
                                                                text_align=TextAlign.LEFT,
                                                                font_family="RobotoSlab",
                                                            )
                                                        ]
                                                    ),

                                                    Container(
                                                        content=Icon(
                                                            icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                                                            size=14,
                                                            color=grey
                                                        ),
                                                        on_click=lambda _: page.go(f"/setting/{user_id}")
                                                    )
                                                ]
                                            )

                                        ]
                                    )
                                ),

                                Container(
                                    padding=padding.only(top=20, left=10, right=10),
                                    content=Column(
                                        controls=[
                                            Row(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    Row(
                                                        controls=[
                                                            Icon(
                                                                icons.LOGOUT,
                                                                size=20,
                                                                color=grey
                                                            ),

                                                            Text(
                                                                value="Log Out",
                                                                size=12,
                                                                color=colors.BLACK,
                                                                text_align=TextAlign.LEFT,
                                                                font_family="RobotoSlab",
                                                            )
                                                        ]
                                                    ),

                                                    Container(
                                                        content=Icon(
                                                            icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                                                            size=14,
                                                            color=grey,
                                                        ),
                                                        on_click=lambda _: page.go("/")
                                                    )
                                                ]
                                            )

                                        ]
                                    )
                                ),

                            ]
                        )
                    )
                ]
            ),
            offset=transform.Offset(-5, 0),
            animate_offset=animation.Animation(400)
        )

        nav = Container(
            width=350,
            height=50,
            content=Column(
                controls=[
                    Container(
                        padding=padding.only(top=-15, bottom=-20),
                        content=Divider(
                            thickness=1,
                            color="#DFDFDF"
                        )
                    ),

                    Container(
                        padding=padding.only(top=-5),
                        content=Row(
                            alignment=MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                IconButton(icon=icons.HOME,
                                           icon_size=20,
                                           icon_color="#858EA9"),
                                IconButton(icon=icons.CHAT_ROUNDED,
                                           icon_size=20,
                                           icon_color="#858EA9",
                                           on_click=lambda _: page.go(f"/patientChatViewDoctor/{user_id}")),
                                IconButton(icon=icons.CALENDAR_MONTH,
                                           icon_size=20,
                                           icon_color="#858EA9",
                                           on_click=lambda _: page.go(f"/booking/{user_id}")),
                                IconButton(icon=icons.PERSON,
                                           icon_size=20,
                                           icon_color="#858EA9",
                                           on_click=lambda _: page.go(f"/profile/{user_id}"))
                            ]
                        )
                    )

                ]
            )
        )

        mainPageContent = Row(
            controls=[
                Container(
                    on_click=hide_side_bar,
                    content=Column(
                        controls=[
                            Row(
                                controls=[
                                    Container(width=350,
                                              height=70,
                                              bgcolor=blue,
                                              alignment=alignment.top_center,
                                              content=Row(
                                                  width=340,
                                                  alignment="spaceBetween",
                                                  controls=[
                                                      Container(padding=padding.only(
                                                          top=25),
                                                          content=IconButton(
                                                              icons.MENU,
                                                              icon_color=colors.WHITE,
                                                              on_click=show_side_bar
                                                          ),
                                                      ),

                                                      Container(padding=padding.only(top=25),
                                                                content=Text(
                                                                    value="Call A Doctor",
                                                                    size=20,
                                                                    font_family="RobotoSlab",
                                                                    color=colors.WHITE,
                                                                    text_align=TextAlign.CENTER)
                                                                ),

                                                      Container(
                                                          padding=padding.only(top=25, right=10),
                                                          content=Image(src=notification_icon,
                                                                        width=22,
                                                                        height=22),
                                                          on_click=lambda _: page.go(f"/patientNotification/{user_id}")
                                                      ),
                                                  ]
                                              ))
                                ]
                            ),

                            Container(
                                padding=padding.only(top=15, bottom=10),
                                content=Row(
                                    controls=[
                                        Container(padding=padding.only(left=8),
                                                  content=Image(src="pic/clinicButton.png",
                                                                width=75,
                                                                height=75),
                                                  on_click=lambda _: page.go(f"/clinic/{user_id}"),
                                                  ),

                                        Container(
                                            content=Image(src="pic/doctorButton.png",
                                                          width=75,
                                                          height=75),
                                            on_click=lambda _: page.go(f"/doctor/{user_id}")
                                        ),

                                        Container(
                                            content=Image(src="pic/prescriptionButton.png",
                                                          width=75,
                                                          height=75),
                                            on_click=lambda _: page.go(f"/patientPrescription/{user_id}")
                                        ),

                                        Container(
                                            content=Image(src="pic/healthTipsButton.png",
                                                          width=75,
                                                          height=75),
                                            on_click=lambda _: page.go(f"/healthTips/{user_id}")
                                        ),
                                    ]
                                )
                            ),

                            Row(
                                controls=[
                                    Container(
                                        padding=padding.only(left=16, right=135),
                                        content=Text(value="Popular Clinic",
                                                     font_family="RobotoSlab",
                                                     size=16,
                                                     color=colors.BLACK)

                                    ),

                                    Container(padding=padding.only(right=5, top=10),
                                              content=TextButton(content=Text("See all >",
                                                                              size=10,
                                                                              italic=True,
                                                                              font_family="RobotoSlab",
                                                                              color=blue)),
                                              on_click=lambda _: page.go(f"/clinic/{user_id}")

                                              ),
                                ]
                            ),

                            displayRecord(clinic),

                            Row(
                                controls=[
                                    Container(
                                        padding=padding.only(left=16, right=130),
                                        content=Text(value="Popular Doctor",
                                                     font_family="RobotoSlab",
                                                     size=16,
                                                     color=colors.BLACK)

                                    ),

                                    Container(padding=padding.only(right=10, top=10),
                                              content=TextButton(content=Text("See all >",
                                                                              size=10,
                                                                              italic=True,
                                                                              font_family="RobotoSlab",
                                                                              color=blue)),
                                              on_click=lambda _: page.go(f"/doctor/{user_id}")
                                              ),
                                ]
                            ),

                            Container(
                                padding=padding.only(left=13, right=10),
                                content=displayDoctorRecord(doctor)
                            ),

                            nav
                        ]
                    )
                )
            ]
        )

        return View(
            "/homepage/:user_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Stack(
                              controls=[
                                  mainPageContent,
                                  sidebar
                              ]
                          )
                          )
            ]
        )
