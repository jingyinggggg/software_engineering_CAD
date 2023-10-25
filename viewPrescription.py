from datetime import date

from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ViewPrescriptionPage:
    def __init__(self):
        self.selected_date = date.today()
        self.show_confirmation = False
        self.show_alert = False
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        # prescription_id = int(params.prescription_id)
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

        name = TextField(
            label="Full Name",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            border_color=blue,
            value="Patient Name",
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            read_only=True
        )

        medical_name = TextField(
            height=40,
            border_color=blue,
            value="",
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            read_only=True
        )

        dosage = TextField(
            height=40,
            border_color=blue,
            value="",
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            read_only=True
        )

        duration_treatment = TextField(
            height=40,
            border_color=blue,
            value="",
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            read_only=True
        )

        doctor_name = TextField(
            label="Assign By",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            border_color=blue,
            value="Doctor Name",
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            read_only=True
        )

        assigned_date = TextField(
            label="Assigned Date",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            border_color=blue,
            value="Date",
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            read_only=True
        )

        instruction = TextField(
            height=40,
            border_color=blue,
            # value=fullName,
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            read_only=True,
            multiline=True,
        )

        return View(
            "/viewPrescription/:user_id",
            # "/viewPrescription/:prescription_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              scroll=True,
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
                                                              on_click=lambda _: page.go(f"/patientPrescription/{user_id}")
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

                                  Container(padding=padding.only(left=10, right=10),
                                            content=Column(
                                                controls=[
                                                    Text("Patient's Name:",
                                                         color="#666666",
                                                         size=14,
                                                         weight=FontWeight.BOLD,
                                                         font_family="RobotoSlab"),

                                                    name,

                                                    Container(
                                                        margin=margin.only(top=10),
                                                        content=Text(
                                                            "Treatment",
                                                            color="#666666",
                                                            size=14,
                                                            weight=FontWeight.BOLD,
                                                            font_family="RobotoSlab"
                                                        )
                                                    ),

                                                    Text(
                                                        "A: Medication Name / Strength",
                                                        color="#666666",
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                    ),

                                                    medical_name,

                                                    Text("B: Quantity / Dosage Frequency",
                                                         color="#666666",
                                                         size=12,
                                                         font_family="RobotoSlab"),

                                                    dosage,

                                                    Text("C: Duration of Treatment / Treatment Frequency",
                                                         color="#666666",
                                                         size=12,
                                                         font_family="RobotoSlab"),

                                                    duration_treatment,

                                                    Container(
                                                        margin=margin.only(top=10),
                                                        content=Text(
                                                            "Specific Instructions",
                                                            color="#666666",
                                                            size=14,
                                                            weight=FontWeight.BOLD,
                                                            font_family="RobotoSlab"
                                                        )
                                                    ),

                                                    instruction,

                                                    Container(
                                                        margin=margin.only(top=10),
                                                        content=Text(
                                                            "Prescription Details",
                                                            color="#666666",
                                                            size=14,
                                                            weight=FontWeight.BOLD,
                                                            font_family="RobotoSlab"
                                                        )
                                                    ),

                                                    doctor_name,

                                                    assigned_date,
                                                ]
                                            )
                                            )
                              ]
                          )
                          )
            ]
        )
