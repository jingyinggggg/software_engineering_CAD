import os
import shutil

import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)
cursor = db.cursor()

def createTable():
    cursor.execute("""CREATE TABLE IF NOT EXISTS clinic(
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

class ClinicProfile:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        clinic_id = int(params.clinic_id)

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

        def get_clinic_details():
            cursor.execute("SELECT * FROM clinic WHERE id  = ?", (clinic_id,))
            clinic_record = cursor.fetchall()

            name = clinic_record[0][1]
            email = clinic_record[0][2]
            password = clinic_record[0][3]
            location = clinic_record[0][4]
            area = clinic_record[0][5]
            working_time = clinic_record[0][6]
            working_day = clinic_record[0][7]
            desc = clinic_record[0][8]
            phone_no = clinic_record[0][9]
            image = clinic_record[0][10]
            map_image = clinic_record[0][11]
            environment_image = clinic_record[0][12]
            reject_reason = clinic_record[0][15]
            closed = clinic_record[0][14]

            return (name, email, password, location, area, working_time,
                    working_day, desc, phone_no, image, map_image,
                    environment_image, reject_reason, closed)

        (clinic_name, clinic_email, clinic_password,
         clinic_location, clinic_area, clinic_working_time,
         clinic_working_day, clinic_desc, clinic_phone_no,
         clinic_image, clinic_map_image, clinic_environment, reject_reason,closed) = get_clinic_details()

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        clinic_nameTextField = TextField(
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

        setTextFieldValue(clinic_nameTextField, clinic_name)

        emailTextField = TextField(
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

        setTextFieldValue(emailTextField, clinic_email)

        clinic_locationTextField = TextField(
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

        setTextFieldValue(clinic_locationTextField, clinic_location)

        clinic_areaDropDown = Dropdown(
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

        setTextFieldValue(clinic_areaDropDown, clinic_area)

        working_dayTextField = TextField(
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

        setTextFieldValue(working_dayTextField, clinic_working_day)

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

        setTextFieldValue(clinic_closed,closed)

        working_timeTextField = TextField(
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

        setTextFieldValue(working_timeTextField, clinic_working_time)

        phoneNumberTextField = TextField(
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

        setTextFieldValue(phoneNumberTextField, clinic_phone_no)

        descriptionTextField = TextField(
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

        setTextFieldValue(descriptionTextField, clinic_desc)

        passwordTextField = TextField(
            label="Password",
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
            dense=True
        )

        setTextFieldValue(passwordTextField, clinic_password)

        clinic_image_textField = TextField(
            label="Clinic Image",
            width=242,
            # value=f"{location_file}",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            hint_text="Filename: clinic_name_image",
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=clinic_image,
            read_only=True
        )

        location_file = clinic_image
        map_file = clinic_map_image
        environment_file = clinic_environment

        def saveUpload(e: FilePickerResultEvent):
            # Get path of the image
            for x in e.files:
                location_file = f"pic/{x.name}"
                setTextFieldValue(clinic_image_textField, x.name)

                # This is to get current location
                copy = os.path.join(os.getcwd(), "pic")
                shutil.copy(x.path, copy)
                page.update()


        file_picker = FilePicker(on_result=saveUpload)

        page.overlay.append(file_picker)

        clinic_imageContainer = Container(
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
            hint_text="Filename: clinic_name_map",
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=clinic_map_image,
            read_only=True
        )

        def saveUploadMap(e: FilePickerResultEvent):
            # Get path of the image
            for x in e.files:
                map_file = f"pic/{x.name}"
                setTextFieldValue(clinic_map_textField, x.name)

                # This is to get current location
                copy = os.path.join(os.getcwd(), "pic")
                shutil.copy(x.path, copy)
                page.update()

        map_picker = FilePicker(on_result=saveUploadMap)

        page.overlay.append(map_picker)

        clinic_mapContainer = Container(
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
            hint_text="Filename: clinic_name_environment",
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=clinic_environment,
            read_only=True
        )

        def saveUploadEnvironment(e: FilePickerResultEvent):
            # Get path of the image
            for x in e.files:
                environment_file = f"pic/{x.name}"
                setTextFieldValue(clinic_environment_textField, x.name)

                # This is to get current location
                copy = os.path.join(os.getcwd(), "pic")
                shutil.copy(x.path, copy)
                page.update()

        environment_picker = FilePicker(on_result=saveUploadEnvironment)

        page.overlay.append(environment_picker)

        clinic_environmentContainer = Container(
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
            content=Text("You have successfully Updated your Profile!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: page.go(f"/clinicHomepage/{clinic_id}"))],
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

        def update_database(e):
            try:
                if (
                        clinic_nameTextField.value != "" and clinic_locationTextField.value != "" and clinic_areaDropDown.value != "" and working_timeTextField.value != ""
                        and working_dayTextField.value != "" and descriptionTextField.value != "" and phoneNumberTextField.value != "" and clinic_image_textField.value != ""
                        and clinic_map_textField.value != "" and clinic_environment_textField.value != "" and passwordTextField.value != "" and emailTextField.value != ""):

                    cursor.execute(
                        "UPDATE clinic SET name = ?, email = ?, password = ?, location = ?, area = ?,"
                        "workingTime = ?, workingDay = ?, clinicDescription = ?, phoneNumber = ?,"
                        "clinicImage = ?, mapImage = ?, environmentImage = ?, rejectReason = null, closed = ? "
                        "WHERE id = ?",
                        (clinic_nameTextField.value, emailTextField.value, passwordTextField.value, clinic_locationTextField.value, clinic_areaDropDown.value,
                         working_timeTextField.value, working_dayTextField.value, descriptionTextField.value, phoneNumberTextField.value,
                         "pic/"+clinic_image_textField.value, "pic/"+clinic_map_textField.value, "pic/"+clinic_environment_textField.value,clinic_closed.value,
                         clinic_id))

                    db.commit()
                    open_dlg(alert_dialog)
                else:
                    open_dlg(error_dialog)

            except sqlite3.Error as e:
                print("SQLite error:", e)

        return View(
            "/clinicProfile/:clinic_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          content=Column(
                              horizontal_alignment=CrossAxisAlignment.CENTER,
                              scroll=ScrollMode.AUTO,
                              controls=[
                                  Container(
                                      width=350,
                                      height=70,
                                      bgcolor=blue,
                                      alignment=alignment.top_center,
                                      content=Row(
                                          controls=[
                                              Container(
                                                  padding=padding.only(left=20, top=25),
                                                  content=Image(
                                                      src="pic/back.png",
                                                      color=colors.WHITE,
                                                      width=20,
                                                      height=20),
                                                  alignment=alignment.top_left,
                                                  on_click=lambda _: page.go(f"/clinicHomepage/{clinic_id}")),

                                              Container(
                                                  padding=padding.only(top=5),
                                                  content=Text(
                                                      value="View Clinic Profile Details",
                                                      size=20,
                                                      font_family="RobotoSlab",
                                                      color=colors.WHITE,
                                                      text_align=TextAlign.CENTER, )

                                              ),
                                          ]
                                      )
                                  ),

                                  Container(
                                      margin=margin.only(left=10, right=10),
                                      content=Column(
                                          controls=[
                                              Container(
                                                  content=Column(
                                                      controls=[
                                                          Container(
                                                              content=
                                                              Text(value="Clinic Details -",
                                                                   size=16,
                                                                   color=colors.BLACK,
                                                                   font_family="RobotoSlab",
                                                                   italic=True,
                                                                   weight=FontWeight.W_500)
                                                          ),
                                                      ]
                                                  )

                                              ),

                                              clinic_nameTextField,

                                              emailTextField,

                                              passwordTextField,

                                              clinic_locationTextField,

                                              clinic_areaDropDown,

                                              Row(
                                                  controls=[
                                                      working_dayTextField,

                                                      clinic_closed
                                                  ]
                                              ),

                                              working_timeTextField,

                                              phoneNumberTextField,

                                              descriptionTextField,

                                              clinic_imageContainer,

                                              clinic_mapContainer,

                                              clinic_environmentContainer,

                                              Container(
                                                  margin=margin.only(top=10, bottom=20),
                                                  content=TextButton(content=Text("Update Details",
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

                                                                     on_click=update_database
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
