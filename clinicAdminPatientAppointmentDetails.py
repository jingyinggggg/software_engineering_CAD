from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminPatientAppointmentDetails:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        booking_id = int(params.booking_id)
        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        c = db.cursor()
        c.execute("""
                        SELECT booking.*, users.* , doctors.fullName
                        FROM booking
                        INNER JOIN users ON booking.patientID = users.id
                        INNER JOIN doctors ON booking.doctorID = doctors.id
                        WHERE bookingID = ?
                    """, (booking_id,))
        record = c.fetchall()

        print(record)

        return View(
            "/admin/clinicAdminPatientAppointmentDetails/:user_id:booking_id",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    border_radius=30,
                    bgcolor="#F4F4F4",
                    content=Column(
                        controls=[
                            Container(
                                padding=padding.only(top=25, left=10),
                                content=Column(
                                    controls=[
                                        Container(
                                            content=Image(
                                                src="pic/back.png",
                                                width=20,
                                                height=20
                                            ),
                                            on_click=lambda _: page.go(
                                                f"/admin/clinicAdminPatientAppointmentList/{user_id}")
                                        ),
                                        Container(
                                            Text(
                                                value="Appointment Details",
                                                color="#3386C5",
                                                weight=FontWeight.W_600,
                                                size=18,
                                            ),
                                        ),
                                    ]
                                )
                            ),
                            Container(
                                width=350,
                                alignment=alignment.center,
                                content=
                                Container(
                                    bgcolor=colors.WHITE,
                                    width=330,
                                    height=500,
                                    padding=padding.all(5),
                                    border_radius=border_radius.all(15),
                                    border=border.all(color="#D3D3D3", width=2),
                                    content=Column(
                                        spacing=0,
                                        controls=[
                                            Container(
                                                Text(
                                                    value=f"Completed" if record[0][9] == 2 else "Upcoming",
                                                    color="#1BC100" if record[0][9] == 2 else "#000000",
                                                    size=15,
                                                    weight=FontWeight.W_500
                                                )
                                            ),
                                            Container(
                                                alignment=alignment.top_right,
                                                content=
                                                Text(
                                                    value=f"Booking ID: {record[0][0]}",
                                                    color=colors.BLACK,
                                                    size=16,
                                                )
                                            ),
                                            Container(
                                                alignment=alignment.top_right,
                                                content=
                                                Text(
                                                    value=f"{record[0][3]} | {record[0][4]}",
                                                    color=colors.BLACK,
                                                    size=18,
                                                    weight=FontWeight.W_600,
                                                )
                                            ),
                                            Container(
                                                alignment=alignment.top_right,
                                                content=
                                                Text(
                                                    value=f"Appointment With Dr. {record[0][26]}",
                                                    color="#3386C5",
                                                    size=18,
                                                    weight=FontWeight.W_600,
                                                )
                                            ),
                                            Container(
                                                alignment=alignment.top_right,
                                                content=
                                                Text(
                                                    value=f"{record[0][5]}",
                                                    color=colors.BLACK,
                                                    size=15,
                                                    weight=FontWeight.W_600,
                                                )
                                            ),
                                            Container(
                                                alignment=alignment.top_right,
                                                content=
                                                Text(
                                                    value=f"Reason: {record[0][7]}",
                                                    color=colors.BLACK,
                                                    size=15,
                                                    weight=FontWeight.W_600,
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=5, top=50, right=20),
                                                # Add padding to the entire container
                                                content=Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Patient ID",
                                                             color="BLACK",
                                                             size=15,
                                                             weight=FontWeight.W_600,
                                                             width=140),

                                                        Text(":",
                                                             color="BLACK",
                                                             size=15),

                                                        Text(value=f"{record[0][1]}",
                                                             color="BLACK",
                                                             size=15,
                                                             text_align=TextAlign.CENTER,
                                                             weight=FontWeight.W_600,
                                                             width=170)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=5, top=5, right=20),
                                                # Add padding to the entire container
                                                content=Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Patient Name",
                                                             color="BLACK",
                                                             size=15,
                                                             weight=FontWeight.W_600,
                                                             width=140),

                                                        Text(":",
                                                             color="BLACK",
                                                             size=15),

                                                        Text(value=f"{record[0][17]}",
                                                             color="BLACK",
                                                             size=15,
                                                             text_align=TextAlign.CENTER,
                                                             weight=FontWeight.W_600,
                                                             width=170)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=5, top=5, right=20),
                                                # Add padding to the entire container
                                                content=Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Patient Email",
                                                             color="BLACK",
                                                             size=15,
                                                             weight=FontWeight.W_600,
                                                             width=140),

                                                        Text(":",
                                                             color="BLACK",
                                                             size=15),

                                                        Text(value=f"{record[0][19]}",
                                                             color="BLACK",
                                                             size=15,
                                                             text_align=TextAlign.CENTER,
                                                             weight=FontWeight.W_600,
                                                             width=170)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=5, top=5, right=20),
                                                # Add padding to the entire container
                                                content=Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Patient Contact",
                                                             color="BLACK",
                                                             size=15,
                                                             weight=FontWeight.W_600,
                                                             width=140),

                                                        Text(":",
                                                             color="BLACK",
                                                             size=15),

                                                        Text(value=f"{record[0][20]}",
                                                             color="BLACK",
                                                             size=15,
                                                             text_align=TextAlign.CENTER,
                                                             weight=FontWeight.W_600,
                                                             width=170)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=5, top=5, right=20),
                                                # Add padding to the entire container
                                                content=Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Patient Birth",
                                                             color="BLACK",
                                                             size=15,
                                                             weight=FontWeight.W_600,
                                                             width=140),

                                                        Text(":",
                                                             color="BLACK",
                                                             size=15),

                                                        Text(value=f"{record[0][22]}",
                                                             color="BLACK",
                                                             size=15,
                                                             text_align=TextAlign.CENTER,
                                                             weight=FontWeight.W_600,
                                                             width=170)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=5, top=5, right=20),
                                                # Add padding to the entire container
                                                content=Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Patient Gender",
                                                             color="BLACK",
                                                             size=15,
                                                             weight=FontWeight.W_600,
                                                             width=140),

                                                        Text(":",
                                                             color="BLACK",
                                                             size=15),

                                                        Text(value=f"{record[0][23]}",
                                                             color="BLACK",
                                                             size=15,
                                                             text_align=TextAlign.CENTER,
                                                             weight=FontWeight.W_600,
                                                             width=170)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=5, top=5, right=20),
                                                # Add padding to the entire container
                                                content=Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Patient Address",
                                                             color="BLACK",
                                                             size=15,
                                                             weight=FontWeight.W_600,
                                                             width=140),

                                                        Text(":",
                                                             color="BLACK",
                                                             size=15),

                                                        Text(value=f"{record[0][24]}",
                                                             color="BLACK",
                                                             size=15,
                                                             text_align=TextAlign.CENTER,
                                                             weight=FontWeight.W_600,
                                                             width=170)
                                                    ]
                                                )
                                            ),
                                            Container(
                                                padding=padding.only(left=5, top=5, right=20),
                                                # Add padding to the entire container
                                                content=Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Patient Emergency Contact",
                                                             color="BLACK",
                                                             size=15,
                                                             weight=FontWeight.W_600,
                                                             width=140),

                                                        Text(":",
                                                             color="BLACK",
                                                             size=15),

                                                        Text(value=f"{record[0][25]}",
                                                             color="BLACK",
                                                             size=15,
                                                             text_align=TextAlign.CENTER,
                                                             weight=FontWeight.W_600,
                                                             width=170)
                                                    ]
                                                )
                                            ),
                                        ]
                                    )
                                ),
                            )
                        ]
                    )
                )
            ]
        )
