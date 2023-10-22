from flet import *
from flet_route import Params, Basket
import sqlite3
from datetime import date
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class Schedule:
    def __init__(self):
        self.show_schedule = False
        self.selected_date = datetime.date.today()
        self.schedule_data = []

    def toggle_schedule(self):
        self.show_schedule = not self.show_schedule

    def showSchedule(self):
        self.toggle_schedule()

    def display_weekly_calendar(self, year, month, day):
        start_of_week = datetime.date(year, month, day) - datetime.timedelta(
            days=datetime.date(year, month, day).weekday())
        end_of_week = start_of_week + datetime.timedelta(days=7)

        week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(6)]

        return week_dates

    def view(self, page: Page, params: Params, basket: Basket, year=None, day=None):
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

        current_date = datetime.date.today()
        week_dates = self.display_weekly_calendar(current_date.year, current_date.month, current_date.day)

        # Define the days of the week (Monday to Sunday)
        days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

        def get_doctor_details():
            c = db.cursor()
            c.execute("SELECT * FROM doctors WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]

            return fullName

        fullName = get_doctor_details()

        # Sample schedule data
        self.schedule_data = [
            {"date": "2023-10-16", "time": "09:00 AM", "event": "Consultation"},
            {"date": "2023-10-17", "time": "10:30 AM", "event": "Follow Up"},
            {"date": "2023-10-18", "time": "14:00 PM", "event": "Conference Call"},
        ]

        return View(
            "/schedule/:user_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Container(
                                        padding=padding.only(right=10),
                                        width=350,
                                        height=80,
                                        alignment=alignment.center,
                                        bgcolor="#3386C5",
                                        content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        IconButton(icons.ARROW_BACK_ROUNDED,
                                                                   icon_size=30,
                                                                   icon_color="WHITE",
                                                                   on_click=lambda _: page.go(
                                                                       f"/login/homepage/{user_id}")),
                                                        Text("Schedule",
                                                             color="WHITE",
                                                             text_align=TextAlign.CENTER,
                                                             size=20,
                                                             font_family="RobotoSlab",
                                                             weight=FontWeight.BOLD),
                                                        IconButton(icons.SEARCH_OUTLINED,
                                                                   icon_color="WHITE")]
                                                    )
                                    )
                                ]),

                            Container(
                                margin=margin.only(left=10),
                                content=Column(
                                    alignment=alignment.center_left,
                                    controls=[Container(
                                        Text(current_date.strftime('%d %B %Y'),
                                             color="#0E446C",
                                             size=14,
                                             weight=FontWeight.BOLD)),
                                        Text("Schedule",
                                             color="#979797",
                                             size=18,
                                             weight=FontWeight.BOLD)])),

                            # Container(padding=padding.only(top=5, left=5),
                            #           margin=margin.only(left=5, top=5),
                            #           content=Row(
                            #               alignment=MainAxisAlignment.SPACE_AROUND,
                            #               controls=[TextButton(date.strftime('%d'),
                            #                                    style=ButtonStyle(shape=CircleBorder(),
                            #                                                      color={
                            #                                                          MaterialState.HOVERED: colors.WHITE},
                            #                                                      overlay_color=colors.INDIGO_400
                            #                                                      ),
                            #                                    on_click=lambda event: self.showSchedule(),
                            #                                    )for date in zip(week_dates)])),
                            #
                            # Container(padding=padding.only(top=5, left=5),
                            #           margin=margin.only(left=5, top=5),
                            #           content=Row(
                            #               alignment=MainAxisAlignment.SPACE_AROUND,
                            #               controls=[Text(day,
                            #                              color="#979797",
                            #                              text_align=TextAlign.CENTER,
                            #                              size=12)for day in zip(days_of_week)])),


                            # Display the week's dates with days of the week
                            Container(padding=padding.only(top=5, left=5),
                                      margin=margin.only(left=5, top=5),
                                      content=Row(
                                          alignment=MainAxisAlignment.SPACE_AROUND,
                                          controls=[
                                              Row(
                                                  alignment=MainAxisAlignment.CENTER,
                                                  controls=[
                                                      Column(
                                                          alignment=MainAxisAlignment.CENTER,
                                                          controls=[
                                                              TextButton(date.strftime('%d'),
                                                                         style=ButtonStyle(shape=CircleBorder(),
                                                                                           color={
                                                                                               MaterialState.HOVERED: colors.WHITE},
                                                                                           overlay_color=colors.INDIGO_400
                                                                                           ),
                                                                         on_click=lambda event: self.showSchedule(),
                                                                         ),
                                                              Text(day,
                                                                   color="#979797",
                                                                   text_align=TextAlign.CENTER,
                                                                   size=12)
                                                          ]
                                                      )
                                                  ]

                                              )
                                              for date, day in zip(week_dates, days_of_week)
                                          ]
                                      )
                                      ),

                            Container(alignment=alignment.center,
                                      border_radius=8,
                                      margin=margin.only(left=10, top=20),
                                      padding=padding.only(left=10, top=10),
                                      border=border.all(color="BLACK"),
                                      width=320,
                                      height=380,
                                      content=Column(controls=
                                                     [Row(alignment=MainAxisAlignment.CENTER,
                                                          controls=[Container(
                                                              alignment=alignment.center,
                                                              content=Text("List of schedule", color="BLACK",
                                                                           weight=FontWeight.BOLD))

                                                          ])
                                                      ] + [Container(
                                                         margin=margin.only(top=5),
                                                         padding=padding.only(left=10, right=10, top=5, bottom=5),
                                                         content=Row(
                                                             alignment=MainAxisAlignment.START,
                                                             controls=[
                                                                 Container(width=120,
                                                                           content=Text("Time", color="BLACK",
                                                                                        weight=FontWeight.BOLD)),
                                                                 Container(width=120,
                                                                           content=Text("Event", color="BLACK",
                                                                                        weight=FontWeight.BOLD)),
                                                             ],
                                                         ))
                                                     ] +
                                                     [
                                                         Container(
                                                             margin=margin.only(top=5),
                                                             padding=padding.only(left=10, right=10, top=5, bottom=5),
                                                             content=Row(
                                                                 alignment=MainAxisAlignment.START,
                                                                 controls=[
                                                                     Container(width=120, content=Text(item["time"],
                                                                                                       color="BLACK")),
                                                                     Container(width=200, content=Text(item["event"],
                                                                                                       color="BLACK")),
                                                                 ],
                                                             ),
                                                         )
                                                         for item in self.schedule_data
                                                     ]
                                                     )
                                      )]))])
