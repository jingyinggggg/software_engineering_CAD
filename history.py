import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class HistoryPage:
    def __init__(self):
        self.selected_filter = "All"

    def get_appointment_detail(self, user_id):
        c = db.cursor()
        sql = '''
        SELECT patientID, appointmentDate, appointmentTime, users.fullName, bookingID
        FROM booking
        INNER JOIN users
        ON booking.patientID = users.id
        WHERE users.id = ? AND booking.bookingStatus = 2;
        '''
        c.execute(sql, (user_id,))
        result = c.fetchall()

        return result

        # if result:
        #     appointmentDate, appointmentTime, fullName = result[0]
        #     return appointmentDate, appointmentTime, fullName
        # else:
        #     return None

    def get_current_date_appointments(self, user_id):
        if self.selected_filter == "All":
            # Get the current date
            current_date = datetime.date.today()
            c = db.cursor()
            # Query the database to fetch appointments for the current date
            c.execute(
                "SELECT appointmentDate, appointmentTime FROM booking "
                "WHERE appointmentDate = ? AND patientID = ?",
                (current_date, user_id))
            appointments = c.fetchall()
            return appointments
        else:
            return []  # Return an empty list for other filter options

    def on_filter_change(self, new_value):
        # Update the selected_filter when the dropdown value changes
        if new_value is None:
            self.selected_filter = "All"
        else:
            self.selected_filter = new_value

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
        user_id = int(params.user_id)

        # patient_data = self.get_patient_name(user_id)
        appointment_data = self.get_appointment_detail(user_id)
        # filter_data = self.get_current_date_appointments(user_id)

        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        lightBlue = "#D0DCEE"
        blue = "#3386C5"
        grey = "#71839B"

        def display_patient_details(patient_details):
            # fullName = patient_details
            if patient_details:

                record_containers = []
                for patient in patient_details:
                    print(patient)

                    def on_more_button_click(record_id=patient[4]):
                        return lambda _: page.go(f"/appointmentDetail/{user_id}{record_id}")

                    record_container = Container(
                        alignment=alignment.center,
                        border_radius=8,
                        padding=padding.only(left=10),
                        margin=margin.only(left=10),
                        border=border.all(color=blue),
                        width=320,
                        height=160,
                        content=Column(controls=[
                            Row(alignment=MainAxisAlignment.START,
                                controls=[Container(
                                    alignment=alignment.top_left,
                                    margin=margin.only(top=10),
                                    content=Text("Appointment Date & Time",
                                                 font_family="RobotoSlab",
                                                 size=14,
                                                 color="#979797"))]),
                            Container(content=Row(alignment=alignment.center,
                                                  controls=[Container(
                                                      Icon(icons.WATCH_LATER_OUTLINED,
                                                           color="BLACK"), ),
                                                      Text(
                                                          # display_appointment_details(f""appointment_data),
                                                          f"{patient[1]} | {patient[2]}",
                                                          weight=FontWeight.W_500,
                                                          size=12,
                                                          color="BLACK")])),

                            Container(
                                content=Row(alignment=alignment.center,
                                            controls=[Container(
                                                Image(
                                                    src="pic/medicalRecord.png",
                                                    border_radius=20,
                                                    width=65,
                                                    height=65), ),
                                                Text(f"{patient[3]}",
                                                     weight=FontWeight.W_700,
                                                     font_family="RobotoSlab",
                                                     size=14,
                                                     color="BLACK"),
                                            ])),

                            # Container(margin=margin.only(left=200, top=-25),
                            #           content=Column(
                            #               alignment=alignment.center,
                            #               controls=[Container(
                            #                   TextButton("more >>",
                            #                              on_click=on_more_button_click())
                            #               )])
                            #           )
                        ]), on_click=on_more_button_click()
                    )
                    record_containers.append(record_container)

                return Column(controls=record_containers)

        # patient_details_control = display_patient_details(patient_data)

        return View(
            "/history/:user_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    # alignment=alignment.center,
                    content=Column(
                        scroll=True,
                        controls=[
                            Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    # top bar container
                                    Container(
                                        padding=padding.only(right=10),
                                        width=350,
                                        height=80,
                                        alignment=alignment.center,
                                        bgcolor="#3386C5",
                                        content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        Container(padding=padding.only(top=5, left=10),
                                                                  content=Image(
                                                                      src="pic/back.png",
                                                                      color=colors.WHITE,
                                                                      width=20,
                                                                      height=20
                                                                  ), on_click=lambda _: page.go(
                                                                f"/login/homepage/{user_id}")),
                                                        Container(
                                                            content=Text("History",
                                                                         color="WHITE",
                                                                         text_align=TextAlign.CENTER,
                                                                         size=20,
                                                                         font_family="RobotoSlab")),
                                                        IconButton(icons.SEARCH_OUTLINED,
                                                                   icon_color="WHITE")]
                                                    )
                                    )]),

                            Container(
                                margin=margin.only(bottom=10),
                                padding=padding.only(left=10),
                                content=Column(
                                    controls=[
                                        Dropdown(
                                            dense=True,
                                            label_style=TextStyle(size=14, weight=FontWeight.W_500, color="#3386C5"),
                                            label="Filter by category",
                                            hint_text="Select a category",
                                            hint_style=TextStyle(color="#71839B", size=14, italic=True),
                                            text_style=TextStyle(size=14, weight=FontWeight.W_500),
                                            options=[
                                                dropdown.Option("All"),
                                                dropdown.Option("1 week ago"),
                                                dropdown.Option("more than 1 weeks")
                                            ],
                                            border_radius=10,
                                            border_color="#3386C5",
                                            color='BLACK',
                                            autofocus=True,
                                            width=320,
                                            # height=80,
                                            focused_color="#71839B",
                                            text_size=12,
                                            content_padding=10,
                                            # on_change=lambda new_value: self.on_filter_change(new_value)
                                        )
                                    ]
                                )
                            ),

                            # patient_details_control,
                            display_patient_details(appointment_data)
                        ]))])
