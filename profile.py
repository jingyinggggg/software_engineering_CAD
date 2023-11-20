# import flet
# from flet import *
# from flet_route import Params, Basket
# import sqlite3
#
# db = sqlite3.connect("cad.db", check_same_thread=False)
#
#
# class ProfilePage:
#     def __init__(self):
#         self.show_sidebar = False
#
#     def view(self, page: Page, params: Params, basket: Basket):
#         # print(params)
#         user_id = int(params.user_id)
#
#         page.title = "Call A Doctor"
#         page.window_width = 380
#         page.window_height = 800
#         page.horizontal_alignment = "center"
#         page.vertical_alignment = "center"
#         page.theme_mode = "dark"
#
#         page.fonts = {
#             "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
#         }
#
#         lightBlue = "#D0DCEE"
#         blue = "#3386C5"
#         grey = "#71839B"
#
#         def get_user_details():
#             c = db.cursor()
#             c.execute("SELECT * FROM users WHERE id = ? AND address != ?", (user_id, ""))
#             record = c.fetchall()
#
#             # fullName = record[0][1]
#             # username = record[0][2]
#             # email = record[0][3]
#             # phoneNumber = record[0][4]
#             # password = record[0][5]
#             # dob = record[0][6]
#             # gender = record[0][7]
#             # address = record[0][8]
#             # emergencyContact = record[0][9]
#             return record
#
#         personal_details = get_user_details()
#
#         def get_username():
#             c = db.cursor()
#             c.execute(f"SELECT username FROM users WHERE id = {user_id}")
#             record = c.fetchone()
#             username = record[0]
#             return username
#
#         username = get_username()
#
#         def displayRecord(records):
#             if records:
#                 for record in records:
#                     return Container(
#                         width=350,
#                         height=500,
#                         bgcolor=lightBlue,
#                         margin=margin.only(top=20),
#                         padding=padding.only(left=10, right=10, top=20, bottom=20),
#                         content=Row(
#                             controls=[
#                                 Container(
#                                     padding=padding.only(left=10),
#                                     content=Column(
#                                         controls=[
#
#                                             Text(
#                                                 value=f"Personal Details",
#                                                 size=14,
#                                                 font_family="RobotoSlab",
#                                                 weight=FontWeight.W_600,
#                                                 color=colors.BLACK,
#                                             ),
#
#                                             Container(
#                                                 margin=margin.only(top=5, bottom=10),
#                                                 content=Row(
#                                                     controls=[
#                                                         Text(
#                                                             width=100,
#                                                             value="Full Name ",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Text(
#                                                             value=":",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Container(
#                                                             content=Text(
#                                                                 value=f"{record[1]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                                 text_align=TextAlign.JUSTIFY
#
#                                                             )
#                                                         )
#
#                                                     ]
#
#                                                 )
#                                             ),
#
#                                             Container(
#                                                 margin=margin.only(bottom=10),
#                                                 content=Row(
#                                                     controls=[
#                                                         Text(
#                                                             width=100,
#                                                             value="Email",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Text(
#                                                             value=":",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Container(
#                                                             content=Text(
#                                                                 value=f"{record[3]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                                 text_align=TextAlign.JUSTIFY
#
#                                                             )
#                                                         )
#
#                                                     ]
#
#                                                 )
#                                             ),
#
#                                             Container(
#                                                 margin=margin.only(bottom=10),
#                                                 content=Row(
#                                                     controls=[
#                                                         Text(
#                                                             width=100,
#                                                             value="Phone Number",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Text(
#                                                             value=":",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Container(
#                                                             content=Text(
#                                                                 value=f"{record[4]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                                 text_align=TextAlign.JUSTIFY
#
#                                                             )
#                                                         )
#                                                     ]
#                                                 )
#                                             ),
#
#                                             Container(
#                                                 margin=margin.only(bottom=10),
#                                                 content=Row(
#                                                     controls=[
#                                                         Text(
#                                                             width=100,
#                                                             value="Date Of Birth",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Text(
#                                                             value=":",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Container(
#                                                             content=Text(
#                                                                 value=f"{record[6]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                                 text_align=TextAlign.JUSTIFY
#
#                                                             )
#                                                         )
#                                                     ]
#                                                 )
#                                             ),
#
#                                             Container(
#                                                 margin=margin.only(bottom=10),
#                                                 content=Row(
#                                                     controls=[
#                                                         Text(
#                                                             width=100,
#                                                             value="Gender",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Text(
#                                                             value=":",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Container(
#                                                             content=Text(
#                                                                 value=f"{record[7]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                                 text_align=TextAlign.JUSTIFY
#
#                                                             )
#                                                         ),
#                                                     ]
#                                                 )
#                                             ),
#
#                                             Container(
#                                                 margin=margin.only(bottom=10),
#                                                 content=Row(
#                                                     controls=[
#                                                         Text(
#                                                             width=100,
#                                                             value="Address",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Text(
#                                                             value=":",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Container(
#                                                             content=Text(
#                                                                 width=180,
#                                                                 value=f"{record[8]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                                 text_align=TextAlign.JUSTIFY
#
#                                                             )
#                                                         )
#                                                     ]
#                                                 )
#                                             ),
#
#                                             Container(
#                                                 margin=margin.only(bottom=10),
#                                                 content=Row(
#                                                     controls=[
#                                                         Text(
#                                                             width=100,
#                                                             value="Emergency Contact",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Text(
#                                                             value=":",
#                                                             size=12,
#                                                             font_family="RobotoSlab",
#                                                             color=grey,
#                                                             text_align=TextAlign.JUSTIFY
#                                                         ),
#
#                                                         Container(
#                                                             content=Text(
#                                                                 value=f"{record[9]}",
#                                                                 size=12,
#                                                                 font_family="RobotoSlab",
#                                                                 color=grey,
#                                                                 text_align=TextAlign.JUSTIFY
#
#                                                             )
#                                                         )
#                                                     ]
#                                                 )
#                                             ),
#
#                                         ]
#                                     )
#                                 )
#                             ]
#                         )
#                     )
#
#             else:
#                 return Container(
#                     margin=margin.only(top=20),
#                     alignment=alignment.center,
#                     content=Text(
#                         width=300,
#                         value="Please complete your personal details at account page so that you can view your "
#                               "completed profile.",
#                         size=14,
#                         color=grey,
#                         font_family="RobotoSlab",
#                         text_align=TextAlign.JUSTIFY
#                     )
#                 )
#
#         return View(
#             "/profile/:user_id",
#             controls=[
#                 Container(width=350,
#                           height=700,
#                           bgcolor=colors.WHITE,
#                           border_radius=30,
#                           # child control
#                           content=Column(
#                               horizontal_alignment="center",
#                               controls=[
#                                   Container(width=350,
#                                             height=70,
#                                             bgcolor=blue,
#                                             alignment=alignment.top_center,
#                                             content=Row(
#                                                 controls=[
#                                                     Container(padding=padding.only(left=20, top=25),
#                                                               content=Image(
#                                                                   src="pic/back.png",
#                                                                   color=colors.WHITE,
#                                                                   width=20,
#                                                                   height=20
#                                                               ),
#                                                               on_click=lambda _: page.go(f"/homepage/{user_id}")
#                                                               ),
#
#                                                     Container(padding=padding.only(left=100, top=25),
#                                                               content=Text(
#                                                                   value="Profile",
#                                                                   size=20,
#                                                                   font_family="RobotoSlab",
#                                                                   color=colors.WHITE,
#                                                                   text_align=TextAlign.CENTER)
#                                                               ),
#                                                 ]
#                                             )
#                                             ),
#
#                                   Container(
#                                       padding=padding.only(top=10),
#                                       content=Column(
#                                           horizontal_alignment="center",
#                                           controls=[
#                                               Image(
#                                                   src="pic/avatar.png",
#                                                   width=75,
#                                                   height=75
#                                               ),
#
#                                               Text(
#                                                   value=username,
#                                                   size=14,
#                                                   text_align=TextAlign.CENTER,
#                                                   color=colors.BLACK,
#                                                   font_family="RobotoSlab",
#                                                   weight=FontWeight.W_500
#                                               )
#                                           ]
#                                       )
#                                   ),
#
#                                   displayRecord(personal_details)
#
#                               ]
#                           )
#                           )
#             ]
#         )

