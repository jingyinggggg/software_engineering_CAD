import os
import shutil

import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


def CreateTable():
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS doctors(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 fullName TEXT NOT NULL,
                 username TEXT ,
                 email TEXT NOT NULL,
                 phoneNumber TEXT NOT NULL,
                 password TEXT ,
                 experience TEXT NOT NULL,
                 specialization TEXT NOT NULL,
                 description TEXT NOT NULL,
                 clinic TEXT NOT NULL,
                 workingTime TEXT NOT NULL,
                 workingDay TEXT NOT NULL,
                 image TEXT NOT NULL,
                 STATUS INTEGER NOT NULL)""")
    db.commit()


# def DeleteColumn():
#     c = db.cursor()
#     c.execute("ALTER TABLE doctors ADD COLUMN image TEXT")
#     db.commit()


class AddDoctorDetailsPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):

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

        # CreateTable()

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        name = TextField(
            label="Doctor Name",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=grey,
                                 font_family="RobotoSlab"
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
                                 color=grey,
                                 font_family="RobotoSlab"
                                 ),
            dense=True
        )

        phoneNumber = TextField(
            label="Phone Number",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=grey,
                                 font_family="RobotoSlab"
                                 ),
            dense=True
        )

        experience = TextField(
            label="Working Experience",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=grey,
                                 font_family="RobotoSlab"
                                 ),
            hint_text="Example: 3 years working experience",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True
        )

        specialization = TextField(
            label="Speciality",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=grey,
                                 font_family="RobotoSlab"
                                 ),
            hint_text="Example: Cardiologists",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True
        )

        description = TextField(
            label="Description",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=grey,
                                 font_family="RobotoSlab"
                                 ),
            hint_text="Please describe that what services can doctor provided...",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True,
            multiline=True
        )

        working_clinic = TextField(
            label="Working Clinic",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=grey,
                                 font_family="RobotoSlab"
                                 ),
            dense=True
        )

        working_time = TextField(
            label="Working Time",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=grey,
                                 font_family="RobotoSlab"
                                 ),
            hint_text="Example: 12:00 pm - 8:00 pm",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True
        )

        working_day = TextField(
            label="Working Day",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=grey,
                                 font_family="RobotoSlab"
                                 ),
            hint_text="Example: Monday - Sunday (except Wednesday)",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True
        )

        doctor_image_textField = TextField(
            label="Doctor Image",
            width=230,
            # value=f"{location_file}",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            value="Filename: clinic_name_doctor_name",
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=grey,
                                 font_family="RobotoSlab"
                                 ),
            dense=True,
            read_only=True
        )

        image_file = Text("")

        def saveUpload(e: FilePickerResultEvent):
            # Get path of the image
            for x in e.files:
                image_file.value = f"pic/{x.name}"
                setTextFieldValue(doctor_image_textField, x.name)

                # This is to get current location
                copy = os.path.join(os.getcwd(), "pic")
                shutil.copy(x.path, copy)
                page.update()

        file_picker = FilePicker(on_result=saveUpload)

        page.overlay.append(file_picker)

        doctor_image = Container(
            content=Row(
                controls=[
                    doctor_image_textField,

                    Container(
                        margin=margin.only(left=-8),
                        content=TextButton(content=Text("📂 Insert file",
                                                        size=12,
                                                        font_family="RobotoSlab",
                                                        color=colors.BLACK,
                                                        text_align=TextAlign.CENTER),
                                           on_click=lambda _: file_picker.pick_files()
                                           )
                    )
                ]
            )
        )

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text(
                "You have upload the doctor details successfully. Doctor will be able to log into their account after it is approved by admin. Please stay tuned to the doctor account approval status.",
                text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg())],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_dlg():
            page.dialog = alert_dialog
            alert_dialog.open = True
            page.update()

        def close_dlg():
            page.dialog = alert_dialog
            alert_dialog.open = False
            page.update()

        def addToDatabase(e):
            CreateTable()
            c = db.cursor()
            if (name.value != "" and email.value != "" and phoneNumber.value != "" and experience.value != ""
                    and specialization.value != "" and description.value != "" and working_clinic.value != ""
                    and working_time.value != "" and working_day.value != "" and image_file.value != ""):
                c.execute(
                    "INSERT INTO doctors (fullName, email, phoneNumber, experience, specialization, "
                    "description, clinic, workingTime, workingDay, image, status)"
                    "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (name.value, email.value, phoneNumber.value, experience.value, specialization.value,
                     description.value, working_clinic.value, working_time.value, working_day.value, image_file.value,
                     1))
                db.commit()
                open_dlg()

        return View(
            "/addDoctorDetails",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              # horizontal_alignment="center",
                              scroll=True,
                              controls=[
                                  Container(width=350,
                                            height=70,
                                            bgcolor=blue,
                                            alignment=alignment.top_center,
                                            content=Row(
                                                controls=[
                                                    Container(padding=padding.only(left=20, top=25),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ),
                                                              on_click=lambda _: page.go(f"/loginUser")
                                                              ),

                                                    Container(padding=padding.only(left=80, top=25),
                                                              content=Text(
                                                                  value="Add Doctor",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),
                                                ]
                                            )
                                            ),

                                  Container(
                                      margin=margin.only(left=10, bottom=10, top=10),
                                      content=Text(value="Please provide us about the doctor details:",
                                                   color=colors.BLACK,
                                                   size=14,
                                                   italic=True,
                                                   font_family="RobotoSlab",
                                                   weight=FontWeight.W_500)
                                  ),

                                  Container(
                                      margin=margin.only(left=10, right=10),
                                      content=Column(
                                          controls=[
                                              name,

                                              email,

                                              phoneNumber,

                                              experience,

                                              specialization,

                                              description,

                                              working_clinic,

                                              working_time,

                                              working_day,

                                              doctor_image,

                                              Container(
                                                  margin=margin.only(top=10, bottom=20),
                                                  content=TextButton(content=Text("Upload",
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
