import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ClinicAdminAccountPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
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

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        def get_user_details():
            c = db.cursor()
            c.execute("SELECT * FROM clinicAdmin WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]
            username = record[0][2]
            email = record[0][3]
            clinicID = record[0][5]

            return fullName, username, email, clinicID

        def get_working_clinic():
            c = db.cursor()
            c.execute(f"SELECT name FROM clinic WHERE id = {clinicID}")
            record = c.fetchone()

            clinic_name = record[0]

            return clinic_name

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        fullName, username, email, clinicID = get_user_details()
        clinic_name = get_working_clinic()

        fullNameTextField = TextField(
            label="Full Name",
            label_style=TextStyle(size=12,
                                  color=colors.BLACK,
                                  weight=FontWeight.W_700),
            height=40,
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
        )

        setTextFieldValue(fullNameTextField, fullName)

        emailTextField = TextField(
            label="Email",
            label_style=TextStyle(size=12,
                                  color=colors.BLACK,
                                  weight=FontWeight.W_700),
            height=40,
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(emailTextField, email)

        workingClinicTextField = TextField(
            label="Working Clinic",
            label_style=TextStyle(size=12,
                                  color=colors.BLACK,
                                  weight=FontWeight.W_700),
            height=40,
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            read_only=True
        )

        setTextFieldValue(workingClinicTextField, clinic_name)

        success_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have updated your personal information successfully!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg())],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Failed", text_align=TextAlign.CENTER),
            content=Text("Something went wrong! Please try again...",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_error_dlg())],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_dlg():
            page.dialog = success_dialog
            success_dialog.open = True
            page.update()

        def close_dlg():
            page.dialog = success_dialog
            success_dialog.open = False
            page.update()

        def open_error_dlg():
            page.dialog = error_dialog
            error_dialog.open = True
            page.update()

        def close_error_dlg():
            page.dialog = error_dialog
            error_dialog.open = False
            page.update()

        def updateProfile(e):
            c = db.cursor()
            if fullNameTextField.value != "" and emailTextField.value != "":
                c.execute(f"UPDATE clinicAdmin SET fullName = ?, email = ? WHERE id = {user_id}",
                          (fullNameTextField.value, emailTextField.value))
                open_dlg()
                db.commit()
                fullName, username, email, clinicID = get_user_details()
                setTextFieldValue(fullNameTextField, fullName)
                setTextFieldValue(emailTextField, email)
            else:
                open_error_dlg()

        return View(
            "/admin/account/:user_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              # horizontal_alignment="center",
                              controls=[
                                  Container(
                                      padding=padding.only(top=25, left=20, bottom=10),
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
                                                  value=" Profile",
                                                  color="#3386C5",
                                                  weight=FontWeight.W_600,
                                                  size=18,
                                              )
                                          ]
                                      ),
                                  ),

                                  Container(
                                      padding=padding.only(top=10, left =110),
                                      content=Column(
                                          horizontal_alignment="center",
                                          controls=[
                                              Image(
                                                  src="pic/avatar.png",
                                                  width=75,
                                                  height=75
                                              ),

                                              Text(
                                                  value=username,
                                                  size=14,
                                                  text_align=TextAlign.CENTER,
                                                  color=colors.BLACK,
                                                  font_family="RobotoSlab",
                                                  weight=FontWeight.W_500
                                              )
                                          ]
                                      )
                                  ),

                                  Container(
                                      margin=margin.only(left=20, right=20, top=20),
                                      padding=padding.only(top=10),
                                      alignment=alignment.center_left,
                                      content=Column(
                                          controls=[
                                              Text(
                                                  value="Personal Information",
                                                  size=12,
                                                  color=colors.BLACK,
                                                  weight=FontWeight.W_600,
                                                  font_family="RobotoSlab",
                                                  text_align=TextAlign.LEFT
                                              ),

                                              fullNameTextField,

                                              emailTextField,

                                              workingClinicTextField,

                                              Container(
                                                  padding=padding.only(top=20),
                                                  content=TextButton(content=Text("Update Profile",
                                                                                  size=16,
                                                                                  color="WHITE",
                                                                                  text_align=TextAlign.CENTER),
                                                                     width=310,
                                                                     height=45,
                                                                     style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                                       shape={
                                                                                           "": RoundedRectangleBorder(
                                                                                               radius=7)}
                                                                                       ),
                                                                     ),
                                                  on_click=updateProfile
                                              ),

                                          ]

                                      )
                                  )

                              ]
                          )
                          )
            ]
        )
