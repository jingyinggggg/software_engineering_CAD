import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)

class ClinicHomepage:

    def __init__(self):
        self.show_sidebar = False

    def view (self, page: Page, params: Params, basket: Basket):

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

        light_blue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        def show_side_bar(e):
            sidebar.offset = transform.Offset(0, 0)
            page.update()

        def hide_side_bar(e):
            sidebar.offset = transform.Offset(-5, 0)
            page.update()

        def get_clinic_details():
            c = db.cursor()
            c.execute("SELECT name, phoneNumber FROM clinic WHERE id = ?",(user_id,))
            record = c.fetchall()

            clinicName = record[0][0]
            phoneNumber = record[0][1]

            return clinicName, phoneNumber

        clinicName, phoneNumber = get_clinic_details()

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
                                                        value=clinicName,
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
                                                        # on_click=lambda _: page.go(f"/medicalRecord/{user_id}")
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
                                                            Image(
                                                                src="pic/booking.png",
                                                                width=20,
                                                                height=20
                                                            ),

                                                            Text(
                                                                value="Bookings",
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
                                                        )
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
                                                            Image(
                                                                src="pic/myDoctors.png",
                                                                width=20,
                                                                height=20
                                                            ),

                                                            Text(
                                                                value="My Doctors",
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
                                                        )
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
                                                        )
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

        body_content = Row(
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
                                                  controls=[
                                                      Container(padding=padding.only(left=10,
                                                                                     top=25),
                                                                    content=IconButton(
                                                                        icons.MENU,
                                                                        icon_color=colors.WHITE,
                                                                        on_click=show_side_bar
                                                                    ),
                                                                ),

                                                      Container(padding=padding.only(left=65,
                                                                                     top=25),
                                                                content=Text(
                                                                    value="Clinic Homepage",
                                                                    size=20,
                                                                    font_family="RobotoSlab",
                                                                    color=colors.WHITE,
                                                                    text_align=TextAlign.CENTER)
                                                                ),
                                                  ]
                                              ))
                                ]
                            ),
                        ]
                    )
                )
            ]
        )

        return View(
            "/clinicHomepage/:user_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          content=Stack(
                              controls=[
                                  body_content,
                                  #sidebar
                              ]
                          )
                          )
            ]
        )