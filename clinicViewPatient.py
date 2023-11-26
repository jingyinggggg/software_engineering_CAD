import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicViewPatient:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        clinic_id = int(params.clinic_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        def get_patient():
            c = db.cursor()
            c.execute("""SELECT users.* 
                        FROM booking
                        INNER JOIN users ON booking.patientID = users.id
                        WHERE clinicID = ? AND booking.bookingStatus = 0 OR booking.bookingStatus = 1""", (clinic_id,))
            patient_info = c.fetchall()

            return patient_info

        patient = get_patient()

        def displayPatient(records):
            if records:
                displayed_patients = set()
                patient_containers = []
                for patient in records:
                    patient_id = patient[0]
                    if patient_id not in displayed_patients:
                        displayed_patients.add(patient_id)

                        patient_container = Container(
                            margin=margin.only(left=10, right=10),
                            width=330,
                            border_radius=10,
                            border=border.all(1, color=blue),
                            content=
                            Row(
                                controls=[
                                    Container(
                                        margin=margin.only(left=10, right=10),
                                        content=Image(
                                            src="pic/avatar.png",
                                            width=60,
                                            height=60,
                                        )
                                    ),

                                    Column(
                                        controls=[
                                            Container(
                                                padding=padding.only(left=10, top=10, right=20),
                                                content=Row(
                                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        Text("Patient Name", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                             width=100),
                                                        Text(" :   ", color="BLACK", size=12),
                                                        Text(f"{patient[1]}", color="BLACK", size=12,
                                                             text_align=TextAlign.JUSTIFY,
                                                             weight=FontWeight.W_600, width=160)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=10, right=20),
                                                # Add padding to the entire container
                                                content=Row(
                                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        Text("Username", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                             width=100),
                                                        Text(" :   ", color="BLACK", size=12),
                                                        Text(f"{patient[2]}", color="BLACK", size=12,
                                                             weight=FontWeight.W_600,
                                                             text_align=TextAlign.JUSTIFY, width=160)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=10, right=20),
                                                # Add padding to the entire container
                                                # margin=margin.only(right=10),
                                                content=Row(
                                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        Text("Date of Birth", color="BLACK", size=12,
                                                             weight=FontWeight.BOLD,
                                                             width=100),
                                                        Text(" :   ", color="BLACK", size=12),
                                                        Text(f"{patient[6]}", color="BLACK", size=12,
                                                             text_align=TextAlign.JUSTIFY,
                                                             weight=FontWeight.W_600, width=160)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=10, right=20),
                                                # Add padding to the entire container
                                                # margin=margin.only(right=10),
                                                content=Row(
                                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        Text("Contact", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                             width=100),
                                                        Text(" :   ", color="BLACK", size=12),
                                                        Text(f"{patient[4]}", color="BLACK", size=12,
                                                             text_align=TextAlign.JUSTIFY,
                                                             weight=FontWeight.W_600, width=160)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=10, right=20, bottom=10),
                                                # Add padding to the entire container
                                                # margin=margin.only(right=10),
                                                content=Row(
                                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        Text("Gender", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                             width=100),
                                                        Text(" :   ", color="BLACK", size=12),
                                                        Text(f"{patient[7]}", color="BLACK", size=12,
                                                             text_align=TextAlign.JUSTIFY,
                                                             weight=FontWeight.W_600, width=160)
                                                    ]
                                                )
                                            ),
                                        ]
                                    )
                                ]
                            )
                        )
                        patient_containers.append(patient_container)

                return Column(controls=patient_containers)
            else:
                return Container()


        return View(
            "/clinicViewPatient/:clinic_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    content=Column(
                        scroll=ScrollMode.AUTO,
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        padding=padding.only(right=120),
                                        width=350,
                                        height=80,
                                        bgcolor="#3386C5",
                                        content=Row(controls=[
                                            Container(padding=padding.only(left=10, top=5),
                                                      content=Image(
                                                          src="pic/back.png",
                                                          color=colors.WHITE,
                                                          width=20,
                                                          height=20
                                                      ),
                                                      on_click=lambda _: page.go(f"/clinicHomepage/{clinic_id}")),
                                            Container(padding=padding.only(left=75),
                                                      content=Text("Patient List",
                                                                   color="WHITE",
                                                                   text_align=TextAlign.CENTER,
                                                                   size=20,
                                                                   font_family="RobotoSlab"
                                                                   ))
                                        ])

                                    )
                                ]
                            ),
                            displayPatient(patient),

                            Container(
                                margin=margin.only(bottom=10)
                            )

                        ])
                )
            ])
