import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicPage:
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
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        area_dropdown = Dropdown(
            dense=True,
            label="Area",
            border_color=blue,
            label_style=TextStyle(size=14,
                                  weight=FontWeight.W_500,
                                  color=blue),
            hint_text="Choose an area",
            hint_style=TextStyle(color=grey,
                                 size=14,
                                 italic=True),
            options=[
                dropdown.Option("Bayan Lepas"),
                dropdown.Option("Sungai Ara"),
                dropdown.Option("Relau"),
            ],
            text_style=TextStyle(size=14,
                                 weight=FontWeight.W_500),
            autofocus=True,
            focused_color=grey,
        )

        def get_clinic_details():
            c = db.cursor()
            c.execute("SELECT id, name, location, area, workingDay, phoneNumber, clinicImage FROM clinic WHERE "
                      "approvalStatus = ?", (1,))
            record = c.fetchall()
            return record

        clinic = get_clinic_details()

        def displayClinic(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewClinic/{user_id}{record_id}")

                    record_container = Container(
                        margin=margin.only(left=10, right=10, top=10),
                        padding=padding.only(left=10, right=10, top=10, bottom=10),
                        border_radius=10,
                        border=border.all(1, blue),
                        content=Row(
                            controls=[
                                Container(
                                    padding=padding.only(top=10, bottom=10),
                                    content=Image(
                                        src=f"{record[6]}",
                                        width=50,
                                        height=50
                                    )
                                ),

                                Container(
                                    content=Column(
                                        controls=[
                                            Text(
                                                value=f"{record[1]}",
                                                size=14,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_600,
                                                color=colors.BLACK
                                            ),

                                            Row(
                                                controls=[
                                                    Text(
                                                        value="📍",
                                                        size=10
                                                    ),

                                                    Container(
                                                        width=215,
                                                        content=Text(
                                                            value=f"{record[2]}",
                                                            size=10,
                                                            font_family="RobotoSlab",
                                                            color=grey,
                                                            text_align=TextAlign.JUSTIFY

                                                        )
                                                    )

                                                ]

                                            ),

                                            Row(
                                                controls=[
                                                    Text(
                                                        value="⏳",
                                                        size=10
                                                    ),

                                                    Container(
                                                        content=Text(
                                                            value=f"{record[4]}",
                                                            size=10,
                                                            font_family="RobotoSlab",
                                                            color=grey,
                                                            text_align=TextAlign.JUSTIFY

                                                        )
                                                    )
                                                ]
                                            ),

                                            Row(
                                                controls=[
                                                    Text(
                                                        value="📞",
                                                        size=10
                                                    ),

                                                    Container(
                                                        margin=margin.only(right=90),
                                                        content=Text(
                                                            value=f"{record[5]}",
                                                            size=10,
                                                            font_family="RobotoSlab",
                                                            color=grey,
                                                            text_align=TextAlign.JUSTIFY

                                                        )
                                                    ),

                                                    Container(
                                                        content=TextButton(
                                                            content=Text(value="More >>",
                                                                         size=9,
                                                                         font_family="RobotoSlab",
                                                                         color=blue),
                                                            on_click=on_more_button_click()
                                                        )
                                                    )

                                                ]
                                            ),
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

        return View(
            "/clinic/:user_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              horizontal_alignment="center",
                              controls=[
                                  Container(width=350,
                                            height=70,
                                            bgcolor=blue,
                                            alignment=alignment.top_center,
                                            padding=padding.only(left=10, right=10),
                                            content=Row(
                                                controls=[
                                                    Container(padding=padding.only(top=25),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ),
                                                              on_click=lambda _: page.go(f"/homepage/{user_id}")
                                                              ),

                                                    Container(padding=padding.only(left=110, top=25),
                                                              content=Text(
                                                                  value="Clinic",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),

                                                ]
                                            )
                                            ),

                                  Container(
                                      padding=padding.only(left=10, right=10, top=10),
                                      content=area_dropdown
                                  ),

                                  displayClinic(clinic),

                                  # Container(
                                  #     margin=margin.only(left=10, right=10, top=10),
                                  #     # padding=padding.only(left=10, right=10, top=10, bottom=5),
                                  #     content=Row(
                                  #         controls=[
                                  #             TextField(
                                  #                 bgcolor=lightBlue,
                                  #                 height=40,
                                  #                 width=325,
                                  #                 dense=True,
                                  #                 border_color=blue,
                                  #                 border_radius=10,
                                  #                 label="Search Clinic",
                                  #                 label_style=TextStyle(color=colors.BLACK,
                                  #                                       size=14,
                                  #                                       italic=True,
                                  #                                       weight=FontWeight.W_400),
                                  #                 text_style=TextStyle(color=colors.BLACK,
                                  #                                      size=12,
                                  #                                      weight=FontWeight.W_400)
                                  #             ),
                                  #
                                  #         ]
                                  #     )
                                  # ),

                              ]
                          )
                          )
            ]
        )
