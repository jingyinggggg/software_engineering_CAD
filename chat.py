from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class Chat:
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
            "/chat/:user_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Container(
                                        padding=padding.only(right=160),
                                        width=350,
                                        height=80,
                                        alignment=alignment.center,
                                        bgcolor="#3386C5",
                                        content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        IconButton(icons.ARROW_BACK_ROUNDED,
                                                                   icon_size=30,
                                                                   icon_color="WHITE",
                                                                   on_click=lambda _: page.go(
                                                                       f"/login/homepage/{user_id}")),
                                                        Text("Chat",
                                                             color="WHITE",
                                                             text_align=TextAlign.CENTER,
                                                             size=20,
                                                             font_family="RobotoSlab",
                                                             weight=FontWeight.BOLD)
                                                    ])
                                    )
                                ]),

                            Container(alignment=alignment.center,
                                      content=Column(
                                          controls=[TextField(label="Search name",
                                                              border_color="#3386C5",
                                                              border_radius=10,
                                                              text_style=TextStyle(size=14,
                                                                                   color=colors.BLACK),
                                                              width=320,
                                                              height=40)]
                                      )),
                            Container(alignment=alignment.center,
                                      border_radius=8,
                                      padding=padding.only(left=10),
                                      margin=margin.only(left=10),
                                      border=border.all(color="BLACK"),
                                      width=320,
                                      content=Row(controls=
                                                  [Column(alignment=MainAxisAlignment.START,
                                                          controls=[Container(
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
                                                                          ]))

                                                          ]),
                                                   Container(padding=padding.only(left=50),
                                                             content=IconButton(icons.ARROW_CIRCLE_RIGHT_OUTLINED,
                                                                                on_click=lambda _:page.go(f"/chat_info/{user_id}")))
                                                   ]),

                                      )]))])
