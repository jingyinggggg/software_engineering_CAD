from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminManageDoctorPage:
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
        blue = "#3386C5"
        lightBlue = "#D0DCEE"

        # Get the appointment details which has updated with the visit proof
        def get_doctor_list():
            c = db.cursor()
            c.execute(
                f"SELECT id, fullName, specialization, image FROM doctors WHERE clinicID = {user_id} AND STATUS = 1")
            record = c.fetchall()

            return record

        doctorList = get_doctor_list()

        def displayDoctor(records):
            if records:
                record_containers = []
                for record in records:
                    def edit_button(record_id=record[0]):
                        return lambda _: page.go(f"/admin/clinicAdminEditDoctorPage/{user_id}{record_id}")

                    def delete_button(record_id=record[0]):
                        return lambda _: page.go(f"/admin/clinicAdminDeleteDoctorPage/{user_id}{record_id}")

                    record_container = Container(
                        margin=margin.only(left=10, right=10, top=10),
                        padding=padding.only(left=10, top=10, bottom=10),
                        border_radius=10,
                        border=border.all(1, blue),
                        content=Row(
                            alignment="spaceBetween",
                            controls=[
                                Container(
                                    margin=margin.only(top=10, bottom=10, right=15),
                                    # padding=padding.only(top=10, bottom=10),
                                    bgcolor=lightBlue,
                                    border_radius=10,
                                    content=Image(
                                        src=f"{record[3]}",
                                        width=60,
                                        height=60,

                                    )
                                ),

                                Container(
                                    # margin=margin.only(top=10),
                                    content=Column(
                                        controls=[
                                            Text(
                                                value=f"Dr. {record[1]}",
                                                size=14,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_600,
                                                color=colors.BLACK
                                            ),

                                            Row(
                                                controls=[
                                                    Text(
                                                        value="🩺",
                                                        size=10
                                                    ),

                                                    Container(
                                                        width=140,
                                                        content=Text(
                                                            value=f"{record[2]}",
                                                            size=9,
                                                            font_family="RobotoSlab",
                                                            color=grey,
                                                            text_align=TextAlign.LEFT


                                                        )
                                                    )

                                                ]

                                            ),
                                        ]
                                    )
                                ),

                                Row(
                                    # width=50,
                                    controls=[
                                        Container(
                                            margin=margin.only(right=-20),
                                            content=IconButton(
                                                icons.EDIT,
                                                icon_size=18,
                                                icon_color=blue,
                                                on_click=edit_button()
                                            )
                                        ),
                                        IconButton(
                                            icons.DELETE,
                                            icon_size=18,
                                            icon_color=blue,
                                            on_click=delete_button()
                                        )
                                    ]
                                )

                                ,

                            ]
                        )
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)
            else:
                return Container(
                    alignment=alignment.center,
                    padding=padding.only(top=120),
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Icon(
                                icons.PENDING_ACTIONS,
                                size=100,
                                color=blue
                            ),

                            Container(
                                padding=padding.only(top=10),
                                content=Text(
                                    value="There is no doctors in the system currently.",
                                    text_align=TextAlign.CENTER,
                                    size=14,
                                    weight=FontWeight.W_500,
                                    color=colors.BLACK,
                                )
                            ),

                        ]
                    )
                )

        return View(
            "/admin/clinicAdminManageDoctor/:user_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#F4F4F4",
                    border_radius=30,
                    content=Column(
                        scroll=True,
                        controls=[
                            Container(
                                padding=padding.only(top=25, left=10),
                                content=Image(
                                    src="pic/back.png",
                                    color="#3386C5",
                                    width=20,
                                    height=20
                                ),
                                on_click=lambda _: page.go(f"/login/adminHomepage/{user_id}")
                            ),

                            Container(
                                margin=margin.only(left=10, right=10),
                                content=Text(
                                    value="Manage Doctor",
                                    color="#3386C5",
                                    weight=FontWeight.W_600,
                                    size=18,
                                ),

                            ),

                            Container(margin=margin.only(right=10),
                                      alignment=alignment.top_right,
                                      content=IconButton(content=Text("Add new doctor",
                                                                      size=10,
                                                                      color=colors.WHITE,
                                                                      text_align=TextAlign.CENTER,
                                                                      weight=FontWeight.W_700),
                                                         # width=155,
                                                         height=30,
                                                         style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                           shape={
                                                                               "": RoundedRectangleBorder(
                                                                                   radius=7)}
                                                                           ),
                                                         on_click=lambda _: page.go(
                                                             f"/admin/clinicAdminAddNewDoctorList/{user_id}")
                                                         )
                                      ),

                            displayDoctor(doctorList)
                        ]
                    )
                )
            ]

        )
