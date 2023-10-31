from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class AdminHomepage:
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

        return View(
            "/login/adminHomepage",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    bgcolor="#F4F4F4",
                    border_radius=30,
                    content=Column(
                        controls=[
                            Container(
                                padding=padding.only(top=25, left=10),
                                content=Column(
                                    controls=[
                                        Text(
                                            value="Welcome",
                                            color="#848484",
                                            weight=FontWeight.W_600,
                                            size=15,
                                        ),
                                        Text(
                                            value="Bwell Clinic admin",
                                            color="#3386C5",
                                            weight=FontWeight.W_600,
                                            size=18,
                                        )
                                    ]
                                ),
                            ),
                            Container(
                                padding=padding.only(top=10),
                                width=350,
                                border_radius=15,
                                content=Row(
                                    controls=[
                                        Container(
                                            width=165,
                                            height=135,
                                            alignment=alignment.center,
                                            content=Column([
                                                Container(
                                                    width=135,
                                                    height=135,
                                                    border_radius=15,
                                                    border=border.all(color="#D3D3D3", width=2),
                                                    bgcolor=colors.WHITE,
                                                    alignment=alignment.center,
                                                    content=Column([
                                                        Container(
                                                            padding=padding.only(top=20),
                                                            width=165,
                                                            height=90,
                                                            content=Image(
                                                                src="pic/patientRequest.png", ),

                                                        ),
                                                        Container(
                                                            alignment=alignment.top_center,
                                                            width=165,
                                                            height=50,
                                                            content=Text(
                                                                font_family="RobotoSlab",
                                                                value="View Patient Request",
                                                                color=colors.BLACK,
                                                                size=10,
                                                                weight=FontWeight.BOLD,
                                                            )
                                                        )
                                                    ])
                                                )
                                            ])
                                        ),
                                        Container(
                                            width=165,
                                            height=135,
                                            alignment=alignment.center,
                                            content=Column([
                                                Container(
                                                    width=135,
                                                    height=135,
                                                    border_radius=15,
                                                    border=border.all(color="#D3D3D3", width=2),
                                                    bgcolor=colors.WHITE,
                                                    alignment=alignment.center,
                                                    content=Column([
                                                        Container(
                                                            padding=padding.only(top=20),
                                                            width=165,
                                                            height=90,
                                                            content=Image(
                                                                src="pic/appointmentList.png", ),

                                                        ),
                                                        Container(
                                                            alignment=alignment.top_center,
                                                            width=165,
                                                            height=40,
                                                            content=Text(
                                                                value="Patient Appointment List",
                                                                font_family="RobotoSlab",
                                                                color=colors.BLACK,
                                                                size=10,
                                                                weight=FontWeight.BOLD,
                                                            )
                                                        )
                                                    ])
                                                )
                                            ])
                                        ),
                                    ]
                                )
                            ),
                            Container(
                                padding=padding.only(top=10),
                                width=350,
                                border_radius=15,
                                content=Row(
                                    controls=[
                                        Container(
                                            width=165,
                                            height=135,
                                            alignment=alignment.center,
                                            content=Column([
                                                Container(
                                                    width=135,
                                                    height=135,
                                                    border_radius=15,
                                                    border=border.all(color="#D3D3D3", width=2),
                                                    bgcolor=colors.WHITE,
                                                    alignment=alignment.center,
                                                    content=Column([
                                                        Container(
                                                            padding=padding.only(top=20),
                                                            width=165,
                                                            height=90,
                                                            content=Image(
                                                                src="pic/doctorManage.png"),

                                                        ),
                                                        Container(
                                                            alignment=alignment.top_center,
                                                            width=165,
                                                            height=50,
                                                            content=Text(
                                                                font_family="RobotoSlab",
                                                                value="Manage Doctor",
                                                                color=colors.BLACK,
                                                                size=10,
                                                                weight=FontWeight.BOLD,
                                                            )
                                                        )
                                                    ])
                                                )
                                            ])
                                        ),
                                        Container(
                                            width=165,
                                            height=135,
                                            alignment=alignment.center,
                                            content=Column([
                                                Container(
                                                    width=135,
                                                    height=135,
                                                    border_radius=15,
                                                    border=border.all(color="#D3D3D3", width=2),
                                                    bgcolor=colors.WHITE,
                                                    alignment=alignment.center,
                                                    content=Column([
                                                        Container(
                                                            padding=padding.only(top=20),
                                                            width=165,
                                                            height=90,
                                                            content=Image(
                                                                src="pic/appointmentStatus.png", ),

                                                        ),
                                                        Container(
                                                            alignment=alignment.top_center,
                                                            width=165,
                                                            height=40,
                                                            content=Text(
                                                                value="Update Appointment Status",
                                                                font_family="RobotoSlab",
                                                                color=colors.BLACK,
                                                                size=9.4,
                                                                weight=FontWeight.BOLD,
                                                            )
                                                        )
                                                    ])
                                                )
                                            ])
                                        ),
                                    ]
                                )
                            ),
                            Container(
                                padding=padding.only(top=10),
                                width=350,
                                border_radius=15,
                                content=Row(
                                    controls=[
                                        Container(
                                            width=165,
                                            height=135,
                                            alignment=alignment.center,
                                            content=Column([
                                                Container(
                                                    width=135,
                                                    height=135,
                                                    border_radius=15,
                                                    border=border.all(color="#D3D3D3", width=2),
                                                    bgcolor=colors.WHITE,
                                                    alignment=alignment.center,
                                                    content=Column([
                                                        Container(
                                                            padding=padding.only(top=20),
                                                            width=165,
                                                            height=90,
                                                            content=Image(
                                                                src="pic/viewClinic.png", ),

                                                        ),
                                                        Container(
                                                            alignment=alignment.top_center,
                                                            width=165,
                                                            height=50,
                                                            content=Text(
                                                                font_family="RobotoSlab",
                                                                value="View Clinic",
                                                                color=colors.BLACK,
                                                                size=10,
                                                                weight=FontWeight.BOLD,
                                                            )
                                                        )
                                                    ])
                                                )
                                            ])
                                        ),
                                        Container(
                                            width=165,
                                            height=135,
                                            alignment=alignment.center,
                                            content=Column([
                                                Container(
                                                    width=135,
                                                    height=135,
                                                    border_radius=15,
                                                    border=border.all(color="#D3D3D3", width=2),
                                                    bgcolor=colors.WHITE,
                                                    alignment=alignment.center,
                                                    content=Column([
                                                        Container(
                                                            padding=padding.only(top=30),
                                                            width=165,
                                                            height=90,
                                                            content=Image(
                                                                src="pic/Setting.png", ),

                                                        ),
                                                        Container(
                                                            alignment=alignment.top_center,
                                                            width=165,
                                                            height=40,
                                                            content=Text(
                                                                value="Setting",
                                                                font_family="RobotoSlab",
                                                                color=colors.BLACK,
                                                                size=10,
                                                                weight=FontWeight.BOLD,
                                                            )
                                                        )
                                                    ])
                                                )
                                            ])
                                        ),
                                    ]
                                )
                            ),
                        ]
                    )
                )
            ]

        )
