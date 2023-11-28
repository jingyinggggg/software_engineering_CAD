import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class DoctorCallInterface:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        patient_id = int(params.patient_id)

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

        def get_patient_name():
            c = db.cursor()
            c.execute("SELECT fullName FROM users WHERE id = ?", (patient_id,))
            record = c.fetchone()

            name = record[0]
            print(name)
            return name

        name = get_patient_name()

        def close_dlg(e):
            call_end_dialog.open = False
            page.update()
            page.go(f"/chat_info/{user_id}{patient_id}")

        call_end_dialog = AlertDialog(
            modal=True,
            title=Text("Call Ended"),
            content=Text(f"Do you wish to end your call with patient {name}?"),
            actions=[
                TextButton("Yes", on_click=close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("End Call!"),
        )

        def open_dlg(e):
            page.dialog = call_end_dialog
            call_end_dialog.open = True
            page.update()

        return View(
            "/doctorCallInterface/:user_id:patient_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=lightBlue,
                          border_radius=30,
                          # child control
                          content=Column(
                              controls=[
                                  Container(padding=padding.only(left=95, top=70),
                                            content=Text(
                                                value=f"{name}",
                                                size=25,
                                                font_family="RobotoSlab",
                                                color=colors.BLACK,
                                                text_align=TextAlign.CENTER,
                                                weight=FontWeight.W_700)
                                            ),
                                  Container(padding=padding.only(left=50, top=20),
                                            content=Icon(icons.ACCOUNT_CIRCLE,
                                                         size=250)),
                                  Container(
                                      content=Row(
                                          controls=[
                                              Container(
                                                  margin=margin.only(left=80, top=200),
                                                  width=60,
                                                  height=60,
                                                  border_radius=60,
                                                  bgcolor=colors.GREY_800,
                                                  content=Icon(icons.MIC_OFF_OUTLINED, size=25)),
                                              Container(
                                                  margin=margin.only(top=200),
                                                  width=60,
                                                  height=60,
                                                  border_radius=60,
                                                  bgcolor=colors.GREY_800,
                                                  content=Icon(icons.VIDEOCAM_ROUNDED, size=25)),
                                              Container(
                                                  margin=margin.only(top=200),
                                                  width=60,
                                                  height=60,
                                                  border_radius=60,
                                                  bgcolor=colors.RED,
                                                  content=Icon(icons.CALL_END_ROUNDED, size=25),
                                                  on_click=open_dlg
                                              ),

                                          ]
                                      )
                                  )
                              ]
                          ))
            ]
        )
