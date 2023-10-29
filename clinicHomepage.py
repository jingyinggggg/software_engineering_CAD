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
                   "Treat the patient this and that", "Bwell Clinic", "12:00pm - 5:00pm", "Tuesday to Saturday (except Thursday)",
                   "pic/doctor.png",
                   1)
                  ),
        db.commit()
        print("1")
    except sqlite3.Error as e:
        print("SQLite error:", e)


def UpdateRow():
    c = db.cursor()
    c.execute("UPDATE doctors SET id = '1' WHERE id = ?", (5,))
    db.commit()



class ClinicHomepage:

    def __init__(self):
        self.show_sidebar = False

    def view (self, page: Page, params: Params, basket: Basket):
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
            c = db.cursor()
            c.execute("SELECT name, phoneNumber , approvalStatus FROM clinic WHERE id = ?", (user_id,))
            record = c.fetchall()

            clinicName = record[0][0]
            phoneNumber = record[0][1]
            approvalStatus = record[0][2]

            return clinicName, phoneNumber, approvalStatus

        clinicName, phoneNumber ,approvalStatus = get_clinic_details()

        def get_doctor_details():
            c = db.cursor()
            c.execute("SELECT fullName, specialization FROM doctors WHERE clinic = ? LIMIT 10", (clinicName,))
            record = c.fetchall()

            doctor_name = record[0][0]
            doctor_spec = record[0][1]

            return doctor_name, doctor_spec

        doctor_name, doctor_spec = get_doctor_details()

        def remove_doctor():
            c = db.cursor()
            c.execute("DELETE FROM doctors WHERE name = ?", (doctor_name,))

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
                return (
                    Container(
                        content=Column(
                            controls=[
                                Container(
                                    margin=margin.only(left=10),
                                    width=250,
                                    height=68,
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
                                    border_radius=10,


                                ),

                                Container(
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
                                                            content=IconButton(
                                                                icons.PERSON_REMOVE_ROUNDED,
                                                                icon_color=colors.RED,
                                                                on_click=remove_doctor,
                                                            )
                                                        ),
                                                        Container(
                                                            content=Text(
                                                                value="Doctor " + doctor_name +
                                                                      " (" + doctor_spec + ")",
                                                                size=14,
                                                                color=colors.BLACK,
                                                                font_family="RobotoSlab",
                                                            )
                                                        ),
                                                    ]
                                                )
                                            ),
                                            Container(
                                                on_click=lambda _: (
                                                    page.go(f"/addDoctorDetails/{clinicName}")
                                                ),
                                                width=150,
                                                height=40,
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
                                            ),

                                        ]
                                    )

                                )

                            ]
                        )
                    )
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

                                # Container(
                                #     padding=padding.only(top=20, left=10, right=10),
                                #     content=Column(
                                #         controls=[
                                #             Row(
                                #                 alignment=MainAxisAlignment.SPACE_BETWEEN,
                                #                 controls=[
                                #                     Row(
                                #                         controls=[
                                #                             Image(
                                #                                 src="pic/myDoctors.png",
                                #                                 width=20,
                                #                                 height=20
                                #                             ),
                                #
                                #                             Text(
                                #                                 value="My Doctors",
                                #                                 size=12,
                                #                                 color=colors.BLACK,
                                #                                 text_align=TextAlign.LEFT,
                                #                                 font_family="RobotoSlab",
                                #                             )
                                #                         ]
                                #                     ),
                                #
                                #                     Container(
                                #                         content=Icon(
                                #                             icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                                #                             size=14,
                                #                             color=grey
                                #                         )
                                #                     )
                                #                 ]
                                #             )
                                #
                                #         ]
                                #     )
                                # ),

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
