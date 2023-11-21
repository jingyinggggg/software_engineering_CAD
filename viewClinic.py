import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ViewClinicPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
        user_id = int(params.user_id)
        clinic_id = int(params.clinic_id)

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

        def get_clinic_details():
            c = db.cursor()
            c.execute("SELECT id, name, location, area, workingTime, workingDay, clinicDescription, "
                      "phoneNumber, clinicImage, mapImage, EnvironmentImage, closed FROM clinic WHERE id = ?", (clinic_id,))
            record = c.fetchall()
            return record

        clinic = get_clinic_details()

        def check_clinic_working_day(workingDay, clinicClosed):
            if clinicClosed == "None":
                return f"{workingDay}"
            else:
                return f"{workingDay} ({clinicClosed} Closed)"

        def displayClinic(records):
            if records:
                record_containers = []
                for record in records:
                    record_container = Column(

                        controls=[
                            Container(
                                width=350,
                                bgcolor=lightBlue,
                                margin=margin.only(top=-10),
                                padding=padding.only(left=10, right=10, top=10, bottom=10),
                                content=Row(
                                    controls=[
                                        Container(
                                            padding=padding.only(top=10, bottom=10),
                                            content=Image(
                                                src=f"{record[8]}",
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
                                                                width=230,
                                                                content=Text(
                                                                    value=f"{record[2]}",
                                                                    size=10,
                                                                    font_family="RobotoSlab",
                                                                    color=colors.BLACK,
                                                                    text_align=TextAlign.JUSTIFY,
                                                                    weight=FontWeight.W_500

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
                                                                    value=check_clinic_working_day(record[5], record[11]),
                                                                    size=10,
                                                                    font_family="RobotoSlab",
                                                                    color=colors.BLACK,
                                                                    text_align=TextAlign.JUSTIFY,
                                                                    weight=FontWeight.W_500

                                                                )
                                                            )
                                                        ]
                                                    ),

                                                    Row(
                                                        controls=[
                                                            Text(
                                                                value="🕛",
                                                                size=10
                                                            ),

                                                            Container(
                                                                content=Text(
                                                                    value=f"{record[4]}",
                                                                    size=10,
                                                                    font_family="RobotoSlab",
                                                                    color=colors.BLACK,
                                                                    text_align=TextAlign.JUSTIFY,
                                                                    weight=FontWeight.W_500

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
                                                                content=Text(
                                                                    value=f"{record[7]}",
                                                                    size=10,
                                                                    font_family="RobotoSlab",
                                                                    color=colors.BLACK,
                                                                    text_align=TextAlign.JUSTIFY,
                                                                    weight=FontWeight.W_500

                                                                )
                                                            ),
                                                        ]
                                                    ),

                                                    Row(
                                                        controls=[
                                                            Text(
                                                                value="📝",
                                                                size=10
                                                            ),

                                                            Container(
                                                                width=230,
                                                                content=Text(
                                                                    value=f"{record[6]}",
                                                                    size=10,
                                                                    font_family="RobotoSlab",
                                                                    color=colors.BLACK,
                                                                    text_align=TextAlign.JUSTIFY,
                                                                    weight=FontWeight.W_500

                                                                )
                                                            )
                                                        ]
                                                    ),

                                                    Container(
                                                        margin=margin.only(left=180),
                                                        content=TextButton(content=Text("View Doctor",
                                                                                        size=9,
                                                                                        font_family="RobotoSlab",
                                                                                        color="WHITE",
                                                                                        text_align=TextAlign.CENTER),
                                                                           height=20,
                                                                           style=ButtonStyle(
                                                                               bgcolor={"": "#3386C5"},
                                                                               shape={
                                                                                   "": RoundedRectangleBorder(
                                                                                       radius=7)}
                                                                           ),
                                                                           on_click=lambda _:page.go(f"/doctorListBasedOnClinic/{user_id}{clinic_id}")
                                                                           )
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),

                            Container(
                                margin=margin.only(left=10, right=10, top=10, bottom=10),
                                padding=padding.only(left=10, right=10, top=10, bottom=10),
                                border_radius=0,
                                width=320,
                                border=border.all(2, lightBlue),
                                content=Column(
                                    controls=[
                                        Text(
                                            value="📍 Google Map",
                                            font_family="RobotoSlab",
                                            size=14,
                                            weight=FontWeight.W_500,
                                            color=colors.BLACK
                                        ),

                                        Image(
                                            src=f"{record[9]}"
                                        )
                                    ]
                                )
                            ),

                            Container(
                                margin=margin.only(left=10, right=10, bottom=20),
                                padding=padding.only(left=10, right=10, top=10, bottom=10),
                                border_radius=0,
                                width=320,
                                border=border.all(2, lightBlue),
                                content=Column(
                                    controls=[
                                        Text(
                                            value="🪴 Environment",
                                            font_family="RobotoSlab",
                                            size=14,
                                            weight=FontWeight.W_500,
                                            color=colors.BLACK
                                        ),

                                        Image(
                                            src=f"{record[10]}"
                                        )
                                    ]
                                )
                            ),
                        ]
                    )

                    record_containers.append(record_container)

                return Column(controls=record_containers)

        return View(
            "/viewClinic/:user_id:clinic_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              horizontal_alignment="center",
                              scroll=True,
                              controls=[
                                  Container(width=350,
                                            height=70,
                                            bgcolor=blue,
                                            alignment=alignment.top_center,
                                            padding=padding.only(left=10, right=10, bottom=0),
                                            content=Row(
                                                controls=[
                                                    Container(padding=padding.only(top=25),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ),
                                                              on_click=lambda _: page.go(f"/clinic/{user_id}")
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

                                  displayClinic(clinic)

                              ]
                          )
                          )
            ]
        )
