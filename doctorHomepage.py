from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class DoctorHomepage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        print(user_id)
        # prescription_id = int(params.prescription_id)
        # booking_id = int(params.booking_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        # Define a function to show the sidebar
        def show_side_bar(e):
            sidebar.offset = transform.Offset(0, 0)
            page.update()

        # Define a function to hide the sidebar
        def hide_side_bar(e):
            sidebar.offset = transform.Offset(-205, 0)
            page.update()

        for x in range(len(page.views)):
            if x > 3:
                page.views.pop()

        def get_patient():
            c = db.cursor()
            c.execute("SELECT bookingID, users.id, users.fullName FROM booking INNER JOIN users ON booking.patientID "
                      "= users.id WHERE doctorID = ? ", (user_id,))
            record = c.fetchall()

            return record

        record = get_patient()

        def get_doctor_details():
            c = db.cursor()
            c.execute("SELECT * FROM doctors WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]
            username = record[0][2]
            phoneNumber = record[0][4]
            image = record[0][12]
            # booking_id = record[0][15]

            return fullName, username, phoneNumber, image
            # return fullName, username, phoneNumber, image, booking_id

        fullName, username, phoneNumber, image = get_doctor_details()

        # Sidebar
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
                                    padding=padding.only(top=20, left=10, right=10),
                                    content=Column(
                                        controls=[
                                            Row(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    Row(
                                                        controls=[
                                                            Icon(
                                                                icons.PERSON,
                                                                size=20,
                                                                color=grey
                                                            ),

                                                            Text(
                                                                value="Profile",
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

                                                        ), on_click=lambda _: page.go(f"/doctorProfile/{user_id}")
                                                    ),
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

                                                        ), on_click=lambda _: page.go(f"/doctorSettingPage/{user_id}")
                                                    ),
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

        # phone container
        return View(
            "/login/homepage/:user_id",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Stack(
                        # scroll=True,
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
                                                                                         f"/doctorNotification/{user_id}"))])]),

                                                    Text(value="Welcome !",
                                                         size=30,
                                                         font_family="RobotoSlab",
                                                         weight=FontWeight.BOLD,
                                                         color="WHITE"),

                                                    Text(value=f"Dr. {fullName}",
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
                                                                    src=f"{image}",
                                                                    width=280,
                                                                    height=280
                                                                )
                                                            ])),

                                                    Container(bgcolor="WHITE",
                                                              padding=padding.only(top=20, left=10),
                                                              alignment=alignment.top_left,
                                                              # width=800,
                                                              # height=320,
                                                              margin=margin.only(top=-100, left=-10, right=-10),
                                                              border_radius=30,
                                                              content=Column(
                                                                  controls=[Text("Our Services",
                                                                                 text_align=TextAlign.CENTER,
                                                                                 size=16,
                                                                                 weight=FontWeight.BOLD,
                                                                                 color="BLACK"),
                                                                            ])

                                                              ),

                                                ])
                                        ),
                                        Container(
                                            alignment=alignment.top_left,
                                            margin=margin.only(top=30, left=30, right=10),
                                            content=Row(
                                                controls=[
                                                    Container(
                                                        padding=padding.only(top=20),
                                                        alignment=alignment.center,
                                                        height=120,
                                                        width=120,
                                                        content=Column(
                                                            controls=[
                                                                Container(
                                                                    Image(
                                                                        src="pic/icons8-history-80.png",
                                                                        width=50,
                                                                    )
                                                                ),
                                                                Container(
                                                                    Text(
                                                                        "History",
                                                                        size=14,
                                                                        color="BLACK",
                                                                        weight=FontWeight.W_500
                                                                    )

                                                                )
                                                            ]
                                                        ),
                                                        border=border.all(width=2, color="BLACK"),
                                                        border_radius=10,
                                                        on_click=lambda _: page.go(f"/history/{user_id}")
                                                    ),

                                                    Container(
                                                        margin=margin.only(left=30, right=10),
                                                        content=Row(
                                                            controls=[
                                                                Container(
                                                                    padding=padding.only(top=20),
                                                                    alignment=alignment.center,
                                                                    height=120,
                                                                    width=120,
                                                                    content=Column(
                                                                        controls=[
                                                                            Container(
                                                                                alignment=alignment.center,
                                                                                content=Image(
                                                                                    src="pic/icons8-appointment-64.png",
                                                                                    width=50,
                                                                                )
                                                                            ),
                                                                            Container(
                                                                                alignment=alignment.center,
                                                                                content=Text(
                                                                                    "Appointment",
                                                                                    size=14,
                                                                                    color="BLACK",
                                                                                    weight=FontWeight.W_500
                                                                                )

                                                                            )
                                                                        ]
                                                                    ),
                                                                    border=border.all(width=2, color="BLACK"),
                                                                    border_radius=10,
                                                                    on_click=lambda _: page.go(
                                                                        f"/appointment/{user_id}")

                                                                )
                                                            ]
                                                        )
                                                    ),


                                                    # Container(
                                                    #     margin=margin.only(left=30),
                                                    #     padding=padding.only(top=20),
                                                    #     alignment=alignment.center,
                                                    #     height=120,
                                                    #     width=120,
                                                    #     content=Column(
                                                    #         controls=[
                                                    #             Container(
                                                    #                 alignment=alignment.center,
                                                    #                 content=Image(
                                                    #                     src="pic/icons8-schedule-100.png",
                                                    #                     width=50,
                                                    #                 )
                                                    #             ),
                                                    #             Container(
                                                    #                 alignment=alignment.center,
                                                    #                 content=Text(
                                                    #                     "Schedule",
                                                    #                     size=14,
                                                    #                     color="BLACK",
                                                    #                     weight=FontWeight.W_500
                                                    #                 )
                                                    #
                                                    #             )
                                                    #         ]
                                                    #     ),
                                                    #     border=border.all(width=2, color="BLACK"),
                                                    #     border_radius=10,
                                                    #     on_click=lambda _: page.go(f"/schedule/{user_id}")
                                                    #
                                                    # )

                                                ])),
                                        Container(
                                            margin=margin.only(top=10, left=30, right=10),
                                            content=Row(
                                                controls=[
                                                    Container(
                                                        padding=padding.only(top=20),
                                                        alignment=alignment.center,
                                                        height=120,
                                                        width=120,
                                                        content=Column(
                                                            controls=[
                                                                Container(
                                                                    alignment=alignment.center,
                                                                    content=Image(
                                                                        src="pic/icons8-chat-64.png",
                                                                        width=50,
                                                                    )
                                                                ),
                                                                Container(
                                                                    alignment=alignment.center,
                                                                    content=Text(
                                                                        "Chat",
                                                                        size=14,
                                                                        color="BLACK",
                                                                        weight=FontWeight.W_500
                                                                    )

                                                                )
                                                            ]
                                                        ),
                                                        border=border.all(width=2, color="BLACK"),
                                                        border_radius=10,
                                                        on_click=lambda _: page.go(f"/chat/{user_id}{record[0][1]}")

                                                    ),

                                                    Container(
                                                        margin=margin.only(left=30),
                                                        padding=padding.only(top=20),
                                                        alignment=alignment.center,
                                                        height=120,
                                                        width=120,
                                                        content=Column(
                                                            controls=[
                                                                Container(
                                                                    alignment=alignment.center,
                                                                    content=Image(
                                                                        src="pic/icons8-prescription-100.png",
                                                                        width=50,
                                                                    )
                                                                ),
                                                                Container(
                                                                    alignment=alignment.center,
                                                                    content=Text(
                                                                        "Prescription",
                                                                        size=14,
                                                                        color="BLACK",
                                                                        weight=FontWeight.W_500
                                                                    )

                                                                )
                                                            ]
                                                        ),
                                                        border=border.all(width=2, color="BLACK"),
                                                        border_radius=10,
                                                        on_click=lambda _: page.go(f"/prescriptionList/{user_id}")

                                                    )

                                                ])),
                                        Container(
                                            margin=margin.only(top=10, left=30, right=10),
                                            content=Row(
                                                controls=[
                                                    Container(
                                                        padding=padding.only(top=20),
                                                        alignment=alignment.center,
                                                        height=120,
                                                        width=120,
                                                        content=Column(
                                                            controls=[
                                                                Container(
                                                                    alignment=alignment.center,
                                                                    content=Image(
                                                                        src="pic/icons8-proof-60.png",
                                                                        width=50,
                                                                    )
                                                                ),
                                                                Container(
                                                                    alignment=alignment.center,
                                                                    content=Text(
                                                                        "Proof Status",
                                                                        size=14,
                                                                        color="BLACK",
                                                                        weight=FontWeight.W_500
                                                                    )

                                                                )
                                                            ]
                                                        ),
                                                        border=border.all(width=2, color="BLACK"),
                                                        border_radius=10,
                                                        on_click=lambda _: page.go(f"/proofStatus/{user_id}")

                                                    )]))
                                    ]
                                )
                            ), sidebar
                        ]
                    )
                )])
