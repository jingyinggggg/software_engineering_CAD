import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ViewMedicalRecordPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
        medicalRecord_id = int(params.medicalRecord_id)

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
            c.execute("SELECT * FROM medicalRecordHistory WHERE id = ?", (medicalRecord_id,))
            record = c.fetchall()

            user_id = record[0][2]
            print(medicalRecord_id)
            bloodType = record[0][3]
            allergies = record[0][4]
            pastMedicalCondition = record[0][5]
            surgicalHistory = record[0][6]
            familyMedicalHistory = record[0][7]
            currentMedicalCondition = record[0][8]
            currentMedication = record[0][9]
            dosage = record[0][10]

            return user_id, bloodType, allergies, pastMedicalCondition, surgicalHistory, familyMedicalHistory, currentMedicalCondition, currentMedication, dosage

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        user_id, bloodType, allergies, pastMedicalCondition, surgicalHistory, familyMedicalHistory, currentMedicalCondition, currentMedication, dosage = get_user_details()

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text("You have updated your medical record successfully!",
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
        setTextFieldValue(bloodTypeTextField, bloodType)

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

        setTextFieldValue(allergiesTextField, allergies)

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

        setTextFieldValue(pastMedicalConditionTextField, pastMedicalCondition)

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

        setTextFieldValue(surgicalHistoryTextField, surgicalHistory)

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

        setTextFieldValue(familyMedicalHistoryTextField, familyMedicalHistory)

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

        setTextFieldValue(currentMedicalConditionTextField, currentMedicalCondition)

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

        setTextFieldValue(currentMedicationTextField, currentMedication)

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

        setTextFieldValue(dosageTextField, dosage)

        def updateRecord(e):
            if (
                    bloodTypeTextField.value != "" and allergiesTextField.value != "" and pastMedicalConditionTextField.value != "" and
                    surgicalHistoryTextField.value != "" and familyMedicalHistoryTextField.value != "" and currentMedicalConditionTextField.value != "" and
                    currentMedicationTextField.value != "" and dosageTextField.value != ""):
                c = db.cursor()
                c.execute(f'UPDATE medicalRecordHistory SET bloodType = ?, allergies = ?, pastMedicalCondition = '
                          f'?, surgicalHistory = ?, familyMedicalHistory = ?, currentMedicalCondition = ?, '
                          f'currentMedication = ?, dosage = ? WHERE id = {medicalRecord_id}',
                          (
                              bloodTypeTextField.value, allergiesTextField.value, pastMedicalConditionTextField.value,
                              surgicalHistoryTextField.value, familyMedicalHistoryTextField.value,
                              currentMedicalConditionTextField.value,
                              currentMedicationTextField.value, dosageTextField.value))
                db.commit()
                open_dlg()
                user_id, bloodType, allergies, pastMedicalCondition, surgicalHistory, familyMedicalHistory, currentMedicalCondition, currentMedication, dosage = get_user_details()
                setTextFieldValue(bloodTypeTextField, bloodType)
                setTextFieldValue(allergiesTextField, allergies)
                setTextFieldValue(pastMedicalConditionTextField, pastMedicalCondition)
                setTextFieldValue(surgicalHistoryTextField, surgicalHistory)
                setTextFieldValue(familyMedicalHistoryTextField, familyMedicalHistory)
                setTextFieldValue(currentMedicalConditionTextField, currentMedicalCondition)
                setTextFieldValue(currentMedicationTextField, currentMedication)
                setTextFieldValue(dosageTextField, dosage)

        return View(
            "/viewMedicalRecord/:medicalRecord_id",
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
                                                        on_click=lambda _: page.go(f"/medicalRecord/{int(user_id)}")
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
                                                  content=TextButton(content=Text("Update",
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
                                                  on_click=updateRecord
                                              ),

                                          ]

                                      )
                                  )

                              ]
                          )
                          )
            ]
        )