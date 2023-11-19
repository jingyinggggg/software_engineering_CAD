from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminUpdateAppointmentPage:
    def __init__(self):
        self.show_sidebar = False

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

        grey = "#71839B"

        # Get the appointment details which has updated with the visit proof
        def get_appointment_details():
            c = db.cursor()
            c.execute("SELECT * FROM booking INNER JOIN clinicAdmin "
                      "ON booking.clinicID = clinicAdmin.clinicID WHERE booking.proof != '' "
                      "AND booking.bookingStatus = 1")
            record = c.fetchall()

            return record

        appointment_record = get_appointment_details()

        def get_patient_details(data):
            c = db.cursor()
            c.execute(f"SELECT * FROM users WHERE id = {data}")
            patient_details = c.fetchall()

            patient_name = patient_details[0][1]

            return patient_name


        def displayAppointment(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/admin/clinicAdminUpdateAppointmentDetails/{user_id}{record_id}")

                    record_container = Container(
                        alignment=alignment.center,
                        content=Column(
                            spacing=0,
                            controls=[
                                Container(
                                    margin=margin.only(left=10, right=10, bottom=20),
                                    padding=padding.only(left=10, right=10, top=10, bottom=10),
                                    border_radius=15,
                                    border=border.all(1, "#D3D3D3"),
                                    content=Row(
                                        controls=[
                                            Container(
                                                margin=margin.only(left=10, right=10),
                                                content=Image(
                                                    src="pic/appointmentList.png",
                                                    width=60,
                                                    height=60
                                                )

                                            ),

                                            Container(
                                                content=Column(
                                                    controls=[
                                                        Container(
                                                            content=Text(
                                                                value=f"Patient: {get_patient_details(record[1])}",
                                                                size=11,
                                                                color=colors.BLACK,
                                                                weight=FontWeight.W_600
                                                            )
                                                        ),

                                                        Container(
                                                            content=Text(
                                                                value=f"Appointment Date: {record[3]}",
                                                                size=11,
                                                                color=colors.BLACK,
                                                                weight=FontWeight.W_600
                                                            )
                                                        ),

                                                        Container(
                                                            content=Text(
                                                                value=f"Appointment Time: {record[4]}",
                                                                size=11,
                                                                color=colors.BLACK,
                                                                weight=FontWeight.W_600
                                                            )
                                                        ),

                                                        Container(
                                                            content=Text(
                                                                value="Patient has visited the doctor successfully and doctor has submitted the evidence.",
                                                                size=10,
                                                                color=colors.BLUE_GREY_600,
                                                                width=210,
                                                                text_align=TextAlign.JUSTIFY,
                                                                weight=FontWeight.W_600
                                                            )
                                                        ),
                                                    ]
                                                )
                                            )
                                        ]
                                    ),
                                    on_click=on_more_button_click()
                                )
                            ]
                        )
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

            else:
                return Container(
                    alignment=alignment.center,
                    margin=margin.only(left=20, right=20, top=150),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Image(
                                src="pic/appointmentStatus.png",
                                width=120,
                                height=120
                            ),
                            Container(
                                margin=margin.only(top=10),
                                content=Text(
                                    value="There are no appointment pending updated the appointment status currently.",
                                    color=colors.BLACK,
                                    # font_family="RobotoSlab",
                                    text_align=TextAlign.CENTER
                                )
                            )
                            ,
                        ]
                    )
                )

        return View(
            "/admin/clinicAdminUpdateAppointment/:user_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#F4F4F4",
                    border_radius=30,
                    content=Column(
                        controls=[
                            Container(
                                padding=padding.only(top=25, left=10, bottom=10),
                                content=Row(
                                    controls=[
                                        Container(
                                            content=Image(
                                                src="pic/back.png",
                                                color="#3386C5",
                                                width=20,
                                                height=20
                                            ),
                                            on_click=lambda _: page.go(f"/login/adminHomepage/{user_id}")
                                        ),
                                        Text(
                                            value=" Update Appointment Status",
                                            color="#3386C5",
                                            weight=FontWeight.W_600,
                                            size=18,
                                        )
                                    ]
                                ),
                            ),

                            displayAppointment(appointment_record)
                        ]
                    )
                )
            ]

        )
