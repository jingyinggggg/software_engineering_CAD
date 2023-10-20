from flet import *
from flet_route import Params, Basket

class DoctorResetPassword:
    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "light"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        return View(
            "/login/resetPassword",
            controls=[
                Container(
                    padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    border=border.all(1, "black"),
                    alignment=alignment.center,
                    content=Column(
                        horizontal_alignment="top_left",
                        controls=[
                            Container(
                                padding=padding.symmetric(vertical=30),
                                content=Row(
                                    vertical_alignment="center",
                                    controls=[
                                        Image(
                                            src="pic/loginPageImage.png",
                                            width=50,
                                            height=50
                                        ),
                                        # Add some space between the image and text
                                        Text(
                                            "Reset Password",
                                            size=18,
                                            font_family="RobotoSlab",
                                            text_align=TextAlign.CENTER,
                                            color="#3386C5"
                                        ),
                                    ]
                                )
                            ),
                            Container(
                                padding=padding.symmetric(vertical=30),
                                content=Column(
                                    horizontal_alignment="center",
                                    controls=[
                                        TextField(label="Email", hint_text="Enter Email"),
                                        TextField(label="New password", hint_text="Enter new password"),
                                        TextField(label="Re-enter password", hint_text="Re-enter new password"),
                                        IconButton(content=Text("Confirm",
                                                                size=16,
                                                                font_family="RobotoSlab",
                                                                color="WHITE",
                                                                text_align=TextAlign.CENTER),
                                             width=300,
                                             height=45,
                                             style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                               shape={"": RoundedRectangleBorder(radius=7)}
                                                               ),
                                             on_click=lambda _:page.go(f"/login")
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
