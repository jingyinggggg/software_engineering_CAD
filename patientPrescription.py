import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class PatientPrescriptionPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
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

        def get_user_prescription_record():
            # pass
            c = db.cursor()
            c.execute(
                "SELECT * FROM prescriptions INNER JOIN doctors ON doctors.id = prescriptions.doctorID WHERE patientID = ? ORDER BY date_signed DESC", (user_id,))
            record = c.fetchall()
            return record

        prescriptionRecord = get_user_prescription_record()

        def displayRecord(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewPrescription/{user_id}/{record_id}")

                    record_container = Container(
                        margin=margin.only(left=15, right=15, top=20),
                        border_radius=10,
                        border=border.all(1, colors.BLACK),
                        padding=padding.only(left=20, right=20, top=20, bottom=20),
                        content=Row(
                            controls=[
                                Container(
                                    # margin=margin.only(top=0),
                                    padding=padding.only(top=-20, right=5),
                                    content=Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            Image(
                                                src="pic/prescription_icon.png",
                                                width=60,
                                                height=70,
                                            )
                                        ]
                                    )
                                ),

                                Column(
                                    controls=[
                                        Container(
                                            width=220,
                                            content=Row(
                                                alignment="spaceBetween",
                                                controls=[
                                                    Text(
                                                        value=f"Assigned by: ",
                                                        color=colors.BLACK,
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                        width=90
                                                    ),
                                                    Text(
                                                        value=f": ",
                                                        color=colors.BLACK,
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY
                                                    ),
                                                    Text(
                                                        value=f"Dr. {record[11]}",
                                                        color=colors.BLACK,
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                        width=120
                                                    )
                                                ]
                                            )

                                        ),

                                        Container(
                                            width=220,
                                            content=Row(
                                                alignment="spaceBetween",
                                                controls=[
                                                    Text(
                                                        value=f"Assigned date",
                                                        color=colors.BLACK,
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                        width=90
                                                    ),
                                                    Text(
                                                        value=f": ",
                                                        color=colors.BLACK,
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY
                                                    ),
                                                    Text(
                                                        value=f"{record[7]}",
                                                        color=colors.BLACK,
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                        width=120
                                                    )
                                                ]
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            content=Row(
                                                alignment="spaceBetween",
                                                controls=[
                                                    Text(
                                                        value=f"Medication",
                                                        color=colors.BLACK,
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                        width=90
                                                    ),
                                                    Text(
                                                        value=f": ",
                                                        color=colors.BLACK,
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                    ),
                                                    Text(
                                                        value=f"{record[4]}",
                                                        color=colors.BLACK,
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                        width=120
                                                    )
                                                ]
                                            )

                                        ),
                                    ]
                                )
                            ]
                        ),
                        on_click=on_more_button_click()
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

            else:
                return Container(
                    padding=padding.only(top=120),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Image(
                                src="pic/prescription_icon.png",
                                width=150,
                                height=150
                            ),

                            Container(
                                padding=padding.only(left=30, right=30),
                                content=Text(
                                    width=250,
                                    value="You do not have any prescription yet.",
                                    text_align=TextAlign.CENTER,
                                    size=12,
                                    color=grey,
                                    font_family="RobotoSlab"
                                )
                            ),

                        ]
                    )
                )

        return View(
            "/patientPrescription/:user_id",
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
                                                              on_click=lambda _: page.go(f"/homepage/{user_id}")
                                                              ),

                                                    Container(padding=padding.only(left=85, top=25),
                                                              content=Text(
                                                                  value="Prescription",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),

                                                ]
                                            )
                                            ),

                                  displayRecord(prescriptionRecord)

                              ]
                          )
                          )
            ]
        )