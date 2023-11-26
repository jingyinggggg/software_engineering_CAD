import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class DoctorNotification:
    def __init__(self):
        pass

    def get_patient_name(self, patient_id):
        c = self.db.cursor()
        c.execute("SELECT fullName FROM users WHERE id = ?", (patient_id,))
        patient_record = c.fetchone()
        if patient_record:
            return patient_record[0]
        else:
            return "Unknown"  # Default if patient information is not available

    def get_appointment_notification_message(self, fullName, appointment_type, patient_name, appointment_date,
                                             appointment_time, appointment_status):
        # if appointment_status == "Requested":
        #     return f"Hi, Dr. {fullName}! You have a new appointment request from patient ({patient_name}) on {appointment_date} at {appointment_time}. Please review and take action."
        appointment_date = datetime.datetime.strptime(appointment_date, "%d %B %Y").date()

        # Calculate the date one day before the appointment
        reminder_date = appointment_date - datetime.timedelta(days=1)
        current_date = datetime.date.today()

        if current_date == reminder_date:
            return f"Hi, Dr. {fullName}! You have an appointment with patient ({patient_name}) tomorrow on {appointment_date} at {appointment_time}."

        if appointment_status == "Confirmed":
            return f"Hi, Dr. {fullName}! Your appointment with patient ({patient_name}) on {appointment_date} at {appointment_time} has been confirmed. See you then."

        if appointment_status == "Rejected":
            return f"Hi, Dr. {fullName}! Your appointment request from patient ({patient_name}) on {appointment_date} at {appointment_time} has been rejected."

        # Default message for other statuses
        return f"Hi, Dr. {fullName}! Don't forget your {appointment_type} with patient ({patient_name}) on {appointment_date} at {appointment_time}."

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        self.db = sqlite3.connect("cad.db", check_same_thread=False)

        def get_doctor_details():
            c = self.db.cursor()
            c.execute("SELECT * FROM doctors WHERE id = ?", (user_id,))
            record = c.fetchall()
            fullName = record[0][1]
            return fullName

        def get_booking_data(status_list):
            c = self.db.cursor()
            query = "SELECT * FROM booking WHERE doctorID = ? AND appointmentStatus IN ({})".format(
                ",".join(["?"] * len(status_list)))
            bindings = [user_id] + status_list
            c.execute(query, bindings)
            records = c.fetchall()
            return records

        fullName = get_doctor_details()
        status_list = ["Scheduled", "Confirmed", "Requested", "Rejected"]  # Customize status list as needed
        booking_data = get_booking_data(status_list)

        current_date = datetime.date.today()  # Get the current date
        notification_controls = []

        for record in booking_data:
            appointment_date = datetime.datetime.strptime(record[3], "%d %B %Y").date()

            # Check if the appointment date is in the future
            if appointment_date >= current_date:
                patient_name = self.get_patient_name(record[1])
                appointment_message = self.get_appointment_notification_message(fullName, record[5], patient_name,
                                                                                record[3], record[4], record[8])

                notification_controls.append(
                    Container(
                        padding=padding.only(left=10, right=10, top=10),
                        alignment=alignment.center,
                        margin=margin.only(left=10, top=5, right=10),
                        width=320,
                        height=95,
                        border_radius=8,
                        border=border.all(width=1, color="BLACK"),
                        content=Row(
                            controls=[
                                Icon(icons.TIPS_AND_UPDATES_OUTLINED, size=40, color="#3D3F99"),
                                Container(
                                    padding=padding.only(left=10),
                                    content=Column(
                                        controls=[
                                            Text(appointment_message, color="BLACK", size=12,
                                                 overflow=TextOverflow.VISIBLE,
                                                 width=230, font_family="RobotoSlab", text_align=TextAlign.JUSTIFY),
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                )

        # Check if there are no notifications
        if not notification_controls:
            # If there are no notifications, display a default message
            default_message = "No notifications at the moment."

            return View(
                "/doctorNotification/:user_id",
                controls=[
                    Container(
                        width=350,
                        height=700,
                        bgcolor="#FFFFFF",
                        border_radius=30,
                        alignment=alignment.center,
                        content=Column(
                            controls=[
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Container(
                                            padding=padding.only(right=120),
                                            width=350,
                                            height=80,
                                            alignment=alignment.center,
                                            bgcolor="#3386C5",
                                            content=Row(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    Container(padding=padding.only(left=10),
                                                        content=Image(
                                                            src="pic/back.png",
                                                            color=colors.WHITE,
                                                            width=20,
                                                            height=20
                                                        ),on_click=lambda _: page.go(
                                                                   f"/login/homepage/{user_id}")),
                                                    Text("Notification",
                                                         color="WHITE",
                                                         text_align=TextAlign.CENTER,
                                                         size=20,
                                                         font_family="RobotoSlab")
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                Container(alignment=alignment.center,
                                          margin=margin.only(top=230),
                                          content=Image(src="pic/icons8-no-notification-64.png"),
                                          ),
                                Container(alignment=alignment.center,
                                          content=Text(default_message, color="BLACK", size=16,
                                                       font_family="RobotoSlab",
                                                       text_align=TextAlign.CENTER))

                            ]
                        )
                    )
                ]
            )

        # If there are notifications, display the list of notification_controls
        return View(
            "/doctorNotification/:user_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        padding=padding.only(right=120),
                                        width=350,
                                        height=80,
                                        alignment=alignment.center,
                                        bgcolor="#3386C5",
                                        content=Row(
                                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                IconButton(icons.ARROW_BACK_ROUNDED,
                                                           icon_size=30,
                                                           icon_color="WHITE",
                                                           on_click=lambda _: page.go(f"/login/homepage/{user_id}")),
                                                Text("Notification",
                                                     color="WHITE",
                                                     text_align=TextAlign.CENTER,
                                                     size=20,
                                                     font_family="RobotoSlab",
                                                     weight=FontWeight.BOLD)
                                            ]
                                        )
                                    )
                                ]
                            ),
                            # Include the list of notification_controls
                            *notification_controls
                        ]
                    )
                )
            ]
        )