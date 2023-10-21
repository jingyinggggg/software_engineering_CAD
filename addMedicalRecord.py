import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


def CreateTable():
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS medicalRecordHistory(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 patientName TEXT NOT NULL,
                 patientUserID INTEGER NOT NULL,
                 bloodType TEXT NOT NULL,
                 allergies TEXT NOT NULL,
                 pastMedicalCondition TEXT NOT NULL,
                 surgicalHistory TEXT,
                 familyMedicalHistory TEXT,
                 currentMedicalCondition TEXT,
                 currentMedication TEXT,
                 dosage TEXT,
                 date TEXT)""")
    db.commit()


# def AddColumn():
#     c = db.cursor()
#     c.execute("ALTER TABLE medicalRecordHistory ADD COLUMN date TEXT")
#     db.commit()


class AddMedicalRecordPage:
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

        date = datetime.datetime.now()
        current_date = date.strftime("%d %b %y")

        def get_user_details():
            c = db.cursor()
            c.execute("SELECT fullName FROM users WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][0]

            # return fullName, username, email, phoneNumber, password
            return fullName

        fullName = get_user_details()

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have added your medical record successfully!",
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

        paddingContainer = Container(padding=padding.only(bottom=1))

        bloodTypeTextField = TextField(
            label="Blood Type",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: B-",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        allergiesTextField = TextField(
            label="Allergies",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="***Including medical allergies",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        pastMedicalConditionTextField = TextField(
            label="Past Medical Condition and Diagnoses",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: Anemia",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        surgicalHistoryTextField = TextField(
            label="Surgical History",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: Surgery - Date",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        familyMedicalHistoryTextField = TextField(
            label="Family Medical History",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: Heart Disease",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        currentMedicalConditionTextField = TextField(
            label="Current Medical Condition",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: Diabetes",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        currentMedicationTextField = TextField(
            label="Current Medication",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: Aspirin",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        dosageTextField = TextField(
            label="Dosage and Frequency",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            border_color=blue,
            hint_text="Example: Dosage - 81mg, Frequency - Once daily",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )

        def addToDatabase(e):
            CreateTable()
            try:
                if (
                        bloodTypeTextField.value != "" and allergiesTextField.value != "" and pastMedicalConditionTextField.value != "" and
                        surgicalHistoryTextField.value != "" and familyMedicalHistoryTextField.value != "" and currentMedicalConditionTextField.value != "" and
                        currentMedicationTextField.value != "" and dosageTextField.value != ""):
                    c = db.cursor()
                    c.execute('INSERT INTO medicalRecordHistory (patientName, patientUserID, bloodType, allergies, '
                              'pastMedicalCondition, surgicalHistory, familyMedicalHistory, currentMedicalCondition, '
                              'currentMedication, dosage, date)'
                              'VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?)',
                              (
                                  fullName, user_id, bloodTypeTextField.value, allergiesTextField.value,
                                  pastMedicalConditionTextField.value,
                                  surgicalHistoryTextField.value, familyMedicalHistoryTextField.value,
                                  currentMedicalConditionTextField.value,
                                  currentMedicationTextField.value, dosageTextField.value, current_date))
                    db.commit()
                    page.update()
                    open_dlg()
                    print("success")
            except Exception as e:
                print(e)

        return View(
            "/addMedicalRecord/:user_id",
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
                                            content=Row(
                                                controls=[
                                                    Container(
                                                        padding=padding.only(top=25, left=20),
                                                        content=Image(
                                                            src="pic/back.png",
                                                            color=colors.WHITE,
                                                            width=20,
                                                            height=20
                                                        ),
                                                        on_click=lambda _: page.go(f"/medicalRecord/{user_id}")
                                                    ),

                                                    Container(
                                                        padding=padding.only(top=25, left=70),
                                                        content=Text(
                                                            value="Medical Reocrd",
                                                            size=18,
                                                            font_family="RobotoSlab",
                                                            color=colors.WHITE,
                                                            text_align=TextAlign.CENTER)
                                                    )
                                                ]
                                            )
                                            ),

                                  Container(
                                      padding=padding.only(left=20, right=20, top=10),
                                      alignment=alignment.center_left,
                                      content=Column(
                                          controls=[
                                              Text(
                                                  value="Medical Information/ History",
                                                  size=12,
                                                  color=colors.BLACK,
                                                  weight=FontWeight.W_600,
                                                  font_family="RobotoSlab",
                                                  text_align=TextAlign.LEFT
                                              ),

                                              bloodTypeTextField,
                                              paddingContainer,

                                              allergiesTextField,
                                              paddingContainer,

                                              pastMedicalConditionTextField,
                                              paddingContainer,

                                              surgicalHistoryTextField,
                                              paddingContainer,

                                              familyMedicalHistoryTextField,
                                              paddingContainer,

                                              currentMedicalConditionTextField,
                                              paddingContainer,

                                              currentMedicationTextField,
                                              paddingContainer,

                                              dosageTextField,
                                              paddingContainer,

                                              Container(
                                                  content=TextButton(content=Text("Add",
                                                                                  size=16,
                                                                                  font_family="RobotoSlab",
                                                                                  color="WHITE",
                                                                                  text_align=TextAlign.CENTER),
                                                                     width=305,
                                                                     height=45,
                                                                     style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                                       shape={
                                                                                           "": RoundedRectangleBorder(
                                                                                               radius=7)}
                                                                                       ),
                                                                     ),
                                                  on_click=addToDatabase
                                              ),

                                          ]

                                      )
                                  )

                              ]
                          )
                          )
            ]
        )
