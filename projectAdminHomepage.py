from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class ProjectAdminHomepage:
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

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        self.db = sqlite3.connect("cad.db", check_same_thread=False)

        def get_project_admin_details():
            c = db.cursor()
            c.execute("SELECT * FROM admin WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]
            username = record[0][2]
            email = record[0][3]
            phoneNumber = record[0][4]

            return fullName, username, email, phoneNumber

        fullName, username, email, phoneNumber = get_project_admin_details()

        def get_requested_clinic(callFrom):
            c = ""
            if callFrom == "Request":
                c = db.cursor()
                c.execute("SELECT * FROM clinic WHERE approvalStatus = ?", (0,))
            elif callFrom == "Accepted":
                c = db.cursor()
                c.execute("SELECT * FROM clinic WHERE approvalStatus = ?", (1,))

            record = c.fetchall()

            # print(record)

            return record

        def displayClinic(callFrom):
            records = get_requested_clinic(callFrom)

            if records:
                record_containers = []
                for record in records:
                    def on_more_click(record_id=record[0]):
                        return lambda _: page.go(f"/projectAdminViewClinicDetail/{user_id}{record_id}")

                    record_container = Container(
                        alignment=alignment.center,
                        border_radius=8,
                        padding=padding.only(left=10, top=10),
                        margin=margin.only(left=10, top=10),
                        border=border.all(color=blue),
                        width=320,
                        height=100,
                        bgcolor="#ffffff",
                        content=Column(
                            controls=[
                                Row(
                                    controls=[
                                        Container(
                                            margin=margin.only(left=10, right=10, top=10),
                                            content=Image(
                                                src=f"{record[10]}",
                                                width=60,
                                                height=60,
                                            )
                                        ),
                                        Column(
                                            controls=[
                                                Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Clinic Name", color="BLACK",
                                                             size=12, weight=FontWeight.W_500,
                                                             width=90),
                                                        Text(": ", color="BLACK", size=12),
                                                        Text(record[1],
                                                             text_align=TextAlign.JUSTIFY,
                                                             color="BLACK", size=12,
                                                             weight=FontWeight.W_600,
                                                             width=100)
                                                    ]
                                                ),
                                                Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Clinic Area", color="BLACK",
                                                             size=12, weight=FontWeight.W_500,
                                                             width=90),
                                                        Text(": ", color="BLACK", size=12),
                                                        Text(record[5], color="BLACK",
                                                             text_align=TextAlign.JUSTIFY,
                                                             size=12, weight=FontWeight.W_600,
                                                             width=100)
                                                    ]
                                                ),
                                                Row(
                                                    alignment="spaceBetween",
                                                    controls=[
                                                        Text("Phone Number", color="BLACK",
                                                             size=12,
                                                             weight=FontWeight.W_500,
                                                             width=90),
                                                        Text(": ", color="BLACK", size=12),
                                                        Text(record[9],
                                                             text_align=TextAlign.JUSTIFY,
                                                             color="BLACK", size=12,
                                                             weight=FontWeight.W_600,
                                                             width=100)
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        on_click=on_more_click()
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
                                src="pic/appointment_icon.png",
                                width=120,
                                height=120
                            ),

                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="You do not have any clinic request yet.",
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

        tab = Tabs(
            width=350,
            selected_index=0,
            animation_duration=300,
            label_color=blue,
            unselected_label_color=grey,
            indicator_tab_size=True,
            indicator_color=blue,
            divider_color=grey,
            tabs=[
                Tab(
                    text="\t\t\t\t\t\t\t\t\t\tRequesting\t\t\t\t\t\t\t\t\t",
                    content=Container(
                        width=340,
                        content=displayClinic("Request")
                    ),
                ),
                Tab(
                    text="\t\t\t\t\t\t\t\t\t\tAccepted\t\t\t\t\t\t\t\t\t",
                    content=Container(
                        width=340,
                        content=displayClinic("Accepted")
                    ),
                )
            ],
            expand=1,
        )

        # phone container
        return View(
            "/projectAdminHomepage/:user_id",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    bgcolor="#F4F4F4",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Stack(
                        # scroll=True,
                        # horizontal_alignment=CrossAxisAlignment.START,
                        controls=[
                            Container(
                                content=Column(
                                    controls=[
                                        Container(
                                            width=350,
                                            # height=250,
                                            bgcolor="#3386C5",
                                            padding=padding.symmetric(horizontal=10, vertical=20),

                                            content=Column(
                                                controls=[
                                                    Row(
                                                        controls=[
                                                            Container(
                                                                content=IconButton(icons.LOGOUT,
                                                                                   icon_color="WHITE",
                                                                                   on_click=lambda _: page.go(f"/"))),
                                                            Container(padding=padding.only(left=20),
                                                                      content=Text(value=f"{fullName.upper()} ",
                                                                                   size=25,
                                                                                   font_family="RobotoSlab",
                                                                                   weight=FontWeight.W_500,
                                                                                   color="WHITE")),
                                                        ]
                                                    )
                                                ])
                                        ),

                                        Container(padding=padding.only(top=10, left=20),
                                                  content=Text("Clinic Sign Up Request",
                                                               size=14,
                                                               color="BLACK",
                                                               font_family="RobotoSlab",
                                                               weight=FontWeight.BOLD)),

                                        tab

                                    ]))
                        ]
                    )
                )
            ]
        )