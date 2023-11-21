import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)
cursor = db.cursor()


def addRow():
    try:
        cursor.execute(
            "INSERT INTO doctors (fullName, username, email, phoneNumber, password, experience, specialization, "
            "description, clinic, workingTime, workingDay, image, status)"
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",

            ("Johnson", "Johnson", "johnson@gmail.com", "0157778709", "123", "3 years experience",
             "Cardiologists",
             "Treat the patient this and that", "Bwell Clinic", "12:00pm - 5:00pm",
             "Tuesday to Saturday (except Thursday)",
             "pic/doctor.png",
             1)
        ),
        db.commit()
        print("1")
    except sqlite3.Error as e:
        print("SQLite error:", e)


# def UpdateRow():
#     c = db.cursor()
#     c.execute("UPDATE doctors SET id = '1' WHERE id = ?", (5,))
#     db.commit()
#
#
# def DeleteRow():
#     cursor.execute("DELETE FROM doctors WHERE id = ?", (6,))
#     db.commit()
#
#
# DeleteRow()

class ClinicHomepage:

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

        light_blue = "#C1D8EA"
        blue = "#3386C5"
        dark_blue = "#0E446C"
        grey = "#71839B"

        def show_side_bar(e):
            sidebar.offset = transform.Offset(0, 0)
            page.update()

        def hide_side_bar(e):
            sidebar.offset = transform.Offset(-5, 0)
            page.update()

        def get_clinic_details():
            try:
                cursor.execute("SELECT id,name, phoneNumber , approvalStatus FROM clinic WHERE id = ?", (user_id,))
                record = cursor.fetchall()

                clinic_id = record[0][0]
                clinicName = record[0][1]
                phoneNumber = record[0][2]
                approvalStatus = record[0][3]

                return clinic_id, clinicName, phoneNumber, approvalStatus
            except sqlite3.Error as e:
                print("SQLite error:", e)

        clinic_id, clinicName, phoneNumber, approvalStatus = get_clinic_details()

        def get_doctor_details():
            try:
                cursor.execute("SELECT * FROM doctors WHERE clinicID = ? LIMIT 10", (clinic_id,))
                doctor_records = cursor.fetchall()

                return doctor_records
            except sqlite3.Error as e:
                print("SQLite error:", e)

        doctor_records = get_doctor_details()

        def approval_status():
            if approvalStatus == 0:
                return Container(
                    width=300,
                    height=60,
                    content=Row(
                        controls=[
                            Container(
                                content=Image(
                                    src=f"pic/pending_request.png"
                                )
                            ),
                            Container(
                                content=Text(
                                    value="Pending",
                                    size=20,
                                    color=colors.YELLOW_700,
                                    weight=FontWeight.BOLD,
                                    font_family="RobotoSlab",
                                )
                            )
                        ]
                    ),
                    border=Border(top=BorderSide(2, colors.BLACK),
                                  left=BorderSide(2, colors.BLACK),
                                  bottom=BorderSide(2, colors.BLACK),
                                  right=BorderSide(2, colors.BLACK)
                                  ),
                    border_radius=10
                )
            elif approvalStatus == 1:
                return Container(
                    width=300,
                    height=60,
                    content=Row(
                        controls=[
                            Container(
                                padding=padding.only(left=20),
                                content=Image(
                                    src=f"pic/approved_request.png"
                                )
                            ),

                            Container(
                                padding=padding.only(left=25),
                                content=Text(
                                    value="Approved",
                                    size=20,
                                    color=colors.GREEN,
                                    weight=FontWeight.BOLD,
                                    font_family="RobotoSlab",

                                )
                            )
                        ]
                    ),
                    border=Border(top=BorderSide(2, colors.BLACK),
                                  left=BorderSide(2, colors.BLACK),
                                  bottom=BorderSide(2, colors.BLACK),
                                  right=BorderSide(2, colors.BLACK)
                                  ),
                    border_radius=10
                )

            else:
                return Container(
                    width=300,
                    height=60,
                    content=Row(
                        controls=[
                            Container(
                                content=Image(
                                    src=f"pic/decline.png"
                                )
                            ),
                            Container(
                                content=Text(
                                    value="Declined",
                                    size=20,
                                    color=colors.RED,
                                    weight=FontWeight.BOLD,
                                    font_family="RobotoSlab",
                                )
                            )
                        ]
                    ),
                    border=Border(top=BorderSide(2, colors.BLACK),
                                  left=BorderSide(2, colors.BLACK),
                                  bottom=BorderSide(2, colors.BLACK),
                                  right=BorderSide(2, colors.BLACK)
                                  ),
                    border_radius=10

                )

        def getDoctorStatus(doctor_status):
            if doctor_status == 1:
                return Container(
                    content=Image(
                        src=f"pic/approved_doctor.png"
                    )
                )
            else:
                return Container(
                    content=Image(
                        src=f"pic/pending_doctor.png"
                    )
                )

        def display_doctor_list(records):
            if records:
                record_containers = []
                for record in records:
                    doctor_status = record[13]

                    record_container = Container(
                        margin=margin.only(left=25),
                        content=Column(
                            controls=[
                                Container(
                                    content=Text(
                                        value="Doctor :",
                                        size=15,
                                        font_family="RobotoSlab",
                                        color=dark_blue,
                                        weight=FontWeight.BOLD,
                                        text_align=TextAlign.LEFT,
                                    ),
                                ),

                                Container(
                                    content=Row(
                                        controls=[
                                            Container(
                                                getDoctorStatus(doctor_status),
                                            ),
                                            Container(
                                                content=Text(
                                                    value=f"Doctor {record[1]} ({record[7]})",
                                                    size=14,
                                                    color=colors.BLACK,
                                                    font_family="RobotoSlab",
                                                ),
                                                # on_click=
                                            ),
                                        ]
                                    )
                                ),

                            ]
                        )

                    )
                    record_containers.append(record_container)
                return Column(controls=record_containers)
            else:
                return Container()

        sidebar = Container(
            padding=10,
            width=200,
            height=700,
            bgcolor=colors.WHITE,
            content=Column(
                controls=[
                    Container(
                        padding=padding.only(top=60, left=10),
                        content=Column(
                            controls=[
                                Row(
                                    controls=[
                                        Image(
                                            src="pic/avatar.png",
                                            width=50,
                                            height=50
                                        ),

                                        Column(
                                            controls=[
                                                Container(
                                                    padding=padding.only(top=5, bottom=-5),
                                                    content=Text(
                                                        value=clinicName,
                                                        size=14,
                                                        font_family="RobotoSlab",
                                                        color=colors.BLACK
                                                    )
                                                ),
                                                Row(
                                                    controls=[
                                                        Icon(
                                                            icons.PHONE,
                                                            color=colors.BLACK,
                                                            size=10
                                                        ),
                                                        Container(
                                                            padding=padding.only(left=-8),
                                                            content=Text(
                                                                value=phoneNumber,
                                                                size=10,
                                                                font_family="RobotoSlab",
                                                                color=colors.BLACK
                                                            )
                                                        )

                                                    ]
                                                )

                                            ]
                                        ),
                                    ]
                                ),

                                Container(
                                    padding=padding.only(top=20, left=10, right=10),
                                    content=Column(
                                        controls=[
                                            Row(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    Row(
                                                        controls=[
                                                            Icon(
                                                                icons.SETTINGS,
                                                                size=20,
                                                                color=grey
                                                            ),

                                                            Text(
                                                                value="Settings",
                                                                size=12,
                                                                color=colors.BLACK,
                                                                text_align=TextAlign.LEFT,
                                                                font_family="RobotoSlab",
                                                            )
                                                        ]
                                                    ),

                                                    Container(
                                                        content=Icon(
                                                            icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                                                            size=14,
                                                            color=grey
                                                        )
                                                    )
                                                ]
                                            )

                                        ]
                                    )
                                ),

                                Container(
                                    padding=padding.only(top=20, left=10, right=10),
                                    content=Column(
                                        controls=[
                                            Row(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    Row(
                                                        controls=[
                                                            Icon(
                                                                icons.LOGOUT,
                                                                size=20,
                                                                color=grey
                                                            ),

                                                            Text(
                                                                value="Log Out",
                                                                size=12,
                                                                color=colors.BLACK,
                                                                text_align=TextAlign.LEFT,
                                                                font_family="RobotoSlab",
                                                            )
                                                        ]
                                                    ),

                                                    Container(
                                                        content=Icon(
                                                            icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                                                            size=14,
                                                            color=grey,
                                                        ),
                                                        on_click=lambda _: page.go("/")
                                                    )
                                                ]
                                            )

                                        ]
                                    )
                                ),

                            ]
                        )
                    )
                ]
            ),
            offset=transform.Offset(-5, 0),
            animate_offset=animation.Animation(400)
        )

        body_content = Row(
            controls=[
                Container(
                    on_click=hide_side_bar,
                    content=Column(
                        controls=[
                            Row(
                                controls=[
                                    Container(width=350,
                                              height=70,
                                              bgcolor=blue,
                                              alignment=alignment.top_center,
                                              content=Row(
                                                  controls=[
                                                      Container(padding=padding.only(left=10, top=25),
                                                                content=IconButton(
                                                                    icons.MENU,
                                                                    icon_color=colors.WHITE,
                                                                    on_click=show_side_bar
                                                                ),
                                                                ),

                                                      Container(padding=padding.only(left=65, top=25),
                                                                content=Text(
                                                                    value="Call A Doctor",
                                                                    size=20,
                                                                    font_family="RobotoSlab",
                                                                    color=colors.WHITE,
                                                                    text_align=TextAlign.CENTER)
                                                                ),
                                                  ]
                                              )
                                              )
                                ]
                            ),

                            Row(
                                controls=[
                                    Container(width=350,
                                              height=120,
                                              bgcolor=light_blue,
                                              margin=margin.only(top=-10),
                                              padding=padding.only(left=20, top=20),
                                              border_radius=border_radius.only(bottom_left=20, bottom_right=20),

                                              content=Column(
                                                  controls=[
                                                      Container(
                                                          content=Text(
                                                              value="Hello ",
                                                              size=18,
                                                              font_family="RobotoSlab",
                                                              color=colors.BLACK,
                                                              text_align=TextAlign.LEFT,
                                                              spans=[
                                                                  TextSpan(
                                                                      clinicName,
                                                                      TextStyle(size=18,
                                                                                font_family="RobotoSlab",
                                                                                color=dark_blue,
                                                                                weight=FontWeight.BOLD)
                                                                  )
                                                              ]
                                                          )
                                                      ),

                                                      Container(
                                                          padding=padding.only(top=10),
                                                          content=Text(
                                                              value="Welcome to ",
                                                              size=18,
                                                              font_family="RobotoSlab",
                                                              color=colors.BLACK,
                                                              text_align=TextAlign.LEFT,
                                                              spans=[
                                                                  TextSpan(
                                                                      "Join Call A Doctor",
                                                                      TextStyle(size=18,
                                                                                font_family="RobotoSlab",
                                                                                color=dark_blue,
                                                                                weight=FontWeight.BOLD)
                                                                  )
                                                              ]
                                                          )
                                                      ),
                                                  ]
                                              )
                                              ),
                                ]
                            ),

                            Row(
                                controls=[
                                    Container(
                                        margin=margin.only(left=25),
                                        content=Column(
                                            controls=[
                                                Container(
                                                    content=Text(
                                                        value="Approval Status :",
                                                        size=15,
                                                        font_family="RobotoSlab",
                                                        color=dark_blue,
                                                        weight=FontWeight.BOLD,
                                                        text_align=TextAlign.LEFT
                                                    ),

                                                ),

                                                approval_status(),

                                            ]
                                        )
                                    ),
                                ]
                            ),

                            display_doctor_list(doctor_records),

                            Container(
                                width=150,
                                height=40,
                                margin=margin.only(left=25),
                                content=Row(
                                    controls=[
                                        Container(
                                            content=IconButton(
                                                icons.PERSON_ADD_ROUNDED,
                                                icon_color=blue,
                                                style=ButtonStyle(elevation={}),

                                            ),

                                        ),
                                        Container(
                                            content=Text(
                                                value="Add A Doctor",
                                                size=13,
                                                color=colors.BLACK,
                                                font_family="RobotoSlab",
                                            ),

                                        ),
                                    ]
                                ),
                                border=Border(top=BorderSide(2, colors.BLACK),
                                              left=BorderSide(2, colors.BLACK),
                                              bottom=BorderSide(2,
                                                                colors.BLACK),
                                              right=BorderSide(2, colors.BLACK)
                                              ),
                                border_radius=10,
                                on_click=lambda _: (
                                    page.go(f"/addDoctorDetails/{clinic_id}")
                                ),
                            ),

                        ]
                    )
                )
            ]
        )

        return View(
            "/clinicHomepage/:user_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          content=Stack(
                              controls=[
                                  body_content,
                                  sidebar
                              ]
                          )
                          )
            ]
        )
