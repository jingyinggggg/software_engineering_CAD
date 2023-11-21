import os
import shutil

import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


def createTable():
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS clinic(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL,
                     password TEXT NOT NULL,
                     location TEXT NOT NULL,
                     area TEXT NOT NULL,
                     workingTime TEXT NOT NULL,
                     workingDay Text NOT NULL,
                     clinicDescription TEXT NOT NULL,
                     phoneNumber TEXT NOT NULL,
                     clinicImage TEXT NOT NULL,
                     mapImage TEXT NOT NULL,
                     environmentImage TEXT NOT NULL,
                     approvalStatus INTEGER NOT NULL,
                     closed TEXT NOT NULL)""")
    db.commit()


# def AddColumn():
#     c = db.cursor()
#     c.execute("ALTER TABLE clinic ADD COLUMN closed TEXT")
#     db.commit()

# def DropTable():
#     c = db.cursor()
#     c.execute('DROP TABLE clinic')
#     db.commit()


class ClinicSignUpPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
        # user_id = int(params.user_id)

        # AddColumn()

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

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        clinic_name = TextField(
            label="Clinic Name",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True
        )

        email = TextField(
            label="Email",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True
        )

        clinic_location = TextField(
            label="Clinic Location",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            multiline=True,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True
        )

        clinic_area = Dropdown(
            dense=True,
            label="Area",
            border_color=blue,
            height=40,
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            options=[
                dropdown.Option("Bayan Lepas"),
                dropdown.Option("Sungai Ara"),
                dropdown.Option("Relau"),
                dropdown.Option("Jelutong"),
                dropdown.Option("Georgetown"),
            ],
            text_style=TextStyle(color=grey,
                                 size=12,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500),
        )

        working_day = TextField(
            label="Working Day",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            hint_text="E.g. Monday - Sunday",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True,
            width=158
        )

        clinic_closed = Dropdown(
            dense=True,
            label="Clinic Closed",
            border_color=blue,
            height=40,
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            options=[
                dropdown.Option("None"),
                dropdown.Option("Monday"),
                dropdown.Option("Tuesday"),
                dropdown.Option("Wednesday"),
                dropdown.Option("Thursday"),
                dropdown.Option("Friday"),
                dropdown.Option("Saturday"),
                dropdown.Option("Sunday"),
            ],
            text_style=TextStyle(color=grey,
                                 size=12,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500),
            width=158,
        )

        working_time = TextField(
            label="Working Time",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            hint_text="Example: 12:00 pm - 8:00 pm",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True
        )

        phoneNumber = TextField(
            label="Phone Number",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True
        )

        description = TextField(
            label="Clinic Description",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            hint_text="Please describe that what services can you provided...",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True,
            multiline=True
        )

        password = TextField(label="Password",
                             password=True,
                             can_reveal_password=True,
                             label_style=TextStyle(font_family="RobotoSlab",
                                                   size=12,
                                                   color=colors.GREY_800),
                             border_color=blue,
                             text_style=TextStyle(size=12,
                                                  color=colors.BLACK,
                                                  font_family="RobotoSlab",
                                                  weight=FontWeight.W_500
                                                  ),
                             dense=True)

        clinic_image_textField = TextField(
            label="Clinic Image",
            width=242,
            # value=f"{location_file}",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            value="Filename: clinic_name_image",
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            read_only=True
        )

        location_file = Text("")
        map_file = Text("")
        environment_file = Text("")

        def saveUpload(e: FilePickerResultEvent):
            # Get path of the image
            for x in e.files:
                location_file.value = f"pic/{x.name}"
                setTextFieldValue(clinic_image_textField, x.name)

                # This is to get current location
                copy = os.path.join(os.getcwd(), "pic")
                shutil.copy(x.path, copy)
                page.update()

        file_picker = FilePicker(on_result=saveUpload)

        page.overlay.append(file_picker)

        clinic_image = Container(
            content=Row(
                controls=[
                    clinic_image_textField,

                    Container(
                        margin=margin.only(left=-18),
                        content=TextButton(content=Text("📂 Insert file",
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        color=colors.BLACK,
                                                        text_align=TextAlign.CENTER,
                                                        weight=FontWeight.W_500),
                                           on_click=lambda _: file_picker.pick_files()
                                           )
                    )
                ]
            )
        )

        clinic_map_textField = TextField(
            label="Clinic Map",
            width=242,
            # value=f"{location_file}",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            value="Filename: clinic_name_map",
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            read_only=True
        )

        def saveUploadMap(e: FilePickerResultEvent):
            # Get path of the image
            for x in e.files:
                map_file.value = f"pic/{x.name}"
                setTextFieldValue(clinic_map_textField, x.name)

                # This is to get current location
                copy = os.path.join(os.getcwd(), "pic")
                shutil.copy(x.path, copy)
                page.update()

        map_picker = FilePicker(on_result=saveUploadMap)

        page.overlay.append(map_picker)

        clinic_map = Container(
            content=Row(
                controls=[
                    clinic_map_textField,

                    Container(
                        margin=margin.only(left=-18),
                        content=TextButton(content=Text("📂 Insert file",
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        color=colors.BLACK,
                                                        text_align=TextAlign.CENTER,
                                                        weight=FontWeight.W_500),
                                           on_click=lambda _: map_picker.pick_files()
                                           )
                    )
                ]
            )
        )

        clinic_environment_textField = TextField(
            label="Clinic Map",
            width=242,
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            value="Filename: clinic_name_environment",
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            read_only=True
        )

        def saveUploadEnvironment(e: FilePickerResultEvent):
            # Get path of the image
            for x in e.files:
                environment_file.value = f"pic/{x.name}"
                setTextFieldValue(clinic_environment_textField, x.name)

                # This is to get current location
                copy = os.path.join(os.getcwd(), "pic")
                shutil.copy(x.path, copy)
                page.update()

        environment_picker = FilePicker(on_result=saveUploadEnvironment)

        page.overlay.append(environment_picker)

        clinic_environment = Container(
            content=Row(
                controls=[
                    clinic_environment_textField,

                    Container(
                        margin=margin.only(left=-18),
                        content=TextButton(content=Text("📂 Insert file",
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        color=colors.BLACK,
                                                        text_align=TextAlign.CENTER,
                                                        weight=FontWeight.W_500),
                                           on_click=lambda _: environment_picker.pick_files()
                                           )
                    )

                ]
            )
        )

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have created your account successfully. Log in to your account to enjoy our service now!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go("/"))],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Failed", text_align=TextAlign.CENTER),
            content=Text(
                "Somthing went wrong! Please make sure that you have filled in the details completely.",
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

        def addToDatabase(e):
            createTable()
            c = db.cursor()
            if (
                    clinic_name.value != "" and clinic_location.value != "" and clinic_area.value != "" and working_time.value != ""
                    and working_day.value != "" and clinic_closed.value != "" and description.value != "" and phoneNumber.value != "" and clinic_image_textField.value != ""
                    and clinic_map_textField.value != "" and clinic_environment_textField.value != "" and password.value != "" and email.value != ""):
                c.execute(
                    "INSERT INTO clinic (name, email, password, location, area, workingTime, workingDay, "
                    "clinicDescription, phoneNumber, clinicImage, mapImage, environmentImage, approvalStatus, closed)"
                    "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (clinic_name.value, email.value, password.value, clinic_location.value, clinic_area.value,
                     working_time.value,
                     working_day.value, description.value, phoneNumber.value, location_file.value, map_file.value,
                     environment_file.value, 0, clinic_closed.value))
                db.commit()
                open_dlg(alert_dialog)
            else:
                open_dlg(error_dialog)

        return View(
            "/clinicSignUp",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          content=Column(
                              horizontal_alignment="center",
                              scroll=True,
                              controls=[
                                  Row(
                                      vertical_alignment="center",
                                      controls=[
                                          Container(
                                              margin=margin.only(left=10, top=20, bottom=10),
                                              content=Image(src="pic/back.png",
                                                            width=20,
                                                            height=20),
                                              alignment=alignment.top_left,
                                              on_click=lambda _: page.go(f"/loginUser")),

                                          Container(
                                              margin=margin.only(top=20, bottom=10),
                                              content=Text(value="Create an account - Clinic",
                                                           size=18,
                                                           color="#3386C5",
                                                           font_family="RobotoSlab",
                                                           italic=True,
                                                           weight=FontWeight.W_500)

                                          ),
                                      ]
                                  ),

                                  Container(
                                      margin=margin.only(left=10, right=10),
                                      content=Column(
                                          controls=[
                                              clinic_name,

                                              email,

                                              password,

                                              clinic_location,

                                              clinic_area,

                                              Row(
                                                  controls=[
                                                      working_day,
                                                      clinic_closed
                                                  ]
                                              ),

                                              working_time,

                                              phoneNumber,

                                              description,

                                              clinic_image,

                                              clinic_map,

                                              clinic_environment,

                                              Container(
                                                  margin=margin.only(top=10, bottom=20),
                                                  content=TextButton(content=Text("Sign Up",
                                                                                  size=16,
                                                                                  font_family="RobotoSlab",
                                                                                  color=colors.WHITE,
                                                                                  text_align=TextAlign.CENTER),
                                                                     width=325,
                                                                     height=45,
                                                                     style=ButtonStyle(bgcolor={"": blue},
                                                                                       shape={
                                                                                           "": RoundedRectangleBorder(
                                                                                               radius=10)}),

                                                                     on_click=addToDatabase
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
