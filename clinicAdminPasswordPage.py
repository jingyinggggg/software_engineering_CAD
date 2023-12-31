from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminPasswordPage:
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

        blue = "#3386C5"
        grey = "#71839B"
        lightBlue = "#D0DCEE"

        def get_user_password():
            c = db.cursor()
            c.execute("SELECT password from clinicAdmin WHERE id = ?", (user_id,))
            record = c.fetchone()
            current_password = record[0]
            return current_password

        current_password = get_user_password()

        current_password_textfield = TextField(label="Current Password",
                                               password=True,
                                               can_reveal_password=True,
                                               label_style=TextStyle(size=12,
                                                                     color=colors.BLACK,
                                                                     weight=FontWeight.W_600),
                                               border_color=blue,
                                               value=f"{current_password}",
                                               text_style=TextStyle(size=12,
                                                                    color=colors.BLACK,
                                                                    weight=FontWeight.W_600
                                                                    ),
                                               dense=True,
                                               read_only=True)

        new_password_textfield = TextField(label="New Password",
                                           password=True,
                                           can_reveal_password=True,
                                           label_style=TextStyle(size=12,
                                                                 color=colors.BLACK,
                                                                 weight=FontWeight.W_600),
                                           border_color=blue,
                                           text_style=TextStyle(size=12,
                                                                color=colors.BLACK,
                                                                weight=FontWeight.W_600
                                                                ),
                                           dense=True)

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have updated your password successfully!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg(alert_dialog))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Failed", text_align=TextAlign.CENTER),
            content=Text("Something went wrong! Please try again...",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg(error_dialog))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_dlg(dialog):
            page.dialog = dialog
            dialog.open = True
            page.update()

        def close_dlg(dialog):
            page.dialog = dialog
            dialog.open = False
            page.update()

        def changePassword(e):
            c = db.cursor()
            if new_password_textfield.value != "":
                c.execute(f"UPDATE clinicAdmin SET password = {new_password_textfield.value} WHERE id = {user_id}")
                db.commit()
                open_dlg(alert_dialog)
                current_password_textfield.value = get_user_password()
                new_password_textfield.value = ""
            else:
                open_dlg(error_dialog)


        password_container = Container(
            padding=padding.only(left=10, right=10),
            content=Column(
                horizontal_alignment="center",
                controls=[
                    Container(
                        margin=margin.only(top=10, bottom=10),
                        content=Text(
                            value="Manage your password, login preference. You may change your password here.",
                            size=12,
                            color=colors.BLACK,
                            text_align=TextAlign.JUSTIFY,
                            weight=FontWeight.W_700
                        )
                    ),

                    Container(
                        margin=margin.only(top=10, bottom=15),
                        content=current_password_textfield
                    ),

                    new_password_textfield,

                    Container(
                        padding=padding.only(top=30),
                        content=TextButton(content=Text("Change Password",
                                                        size=16,
                                                        color="WHITE",
                                                        text_align=TextAlign.CENTER),
                                           width=323,
                                           height=45,
                                           style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                             shape={
                                                                 "": RoundedRectangleBorder(
                                                                     radius=7)}
                                                             ),
                                           on_click=changePassword
                                           ),
                    )
                ]
            )
        )

        return View(
            "/admin/password/:user_id",
            controls=[Container(
                width=350,
                height=700,
                bgcolor="#FFFFFF",
                border_radius=30,
                alignment=alignment.center,
                content=Column(
                    controls=[
                        Container(
                            padding=padding.only(top=25, left=10, bottom=10),
                            content=Column(
                                controls=[
                                    Container(
                                        content=Image(
                                            src="pic/back.png",
                                            color="#3386C5",
                                            width=20,
                                            height=20
                                        ),
                                        on_click=lambda _: page.go(f"/admin/setting/{user_id}")
                                    ),
                                    Text(
                                        value=" Password & Security",
                                        color="#3386C5",
                                        weight=FontWeight.W_600,
                                        size=18,
                                    )
                                ]
                            ),
                        ),

                        password_container

                    ]
                ))
            ]
        )
