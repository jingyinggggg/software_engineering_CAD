import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class MedicalRecordPage:
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

        def get_user_medical_record():
            c = db.cursor()
            c.execute(
                "SELECT id, allergies, pastMedicalCondition, currentMedicalCondition, date FROM medicalRecordHistory "
                "WHERE patientUserID = ? ORDER BY date DESC", (user_id,))
            record = c.fetchall()
            return record

        medicalRecord = get_user_medical_record()

        def displayRecord(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewMedicalRecord/{record_id}")

                    record_container = Container(
                        margin=margin.only(left=15, right=15, top=20),
                        border_radius=10,
                        border=border.all(1, colors.BLACK),
                        padding=padding.only(left=20, right=20, top=20, bottom=20),
                        content=Row(
                            controls=[
                                Container(
                                    # margin=margin.only(top=0),
                                    padding=padding.only(top=-10),
                                    content=Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            Image(
                                                src="pic/medicalRecord.png",
                                                color=grey,
                                                width=40,
                                                height=40,
                                            ),
                                            Text(
                                                value=f"{record[4]}",
                                                color=colors.BLACK,
                                                size=10,
                                                weight=FontWeight.W_700
                                            )
                                        ]
                                    )
                                ),

                                Column(
                                    controls=[
                                        Container(
                                            width=220,
                                            content=Text(
                                                value=f"Past Medical Condition: {record[2]}",
                                                color=colors.BLACK,
                                                size=12,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            content=Text(
                                                value=f"Current Medical Condition: {record[3]}",
                                                color=colors.BLACK,
                                                size=12,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            content=Text(
                                                value=f"Allergies: {record[1]}",
                                                color=colors.BLACK,
                                                size=12,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(padding=padding.only(left=160, bottom=-10, top=-10),
                                                  content=TextButton(
                                                      content=Text(
                                                          "More >>",
                                                          size=10,
                                                          italic=True,
                                                          font_family="RobotoSlab",
                                                          color=blue),
                                                      on_click=on_more_button_click()
                                                  )

                                                  ),
                                    ]
                                )
                            ]
                        )
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
                                src="pic/addMedicalRecord.png",
                                width=150,
                                height=150
                            ),

                            Container(
                                padding=padding.only(top=10),
                                content=Text(
                                    value="Add a medical record",
                                    text_align=TextAlign.CENTER,
                                    size=18,
                                    weight=FontWeight.W_500,
                                    color=colors.BLACK,
                                    font_family="RobotoSlab"
                                )
                            ),

                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="A detailed health history helps a doctor diagnose you better.",
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
            "/medicalRecord/:user_id",
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
                                            padding=padding.only(left=20, top=20),
                                            content=Row(
                                                alignment="spaceBetween",
                                                controls=[
                                                    Container(
                                                        content=Image(
                                                            src="pic/back.png",
                                                            color=colors.WHITE,
                                                            width=20,
                                                            height=20
                                                        ),
                                                        on_click=lambda _: page.go(f"/homepage/{user_id}")
                                                    ),

                                                    Text(
                                                        value="Medical Reocrd",
                                                        size=20,
                                                        font_family="RobotoSlab",
                                                        color=colors.WHITE,
                                                        text_align=TextAlign.CENTER),

                                                    Container(
                                                        content=IconButton(
                                                            icon=icons.ADD,
                                                            icon_color=colors.WHITE,
                                                            on_click=lambda _: page.go(f"/addMedicalRecord/{user_id}")
                                                        )
                                                    )

                                                ]
                                            )
                                            ),

                                  displayRecord(medicalRecord)

                              ]
                          )
                          )
            ]
        )