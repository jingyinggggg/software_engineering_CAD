from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class DoctorHomepage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        # user_id = int(params.user_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        grey = "#71839B"

        # def get_doctor_details():
        #     c = db.cursor()
        #     c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        #     record = c.fetchall()
        #
        #     fullName = record[0][1]
        #     username = record[0][2]
        #
        #     return fullName, username
        # fullName, username = get_doctor_details()

        def show_side_bar(e):
            sidebar.offset = transform.Offset(0, 0)
            page.update()

        def hide_side_bar(e):
                sidebar.offset = transform.Offset(-5, 0)
                page.update()

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
                                    # Row(
                                    #     controls=[
                                    #         Image(
                                    #             src="pic/avatar.png",
                                    #             width=50,
                                    #             height=50
                                    #         ),
                                    #
                                    #         Column(
                                    #             controls=[
                                    #                 Container(
                                    #                     padding=padding.only(top=5, bottom=-5),
                                    #                     content=Text(
                                    #                         value=username,
                                    #                         size=14,
                                    #                         font_family="RobotoSlab",
                                    #                         color=colors.BLACK
                                    #                     )
                                    #                 ),
                                    #                 Row(
                                    #                     controls=[
                                    #                         Icon(
                                    #                             icons.PHONE,
                                    #                             color=colors.BLACK,
                                    #                             size=10
                                    #                         ),
                                    #                         Container(
                                    #                             padding=padding.only(left=-8),
                                    #                             content=Text(
                                    #                                 value=phoneNumber,
                                    #                                 size=10,
                                    #                                 font_family="RobotoSlab",
                                    #                                 color=colors.BLACK
                                    #                             )
                                    #                         )
                                    #
                                    #                     ]
                                    #                 )
                                    #
                                    #             ]
                                    #         ),
                                    #     ]
                                    # ),

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
            margin=margin.only(top=20),
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
                                IconButton(icon=icons.PERSON,
                                           icon_size=20,
                                           icon_color="#858EA9",
                                           # on_click=lambda _: page.go(f"/profile/{user_id}")
                                           )
                            ]
                        )
                    )

                ]
            )
        )

        # phone container
        return View(
            "/login/homepage",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,

                    content=Stack(
                        # horizontal_alignment=CrossAxisAlignment.START,
                        controls=[
                            Container(
                                on_click=hide_side_bar,
                                content=Column(
                                    controls=[
                                        Container(
                                            width=350,
                                            height=250,
                                            bgcolor="#3386C5",
                                            padding=padding.symmetric(horizontal=10, vertical=20),

                                            content=Column(
                                                controls=[
                                                    Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                        controls=[
                                                            Container(
                                                                content=IconButton(icons.MENU,
                                                                                   icon_color="WHITE",
                                                                                   on_click=show_side_bar)),
                                                            Row(controls=[IconButton(icons.CIRCLE_NOTIFICATIONS_ROUNDED,
                                                                                     icon_color="WHITE",
                                                                                     on_click=lambda _: page.go(
                                                                                         f"/notification"))])]),

                                                    Text(value="Welcome !",
                                                         size=30,
                                                         font_family="RobotoSlab",
                                                         weight=FontWeight.BOLD,
                                                         color="WHITE"),

                                                    Text(value="Dr.",
                                                         size=30,
                                                         font_family="RobotoSlab",
                                                         weight=FontWeight.BOLD,
                                                         color="WHITE"),

                                                    Container(
                                                        padding=padding.only(left=100, top=-140),

                                                        content=Row(
                                                            # horizontal_alignment="top_left",
                                                            controls=[
                                                                Image(
                                                                    src="pic/doctor.png",
                                                                    width=280,
                                                                    height=280
                                                                )
                                                            ])),

                                                    Container(bgcolor="WHITE",
                                                              padding=padding.only(top=10, left=10),
                                                              alignment=alignment.top_left,
                                                              width=800,
                                                              height=800,
                                                              margin=margin.only(top=-100, left=-10, right=-10),
                                                              border_radius=30,
                                                              content=Column(
                                                                  controls=[Text("Our Services",
                                                                                 text_align=TextAlign.CENTER,
                                                                                 size=16,
                                                                                 font_family="RobotoSlab",
                                                                                 weight=FontWeight.W_500,
                                                                                 color="BLACK"),
                                                                            ])

                                                              ),

                                                ])),
                                        Container(
                                            alignment=alignment.center,
                                            margin=margin.only(top=10),
                                            content=Row(
                                                alignment=MainAxisAlignment.SPACE_EVENLY,
                                                controls=[
                                                    Container(
                                                        content=IconButton(
                                                            icons.HISTORY,
                                                            icon_color="#3D3F99",
                                                            icon_size=45,
                                                            tooltip="view history",
                                                            on_click=lambda _: page.go(f"/history")
                                                        ),
                                                        border_radius=50,
                                                        border=border.all(1, "#000000"),
                                                        height=60,
                                                        width=60,

                                                    ),

                                                    Container(
                                                        content=IconButton(
                                                            icons.DATE_RANGE_ROUNDED,
                                                            icon_color="#3D3F99",
                                                            icon_size=45,
                                                            tooltip="view schedule",
                                                            on_click=lambda _: page.go(f"/schedule")
                                                        ),
                                                        border_radius=50,
                                                        border=border.all(1, "#000000"),
                                                        height=60,
                                                        width=60
                                                        # Add border here
                                                    ),
                                                    Container(
                                                        content=IconButton(
                                                            icons.WECHAT,
                                                            icon_color="#3D3F99",
                                                            icon_size=45,
                                                            tooltip="view chat",
                                                            on_click=lambda _: page.go(f"/chat")
                                                        ),
                                                        border_radius=50,
                                                        border=border.all(1, "#000000"),
                                                        height=60,
                                                        width=60
                                                        # Add border here
                                                    )
                                                ]
                                            )
                                        ),
                                        Container(alignment=alignment.center,
                                                  content=Row(alignment=MainAxisAlignment.SPACE_EVENLY,
                                                              controls=[Container(
                                                                  content=Text("History",
                                                                               font_family="RobotoSlab",
                                                                               size=14,
                                                                               color="BLACK"),
                                                              ),
                                                                  Text("Schedule",
                                                                       font_family="RobotoSlab",
                                                                       size=14,
                                                                       color="BLACK"),
                                                                  Text("Chat",
                                                                       font_family="RobotoSlab",
                                                                       size=14,
                                                                       color="BLACK")])),

                                        Container(alignment=alignment.center,
                                                  padding=padding.only(left=10, top=30, right=10),
                                                  content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                              controls=[Container(
                                                                  content=Text("Appointment",
                                                                               font_family="RobotoSlab",
                                                                               color="BLACK",
                                                                               size=16,
                                                                               weight=FontWeight.W_500)),
                                                                  Text(disabled=False,
                                                                       spans=[TextSpan(
                                                                           "see more",
                                                                           TextStyle(
                                                                               decoration=TextDecoration.UNDERLINE,
                                                                               color="#3386C5"),
                                                                           on_click=lambda _: page.go(f"/schedule"))])

                                                              ])),

                                        Container(alignment=alignment.center,
                                                  border_radius=8,
                                                  padding=padding.only(left=10),
                                                  margin=margin.only(left=10),
                                                  border=border.all(color="BLACK"),
                                                  width=320,
                                                  height=180,
                                                  content=Column(controls=
                                                                 [Row(alignment=MainAxisAlignment.START,
                                                                      controls=[Container(
                                                                          alignment=alignment.top_left,
                                                                          margin=margin.only(top=10),
                                                                          content=
                                                                          Text("Appointment Date & Time",
                                                                               font_family="RobotoSlab",
                                                                               size=14,
                                                                               color="#979797"))]
                                                                      ),
                                                                  Container(content=Row(alignment=alignment.center,
                                                                                        controls=[Container(
                                                                                            Icon(
                                                                                                icons.WATCH_LATER_OUTLINED,
                                                                                                color="BLACK"), ),
                                                                                            Text(
                                                                                                "Tue Oct 02 | 09:00AM - 10.00 AM",
                                                                                                weight=FontWeight.W_500,
                                                                                                size=12,
                                                                                                color="BLACK")])),

                                                                  Container(
                                                                      content=Row(alignment=alignment.center,
                                                                                  controls=[Container(
                                                                                      Image(src="pic/patient.png",
                                                                                            border_radius=20,
                                                                                            width=65,
                                                                                            height=65), ),
                                                                                      Text("Melody Wong Yi Yi",
                                                                                           weight=FontWeight.W_500,
                                                                                           size=14,
                                                                                           color="BLACK"),
                                                                                  ])),
                                                                  Container(margin=margin.only(left=75, top=-35),
                                                                            content=Column(alignment=alignment.center,
                                                                                           controls=[Container(
                                                                                               Text("Consultation",
                                                                                                    color="#979797"))])),

                                                                  Container(margin=margin.only(left=200, top=-20),
                                                                            content=Column(alignment=alignment.center,
                                                                                           controls=[Container(
                                                                                               FilledButton("more...",
                                                                                                            on_click=lambda
                                                                                                                _: page.go(
                                                                                                                f"/appointmentDetail"))

                                                                                           )]))

                                                                  ])),

                                        nav,
                                    ]
                                )
                            ),

                            sidebar


                            # ResponsiveRow([Container(Text())])
                        ]))])