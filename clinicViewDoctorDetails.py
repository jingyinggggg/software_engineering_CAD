import os
import shutil

import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)
cursor = db.cursor()

class ClinicViewDoctorDetails:

    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):

        doctor_id = int(params.doctor_id)
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
            try:
                cursor.execute("SELECT name, phoneNumber  FROM clinic WHERE id = ?", (clinic_id,))
                record = cursor.fetchall()

                clinicName = record[0][0]
                phoneNumber = record[0][1]

                return  clinicName, phoneNumber
            except sqlite3.Error as e:
                print("SQLite error:", e)

        clinic_name, clinic_phone_number = get_clinic_details()

        def get_doctor_details():
            try:
                cursor.execute("SELECT fullName, username, email, password, experience, "
                               "specialization, description, workingTime, workingDay, image "
                               "FROM doctors WHERE id = ?", (doctor_id,))
                doctor_records = cursor.fetchall()

                doctor_fullName = doctor_records[0][0]
                doctor_username = doctor_records[0][1]
                doctor_email = doctor_records[0][2]
                doctor_password = doctor_records[0][3]
                doctor_experience = doctor_records[0][4]
                doctor_specialization = doctor_records[0][5]
                doctor_desc = doctor_records[0][6]
                doctor_working_time = doctor_records[0][7]
                doctor_working_day = doctor_records[0][8]
                doctor_image = doctor_records[0][9]

                return (doctor_fullName, doctor_username,
                        doctor_email, doctor_password,
                        doctor_experience, doctor_specialization,
                        doctor_desc, doctor_working_time,
                        doctor_working_day,
                        doctor_image)

            except sqlite3.Error as e:
                print("SQLite error:", e)

        (doctor_fullName, doctor_username,
         doctor_email, doctor_password,
         doctor_experience, doctor_specialization,
         doctor_desc, doctor_working_time,
         doctor_working_day, doctor_image) = get_doctor_details()

        username = TextField(
            label="Doctor Username",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=doctor_username,
            read_only=True
        )

        password = TextField(
            label="Doctor Password",
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
            dense=True,
            value=doctor_password,
            read_only=True
        )

        name = TextField(
            label="Doctor Name",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=doctor_fullName,
            read_only=True
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
            dense=True,
            value=doctor_email,
            read_only=True
        )

        phoneNumber = TextField(
            label="Clinic Phone Number",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=clinic_phone_number,
            read_only=True
        )

        experience = TextField(
            label="Working Experience",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=doctor_experience,
            read_only=True,

        )

        specialization = TextField(
            dense=True,
            label="Specialization",
            border_color=blue,
            height=40,
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            text_style=TextStyle(color=colors.BLACK,
                                 size=12,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500),
            value=doctor_specialization,
            read_only=True,
        )

        description = TextField(
            label="Description",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=doctor_desc,
            multiline=True
        )

        working_clinic = TextField(
            label="Working Clinic",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            read_only=True,
            value=clinic_name,
            dense=True
        )

        working_time = TextField(
            label="Working Start Time",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=doctor_working_time,
            read_only=True
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
            dense=True,
            value=doctor_working_day,
            read_only=True
        )

        doctor_image_textField = TextField(
            label="Doctor Image",
            width=230,
            # value=f"{location_file}",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            hint_text="Filename: clinic_name_doctor_name",
            border_color=blue,
            text_style=TextStyle(size=10,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab",
                                 weight=FontWeight.W_500
                                 ),
            dense=True,
            value=doctor_image,
            read_only=True
        )

        return View(
            "/clinicViewDoctorDetails/:doctor_id:clinic_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          content=Column(
                              scroll=ScrollMode.AUTO,
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
                                                              on_click=lambda _: page.go(f"/clinicHomepage/{clinic_id}")
                                                              ),

                                                    Container(padding=padding.only(left=30, top=25),
                                                              content=Text(
                                                                  value="View Doctor Details",
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
                                      content=Text(value="Doctor Details:",
                                                   color=colors.BLACK,
                                                   size=14,
                                                   italic=True,
                                                   font_family="RobotoSlab",
                                                   weight=FontWeight.W_500)
                                  ),

                                  Container(
                                      padding=padding.only(bottom=20),
                                      margin=margin.only(left=10, right=10),
                                      content=Column(
                                          controls=[
                                              username,

                                              password,

                                              name,

                                              email,

                                              phoneNumber,

                                              experience,

                                              specialization,

                                              description,

                                              working_clinic,

                                              working_time,

                                              working_day,

                                              doctor_image_textField,

                                          ]
                                      )
                                  )


                              ]
                          )
                          )
            ]
        )