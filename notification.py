import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class Notification:
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

        def get_doctor_details():
            c = db.cursor()
            c.execute("SELECT * FROM doctors WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]

            return fullName

        fullName = get_doctor_details()

        return View(
            "/notification/:user_id",
            # phone border
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Row(alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        padding=padding.only(right=120),
                                        width=350,
                                        height=80,
                                        alignment=alignment.center,
                                        bgcolor="#3386C5",
                                        content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[IconButton(icons.ARROW_BACK_ROUNDED,
                                                                         icon_size=30,
                                                                         icon_color="WHITE",
                                                                         on_click=lambda _: page.go(
                                                                             f"/login/homepage/{user_id}")),
                                                              Text("Notification",
                                                                   color="WHITE",
                                                                   text_align=TextAlign.CENTER,
                                                                   size=20,
                                                                   font_family="RobotoSlab",
                                                                   weight=FontWeight.BOLD)]))
                                ]),
                            Container(
                                padding=padding.only(left=10, right=10, top=5),
                                alignment=alignment.center,
                                margin=margin.only(left=10, top=5, right=10),
                                # Adjusted margin to reduce the space at the bottom
                                width=320,
                                height=95,
                                border_radius=8,
                                border=border.all(width=1, color="BLACK"),
                                content=Row(
                                    controls=[
                                        Icon(icons.TIPS_AND_UPDATES_OUTLINED,
                                             size=40,
                                             color="#3D3F99"),
                                        Column(
                                            controls=[
                                                Text("Appointment reminder",
                                                     color="BLACK",
                                                     size=14,
                                                     font_family="RobotoSlab",
                                                     weight=FontWeight.BOLD),
                                                Text(f"Hi, Dr. {fullName}! Don't forget your appointment with patient "
                                                     "(Wong Yi Yi) on 9 am!",
                                                     size=12,
                                                     color="BLACK",
                                                     overflow=TextOverflow.VISIBLE,
                                                     width=250,
                                                     font_family="RobotoSlab")
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
