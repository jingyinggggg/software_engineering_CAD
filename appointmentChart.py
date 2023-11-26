import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
from datetime import datetime, timedelta
import plotly.graph_objects as go
from flet.plotly_chart import PlotlyChart

db = sqlite3.connect("cad.db", check_same_thread=False)
cursor = db.cursor()


class ClinicViewAppointmentChart:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
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

        # Get today date
        today = datetime.today()

        # Get the start date of current week
        start_of_week = today - timedelta(days=today.weekday())

        # Get the end date of current week
        end_of_week = start_of_week + timedelta(days=6)

        # Format the date
        formatted_start_date = start_of_week.strftime("%d %B %Y")
        formatted_end_date = end_of_week.strftime("%d %B %Y")

        def get_requested_appointment(start_date, end_date):
            c = db.cursor()
            c.execute(
                f"SELECT COUNT(*) FROM booking WHERE (appointmentDate BETWEEN ? AND ?) AND bookingStatus = ? AND clinicID = ?",
                (start_date, end_date, 0, clinic_id))
            record = c.fetchone()

            if record:
                requested_count = record[0]

            return requested_count

        requested_count = get_requested_appointment(formatted_start_date, formatted_end_date)

        def get_scheduled_appointment(start_date, end_date):
            c = db.cursor()
            c.execute(
                f"SELECT COUNT(*) FROM booking WHERE (appointmentDate BETWEEN ? AND ?) AND bookingStatus = ? AND clinicID = ?",
                (start_date, end_date, 1, clinic_id))
            record = c.fetchone()

            if record:
                scheduled_count = record[0]

            return scheduled_count

        scheduled_count = get_scheduled_appointment(formatted_start_date, formatted_end_date)

        def get_completed_appointment(start_date, end_date):
            c = db.cursor()
            c.execute(
                f"SELECT COUNT(*) FROM booking WHERE (appointmentDate BETWEEN ? AND ?) AND bookingStatus = ? AND clinicID = ?",
                (start_date, end_date, 2, clinic_id))
            record = c.fetchone()

            if record:
                completed_count = record[0]

            return completed_count

        completed_count = get_completed_appointment(formatted_start_date, formatted_end_date)

        def get_rejected_appointment(start_date, end_date):
            c = db.cursor()
            c.execute(
                f"SELECT COUNT(*) FROM booking WHERE (appointmentDate BETWEEN ? AND ?) AND bookingStatus = ? AND clinicID = ?",
                (start_date, end_date, -1, clinic_id))
            record = c.fetchone()

            if record:
                rejected_count = record[0]

            return rejected_count

        rejected_count = get_rejected_appointment(formatted_start_date, formatted_end_date)

        def generateChart(request, schedule, complete, reject):
            labels = ["Requested", "Scheduled", "Completed", "Rejected"]
            values = [request, schedule, complete, reject]

            # Define custom colors for the pie chart
            custom_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

            fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent',
                                         marker=dict(colors=custom_colors))])
            fig.update_layout(
                # title="Chart of clinic's appointment for current week",  # Set the title of the chart
                # title_font=dict(size=13),  # Adjust the title font size
                margin=dict(l=0, r=0, t=10, b=20),  # Adjust margins for the chart
                height=220,  # Set the height of the chart
                width=350,  # Set the width of the chart
            )

            fig.update_traces(
                textfont=dict(size=13,
                              # family="RobotoSlab",
                              color=colors.BLACK),  # Set text font size for hover labels
            )

            return PlotlyChart(figure=fig, expand=True)

        return View(
            "/clinicViewAppointmentChart/:clinic_id",
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
                                                              on_click=lambda _: page.go(
                                                                  f"/clinicViewAppointment/{clinic_id}")
                                                              ),

                                                    Container(padding=padding.only(left=80, top=25),
                                                              content=Text(
                                                                  value="Clinic Chart",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),
                                                ]
                                            )
                                            ),

                                  Container(
                                      width=330,
                                      height=350,
                                      content=Column(
                                          controls=[
                                              Container(
                                                  margin=margin.only(top=10, left=10),
                                                  content=Text(
                                                      value="Below is the chart of clinic's appointment for current week:",
                                                      size=13,
                                                      font_family="RobotoSlab",
                                                      weight=FontWeight.BOLD,
                                                      color=colors.BLACK,
                                                      text_align=TextAlign.JUSTIFY
                                                  )
                                              ),
                                              # generateChart(5, 3, 2, 7)
                                              generateChart(requested_count, scheduled_count, completed_count,
                                                            rejected_count),

                                          ]
                                      )
                                      # content=generateChart(requested_count,scheduled_count,completed_count,rejected_count)
                                  ),

                                  Container(
                                      margin=margin.only(left=10, right=10),
                                      content=Column(
                                          controls=[
                                              Text("Chart Summary :",
                                                   size=13,
                                                   color=colors.BLACK,
                                                   font_family="RobotoSlab",
                                                   weight=FontWeight.BOLD),

                                              Row(
                                                  controls=[
                                                      Text("-", size=12, color=colors.BLACK, font_family="RobotoSlab",
                                                           weight=FontWeight.W_500),
                                                      Text(
                                                          f"There are {requested_count} requested appointment awaiting for clinic admin to review.",
                                                          size=12,
                                                          color=colors.BLACK,
                                                          font_family="RobotoSlab",
                                                          weight=FontWeight.W_500,
                                                          width=310,
                                                          text_align=TextAlign.JUSTIFY)
                                                  ]
                                              ),

                                              Row(
                                                  controls=[
                                                      Text("-", size=12, color=colors.BLACK, font_family="RobotoSlab",
                                                           weight=FontWeight.W_500),
                                                      Text(f"There are {scheduled_count} scheduled appointment.",
                                                           size=12,
                                                           color=colors.BLACK,
                                                           font_family="RobotoSlab",
                                                           weight=FontWeight.W_500,
                                                           width=310,
                                                           text_align=TextAlign.JUSTIFY
                                                           )
                                                  ]
                                              ),

                                              Row(
                                                  controls=[
                                                      Text("-", size=12, color=colors.BLACK, font_family="RobotoSlab",
                                                           weight=FontWeight.W_500),
                                                      Text(f"There are {completed_count} completed appointment.",
                                                           size=12,
                                                           color=colors.BLACK,
                                                           font_family="RobotoSlab",
                                                           weight=FontWeight.W_500,
                                                           width=310,
                                                           text_align=TextAlign.JUSTIFY)
                                                  ]
                                              ),

                                              Row(
                                                  controls=[
                                                      Text("-", size=12, color=colors.BLACK, font_family="RobotoSlab",
                                                           weight=FontWeight.W_500),
                                                      Text(f"There are {rejected_count} rejected appointment.",
                                                           size=12,
                                                           color=colors.BLACK,
                                                           font_family="RobotoSlab",
                                                           weight=FontWeight.W_500,
                                                           width=310,
                                                           text_align=TextAlign.JUSTIFY
                                                           )
                                                  ]
                                              )
                                          ]
                                      )
                                      # Text(
                                      #     value=f"Based on the current appointment in the system:\n"
                                      #           f"- There are {requested_count} requested appointment awaiting for clinic admin to review.\n"
                                      #           f"- There are {scheduled_count} scheduled appointment.\n"
                                      #           f"- There are {completed_count} completed appointment.\n"
                                      #           f"- There are {rejected_count} rejected appointment.",
                                      #     size=12,
                                      #     font_family="RobotoSlab",
                                      #     color=colors.BLACK
                                      # )
                                  )

                              ]
                          )
                          )
            ]
        )
