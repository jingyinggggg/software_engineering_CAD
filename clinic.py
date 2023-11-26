import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicPage:
    def __init__(self):
        self.show_sidebar = False

    def get_clinic_details(self, selected_area):
        c = db.cursor()
        if selected_area:
            if selected_area == "All":
                c.execute(
                    "SELECT id, name, location, area, workingTime, workingDay, clinicDescription, phoneNumber,"
                    "clinicImage, closed FROM clinic WHERE approvalStatus = ?",
                    (1,))
            else:
                c.execute(
                    "SELECT id, name, location, area, workingTime, workingDay, clinicDescription, phoneNumber,"
                    "clinicImage, closed FROM clinic WHERE approvalStatus = ? AND area = ?",
                    (1, selected_area,))
        else:
            c.execute(
                "SELECT id, name, location, area, workingTime, workingDay, clinicDescription, phoneNumber,"
                "clinicImage, closed FROM clinic WHERE approvalStatus = ?",
                (1,))
        record = c.fetchall()
        return record


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

        def refresh_clinic_list(e):
            updated_clinic_list = self.get_clinic_details(area_dropdown.value)

            # Update the clinic_list control with the updated data
            clinic_list.controls.clear()
            clinic_list.controls.append(displayClinic(updated_clinic_list))

            # Update the page to reflect the changes
            page.update()

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
                dropdown.Option("All"),
                dropdown.Option("Bayan Lepas"),
                dropdown.Option("Sungai Ara"),
                dropdown.Option("Relau"),
                dropdown.Option("Jelutong"),
                dropdown.Option("Georgetown"),
            ],
            text_style=TextStyle(size=14,
                                 weight=FontWeight.W_500),
            autofocus=True,
            focused_color=grey,
            on_change=refresh_clinic_list
        )

        clinic = self.get_clinic_details(area_dropdown.value)

        def check_clinic_working_day(workingDay, clinicClosed):
            if clinicClosed == "None":
                return f"{workingDay}"
            else:
                return f"{workingDay} ({clinicClosed} Closed)"

        def displayClinic(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewClinic/{user_id}{record_id}")

                    record_container = Container(
                        margin=margin.only(left=10, right=10, bottom=20),
                        padding=padding.only(left=10, right=10, top=10, bottom=10),
                        border_radius=10,
                        border=border.all(1, blue),
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
                                                            value=check_clinic_working_day(record[5],record[9]),
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
                                                            value=f"{record[7]}",
                                                            size=10,
                                                            font_family="RobotoSlab",
                                                            color=grey,
                                                            text_align=TextAlign.JUSTIFY

                                                        )
                                                    )
                                                ]
                                            ),
                                        ]
                                    )
                                )
                            ]
                        ),
                        on_click=on_more_button_click()
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

            else:
                return Container(
                    content=Text(
                        value="There are no clinic in the selected area.",
                        color=colors.BLACK,
                        font_family="RobotoSlab"
                    )
                )

        clinic_list = displayClinic(clinic)

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
                              scroll=True,
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
                                      padding=padding.only(left=10, right=10, top=10, bottom=10),
                                      content=area_dropdown
                                  ),

                                  clinic_list
                              ]
                          )
                          )
            ]
        )
