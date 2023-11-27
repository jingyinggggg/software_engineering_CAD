import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicViewAppointment:
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

        def get_appointment():
            c = db.cursor()
            c.execute("""SELECT booking.patientID, booking.doctorID, booking.reasonVisit, booking.appointmentStatus,
                       users.fullName as patientName, users.gender,
                       doctors.fullName as doctorName
                       FROM booking
                       INNER JOIN users ON booking.patientID = users.id
                       INNER JOIN doctors ON booking.doctorID = doctors.id
                       WHERE booking.clinicID = ? """, (clinic_id,))
            appointments = c.fetchall()
            return appointments

        appointments = get_appointment()

        def display_patient(appointments):
            patient_containers = []
            for appointment in appointments:
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
                                                     width=90),
                                                Text(" :   ", color="BLACK", size=12),
                                                Text(value=appointment[4], color="BLACK", size=12,
                                                     text_align=TextAlign.JUSTIFY,
                                                     weight=FontWeight.W_600, width=160)
                                            ]
                                        )
                                    ),
                                    Container(
                                        padding=padding.only(left=10, right=20),  # Add padding to the entire container
                                        content=Row(
                                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                Text("Gender", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                     width=90),
                                                Text(" :   ", color="BLACK", size=12),
                                                Text(value=appointment[5], color="BLACK", size=12,
                                                     text_align=TextAlign.JUSTIFY,
                                                     weight=FontWeight.W_600, width=160)
                                            ]
                                        )
                                    ),
                                    Container(
                                        padding=padding.only(left=10, right=20),  # Add padding to the entire container
                                        content=Row(
                                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                Text("Reason Visit", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                     width=90),
                                                Text(" :   ", color="BLACK", size=12),
                                                Text(value=appointment[2], color="BLACK", size=12,
                                                     text_align=TextAlign.JUSTIFY,
                                                     weight=FontWeight.W_600, width=110)
                                            ]
                                        )
                                    ),
                                    Container(
                                        padding=padding.only(left=10, right=20),  # Add padding to the entire container
                                        content=Row(
                                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                Text("Appointment Status", color="BLACK", size=12,
                                                     weight=FontWeight.BOLD,
                                                     width=90),
                                                Text(" :   ", color="BLACK", size=12),
                                                Text(value=appointment[3], color="BLACK", size=12,
                                                     text_align=TextAlign.JUSTIFY,
                                                     weight=FontWeight.W_600, width=160)
                                            ]
                                        )
                                    ),
                                    Container(
                                        padding=padding.only(left=10, right=20, bottom=10),
                                        # Add padding to the entire container
                                        content=Row(
                                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                Text("Doctor name", color="BLACK", size=12, weight=FontWeight.BOLD,
                                                     width=90),
                                                Text(" :   ", color="BLACK", size=12),
                                                Text(value=appointment[6], color="BLACK", size=12,
                                                     weight=FontWeight.W_600,
                                                     text_align=TextAlign.JUSTIFY, width=160)
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

        return View(
            "/clinicViewAppointment/:clinic_id",
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
                                controls=[
                                    Container(width=350,
                                              height=70,
                                              bgcolor=blue,
                                              alignment=alignment.top_center,
                                              content=Row(
                                                  width=340,
                                                  alignment="spaceBetween",
                                                  controls=[
                                                      Container(
                                                          padding=padding.only(left=10, top=15),
                                                          content=Image(
                                                              src="pic/back.png",
                                                              color=colors.WHITE,
                                                              width=20,
                                                              height=20
                                                          ),
                                                          on_click=lambda _: page.go(f"/clinicHomepage/{clinic_id}")
                                                      ),

                                                      Container(
                                                          padding=padding.only(top=15),
                                                          content=Text("Appointment List",
                                                                       color="WHITE",
                                                                       text_align=TextAlign.CENTER,
                                                                       size=20,
                                                                       font_family="RobotoSlab"
                                                                       )
                                                                       ),

                                                      Container(
                                                          padding=padding.only(top=15),
                                                          content=IconButton(
                                                              icons.ADD_CHART,
                                                              icon_size=25,
                                                              icon_color=colors.WHITE,
                                                              on_click=lambda _: page.go(
                                                                  f"/clinicViewAppointmentChart/{clinic_id}"),

                                                          ),
                                                      ),
                                                  ]
                                              ))
                                ]
                            )

                            # Row(
                            #     alignment=MainAxisAlignment.CENTER,
                            #     controls=[
                            #         Container(
                            #             padding=padding.only(right=120),
                            #             width=350,
                            #             height=80,
                            #             bgcolor="#3386C5",
                            #             content=Row(
                            #                 width=340,
                            #                 alignment="center",
                            #                 controls=[
                            #                     Container(
                            #                         padding=padding.only(left=10, top=5),
                            #                         content=Image(
                            #                             src="pic/back.png",
                            #                             color=colors.WHITE,
                            #                             width=20,
                            #                             height=20
                            #                         ),
                            #                         on_click=lambda _: page.go(f"/clinicHomepage/{clinic_id}")
                            #                     ),
                            #
                            #                     Container(
                            #                         padding=padding.only(left=0),
                            #                         content=Text("Appointment List",
                            #                                      color="WHITE",
                            #                                      text_align=TextAlign.CENTER,
                            #                                      size=20,
                            #                                      font_family="RobotoSlab"
                            #                                      )
                            #                                      ),
                            #                     Container(
                            #                         # padding=padding.only(left=20),
                            #                         content=IconButton(
                            #                             icons.ADD_CHART,
                            #                             icon_size=25,
                            #                             icon_color=colors.WHITE,
                            #                             on_click=lambda _: page.go(
                            #                                 f"/clinicViewAppointmentChart/{clinic_id}"),
                            #
                            #                         ),
                            #                     )
                            #                 ])
                            #
                            #         )
                            #     ]
                            # )
                            ,
                            display_patient(appointments),

                            Container(
                                margin=margin.only(bottom=20)
                            )
                        ])
                )
            ])
