import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class PatientCallDoctorPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        doctor_id = int(params.doctor_id)

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

        def get_doctor_name():
            c = db.cursor()
            c.execute("SELECT fullName, image FROM doctors WHERE id = ?", (doctor_id,))
            record = c.fetchall()

            doctorName = record[0][0]
            image = record[0][1]

            return doctorName, image

        doctorName, image = get_doctor_name()

        call_end_dialog = AlertDialog(
            modal=True,
            title=Text("Call Ended"),
            content=Text(f"Do you wish to end your call with Dr {doctorName}?"),
            actions=[
                TextButton("Yes", on_click=lambda _:page.go(f"/patientChat/{user_id}{doctor_id}")),
                TextButton("No", on_click=lambda _:close_dlg()),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        def open_dlg(e):
            page.dialog = call_end_dialog
            call_end_dialog.open = True
            page.update()

        def close_dlg():
            page.dialog = call_end_dialog
            call_end_dialog.open = False
            page.update()


        return View(
            "/patientCall/:user_id:doctor_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              horizontal_alignment="center",
                              controls=[
                                  Container(
                                      width=350,
                                      height=70,
                                      bgcolor=blue,
                                      alignment=alignment.top_center,
                                      padding=padding.only(left=10, bottom=0),
                                      content=Row(
                                          controls=[
                                              Container(
                                                  alignment=alignment.center,
                                                  padding=padding.only(left=115, top=25),
                                                  content=Text(
                                                      value="Voice Call",
                                                      size=20,
                                                      font_family="RobotoSlab",
                                                      color=colors.WHITE,
                                                      text_align=TextAlign.CENTER)
                                              ),

                                          ]
                                      )
                                  ),

                                  Container(
                                      margin=margin.only(top=150, bottom=10),
                                      # padding=padding.only(top=10, bottom=10),
                                      bgcolor=lightBlue,
                                      border_radius=50,
                                      content=Image(
                                          src=f"{image}",
                                          width=100,
                                          height=100,

                                      )
                                  ),

                                  Container(
                                      content=Text(
                                          value=f"Calling with Dr. {doctorName} ...",
                                          font_family="RobotoSlab",
                                          size=14,
                                          color=colors.BLACK

                                      )
                                  ),

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
                                                  content=Icon(icons.CALL_END_ROUNDED, size=25,),
                                                  on_click=open_dlg
                                              ),

                                          ]
                                      )
                                  )

                              ]
                          )
                          )
            ]
        )
