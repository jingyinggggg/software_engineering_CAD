import time

from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class AdminPatientRequestList:
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

        yes_dialog = AlertDialog(
            modal=True,
            title=Text("Success"),
            content=Text(f"You have scheduled the appointment successfully!"),
            actions=[
                TextButton("Done", on_click=lambda _:page.go(f"/login/adminHomepage/{user_id}")),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        def open_dlg():
            page.dialog = yes_dialog
            yes_dialog.open = True
            page.update()

        a = "testing"

        dialog = Container(
            border_radius=30,
            margin=margin.only(top=40, left=10, right=10),
            border=border.all(color="#D3D3D3", width=2),
            bgcolor=colors.WHITE,
            height=400,
            alignment=alignment.center,
            content=Text(
                value=a,
                color=colors.RED,
            ),
            offset=transform.Offset(0, 2),
            animate_offset=animation.Animation(duration=300)
        )

        reject_reason = TextField(
            label="Enter the reject reason",
            label_style=TextStyle(size=12,
                                  color=colors.BLACK,
                                  weight=FontWeight.W_500),
            border_color=colors.BLACK,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                  weight=FontWeight.W_500),
            multiline=True
        )

        def accept_request(bookingId):
            # print(bookingId)
            c = db.cursor()
            c.execute(
                f"UPDATE booking SET appointmentStatus = ?, bookingStatus = ? WHERE bookingID = ?",
                ("Scheduled", 1, bookingId)
            )
            db.commit()
            open_dlg()



        # def update_booking_status_to_reject(recordID):
        #     c = db.cursor()
        #     c.execute("UPDATE booking SET appointmentStatus = ?, bookingStatus = ?, rejectReason = ?, "
        #               "reassignDoctorID = ? WHERE bookingID = ?",("Rejected", -1, reject_reason.value, available.value, recordID))

        available = Dropdown(
            dense=True,
            label="Assign new doctor to current patient",
            border_color=colors.BLACK,
            height=60,
            label_style=TextStyle(size=12,
                                  color=colors.BLACK,
                                  weight=FontWeight.W_500),
            options=[
                dropdown.Option("None"),
            ],
            text_style=TextStyle(color="#71839B",
                                 size=12,
                                 weight=FontWeight.W_500),

        )

        def get_request_booking(user_id):
            c = db.cursor()
            c.execute("""
                SELECT booking.*, users.* , doctors.fullName
                FROM booking
                INNER JOIN users ON booking.patientID = users.id
                INNER JOIN doctors ON booking.doctorID = doctors.id
                WHERE booking.bookingStatus = ? AND booking.clinicID = ?
                ORDER BY booking.bookingID ASC
            """, (0, user_id))
            record = c.fetchall()

            list_containers = []

            def get_clinic_doctor(date, time):
                c = db.cursor()
                c.execute(
                    "SELECT doctors.id FROM booking INNER JOIN doctors ON booking.doctorID = doctors.id WHERE appointmentDate = ? AND appointmentTime = ? AND bookingStatus = 1",
                    (date, time))
                NAdoctorList = c.fetchall()

                # Extracting doctor IDs from NAdoctorList
                excluded_doctor_ids = [doctor[0] for doctor in NAdoctorList]

                if excluded_doctor_ids:
                    c.execute("SELECT id, fullName FROM doctors WHERE id NOT IN ({}) AND clinicID = ?".format(
                        ','.join('?' * len(excluded_doctor_ids))), (*excluded_doctor_ids, user_id))
                else:
                    c.execute("SELECT id, fullName FROM doctors WHERE clinicID = ?", (user_id,))

                AvailableDoctorList = c.fetchall()

                available.options.clear()

                if len(AvailableDoctorList) != 0:
                    available.options.append(dropdown.Option("None"))
                    for AvailableDoctorLists in AvailableDoctorList:
                        available.options.append(dropdown.Option(AvailableDoctorLists[1]))
                        # print(available.value)
                else:
                    available.options.append(dropdown.Option("None"))

                return available

            def showDialog(records, callFrom):
                print(records)
                for x in list_containers:
                    x.visible = False

                dialog.content = []

                # Add new content based on the 'records' parameter
                if callFrom == "Accept":
                    dialog.content = Container(
                        padding=padding.only(top=10),
                        alignment=alignment.center,
                        content=
                        Column(
                            controls=[
                                Container(
                                    padding=padding.only(right=10),
                                    alignment=alignment.top_right,
                                    content=Image(
                                        src="pic/close.png",
                                        width=20,
                                        height=20
                                    ),
                                    on_click=lambda e: closeDialog(e),
                                ),
                                Container(
                                    padding=padding.only(left=5, right=10),
                                    width=310,
                                    content=Row(
                                        controls=[
                                            Container(
                                                content=Column(
                                                    spacing=1,
                                                    controls=[

                                                        Text(color="#6A6A6A", weight=FontWeight.W_600,
                                                             value=f"Patient Name: "),
                                                        Text(color="#6A6A6A", weight=FontWeight.W_600,
                                                             value=f"Date | Time:"),
                                                        Text(color="#6A6A6A", weight=FontWeight.W_600,
                                                             value=f"Doctor:"),
                                                        # Add more Text controls as needed
                                                    ]
                                                )
                                            ),
                                            Container(
                                                width=205,
                                                content=Column(

                                                    spacing=1,
                                                    controls=[
                                                        Container(
                                                            alignment=alignment.top_right,
                                                            content=
                                                            Text(color=colors.BLACK, weight=FontWeight.W_600,
                                                                 value=records[16], ),
                                                            # Add more Text controls as needed
                                                        ),
                                                        Container(
                                                            alignment=alignment.top_right,
                                                            content=
                                                            Text(color=colors.BLACK, weight=FontWeight.W_600,
                                                                 value=f"{records[3]} | {records[4]}"),
                                                            # Add more Text controls as needed
                                                        ),
                                                        Container(
                                                            alignment=alignment.top_right,
                                                            content=
                                                            Text(color=colors.BLACK, weight=FontWeight.W_600,
                                                                 value=f"Dr. {records[25]}"),
                                                            # Add more Text controls as needed
                                                        )
                                                    ]
                                                ),
                                            ),

                                        ],
                                    )
                                ),
                                Container(
                                    width=310,
                                    alignment=alignment.center,
                                    padding=padding.only(top=20),
                                    content=Image(
                                        src="pic/question.png",
                                        width=100,
                                        height=100,
                                    )
                                ),
                                Container(
                                    padding=padding.only(top=20),
                                    content=Container(
                                        alignment=alignment.center,
                                        content=
                                        Text(
                                            text_align=alignment.center,
                                            value="Are you sure want to accept this appointment?",
                                            color=colors.BLACK,
                                            weight=FontWeight.W_600,
                                        )

                                    ),
                                ),

                                Container(
                                    width=320,
                                    height=50,
                                    alignment=alignment.center,
                                    padding=padding.only(top=15),
                                    content=Container(
                                        width=260,
                                        alignment=alignment.center,
                                        content=
                                        Row(
                                            alignment=alignment.center,
                                            spacing=20,
                                            controls=[
                                                Container(
                                                    width=120,
                                                    padding=padding.only(right=0),
                                                    content=Container(
                                                        border_radius=border_radius.all(8),
                                                        alignment=alignment.center,
                                                        width=95,
                                                        height=80,
                                                        bgcolor="#FFC107",
                                                        content=Text(
                                                            value="Yes",
                                                            color=colors.WHITE,
                                                            size=18,
                                                            weight=FontWeight.W_500,
                                                        ),

                                                        on_click=lambda e: accept_request(records[0])
                                                    ),
                                                ),
                                                Container(
                                                    width=120,
                                                    padding=padding.only(left=0),
                                                    content=Container(
                                                        border_radius=border_radius.all(8),
                                                        alignment=alignment.center,
                                                        width=95,
                                                        height=80,
                                                        border=border.all(2, "#FFC107"),
                                                        bgcolor=colors.WHITE,
                                                        content=Text(
                                                            value="No",
                                                            color="#FFC107",
                                                            size=18,
                                                            weight=FontWeight.W_500,
                                                        ),
                                                        on_click=lambda e: closeDialog(e),
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ),
                            ]
                        )
                    )
                elif callFrom == "Reject":
                    dialog.content = Container(
                        padding=padding.only(top=10),
                        alignment=alignment.center,
                        content=
                        Column(
                            controls=[
                                Container(
                                    padding=padding.only(right=10),
                                    alignment=alignment.top_right,
                                    content=Image(
                                        src="pic/close.png",
                                        width=20,
                                        height=20
                                    ),
                                    on_click=lambda e: closeDialog(e),
                                ),
                                Container(
                                    padding=padding.only(left=5, right=10),
                                    width=310,
                                    content=Row(
                                        controls=[
                                            Container(
                                                content=Column(
                                                    spacing=1,
                                                    controls=[

                                                        Text(color="#6A6A6A", weight=FontWeight.W_600,
                                                             value=f"Patient Name: "),
                                                        Text(color="#6A6A6A", weight=FontWeight.W_600,
                                                             value=f"Date | Time:"),
                                                        Text(color="#6A6A6A", weight=FontWeight.W_600,
                                                             value=f"Doctor:"),
                                                        # Add more Text controls as needed
                                                    ]
                                                )
                                            ),
                                            Container(
                                                width=205,
                                                content=Column(

                                                    spacing=1,
                                                    controls=[
                                                        Container(
                                                            alignment=alignment.top_right,
                                                            content=
                                                            Text(color=colors.BLACK, weight=FontWeight.W_600,
                                                                 value=records[16], ),
                                                            # Add more Text controls as needed
                                                        ),
                                                        Container(
                                                            alignment=alignment.top_right,
                                                            content=
                                                            Text(color=colors.BLACK, weight=FontWeight.W_600,
                                                                 value=f"{records[3]} | {records[4]}"),
                                                            # Add more Text controls as needed
                                                        ),
                                                        Container(
                                                            alignment=alignment.top_right,
                                                            content=
                                                            Text(color=colors.BLACK, weight=FontWeight.W_600,
                                                                 value=f"Dr. {records[25]}"),
                                                            # Add more Text controls as needed
                                                        ),

                                                    ]
                                                ),
                                            ),
                                        ],
                                    )
                                ),

                                Container(
                                    margin=margin.only(left=10, top=20),
                                    alignment=alignment.top_left,
                                    content=
                                    Text(
                                        "Reject Reason",
                                        size=12,
                                        color=colors.BLACK)
                                ),

                                Container(
                                    margin=margin.only(left=10, right=10),
                                    content=reject_reason
                                ),

                                Container(
                                    margin=margin.only(left=10, top=10),
                                    alignment=alignment.top_left,
                                    content=
                                    Text(
                                        "Assign New Doctor",
                                        size=12,
                                        color=colors.BLACK)
                                ),

                                Container(
                                    margin=margin.only(left=10, right=10),
                                    content=get_clinic_doctor(records[3], records[4])
                                ),

                                Container(
                                    margin=margin.only(right=10),
                                    alignment=alignment.bottom_right,
                                    content=IconButton(content=Text("Submit",
                                                                    size=12,
                                                                    color=colors.BLACK,
                                                                    text_align=TextAlign.CENTER,
                                                                    weight=FontWeight.W_700),
                                                       width=100,
                                                       height=40,
                                                       style=ButtonStyle(bgcolor={"": colors.BLUE_400},
                                                                         shape={
                                                                             "": RoundedRectangleBorder(
                                                                                 radius=7)}
                                                                         ),
                                                       # on_click=update_booking_status_to_reject(record[0])
                                                       )
                                )

                            ]
                        )
                    )

                dialog.offset = transform.Offset(0, 0)
                page.update()

            def closeDialog(e):
                for x in list_containers:
                    x.visible = True

                dialog.offset = transform.Offset(0, 2)
                page.update()

                # Clear the selected value in the dropdown
                available.value = None

                # Check if "None" option exists in the dropdown options
                none_option_index = next((i for i, option in enumerate(available.options) if option.value == "None"),
                                         None)

                # Preserve "None" and clear other options
                if none_option_index is not None:
                    none_option = available.options[none_option_index]
                    # Clear all options except the "None" option
                    available.options = [none_option]

            if record:
                count = 1
                for records in record:
                    list_container = Container(
                        alignment=alignment.center,
                        content=Column(
                            spacing=0,
                            controls=[
                                Container(
                                    bgcolor=colors.WHITE,
                                    width=330,
                                    height=160,
                                    border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15),
                                    border=border.all(color="#D3D3D3", width=2),
                                    content=Row(
                                        spacing=0,
                                        alignment=alignment.center,
                                        height=150,
                                        controls=[
                                            Column(
                                                width=80,
                                                height=150,
                                                spacing=0,
                                                controls=[
                                                    Container(
                                                        margin=margin.only(left=5),
                                                        alignment=alignment.top_left,
                                                        content=Text(
                                                            value=f"Patient {count}",
                                                            color="#A9A9A9",
                                                            size=11,
                                                        )
                                                    ),
                                                    Container(
                                                        height=100,
                                                        alignment=alignment.center,
                                                        content=Image(
                                                            src="pic/male_patient.png" if records[21] == "Male" else "pic/female_patient.png",
                                                            width=65,
                                                        )
                                                    ),
                                                    Container(
                                                        alignment=alignment.bottom_center,
                                                        content=Text(
                                                            value=records[16],
                                                            color=colors.BLACK,
                                                            size=12,
                                                            weight=FontWeight.W_600,
                                                        )
                                                    ),
                                                ]
                                            ),
                                            Container(
                                                padding=padding.only(left=2),
                                                content=
                                                Column(
                                                    width=250,
                                                    controls=[
                                                        Column(
                                                            height=8,
                                                            controls=[
                                                                Text(
                                                                    color=colors.BLACK,
                                                                    value=records[5],
                                                                    size=12,
                                                                )
                                                            ]
                                                        ),
                                                        Row(
                                                            width=200,
                                                            # Increase the width to accommodate both titles and data
                                                            height=150,
                                                            spacing=0,
                                                            controls=[
                                                                # Left side (titles)
                                                                Column(
                                                                    width=85,
                                                                    spacing=0,
                                                                    controls=[
                                                                        Text(
                                                                            value="Doctor",
                                                                            size=12,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value="Date | Time",
                                                                            size=12,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value="Reason",
                                                                            size=12,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value="Date of Birth",
                                                                            size=12,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value="Mobile No",
                                                                            size=12,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value="Gender",
                                                                            size=12,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value="Address",
                                                                            size=12,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                    ],
                                                                ),
                                                                # Right side (data)
                                                                Column(
                                                                    width=165,
                                                                    spacing=1.3,
                                                                    controls=[
                                                                        Text(
                                                                            value=f"DR.{records[25]}",
                                                                            size=11,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value=f"{records[3]} | {records[4]}",
                                                                            size=11,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value=f"{records[7]}",
                                                                            size=11,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value=f"{records[21]}",
                                                                            size=11,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value=f"{records[19]}",
                                                                            size=11,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value=f"{records[22]}",
                                                                            size=11,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                        Text(
                                                                            value=f"{records[23]}",
                                                                            size=11,
                                                                            color=colors.BLACK,
                                                                            weight=FontWeight.W_600,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ]
                                                        )

                                                    ]
                                                ),
                                            )
                                        ]
                                    )
                                ),
                                Container(
                                    width=330,
                                    height=30,
                                    alignment=alignment.top_right,
                                    content=Row(
                                        width=150,
                                        spacing=0,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                width=75,
                                                height=30,
                                                bgcolor="#7DEB6B",
                                                content=Text(
                                                    value="Accept",
                                                    color=colors.BLACK,
                                                    size=12,
                                                    weight=FontWeight.W_500,
                                                ),
                                                on_click=lambda e, r=records: showDialog(r, "Accept"),
                                            ),
                                            Container(
                                                alignment=alignment.center,
                                                width=75,
                                                height=30,
                                                bgcolor="#F25757",
                                                content=Text(
                                                    value="Reject",
                                                    color=colors.BLACK,
                                                    size=12,
                                                    weight=FontWeight.W_500,
                                                ),
                                                on_click=lambda e, r=records: showDialog(r, "Reject"),
                                            )
                                        ]
                                    )
                                ),
                            ],
                        )
                    )
                    count = count + 1
                    list_containers.append(list_container)

                return Container(width=330, content=Column(controls=list_containers))
            else:
                return Container(
                    alignment=alignment.center,
                    margin=margin.only(left=20, right=20, top=150),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Image(
                                src="pic/patientRequest.png",
                                width=120,
                                height=120
                            ),
                            Container(
                                margin=margin.only(top=10),
                                content=Text(
                                    value="There are no requested appointment currently.",
                                    color=colors.BLACK,
                                    text_align=TextAlign.CENTER,
                                    weight=FontWeight.W_500
                                )
                            )
                            ,
                        ]
                    )
                )

        requested_booking = get_request_booking(user_id)

        return View(
            "/admin/adminPatientRequestList/:user_id",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    border_radius=30,
                    bgcolor="#F4F4F4",
                    content=Column(
                        scroll=True,
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
                                                value="Patient Request List",
                                                color="#3386C5",
                                                weight=FontWeight.W_600,
                                                size=18,
                                            ),
                                        )
                                    ]
                                )

                            ),
                            Container(
                                alignment=alignment.center,
                                content=requested_booking,

                            ),
                            dialog
                        ]
                    )
                )
            ]
        )