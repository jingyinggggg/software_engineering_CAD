from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminSettingPage:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        blue = "#3386C5"
        grey = "#71839B"
        lightBlue = "#D0DCEE"

        return View(
            "/admin/setting/:user_id",
            controls=[Container(
                width=350,
                height=700,
                bgcolor="#FFFFFF",
                border_radius=30,
                alignment=alignment.center,
                content=Column(
                    controls=[
                        Container(
                            padding=padding.only(top=25, left=10, bottom=10),
                            content=Column(
                                controls=[
                                    Container(
                                        content=Image(
                                            src="pic/back.png",
                                            color="#3386C5",
                                            width=20,
                                            height=20
                                        ),
                                        on_click=lambda _: page.go(f"/login/adminHomepage/{user_id}")
                                    ),
                                    Text(
                                        value=" Setting",
                                        color="#3386C5",
                                        weight=FontWeight.W_600,
                                        size=18,
                                    )
                                ]
                            ),
                        ),

                        Container(
                            width=350,
                            height=50,
                            bgcolor=colors.WHITE,
                            margin=margin.only(top=5,bottom=10),
                            shadow=BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=colors.BLUE_GREY_300,
                                offset=Offset(0, 0),
                                blur_style=ShadowBlurStyle.NORMAL,
                            ),
                            content=Row(
                                controls=[
                                    Container(
                                        margin=margin.only(left=15),
                                        content=Icon(
                                            icons.ACCOUNT_BOX,
                                            size=20,
                                            color=blue
                                        )
                                    ),

                                    Text(
                                        width=260,
                                        value="Account",
                                        size=14,
                                        color=grey,
                                        font_family="RobotoSlab",
                                        weight=FontWeight.W_500
                                    ),

                                    Container(
                                        alignment=alignment.center,
                                        content=Icon(
                                            icons.ARROW_RIGHT,
                                            size=22,
                                            color=grey
                                        ),
                                        on_click=lambda _:page.go(f"/admin/account/{user_id}")
                                    ),
                                ]

                            )
                        ),

                        Container(
                            width=350,
                            height=50,
                            bgcolor=colors.WHITE,
                            margin=margin.only(bottom=10),
                            shadow=BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=colors.BLUE_GREY_300,
                                offset=Offset(0, 0),
                                blur_style=ShadowBlurStyle.NORMAL,
                            ),
                            content=Row(
                                controls=[
                                    Container(
                                        margin=margin.only(left=15),
                                        content=Icon(
                                            icons.LOCK,
                                            size=20,
                                            color=blue
                                        )
                                    ),

                                    Text(
                                        width=260,
                                        value="Password & Security",
                                        size=14,
                                        color=grey,
                                        font_family="RobotoSlab",
                                        weight=FontWeight.W_500
                                    ),

                                    Container(
                                        alignment=alignment.center,
                                        content=Icon(
                                            icons.ARROW_RIGHT,
                                            size=22,
                                            color=grey
                                        ),
                                        on_click=lambda _: page.go(f"/admin/password/{user_id}")
                                    ),
                                ]

                            )
                        ),

                        Container(
                            width=350,
                            height=50,
                            bgcolor=colors.WHITE,
                            # margin=margin.only(top=-10),
                            shadow=BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=colors.BLUE_GREY_300,
                                offset=Offset(0, 0),
                                blur_style=ShadowBlurStyle.NORMAL,
                            ),
                            content=Row(
                                controls=[
                                    Container(
                                        margin=margin.only(left=15),
                                        content=Icon(
                                            icons.LOGOUT,
                                            size=20,
                                            color=blue
                                        )
                                    ),

                                    Text(
                                        width=260,
                                        value="Log Out",
                                        size=14,
                                        color=grey,
                                        font_family="RobotoSlab",
                                        weight=FontWeight.W_500
                                    ),

                                    Container(
                                        alignment=alignment.center,
                                        content=Icon(
                                            icons.ARROW_RIGHT,
                                            size=22,
                                            color=grey
                                        ),
                                        on_click=lambda _: page.go(f"/loginUser")
                                    ),
                                ]

                            )
                        )

                    ]
                ))
            ]
        )
