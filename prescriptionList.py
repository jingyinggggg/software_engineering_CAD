import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class PrescriptionList:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        # booking_id = int(params.booking_id)
        # patient_id = int(params.patient_id)

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

        def get_prescription_list():
            c = db.cursor()
            # c.execute("SELECT * FROM prescriptions INNER JOIN booking ON prescriptions.bookingID = booking.bookingID "
            #           "WHERE prescriptions.doctorID = ? AND booking.bookingID = ?",
            #           (user_id, booking_id,))
            c.execute(f"SELECT * FROM prescriptions WHERE doctorID = {user_id}")
            record = c.fetchall()
            return record

        prescription = get_prescription_list()

        # def get_patient():
        #     c = db.cursor()
        #     c.execute("SELECT * FROM users WHERE id = ?", (patient_id,))
        #     patient_info = c.fetchall()
        #     return patient_info
        #
        # patient = get_patient()

        def displayPrescriptionList(records):
            if records:
                record_containers = []
                for record in records:
                    record_container = Container(
                        margin=margin.only(left=10),
                        width=330,
                        height=100,
                        border_radius=10,
                        border=border.all(1, color=colors.BLACK),
                        content=Row(
                            controls=[
                                Container(
                                    margin=margin.only(left=10, right=10),
                                    content=Image(
                                        src="pic/female_patient.png",
                                        width=60,
                                        height=60,
                                    )
                                ),

                                Column(
                                    controls=[
                                        Container(
                                            padding=padding.only(left=10, top=10, right=20),
                                            content=Row(
                                                alignment="spaceBetween",
                                                controls=[
                                                    Text("Patient Name", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                         width=80),
                                                    Text(" :   ", color="BLACK", size=12),
                                                    Text(f"{record[3]}", color="BLACK", size=12,
                                                         text_align=TextAlign.JUSTIFY,
                                                         weight=FontWeight.W_600, width=160)
                                                ]
                                            )
                                        ),
                                        Container(
                                            padding=padding.only(left=10, right=20),
                                            # Add padding to the entire container
                                            content=Row(
                                                alignment="spaceBetween",
                                                controls=[
                                                    Text("Date Signed", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                         width=80),
                                                    Text(" :   ", color="BLACK", size=12),
                                                    Text(f"{record[7]}", color="BLACK", size=12,
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
                                                alignment="spaceBetween",
                                                controls=[
                                                    Text("Medication", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                         width=80),
                                                    Text(" :   ", color="BLACK", size=12),
                                                    Text(f"{record[4]}", color="BLACK", size=12,
                                                         text_align=TextAlign.JUSTIFY,
                                                         weight=FontWeight.W_600, width=160)
                                                ]
                                            )
                                        )]
                                )
                            ]
                        # ), on_click=lambda _: print(f"Prescription ID:{record[0]}")
                        ), on_click=lambda _: page.go(f"/prescription/{user_id}/{record[0]}")
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

            else:
                return Container(
                    padding=padding.only(top=140),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Image(
                                src="pic/prescription_icon.png",
                                width=120,
                                height=120
                            ),

                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="You do not have any generated prescription yet.",
                                    text_align=TextAlign.CENTER,
                                    size=12,
                                    color=colors.BLACK,
                                    font_family="RobotoSlab",
                                    weight=FontWeight.W_500
                                )
                            ),

                        ]
                    )
                )
            #
            # return (
            #     Container(
            #         margin=margin.only(left=10),
            #         width=330,
            #         height=100,
            #         border_radius=10,
            #         border=border.all(1, color=colors.BLACK),
            #         content=
            #         Row(
            #             controls=[
            #                 Container(
            #                     margin=margin.only(left=10, right=10),
            #                     content=Image(
            #                         src="pic/female_patient.png",
            #                         width=60,
            #                         height=60,
            #                     )
            #                 ),
            #
            #                 Column(
            #                     controls=[
            #                         Container(
            #                             padding=padding.only(left=10, top=10, right=20),
            #                             content=Row(
            #                                 alignment="spaceBetween",
            #                                 controls=[
            #                                     Text("Patient Name", color="BLACK", size=12, weight=FontWeight.BOLD,
            #                                          width=80),
            #                                     Text(" :   ", color="BLACK", size=12),
            #                                     # Text(f"{patient[0][1]}", color="BLACK", size=12,
            #                                     #      text_align=TextAlign.JUSTIFY,
            #                                     #      weight=FontWeight.W_600, width=160)
            #                                 ]
            #                             )
            #                         ),
            #                         Container(
            #                             padding=padding.only(left=10, right=20),  # Add padding to the entire container
            #                             content=Row(
            #                                 alignment="spaceBetween",
            #                                 controls=[
            #                                     Text("Date Signed", color="BLACK", size=12, weight=FontWeight.BOLD,
            #                                          width=80),
            #                                     Text(" :   ", color="BLACK", size=12),
            #                                     # Text(f"{prescription[0][7]}", color="BLACK", size=12,
            #                                     #      weight=FontWeight.W_600,
            #                                     #      text_align=TextAlign.JUSTIFY, width=160)
            #                                 ]
            #                             )
            #                         ),
            #                         Container(
            #                             padding=padding.only(left=10, right=20),  # Add padding to the entire container
            #                             # margin=margin.only(right=10),
            #                             content=Row(
            #                                 alignment="spaceBetween",
            #                                 controls=[
            #                                     Text("Medication", color="BLACK", size=12, weight=FontWeight.BOLD,
            #                                          width=80),
            #                                     Text(" :   ", color="BLACK", size=12),
            #                                     # Text(f"{prescription[0][4]}", color="BLACK", size=12,
            #                                     #      text_align=TextAlign.JUSTIFY,
            #                                     #      weight=FontWeight.W_600, width=160)
            #                                 ]
            #                             )
            #                         )]
            #                 )
            #             ]
            #         ), on_click=lambda _: page.go(f"/prescription/{user_id}{booking_id}")
            #     )
            # )

        return View(
            "/prescriptionList/:user_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Column(
                        # alignment=MainAxisAlignment.CENTER,
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
                                                      on_click=lambda _: page.go(f"/login/homepage/{user_id}")),
                                            Container(padding=padding.only(left=75),
                                                      content=Text("Prescription",
                                                                   color="WHITE",
                                                                   text_align=TextAlign.CENTER,
                                                                   size=20,
                                                                   font_family="RobotoSlab"
                                                                   ))
                                        ])

                                    )
                                ]), displayPrescriptionList(prescription)
                        ])
                )
            ])