import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ProfilePage:
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
            c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]
            username = record[0][2]
            email = record[0][3]
            phoneNumber = record[0][4]
            password = record[0][5]
            dob = record[0][6]
            gender = record[0][7]
            address = record[0][8]
            emergencyContact = record[0][9]

            # return fullName, username, email, phoneNumber, password
            return fullName, username, email, phoneNumber, password, dob, gender, address, emergencyContact

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        fullName, username, email, phoneNumber, password, dob, gender, address, emergencyContact = get_user_details()

        fullNameTextField = TextField(
            label="Full Name",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            border_color=blue,
            # value=fullName,
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True,
            read_only=True
        )

        setTextFieldValue(fullNameTextField,fullName)

        emailTextField = TextField(
            label="Email",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(emailTextField,email)

        phoneNumberTextField = TextField(
            label="Phone Number",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(phoneNumberTextField,phoneNumber)

        dobTextField = TextField(
            label="Date Of Birth",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            border_color=blue,
            hint_text="Example: 26 October 2003",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(dobTextField, dob)

        genderTextField = Dropdown(
            height=40,
            dense=True,
            label="Gender",
            border_color=blue,
            label_style=TextStyle(size=12,
                                  weight=FontWeight.W_500,
                                  color=colors.GREY_800),
            hint_text="Please select your gender",
            hint_style=TextStyle(color=grey,
                                 size=12,
                                 italic=True),
            options=[
                dropdown.Option("Male"),
                dropdown.Option("Female"),
            ],
            text_style=TextStyle(size=12,
                                 color=grey,
                                 weight=FontWeight.W_500),
        )

        # genderTextField = TextField(
        #     label="Gender",
        #     label_style=TextStyle(font_family="RobotoSlab",
        #                           size=12,
        #                           color=colors.GREY_800),
        #     height=40,
        #     border_color=blue,
        #     hint_text="Example: Female",
        #     hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
        #     text_style=TextStyle(size=12,
        #                          color=colors.GREY_800,
        #                          weight=FontWeight.W_600,
        #                          ),
        #     dense=True
        # )

        setTextFieldValue(genderTextField, gender)

        addressTextField = TextField(
            label="Address",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            border_color=blue,
            hint_text="Example: Golden Triangle",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(addressTextField, address)

        emergencyContactTextField = TextField(
            label="Emergency Contact",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            height=40,
            border_color=blue,
            hint_text="*** Please enter your family's contact ***",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        setTextFieldValue(emergencyContactTextField, emergencyContact)

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have updated your personal information successfully!",
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

        def updateProfile(e):
            c = db.cursor()
            if fullNameTextField.value != "" and emailTextField.value != "" and phoneNumberTextField.value != "" and dobTextField.value != "" and genderTextField.value != "" and addressTextField.value != "" and emergencyContactTextField != "":
                c.execute(
                    f"UPDATE users SET dob = ?, gender = ?, address = ?, emergencyContact = ? WHERE id = {user_id}",
                    (
                    dobTextField.value, genderTextField.value, addressTextField.value, emergencyContactTextField.value))
                open_dlg()
                db.commit()
                fullName, username, email, phoneNumber, password, dob, gender, address, emergencyContact = get_user_details()
                setTextFieldValue(fullNameTextField, fullName)
                setTextFieldValue(emailTextField, email)
                setTextFieldValue(phoneNumberTextField,phoneNumber)
                setTextFieldValue(dobTextField, dob)
                setTextFieldValue(genderTextField, gender)
                setTextFieldValue(addressTextField, address)
                setTextFieldValue(emergencyContactTextField, emergencyContact)

        return View(
            "/profile/:user_id",
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
                                            content=Row(
                                                controls=[
                                                    Container(padding=padding.only(left=20, top=25),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ),
                                                              on_click=lambda _: page.go(f"/homepage/{user_id}")
                                                              ),

                                                    Container(padding=padding.only(left=100, top=25),
                                                              content=Text(
                                                                  value="Profile",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),
                                                ]
                                            )
                                            ),

                                  Container(
                                      padding=padding.only(top=10),
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
                                      margin=margin.only(left=20,right=20),
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

                                              phoneNumberTextField,

                                              dobTextField,

                                              genderTextField,

                                              addressTextField,

                                              emergencyContactTextField,

                                              Container(
                                                  padding=padding.only(top=20),
                                                  content=TextButton(content=Text("Update Profile",
                                                                                  size=16,
                                                                                  font_family="RobotoSlab",
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
