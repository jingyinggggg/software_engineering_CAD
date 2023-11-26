import datetime
from datetime import date
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class Prescription:
    def __init__(self):
        pass
        # self.selected_date = date.today()
        # self.show_confirmation = False
        # self.show_alert = False

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        # booking_id = int(params.booking_id)
        prescription_id = int(params.prescription_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        def get_prescription_details(prescription_id):
            c = db.cursor()
            c.execute(f"SELECT * FROM prescriptions WHERE prescriptionID = {prescription_id}")
            prescription = c.fetchall()

            # print(prescription[0])

            patient_first_name = prescription[0][3].split()[-2:]
            patient_last_name = prescription[0][3].split()[0]
            prescription_id = prescription[0][0]
            patient_id = prescription[0][2]
            medication_name = prescription[0][4]
            quantity = prescription[0][5]
            duration = prescription[0][6]
            date_signed = prescription[0][7]
            instruction = prescription[0][8]

            # return prescription
            return patient_first_name,patient_last_name,prescription_id,patient_id,medication_name,quantity,duration,date_signed,instruction

        patient_first_name,patient_last_name,prescription_id,patient_id,medication_name,quantity,duration,date_signed,instruction = get_prescription_details(prescription_id)

        def setTextFieldValue(textField, value):
            if value != "":
                textField.value = value

        paddingContainer = Container(padding=padding.only(bottom=1))

        medicationName = TextField(
            width=320,
            read_only=True,
            border_color=colors.BLUE,
            hint_text="Example: Panadol",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )
        setTextFieldValue(medicationName, medication_name)

        quantityTextField = TextField(
            width=320,
            read_only=True,
            border_color=colors.BLUE,
            hint_text="Example: 5mg",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )
        setTextFieldValue(quantityTextField, quantity)

        durationTextField = TextField(
            width=320,
            read_only=True,
            border_color=colors.BLUE,
            hint_text="Example: 1 month",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )
        setTextFieldValue(durationTextField, duration)

        dateSignedTextField = TextField(
            width=320,
            read_only=True,
            border_color=colors.BLUE,
            hint_text="Example: 25/11/2023",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            # value=date_signed.strftime('%d/%m/%Y'),
            dense=True
        )
        setTextFieldValue(dateSignedTextField, date_signed)

        instructionTextField = TextField(
            width=320,
            multiline=True,
            read_only=True,
            border_color=colors.BLUE,
            hint_text="Please take your medicine after meal.",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 weight=FontWeight.W_600,
                                 ),
            dense=True
        )
        setTextFieldValue(instructionTextField, instruction)

        return View(
            "/prescription/:user_id/:prescription_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    # alignment=MainAxisAlignment.CENTER,
                    content=Column(
                        scroll=True,
                        controls=[
                            Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Container(
                                        padding=padding.only(right=120),
                                        width=350,
                                        height=80,
                                        bgcolor="#3386C5",
                                        content=Row(controls=[
                                            Container(padding=padding.only(left=10, top=5),
                                                      content=Image(
                                                          src="pic/back.png",
                                                          color=colors.WHITE,
                                                          width=20,
                                                          height=20
                                                      ),
                                                      on_click=lambda _: page.go(f"/prescriptionList/{user_id}")),
                                            Container(padding=padding.only(left=50),
                                                      content=Text("View Prescription",
                                                                   color="WHITE",
                                                                   text_align=TextAlign.CENTER,
                                                                   size=20,
                                                                   font_family="RobotoSlab")),
                                            # Container(padding=padding.only(left=30),
                                            #           content=Icon(icons.MODE_EDIT_OUTLINED,
                                            #                        size=20,
                                            #                        color=colors.WHITE),
                                            #           on_click=lambda _: page.go(f"/editPrescription/{user_id}{booking_id}")
                                            #           )
                                        ]
                                        )
                                    )
                                ]),
                            Container(
                                padding=padding.only(left=10),
                                content=Column(
                                    controls=[
                                        Text(
                                            "Patient's Name:",
                                            color="#666666",
                                            size=14,
                                            weight=FontWeight.BOLD
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.START,
                                            controls=[
                                                TextField(
                                                    label="First Name",
                                                    read_only=True,
                                                    value=' '.join(patient_first_name),
                                                    width=150,
                                                    height=35,
                                                    label_style=TextStyle(color="BLACK"),
                                                    border_color=colors.BLACK,
                                                    text_style=TextStyle(size=12, color=colors.BLACK,
                                                                         weight=FontWeight.W_600),
                                                ),
                                                TextField(
                                                    label="Last Name",
                                                    read_only=True,
                                                    value=patient_last_name,
                                                    width=150,
                                                    height=35,
                                                    label_style=TextStyle(color="BLACK"),
                                                    border_color=colors.BLACK,
                                                    text_style=TextStyle(size=12, color=colors.BLACK,
                                                                         weight=FontWeight.W_600),
                                                )
                                            ]
                                        ),
                                        Text(
                                            "Treatment",
                                            color="#666666",
                                            size=14,
                                            weight=FontWeight.BOLD
                                        ),
                                        Text(
                                            "A: Medication Name / Strength",
                                            color="#666666",
                                            size=12,
                                            weight=FontWeight.W_600
                                        ),
                                        medicationName,

                                        Text(
                                            "B: Quantity / Dosage Frequency",
                                            color="#666666",
                                            size=12,
                                            weight=FontWeight.W_600
                                        ),
                                        quantityTextField,

                                        Text(
                                            "C: Duration of Treatment / Treatment Frequency",
                                            color="#666666",
                                            size=12,
                                            weight=FontWeight.W_600
                                        ),
                                        durationTextField,
                                        paddingContainer,

                                        Text(
                                            "Date Signed",
                                            color="#666666",
                                            size=14,
                                            weight=FontWeight.BOLD
                                        ),
                                        dateSignedTextField,
                                        paddingContainer,

                                        Text(
                                            "Specific Instructions",
                                            color="#666666",
                                            size=14,
                                            weight=FontWeight.BOLD
                                        ),
                                        instructionTextField,

                                        Container(padding=padding.only(top=10, bottom=10),
                                                  content=TextButton(content=Text("Edit",
                                                                                  size=16,
                                                                                  font_family="RobotoSlab",
                                                                                  color="WHITE",
                                                                                  text_align=TextAlign.CENTER),
                                                                     width=320,
                                                                     height=45,
                                                                     style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                                       shape={
                                                                                           "": RoundedRectangleBorder(
                                                                                               radius=7)}
                                                                                       ),
                                                                     on_click=lambda _: page.go(
                                                                         f"/editPrescription/{user_id}/{prescription_id}")
                                                                     ),

                                                  ),
                                    ]
                                )
                            )
                        ]
                    )
                )
            ])
