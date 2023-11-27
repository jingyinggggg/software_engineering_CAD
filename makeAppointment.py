import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import calendar  # built-in python calendar library
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)

def CreateTable():
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS booking(
                 bookingID INTEGER PRIMARY KEY AUTOINCREMENT,
                 patientID INTEGER NOT NULL,
                 doctorID INTEGER NOT NULL,
                 appointmentDate TEXT NOT NULL,
                 appointmentTime TEXT NOT NULL,
                 appointmentType TEXT NOT NULL, 
                 clinicID INTEGER NOT NULL,
                 reasonVisit TEXT NOT NULL,
                 appointmentStatus TEXT,
                 bookingStatus INTEGER NOT NULL,
                 rejectReason TEXT,
                 proof TEXT,
                 proofStatus INTEGER,
                 proofRejectReason TEXT,
                 reassignDoctorID INTEGER,
                 prescriptionStatus INTEGER)""")
    db.commit()


def dropTable():
    c = db.cursor()
    c.execute("DROP table booking")


class MakeAppointmentPage:

    def __init__(self):
        self.calendar_grid = None
        self.chosen_date = None
        self.selected_time_slot = None
        self.time_slots_column = None
        self.appointment_date = None

    def generate_calendar(self, page):
        lightBlue = "#D0DCEE"
        current_date = datetime.date.today()
        current_year = current_date.year
        current_month = current_date.month
        days_in_month = calendar.monthrange(current_year, current_month)[1]

        self.calendar_grid = Column(
            wrap=True,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )

        for month in range(current_month, current_month + 1):
            month_label = Container(
                margin=margin.only(bottom=-10),
                alignment=alignment.center,
                content=Text(
                    f"{calendar.month_name[month]} {current_year}",
                    size=14,
                    weight="bold",
                    color=colors.BLACK,
                    text_align=TextAlign.CENTER
                )
            )

            month_matrix = calendar.monthcalendar(current_year, month)
            month_grid = Column(alignment=MainAxisAlignment.CENTER,
                                spacing=20)
            month_grid.controls.append(
                Row(
                    alignment=MainAxisAlignment.START,
                    controls=[month_label]
                )
            )

            weekday_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            weekday_row = Row()
            for weekday in weekday_labels:
                day_container = Container(
                    width=28,
                    height=28,
                    alignment=alignment.center,
                    content=Text(weekday, size=12, color=colors.BLACK),
                    margin=margin.only(right=10, bottom=-10)
                )
                weekday_row.controls.append(day_container)

            month_grid.controls.append(weekday_row)

            for week in month_matrix:
                week_container = Row()
                for day in week:
                    if day == 0:
                        day_container = Container(
                            width=28,
                            height=28,
                            alignment=alignment.center,
                            content=None,
                            margin=margin.only(right=10)
                        )
                    else:
                        day_container = Container(
                            width=28,
                            height=28,
                            border=None,
                            alignment=alignment.center,
                            on_click=lambda control, date=day: self.date_clicked(date),
                            content=Text(str(day), size=12, color=colors.BLACK, weight=FontWeight.W_500),
                            margin=margin.only(right=10, bottom=-10),
                        )

                    if day == current_date.day and month == current_date.month and current_year == current_date.year:
                        day_container.border_radius = 14
                        day_container.bgcolor = "#3386C5"
                        day_container.content.color = colors.WHITE

                    if day == self.chosen_date:
                        day_container.border_radius = 14
                        day_container.bgcolor = colors.WHITE
                        day_container.content.color = "#3386C5"

                    if day < current_date.day:
                        if day_container.content:
                            # day_container.bgcolor = colors.GREY_800
                            day_container.content.color = "#818589"
                            day_container.disabled = True

                    week_container.controls.append(day_container)

                month_grid.controls.append(week_container)

            self.calendar_grid.controls.append(month_grid)

        return Container(
            width=350,
            bgcolor=lightBlue,
            padding=padding.only(left=10, right=10, top=20, bottom=20),
            content=Container(
                width=330,
                alignment=alignment.center,
                margin=margin.only(left=10, right=10),
                content=self.calendar_grid  # Use self.calendar_grid here
            )
        )

    def date_clicked(self, date):
        if date:
            # Reset the previously chosen date
            if self.chosen_date:
                self.reset_date_color(self.chosen_date)

            self.chosen_date = date
            print(f"Chosen Date: {self.chosen_date}")

            # Update the color for the newly chosen date
            for month_grid in self.calendar_grid.controls:
                for week_container in month_grid.controls[1:]:
                    for day_container in week_container.controls:
                        if day_container.content and day_container.content.value == str(date):
                            day_container.border_radius = 14
                            day_container.bgcolor = colors.WHITE
                            day_container.content.color = "#3386C5"
                            day_container.update()

    def reset_date_color(self, date):
        # Reset the properties for a specific date
        for month_grid in self.calendar_grid.controls:
            for week_container in month_grid.controls[1:]:
                for day_container in week_container.controls:
                    if day_container.content and day_container.content.value == str(date):
                        day_container.border_radius = None  # Reset the border_radius
                        day_container.bgcolor = None  # Reset the background color
                        day_container.content.color = colors.BLACK  # Reset the text color
                        day_container.update()

    def generate_time_slots(self, working_time):
        start_time, end_time = working_time.split(" - ")
        start_time = datetime.datetime.strptime(start_time, "%I:%M %p")
        end_time = datetime.datetime.strptime(end_time, "%I:%M %p")

        time_slots = []

        while start_time < end_time:
            end_of_slot = start_time + datetime.timedelta(hours=1.5)
            start_time_str = start_time.strftime("%I:%M %p")
            end_of_slot_str = end_of_slot.strftime("%I:%M %p")

            # Check if the current time slot is the selected time slot
            is_selected = start_time_str == self.selected_time_slot

            # Define the button's bgcolor based on selection
            bgcolor = colors.WHITE if is_selected else "#3386C5"
            text_color = "#3386C5" if is_selected else colors.WHITE

            def on_time_slot_click(control, time=start_time_str):
                self.time_slot_clicked(control, time, is_selected)

            time_slot_button = Container(
                margin=margin.only(left=10, bottom=5),
                content=TextButton(
                    content=Text(start_time_str, size=14, color=text_color, font_family="RobotoSlab"),
                    width=95,
                    height=45,
                    style=ButtonStyle(bgcolor={"": bgcolor}, shape={"": RoundedRectangleBorder(radius=7)},
                                      side={"": BorderSide(1, "#3386C5")}, ),
                    on_click=on_time_slot_click,
                )
            )

            time_slots.append(time_slot_button)

            start_time = end_of_slot

        rows = [time_slots[i:i + 3] for i in range(0, len(time_slots), 3)]

        self.time_slots_column = Column(
            controls=[Row(controls=row, spacing=10) for row in rows]
        )

        return self.time_slots_column

    def time_slot_clicked(self, button, time, is_selected):
        # Reset the previously selected time slot
        if self.selected_time_slot:
            self.reset_time_slot_color(self.selected_time_slot)

        # Set the new selected time slot
        self.selected_time_slot = time
        print(self.selected_time_slot)

        for row in self.time_slots_column.controls:
            for i, button in enumerate(row.controls):
                # Get the stored text for the button
                button_text = button.content.content.value
                if button_text == time:
                    # Create a new button with the original style and the same text
                    new_button = Container(
                        margin=margin.only(left=10, bottom=5),
                        content=TextButton(
                            content=Text(button_text, size=14, color="#3386C5", font_family="RobotoSlab"),
                            width=95,
                            height=45,
                            style=ButtonStyle(bgcolor={"": colors.WHITE}, shape={"": RoundedRectangleBorder(radius=7)},
                                              side={"": BorderSide(1, "#3386C5")}, ),
                            on_click=lambda control, time_slot=button_text: self.time_slot_clicked(control, time_slot,
                                                                                                   True)
                        )
                    )

                    # Replace the old button with the new one in the time_slots_column controls
                    row.controls[i] = new_button

        # Update your layout to reflect the changes
        self.time_slots_column.update()

        if self.chosen_date:
            current_date = datetime.date.today()
            current_month = current_date.month
            current_year = current_date.year  # Get the current year
            month_name = calendar.month_name[current_month]
            self.appointment_date = f"{self.chosen_date} {month_name} {current_year}"

    def reset_time_slot_color(self, time):
        for row in self.time_slots_column.controls:
            for i, button in enumerate(row.controls):
                # Get the stored text for the button
                button_text = button.content.content.value
                if button_text == time:
                    # Create a new button with the original style and the same text
                    new_button = Container(
                        margin=margin.only(left=10, bottom=5),
                        content=TextButton(
                            content=Text(button_text, size=14, color=colors.WHITE, font_family="RobotoSlab"),
                            width=95,
                            height=45,
                            style=ButtonStyle(bgcolor={"": "#3386C5"}, shape={"": RoundedRectangleBorder(radius=7)}),
                            on_click=lambda control, time_slot=button_text: self.time_slot_clicked(control, time_slot,
                                                                                                   False)
                        )
                    )

                    # Replace the old button with the new one in the time_slots_column controls
                    row.controls[i] = new_button

        # Update your layout to reflect the changes
        self.time_slots_column.update()

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        doctor_id = int(params.doctor_id)
        previous_page_route = params.previous_page

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

        def get_doctor_working_time():
            c = db.cursor()
            c.execute("SELECT workingTime, clinicID from doctors WHERE id = ?", (doctor_id,))
            record = c.fetchall()

            workingTime = record[0][0]
            clinic_id = record[0][1]
            return workingTime, clinic_id

        workingTime, clinic_id = get_doctor_working_time()
        time_slot_button = self.generate_time_slots(workingTime)

        appointment_type = TextField(
            dense=True,
            label="Appointment Type",
            border_color=blue,
            height=45,
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab"
                                 ),
            value="Offline Appointment (Visit doctor at clinic)",
            read_only=True
        )

        current_date = datetime.date.today()

        reason_visit = TextField(
            label="Reason Visit",
            label_style=TextStyle(font_family="RobotoSlab",
                                  size=12,
                                  color=colors.GREY_800),
            # height=50,
            border_color=blue,
            text_style=TextStyle(size=12,
                                 color=colors.BLACK,
                                 font_family="RobotoSlab"
                                 ),
            hint_text="Please enter the reason of visit",
            hint_style=TextStyle(size=12, color=colors.GREY_500, italic=True),
            dense=True,
            multiline=True,
            min_lines=1,
            max_lines=3
        )

        # current_year = current_date.year
        # current_month = current_date.month
        #
        # month_name = calendar.month_name[current_month]

        alert_dialog = AlertDialog(
            modal=False,
            title=Text("Success", text_align=TextAlign.CENTER),
            content=Text(
                f"You have submitted your request to visit this doctor."
                f"\nPlease wait for the admin to review your request."
                f"\nYou can check your request status in booking page ",
                text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: navigate_homepage())],
            actions_alignment=MainAxisAlignment.CENTER,
            open=True
        )

        error_dialog = AlertDialog(
            modal=False,
            title=Text("Failes", text_align=TextAlign.CENTER),
            content=Text(
                f"Something went wrong! Please try again...",
                text_align=TextAlign.CENTER),
            actions=[TextButton("Done", on_click=lambda _: close_dlg())],
            actions_alignment=MainAxisAlignment.CENTER,
            open=True
        )

        def navigate_homepage():
            try:
                page.go(f"/homepage/{user_id}")
                self.chosen_date = None
                self.selected_time_slot = None
                page.update()
            except Exception as e:
                print(f"Error navigating to homepage: {e}")

        def open_dlg():
            page.dialog = alert_dialog
            alert_dialog.open = True
            page.update()

        def open_dlg1():
            page.dialog = error_dialog
            error_dialog.open = True
            page.update()

        def close_dlg():
            page.dialog = error_dialog
            error_dialog.open = False
            page.update()

        def addToDatabase(e):
            CreateTable()
            c = db.cursor()
            if (self.chosen_date != "" and self.selected_time_slot != "" and appointment_type.value != ""
                    and reason_visit.value != ""):
                c.execute(f"INSERT INTO booking (patientID, doctorID, appointmentDate, appointmentTime, "
                          f"appointmentType, clinicID, reasonVisit, appointmentStatus, bookingStatus)"
                          f"VALUES (?,?,?,?,?,?,?,?,?)",
                          (user_id, doctor_id, self.appointment_date, self.selected_time_slot, appointment_type.value,
                           clinic_id, reason_visit.value, "Requested",0))
                db.commit()
                open_dlg()
            else:
                open_dlg1()

        def back_previous_page():
            self.chosen_date = None
            self.selected_time_slot = None
            return page.go(f"/viewDoctor/{user_id}{doctor_id}{previous_page_route}")

        return View(
            "/makeAppointment/:user_id:doctor_id:previous_page",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              scroll=True,
                              # horizontal_alignment="center",
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
                                                              on_click=lambda _: back_previous_page()
                                                              ),

                                                    Container(padding=padding.only(left=75, top=25),
                                                              content=Text(
                                                                  value="Appointment",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),
                                                ]
                                            )
                                            ),

                                  Container(
                                      margin=margin.only(top=10, left=10),
                                      content=Text(
                                          value="Please select a date:",
                                          size=14,
                                          font_family="RobotoSlab",
                                          color=colors.BLACK,
                                          weight=FontWeight.W_500,
                                          # italic=True
                                      )
                                  ),

                                  self.generate_calendar(page),

                                  Container(
                                      margin=margin.only(top=10, left=10),
                                      content=Text(
                                          value="Please select a time slot:",
                                          size=14,
                                          font_family="RobotoSlab",
                                          color=colors.BLACK,
                                          weight=FontWeight.W_500,
                                          # italic=True
                                      )
                                  ),

                                  time_slot_button,

                                  Container(
                                      margin=margin.only(left=10, top=10, right=10),
                                      alignment=alignment.center,
                                      content=appointment_type
                                  ),

                                  Container(
                                      margin=margin.only(left=10, top=10, right=10),
                                      alignment=alignment.center,
                                      content=reason_visit
                                  ),

                                  Container(padding=padding.only(top=10, bottom=30),
                                            alignment=alignment.center,
                                            content=IconButton(content=Text("Request",
                                                                            size=16,
                                                                            font_family="RobotoSlab",
                                                                            color="WHITE",
                                                                            text_align=TextAlign.CENTER),
                                                               width=330,
                                                               height=45,
                                                               style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                                                 shape={"": RoundedRectangleBorder(
                                                                                     radius=7)}
                                                                                 ),
                                                               on_click=addToDatabase
                                                               )
                                            )

                              ]
                          )
                          )
            ]
        )
