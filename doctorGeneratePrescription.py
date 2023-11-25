import datetime
from datetime import date
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class DoctorGeneratePrescription:
    def __init__(self):
        self.selected_date = date.today()
        self.show_confirmation = False
        self.show_alert = False

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        booking_id = int(params.booking_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        medicationName_value = ""
        quantity_value = ""
        duration_value = ""
        instruction_value = ""
        dateSigned = datetime.datetime.now().strftime('%Y-%m-%d')

        def create_prescriptions_table():
            c = db.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS prescriptions (
                    prescriptionID INTEGER PRIMARY KEY AUTOINCREMENT,
                    patientID INTEGER NOT NULL,
                    bookingID INTEGER NOT NULL,
                    patientName TEXT NOT NULL,
                    medicationName TEXT NOT NULL,
                    quantity TEXT NOT NULL,
                    duration TEXT NOT NULL,
                    date_signed DATE NOT NULL,
                    instructions TEXT NOT NULL
                )
            ''')
            db.commit()

        # def DeleteRow():
        #     c=db.cursor()
        #     c.execute("DELETE FROM prescriptions WHERE id =?",(2,))
        #     db.commit()
        #
        # DeleteRow()

        def get_appointment_details():
            c = db.cursor()
            c.execute("SELECT booking.*, users.id, users.fullName FROM booking INNER JOIN users ON booking.patientID = users.id "
                      "WHERE bookingID = ? AND doctorID = ?", (booking_id, user_id))
            data = c.fetchall()
            return data

        appointmentData = get_appointment_details()
        patientID = appointmentData[0][15]
        bookingID = appointmentData[0][0]
        patientName = appointmentData[0][16]
        patient_first_name = appointmentData[0][16].split()[-2:]
        patient_last_name = appointmentData[0][16].split()[0]

        def update_database():
            # Create the 'prescriptions' table if it doesn't exist
            create_prescriptions_table()

            c = db.cursor()

            c.execute('''
                INSERT INTO prescriptions (patientID, bookingID, patientName, medicationName, quantity, duration, dateSigned, instructions)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (patientID, bookingID, patientName, medicationName_value, quantity_value, duration_value, dateSigned, instruction_value))

            db.commit()

        def Update(booking_id):
            c = db.cursor()
            c.execute("UPDATE booking SET prescriptionStatus = ? WHERE bookingID = ?", (1, booking_id))
            db.commit()

        # Assuming you have the bookingID when generating the prescription
        # You can call Update function after inserting into prescriptions
        update_database()
        Update(bookingID)

        def validate_all_fields(value1, value2, value3):
            if value1 and value2 and value3:
                return False  # All fields are not empty, validation successful
            else:
                return True

        def close_error_dialog(_):
            page.dialog = error_dialog
            error_dialog.open = False
            page.update()

        error_dialog = AlertDialog(
            modal=True,
            title=Text("Alert", text_align=TextAlign.CENTER),
            content=Text("Please enter all the field before submit.", text_align=TextAlign.CENTER),
            actions=[TextButton("OK", on_click=close_error_dialog)],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_error_dialog():
            # error_dialog.content.text = message
            page.dialog = error_dialog
            error_dialog.open = True
            page.update()

        def close_alert_dialog(_):
            page.dialog = alert_dialog
            alert_dialog.open = False
            # Trigger the navigation to the homepage
            page.go(f"/login/homepage/{user_id}")

        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Alert", text_align=TextAlign.CENTER),
            content=Text("Prescription generated successfully!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("OK", on_click=close_alert_dialog)],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_alert_dialog():
            page.dialog = alert_dialog
            # Show the success dialog
            alert_dialog.open = True
            page.update()

        def update_variable(value, variable_name):
            nonlocal medicationName_value, quantity_value, duration_value, instruction_value

            if variable_name == "medication_name":
                medicationName_value = value
            elif variable_name == "quantity":
                quantity_value = value
            elif variable_name == "duration":
                duration_value = value
            elif variable_name == "instruction":
                instruction_value = value

            page.update()

        def on_generate_click():
            # Validate all fields
            if validate_all_fields(medicationName_value, quantity_value, duration_value):
                open_error_dialog()
            else:
                # Update the database with the captured values
                update_database()
                # Show the success dialog
                open_alert_dialog()

        return View(
            "/doctorGeneratePrescription/:user_id:booking_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    # alignment=MainAxisAlignment.CENTER,
                    content=Column(
                        controls=[
                            Row(alignment=MainAxisAlignment.CENTER,
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
                                                      on_click=lambda _: page.go(
                                                          f"/login/homepage/{user_id}")),
                                            Container(padding=padding.only(left=35),
                                                      content=Text("Generate Prescription",
                                                                   color="WHITE",
                                                                   text_align=TextAlign.CENTER,
                                                                   size=20,
                                                                   font_family="RobotoSlab"))]
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
                                        Row(
                                            alignment=MainAxisAlignment.START,
                                            controls=[
                                                TextField(
                                                    value=medicationName_value,
                                                    width=310,
                                                    height=35,
                                                    label_style=TextStyle(color="BLACK"),
                                                    border_color=colors.BLACK,
                                                    text_style=TextStyle(size=12, color=colors.BLACK),
                                                    on_change=lambda event: update_variable(event.control.value,
                                                                                            "medication_name")
                                                )
                                            ]
                                        ),
                                        Text(
                                            "B: Quantity / Dosage Frequency",
                                            color="#666666",
                                            size=12,
                                            weight=FontWeight.W_600
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.START,
                                            controls=[
                                                TextField(
                                                    value=quantity_value,
                                                    width=310,
                                                    height=35,
                                                    label_style=TextStyle(color="BLACK"),
                                                    border_color=colors.BLACK,
                                                    text_style=TextStyle(size=12, color=colors.BLACK),
                                                    on_change=lambda event: update_variable(event.control.value,
                                                                                            "quantity")
                                                )
                                            ]
                                        ),
                                        Text(
                                            "C: Duration of Treatment / Treatment Frequency",
                                            color="#666666",
                                            size=12,
                                            weight=FontWeight.W_600
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.START,
                                            controls=[
                                                TextField(
                                                    value=duration_value,
                                                    width=310,
                                                    height=35,
                                                    label_style=TextStyle(color="BLACK"),
                                                    border_color=colors.BLACK,
                                                    text_style=TextStyle(size=14, color=colors.BLACK),
                                                    on_change=lambda event: update_variable(event.control.value,
                                                                                            "duration"),
                                                )
                                            ]
                                        ),
                                        Text(
                                            "Date Signed",
                                            color="#666666",
                                            size=14,
                                            weight=FontWeight.BOLD
                                        ),
                                        TextField(
                                            label="Today's Date:",
                                            width=310,
                                            height=35,
                                            label_style=TextStyle(color="BLACK"),
                                            border_color=colors.BLACK,
                                            text_style=TextStyle(size=12, color=colors.BLACK,
                                                                 weight=FontWeight.W_600),
                                            value=self.selected_date.strftime('%d/%m/%Y'),
                                            read_only=True
                                            # Display selected date in the TextField
                                        ),
                                        Text(
                                            "Specific Instructions",
                                            color="#666666",
                                            size=14,
                                            weight=FontWeight.BOLD
                                        ),
                                        Row(
                                            alignment=MainAxisAlignment.START,
                                            controls=[
                                                TextField(
                                                    value=instruction_value,
                                                    multiline=True,
                                                    width=310,
                                                    label_style=TextStyle(color="BLACK"),
                                                    border_color=colors.BLACK,
                                                    text_style=TextStyle(size=12, color=colors.BLACK),
                                                    on_change=lambda event: update_variable(event.control.value,
                                                                                            "instruction")
                                                )
                                            ]
                                        ),
                                        Container(
                                            padding=padding.only(left=70),
                                            content=Column(
                                                controls=[
                                                    FilledButton(
                                                        text="Generate",
                                                        width=200,
                                                        on_click=lambda _: on_generate_click()
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ),
                alert_dialog,
                error_dialog
            ])
