import time

from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminPatientAppointmentList:
    def __init__(self):
        pass

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

        currentDate = datetime.date.today()
        formatted_date = currentDate.strftime("%d %B %Y")
        test_date = "12 November 2023"

        def createAppointmentList(count, records):
            return Column(
                controls=[
                    Row(
                        width=330,
                        spacing=5,
                        controls=[
                            Container(
                                margin=margin.only(left=3, bottom=15),
                                width=10,
                                height=10,
                                bgcolor="#1BC100" if records[9] == 2 else "#AEAEAE",
                                border_radius=20,
                                on_click=lambda _: page.go(
                                    f"/admin/clinicAdminPatientAppointmentDetails/{user_id}{records[0]}")
                            ),
                            Column(
                                spacing=0,
                                controls=[
                                    Row(
                                        spacing=2,
                                        controls=[
                                            Text(
                                                value=f"{count}. {records[5]} ",
                                                color=colors.BLACK,
                                                size=11,
                                                weight=FontWeight.W_700,
                                            ),
                                            Container(
                                                width=55,
                                                alignment=alignment.top_right,
                                                content=
                                                Text(
                                                    value=records[4],
                                                    color=colors.BLACK,
                                                    size=12,
                                                    weight=FontWeight.W_600,
                                                ),
                                            )

                                        ]
                                    ),
                                    Row(
                                        spacing=2,
                                        controls=[
                                            Text(
                                                value=f"Patient name: {records[15]}",
                                                color=colors.BLACK,
                                                size=11,
                                                weight=FontWeight.W_700,
                                            ),
                                            Container(
                                                width=155,
                                                alignment=alignment.top_right,
                                                content=
                                                Text(
                                                    value=f"Doctor {records[24]}",
                                                    color=colors.BLACK,
                                                    weight=FontWeight.W_600,
                                                    size=12,
                                                ),
                                            )

                                        ]
                                    ),
                                ]
                            ),

                        ]

                    )
                ]
            )

        def getAppointmentList(user_id, date):
            c = db.cursor()
            c.execute("""
                SELECT booking.*, users.* , doctors.fullName
                FROM booking
                INNER JOIN users ON booking.patientID = users.id
                INNER JOIN doctors ON booking.doctorID = doctors.id
                WHERE booking.bookingStatus IN (1,2) AND booking.clinicID = ? AND booking.appointmentDate = ?
                ORDER BY booking.bookingID ASC
            """, (user_id, date))
            record = c.fetchall()

            AppointmentListContainer = []

            available = False
            if record:
                available = True
                count = 1
                for records in record:
                    AppointmentListContainer.append(createAppointmentList(count, records))
                    count += 1

            return Container(width=330, content=Column(
                controls=AppointmentListContainer)) if available is True \
                else Container(width=330, content=Text(value="There are no appointment currently",color=colors.RED,size=11,weight=FontWeight.W_600))

        getItem = getAppointmentList(user_id, formatted_date)
        print(getItem)

        def getUpcomingAppointmentDetails(user_id):

            d = db.cursor()
            d.execute("""
                SELECT booking.appointmentDate
                FROM booking 
                WHERE booking.bookingStatus IN (1,2) AND booking.clinicID = ? AND booking.appointmentDate > ?
                ORDER BY booking.bookingID ASC
            """, (user_id, formatted_date))
            record = d.fetchall()
            filterRecord = []

            for x in record:
                if x not in filterRecord:
                    filterRecord.append(x)

            bg_container_list = []

            def getUpcomingItem(user_id, date):
                e = db.cursor()
                e.execute("""
                                SELECT booking.*, users.* , doctors.fullName
                                FROM booking
                                INNER JOIN users ON booking.patientID = users.id
                                INNER JOIN doctors ON booking.doctorID = doctors.id
                                WHERE booking.bookingStatus IN (1,2) AND booking.clinicID = ? AND booking.appointmentDate = ?
                                ORDER BY booking.bookingID ASC
                            """, (user_id, date))
                UpcomingRecord = e.fetchall()

                print(UpcomingRecord)

                UpcomingAppointmentListContainer = []

                if UpcomingRecord:
                    count = 1
                    for upcomingRecords in UpcomingRecord:
                        UpcomingAppointmentListContainer.append(createAppointmentList(count, upcomingRecords))
                        count += 1

                return Container(width=330, content=Column(controls=UpcomingAppointmentListContainer))

            if record:
                print(filterRecord)
                for records in filterRecord:
                    bg_container = Container(
                        padding=padding.only(bottom=10),
                        alignment=alignment.center,
                        content=
                        Column(
                            spacing=1,
                            controls=[
                                Container(
                                    content=Row(
                                        width=330,
                                        controls=[
                                            Container(
                                                Text(
                                                    value="Upcoming on" if records == filterRecord[0] else "",
                                                    color=colors.BLACK,
                                                    size=20,
                                                    weight=FontWeight.W_700,
                                                )
                                            ),
                                            Container(
                                                width=190 if records == filterRecord[0] else 315,
                                                height=10,
                                                content=Column(
                                                    controls=[
                                                        Container(
                                                            alignment=alignment.bottom_right,
                                                            content=Text(
                                                                value=records[0],
                                                                color=colors.BLACK,
                                                                size=15,
                                                                weight=FontWeight.W_600,
                                                            )
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]
                                    )
                                ),
                                Container(
                                    bgcolor=colors.WHITE,
                                    width=330,
                                    padding=padding.only(top=5, bottom=5),
                                    border_radius=border_radius.all(15),
                                    border=border.all(color="#D3D3D3", width=2),
                                    content=getUpcomingItem(user_id, records[0])
                                )
                            ]
                        )
                    )
                    bg_container_list.append(bg_container)

            return Column(spacing=1, alignment=alignment.center, controls=bg_container_list, width=350)

        getUpcomingDate = getUpcomingAppointmentDetails(user_id)

        return View(
            "/admin/clinicAdminPatientAppointmentList/:user_id",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    border_radius=30,
                    bgcolor="#F4F4F4",
                    content=Column(
                        scroll=True,
                        spacing=5,
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
                                            on_click=lambda _: page.go(f"/login/adminHomepage/{user_id}")
                                        ),
                                        Container(
                                            Text(
                                                value="Patient Appointment List",
                                                color="#3386C5",
                                                weight=FontWeight.W_600,
                                                size=18,
                                            ),
                                        )
                                    ]
                                )
                            ),
                            Container(
                                padding=padding.only(left=10),
                                content=Row(
                                    controls=[
                                        Container(
                                            width=8,
                                            height=8,
                                            bgcolor="#1BC100",
                                            border_radius=20,
                                        ),
                                        Container(
                                            content=Text(
                                                value="Completed",
                                                color="#404040",
                                                weight=FontWeight.W_600,
                                                size=11,
                                            )
                                        ),
                                        Container(
                                            width=8,
                                            height=8,
                                            bgcolor="#AEAEAE",
                                            border_radius=20,
                                        ),
                                        Container(
                                            content=Text(
                                                value="Upcoming",
                                                color="#404040",
                                                weight=FontWeight.W_600,
                                                size=11,
                                            )
                                        ),
                                    ]
                                )
                            ),
                            Container(
                                alignment=alignment.center,
                                content=Column(
                                    spacing=1,
                                    controls=[
                                        Container(
                                            content=Row(
                                                width=330,
                                                controls=[
                                                    Container(
                                                        Text(
                                                            value="Today",
                                                            color=colors.BLACK,
                                                            size=25,
                                                            weight=FontWeight.W_700,
                                                        )
                                                    ),
                                                    Container(
                                                        width=250,
                                                        height=10,
                                                        content=Column(
                                                            controls=[
                                                                Container(
                                                                    alignment=alignment.bottom_right,
                                                                    content=
                                                                    Text(
                                                                        value=formatted_date,
                                                                        color=colors.BLACK,
                                                                        size=15,
                                                                        weight=FontWeight.W_700,
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            )
                                        ),
                                        Container(
                                            bgcolor=colors.WHITE,
                                            width=330,
                                            padding=padding.only(top=5, bottom=5),
                                            border_radius=border_radius.all(15),
                                            border=border.all(color="#D3D3D3", width=2),
                                            content=getItem
                                        ),
                                    ]
                                ),
                            ),
                            getUpcomingDate
                        ]
                    )
                )
            ]
        )
