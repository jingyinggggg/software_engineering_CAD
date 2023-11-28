import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ProofStatus:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
        user_id = int(params.user_id)
        # booking_id = int(params.booking_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 800
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        def get_request_proof():
            c = db.cursor()
            c.execute("SELECT * FROM booking INNER JOIN users ON booking.patientID = users.id WHERE booking.doctorID = ? AND proofStatus = ? ", (user_id, 0,))
            record = c.fetchall()
            return record

        requested_booking = get_request_proof()

        def displayRequestProof(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewProof/{user_id}/{record_id}")

                    record_container = Container(
                        margin=margin.only(left=15, right=15, top=20),
                        border_radius=10,
                        border=border.all(1, colors.BLACK),
                        padding=padding.only(left=20, right=20, top=20, bottom=20),
                        content=Row(
                            controls=[
                                Container(
                                    padding=padding.only(top=-10),
                                    content=Image(
                                        src="pic/icons8-proof-60.png",
                                        width=50,
                                        height=50,
                                    )

                                ),

                                Column(
                                    controls=[
                                        Container(
                                            width=235,
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        value="Patient Name: ",
                                                        color=colors.BLACK,
                                                        size=11,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                    ),

                                                    Container(
                                                        margin=margin.only(left=-8),
                                                        content=Text(
                                                            value=record[17],
                                                            color=colors.BLACK,
                                                            size=11,
                                                            font_family="RobotoSlab",
                                                            weight=FontWeight.W_600,  # Set the text to bold
                                                            text_align=TextAlign.JUSTIFY,
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        Container(
                                            margin=margin.only(bottom=-3),
                                            width=220,
                                            content=Text(
                                                value=f"Appointment Date: {record[3]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Appointment Time: {record[4]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        )
                                    ]
                                )
                            ]
                        ),

                        on_click=on_more_button_click()
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
                                src="pic/icons8-proof-60.png",
                                width=120,
                                height=120
                            ),

                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="You do not have any submitted proof yet.",
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

        def get_approved_proof():
            c = db.cursor()
            c.execute("SELECT * FROM booking INNER JOIN users ON booking.patientID = users.id WHERE doctorID = ? AND proofStatus = ? AND prescriptionStatus is null ", (user_id, 1,))
            record = c.fetchall()
            print(record)
            return record

        approve_proof = get_approved_proof()

        def displayApprovedProof(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(booking_id=record[0]):
                        return lambda _: page.go(f"/viewProof/{user_id}/{booking_id}")

                    record_container = Container(
                        margin=margin.only(left=15, right=15, top=20),
                        border_radius=10,
                        border=border.all(1, colors.BLACK),
                        padding=padding.only(left=20, right=20, top=20, bottom=20),
                        content=Row(
                            controls=[
                                Container(
                                    padding=padding.only(top=-10),
                                    content=Image(
                                        src="pic/icons8-proof-60.png",
                                        width=50,
                                        height=50,
                                    )

                                ),

                                Column(
                                    controls=[
                                        Container(
                                            width=235,
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        value="Patient Name: ",
                                                        color=colors.BLACK,
                                                        size=11,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                    ),

                                                    Container(
                                                        margin=margin.only(left=-8),
                                                        content=Text(
                                                            value=record[17],
                                                            color=colors.BLACK,
                                                            size=11,
                                                            font_family="RobotoSlab",
                                                            weight=FontWeight.W_600,  # Set the text to bold
                                                            text_align=TextAlign.JUSTIFY,
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        Container(
                                            margin=margin.only(bottom=-3),
                                            width=220,
                                            content=Text(
                                                value=f"Appointment Date: {record[3]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Appointment Time: {record[4]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        )
                                    ]
                                )
                            ]
                        ),

                        on_click=on_more_button_click()
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
                                src="pic/icons8-proof-60.png",
                                width=120,
                                height=120
                            ),

                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="You do not have any approved proof yet.",
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

        def get_rejected_proof():
            c = db.cursor()
            c.execute("SELECT * FROM booking INNER JOIN users ON booking.patientID = users.id WHERE doctorID = ? AND proofStatus = ? ", (user_id, -1,))
            record = c.fetchall()
            return record

        rejected_proof = get_rejected_proof()

        def displayRejectedProof(records):
            if records:
                record_containers = []
                for record in records:
                    def on_more_button_click(record_id=record[0]):
                        return lambda _: page.go(f"/viewProof/{user_id}/{record_id}")

                    record_container = Container(
                        margin=margin.only(left=15, right=15, top=20),
                        border_radius=10,
                        border=border.all(1, colors.BLACK),
                        padding=padding.only(left=20, right=20, top=20, bottom=20),
                        content=Row(
                            controls=[
                                Container(
                                    padding=padding.only(top=-10),
                                    content=Image(
                                        src="pic/icons8-proof-60.png",
                                        width=50,
                                        height=50,
                                    )

                                ),

                                Column(
                                    controls=[
                                        Container(
                                            width=235,
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        value="Patient Name: ",
                                                        color=colors.BLACK,
                                                        size=11,
                                                        font_family="RobotoSlab",
                                                        weight=FontWeight.W_500,
                                                        text_align=TextAlign.JUSTIFY,
                                                    ),

                                                    Container(
                                                        margin=margin.only(left=-8),
                                                        content=Text(
                                                            value=record[17],
                                                            color=colors.BLACK,
                                                            size=11,
                                                            font_family="RobotoSlab",
                                                            weight=FontWeight.W_600,  # Set the text to bold
                                                            text_align=TextAlign.JUSTIFY,
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        Container(
                                            margin=margin.only(bottom=-3),
                                            width=220,
                                            content=Text(
                                                value=f"Appointment Date: {record[3]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        ),

                                        Container(
                                            width=220,
                                            margin=margin.only(bottom=-3),
                                            content=Text(
                                                value=f"Appointment Time: {record[4]}",
                                                color=colors.BLACK,
                                                size=11,
                                                font_family="RobotoSlab",
                                                weight=FontWeight.W_500,
                                                text_align=TextAlign.JUSTIFY
                                            )
                                        )
                                    ]
                                )
                            ]
                        ),
                        on_click=on_more_button_click()
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
                                src="pic/icons8-proof-60.png",
                                width=120,
                                height=120
                            ),

                            Container(
                                padding=padding.only(top=10, left=30, right=30),
                                content=Text(
                                    value="You do not have any rejected proof yet.",
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
                    text="\t\t\tSubmitted\t\t\t",
                    content=Container(
                        content=displayRequestProof(requested_booking)
                    ),
                ),

                Tab(
                    text="\t\t\tApproved\t\t\t",
                    content=Container(
                        width=340,
                        content=displayApprovedProof(approve_proof)
                    ),
                ),
                Tab(
                    text="\t\t\tRejected\t\t\t",
                    content=Container(
                        width=340,
                        content=displayRejectedProof(rejected_proof)
                    ),
                ),
            ],
            expand=1,
        )

        return View(
            "/proofStatus/:user_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              horizontal_alignment="center",
                              controls=[
                                  Container(width=350,
                                            height=70,
                                            bgcolor=blue,
                                            alignment=alignment.top_center,
                                            padding=padding.only(left=10, right=10),
                                            content=Row(
                                                controls=[
                                                    Container(padding=padding.only(top=25),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ),
                                                              on_click=lambda _: page.go(f"/login/homepage/{user_id}")
                                                              ),

                                                    Container(padding=padding.only(left=75, top=25),
                                                              content=Text(
                                                                  value="Proof Status",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),

                                                ]
                                            )
                                            ),

                                  tab
                              ]
                          )
                          )
            ]
        )