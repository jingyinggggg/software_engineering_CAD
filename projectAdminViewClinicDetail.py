from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class ProjectAdminViewClinicDetail:
    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
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

        self.db = sqlite3.connect("cad.db", check_same_thread=False)

        def get_clinic_details():
            c = db.cursor()
            c.execute("SELECT * FROM clinic WHERE id = ?", (clinic_id,))
            record = c.fetchall()

            return record

        clinic = get_clinic_details()

        reject_reason_container = TextField(
            label="Enter the reject reason" if clinic[0][13] == 0 else "Enter the disable reason",
            label_style=TextStyle(size=12,
                                  color=colors.BLACK,
                                  weight=FontWeight.W_500),
            border_color=colors.BLACK,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_500),
            multiline=True
        )

        def close_dialog(dialog, redirect_url=None):
            page.dialog = dialog
            dialog.open = False
            if redirect_url:
                page.go(redirect_url)
            page.update()

        def open_dialog(dialog):
            page.dialog = dialog
            dialog.open = True
            page.update()

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Alert", text_align=TextAlign.CENTER),
            content=Text(f"You have accepted {clinic[0][1]}'s request !",
                         text_align=TextAlign.CENTER),
            actions=[
                TextButton("OK", on_click=lambda _: close_dialog(alert_dialog, f"/projectAdminHomepage/{user_id}"))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        Reject_alert_dialog = AlertDialog(
            modal=True,
            title=Text("Alert", text_align=TextAlign.CENTER),
            content=Text(f"Please enter reject reason",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("OK", on_click=lambda _: close_dialog(Reject_alert_dialog))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        SuccessfulReject_dialog = AlertDialog(
            modal=True,
            title=Text("Alert", text_align=TextAlign.CENTER),
            content=Text(f"You have rejected {clinic[0][1]}'s request !",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("OK", on_click=lambda _: close_dialog(SuccessfulReject_dialog,
                                                                      f"/projectAdminHomepage/{user_id}"))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        disable_dialog = AlertDialog(
            modal=True,
            title=Text("Alert", text_align=TextAlign.CENTER),
            content=Text(f"You have change {clinic[0][1]} to status request !",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("OK", on_click=lambda _: close_dialog(disable_dialog,
                                                                      f"/projectAdminHomepage/{user_id}"))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_Reject_alert_dialog():
            open_dialog(Reject_alert_dialog)

        def open_alert_dialog():
            open_dialog(alert_dialog)
            update_accept_database()

        def open_SuccessfulReject_alert_dialog():
            open_dialog(SuccessfulReject_dialog)

        def disable_alert_dialog():
            open_dialog(disable_dialog)

        def update_accept_database():
            c = db.cursor()
            c.execute("UPDATE clinic SET approvalStatus = 1 WHERE id = ?", (clinic_id,))

            db.commit()

        def update_reject_database():
            c = db.cursor()
            c.execute("UPDATE clinic SET approvalStatus = -1, rejectReason = ? WHERE id = ?",
                      (reject_reason_container.value, clinic_id,))

            db.commit()

        def disable_clinic():
            if reject_reason_container.value != "":
                c = db.cursor()
                c.execute("UPDATE clinic SET approvalStatus = 0, rejectReason = ? WHERE id = ?",
                          (reject_reason_container.value, clinic_id,))

                db.commit()
                disable_alert_dialog()
            else:
                open_Reject_alert_dialog()

        def reject_reason():
            if reject_reason_container.value != "":
                update_reject_database()  # Call the database update function here
                open_SuccessfulReject_alert_dialog()
            else:
                open_Reject_alert_dialog()

        # phone container
        return View(
            "/projectAdminViewClinicDetail/:user_id:clinic_id",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    bgcolor="#F4F4F4",
                    border_radius=30,
                    # alignment=alignment.center,
                    content=Stack(
                        # scroll=True,
                        # horizontal_alignment=CrossAxisAlignment.START,
                        controls=[
                            Container(
                                content=Column(
                                    scroll=True,
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
                                                            Container(padding=padding.only(top=5, left=10),
                                                                      content=Image(
                                                                          src="pic/back.png",
                                                                          color=colors.WHITE,
                                                                          width=20,
                                                                          height=20
                                                                      ), on_click=lambda _: page.go(
                                                                    f"/projectAdminHomepage/{user_id}")),

                                                            Container(padding=padding.only(left=95),
                                                                      content=Text(value=f"Clinic",
                                                                                   size=20,
                                                                                   font_family="RobotoSlab",
                                                                                   weight=FontWeight.W_500,
                                                                                   color="WHITE"))
                                                        ]
                                                    )
                                                ])
                                        ),
                                        Container(
                                            width=350,
                                            bgcolor=lightBlue,
                                            margin=margin.only(top=-10),
                                            padding=padding.only(left=10, right=10, top=10, bottom=10),
                                            content=Row(
                                                controls=[
                                                    Container(
                                                        padding=padding.only(top=10, bottom=10),
                                                        content=Image(
                                                            src=f"{clinic[0][10]}",
                                                            width=50,
                                                            height=50
                                                        )
                                                    ),

                                                    Container(
                                                        content=Column(
                                                            controls=[
                                                                Text(
                                                                    value=f"{clinic[0][1]}",
                                                                    size=14,
                                                                    font_family="RobotoSlab",
                                                                    weight=FontWeight.W_600,
                                                                    color=colors.BLACK
                                                                ),

                                                                Row(
                                                                    controls=[
                                                                        Text(
                                                                            value="📍",
                                                                            size=12
                                                                        ),

                                                                        Container(
                                                                            width=230,
                                                                            content=Text(
                                                                                value=f"{clinic[0][4]}",
                                                                                size=10,
                                                                                font_family="RobotoSlab",
                                                                                color=colors.BLACK,
                                                                                text_align=TextAlign.JUSTIFY,
                                                                                weight=FontWeight.W_500

                                                                            )
                                                                        )

                                                                    ]

                                                                ),

                                                                Row(
                                                                    controls=[
                                                                        Text(
                                                                            value="⏳",
                                                                            size=12
                                                                        ),

                                                                        Container(
                                                                            content=Text(
                                                                                value=f"{clinic[0][7]}",
                                                                                size=10,
                                                                                font_family="RobotoSlab",
                                                                                color=colors.BLACK,
                                                                                text_align=TextAlign.JUSTIFY,
                                                                                weight=FontWeight.W_500

                                                                            )
                                                                        )
                                                                    ]
                                                                ),

                                                                Row(
                                                                    controls=[
                                                                        Text(
                                                                            value="🕛",
                                                                            size=12
                                                                        ),

                                                                        Container(
                                                                            content=Text(
                                                                                value=f"{clinic[0][6]}",
                                                                                size=10,
                                                                                font_family="RobotoSlab",
                                                                                color=colors.BLACK,
                                                                                text_align=TextAlign.JUSTIFY,
                                                                                weight=FontWeight.W_500

                                                                            )
                                                                        )
                                                                    ]
                                                                ),

                                                                Row(
                                                                    controls=[
                                                                        Text(
                                                                            value="📞",
                                                                            size=12
                                                                        ),

                                                                        Container(
                                                                            content=Text(
                                                                                value=f"{clinic[0][9]}",
                                                                                size=10,
                                                                                font_family="RobotoSlab",
                                                                                color=colors.BLACK,
                                                                                text_align=TextAlign.JUSTIFY,
                                                                                weight=FontWeight.W_500

                                                                            )
                                                                        ),
                                                                    ]
                                                                ),

                                                                Row(
                                                                    controls=[
                                                                        Text(
                                                                            value="📝",
                                                                            size=12
                                                                        ),

                                                                        Container(
                                                                            width=230,
                                                                            content=Text(
                                                                                value=f"{clinic[0][8]}",
                                                                                size=10,
                                                                                font_family="RobotoSlab",
                                                                                color=colors.BLACK,
                                                                                text_align=TextAlign.JUSTIFY,
                                                                                weight=FontWeight.W_500

                                                                            )
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        Container(
                                            margin=margin.only(left=10, right=10, top=10, bottom=10),
                                            padding=padding.only(left=10, right=10, top=10, bottom=10),
                                            border_radius=0,
                                            width=320,
                                            border=border.all(2, lightBlue),
                                            content=Column(
                                                controls=[
                                                    Text(
                                                        value="📍 Google Map",
                                                        font_family="RobotoSlab",
                                                        size=14,
                                                        weight=FontWeight.W_500,
                                                        color=colors.BLACK
                                                    ),

                                                    Image(
                                                        src=f"{clinic[0][11]}"
                                                    )
                                                ]
                                            )
                                        ),

                                        Container(
                                            margin=margin.only(left=10, right=10, bottom=20),
                                            padding=padding.only(left=10, right=10, top=10, bottom=10),
                                            border_radius=0,
                                            width=320,
                                            border=border.all(2, lightBlue),
                                            content=Column(
                                                controls=[
                                                    Text(
                                                        value="🪴 Environment",
                                                        font_family="RobotoSlab",
                                                        size=14,
                                                        weight=FontWeight.W_500,
                                                        color=colors.BLACK
                                                    ),

                                                    Image(
                                                        src=f"{clinic[0][12]}"
                                                    )
                                                ]
                                            )
                                        ),
                                        Container(
                                            padding=padding.only(left=5,right=5),
                                            content=reject_reason_container,
                                        ),

                                        Container(
                                            Row(
                                                controls=[
                                                    Container(
                                                        padding=padding.only(left=10, bottom=20),
                                                        content=ElevatedButton(
                                                            text="✔ Accept",
                                                            bgcolor=lightBlue,
                                                            color="BLACK",
                                                            width=150,
                                                            height=45,
                                                            on_click=lambda _: open_alert_dialog()

                                                        )
                                                    ),
                                                    Container(
                                                        padding=padding.only(left=10, bottom=20),
                                                        content=ElevatedButton(
                                                            text="✗ Reject",
                                                            bgcolor=colors.RED,
                                                            color="BLACK",
                                                            width=150,
                                                            height=45,
                                                            on_click=lambda _: reject_reason()
                                                        )
                                                    ),
                                                ] if clinic[0][13] == 0 else "",
                                            )
                                        ),
                                        Container(
                                            alignment=alignment.center,
                                            content=
                                            Column(
                                                controls=[
                                                    Container(
                                                        padding=padding.only(left=10, bottom=20),
                                                        content=ElevatedButton(
                                                            text="✗ Disable this clinic",
                                                            bgcolor=colors.RED,
                                                            color="BLACK",
                                                            width=200,
                                                            height=45,
                                                            on_click=lambda _: disable_clinic()
                                                        )
                                                    )
                                                ] if clinic[0][13] == 1 else ""
                                            )
                                        )

                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
