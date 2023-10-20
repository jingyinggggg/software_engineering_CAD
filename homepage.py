import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

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

        def show_side_bar(e):
            sidebar.offset = transform.Offset(0, 0)
            page.update()

        def hide_side_bar(e):
            sidebar.offset = transform.Offset(-5, 0)
            page.update()

        def get_user_details():
            c = db.cursor()
            c.execute("SELECT username, phoneNumber FROM users WHERE id = ?", (user_id,))
            record = c.fetchall()

            username = record[0][0]
            phoneNumber = record[0][1]

            return username, phoneNumber

        username, phoneNumber = get_user_details()

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
                                           icon_color="#858EA9"),
                                IconButton(icon=icons.NOTIFICATIONS,
                                           icon_size=20,
                                           icon_color="#858EA9"),
                                IconButton(icon=icons.PERSON,
                                           icon_size=20,
                                           icon_color="#858EA9",
                                           on_click=lambda _:page.go(f"/profile/{user_id}"))
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
                                                                    value="Call A Doctor",
                                                                    size=20,
                                                                    font_family="RobotoSlab",
                                                                    color=colors.WHITE,
                                                                    text_align=TextAlign.CENTER)
                                                                ),
                                                  ]
                                              ))
                                ]
                            ),

                            # Container(
                            #     padding=padding.only(left=10, right=10, top=10, bottom=5),
                            #     content=Row(
                            #         controls=[
                            #             TextField(
                            #                 bgcolor=lightBlue,
                            #                 height=40,
                            #                 width=300,
                            #                 border_color=blue,
                            #                 label="Search",
                            #                 label_style=TextStyle(color=colors.BLACK,
                            #                                       size=14,
                            #                                       italic=True,
                            #                                       weight=FontWeight.W_400),
                            #                 text_style=TextStyle(color=colors.BLACK,
                            #                                      size=12,
                            #                                      weight=FontWeight.W_400)
                            #             ),
                            #
                            #             Icon(icons.SEARCH,
                            #                  color=blue,
                            #                  size=20)
                            #
                            #         ]
                            #     )
                            # ),

                            Container(
                                padding=padding.only(top=15, bottom=10),
                                content=Row(
                                    controls=[
                                        Container(padding=padding.only(left=8),
                                                  content=Image(src="pic/clinicButton.png",
                                                                width=75,
                                                                height=75)
                                                  ),

                                        Container(
                                            content=Image(src="pic/doctorButton.png",
                                                          width=75,
                                                          height=75)
                                        ),

                                        Container(
                                            content=Image(src="pic/prescriptionButton.png",
                                                          width=75,
                                                          height=75)
                                        ),

                                        Container(
                                            content=Image(src="pic/healthTipsButton.png",
                                                          width=75,
                                                          height=75)
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
                                                                              color=blue))

                                              ),
                                ]
                            ),

                            Container(
                                padding=padding.only(left=15),
                                content=Container(
                                    bgcolor=lightBlue,
                                    width=315,
                                    height=55,
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
                                                        content=Text(value="Bwell Clinic",
                                                                     size=12,
                                                                     color=colors.BLACK,
                                                                     font_family="RobotoSlab",
                                                                     weight=FontWeight.W_500
                                                                     )
                                                    ),

                                                    Container(padding=padding.only(top=-5),
                                                              content=Text(
                                                                  value="1-G-16, Imperial Grande, Persiaran Relau, Sungai Ara, 11900\nBayan Lepas, Pulau Pinang",
                                                                  size=8,
                                                                  color=colors.BLACK,
                                                                  font_family="RobotoSlab")
                                                              )

                                                ]
                                            )

                                        ]
                                    )
                                ),

                            ),

                            Container(
                                padding=padding.only(left=15, top=5, bottom=15),
                                content=Container(
                                    bgcolor=lightBlue,
                                    width=315,
                                    height=55,
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
                                                        content=Text(value="Dr Ng Clinic",
                                                                     size=12,
                                                                     color=colors.BLACK,
                                                                     font_family="RobotoSlab",
                                                                     weight=FontWeight.W_500
                                                                     )
                                                    ),

                                                    Container(padding=padding.only(top=-5),
                                                              content=Text(
                                                                  value="29-1-32, GOLDEN TRIANGLE, Jln Paya Terubung, Sungai Ara,\n11900 Bayan Lepas, Pulau Pinang",
                                                                  size=8,
                                                                  color=colors.BLACK,
                                                                  font_family="RobotoSlab")
                                                              )

                                                ]
                                            )

                                        ]
                                    )
                                ),

                            ),

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
                                                                              color=blue))

                                              ),
                                ]
                            ),

                            Container(
                                padding=padding.only(left=13, right=10),
                                content=Row(
                                    controls=[
                                        Container(
                                            bgcolor=lightBlue,
                                            width=155,
                                            height=195,
                                            border_radius=7,
                                            content=Column(
                                                horizontal_alignment="center",
                                                controls=[
                                                    Container(padding=padding.only(top=-10),
                                                              content=Image(
                                                                  src="pic/doctor1.png",
                                                                  width=155,
                                                                  height=160,
                                                                  fit=ImageFit,

                                                              )
                                                              ),

                                                    Container(padding=padding.only(top=-13),
                                                              content=Text(value="Dr. Jenny",
                                                                           size=13,
                                                                           color=colors.BLACK,
                                                                           text_align=TextAlign.CENTER,
                                                                           font_family="RobotoSlab",
                                                                           weight=FontWeight.W_500)
                                                              ),

                                                    Container(padding=padding.only(top=-10),
                                                              content=Text(
                                                                  value="Radiologists",
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
                                        ),

                                        Container(
                                            bgcolor=lightBlue,
                                            width=155,
                                            height=195,
                                            border_radius=7,
                                            content=Column(
                                                horizontal_alignment="center",
                                                controls=[
                                                    Container(
                                                        padding=padding.only(top=-10),
                                                        content=Image(
                                                            src="pic/doctor2.png",
                                                            width=155,
                                                            height=160,
                                                            fit=ImageFit,

                                                        )
                                                    ),

                                                    Container(
                                                        padding=padding.only(top=-13),
                                                        content=Text(value="Dr. Johnson",
                                                                     size=13,
                                                                     color=colors.BLACK,
                                                                     text_align=TextAlign.CENTER,
                                                                     font_family="RobotoSlab",
                                                                     weight=FontWeight.W_500)
                                                    ),

                                                    Container(
                                                        padding=padding.only(top=-10),
                                                        content=Text(
                                                            value="Cardiologists",
                                                            size=8,
                                                            color=colors.BLACK,
                                                            text_align=TextAlign.CENTER,
                                                            font_family="RobotoSlab",
                                                            weight=FontWeight.W_500)
                                                    ),

                                                    Container(
                                                        padding=padding.only(top=-12),
                                                        content=Image(
                                                            src="pic/star.png",
                                                            width=60,
                                                            height=20)
                                                    )

                                                ]
                                            )
                                        ),

                                    ]
                                )

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

