from flet import *
from flet_route import Params, Basket, params, basket
import sqlite3
from datetime import date
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


def showSchedule():
    Container(alignment=alignment.center,
              border_radius=8,
              padding=padding.only(left=10),
              border=border.all(color="BLACK"),
              width=320,
              height=180,
              content=Column(controls=
                             [Row(alignment=MainAxisAlignment.START,
                                  controls=[Container(
                                      alignment=alignment.top_left,
                                      margin=margin.only(top=10),
                                      content=
                                      Text("Appointment Date & Time",
                                           font_family="RobotoSlab",
                                           size=14,
                                           color="#979797"))]
                                  ),
                              Container(content=Row(alignment=alignment.center,
                                                    controls=[Container(
                                                        Icon(icons.WATCH_LATER_OUTLINED,
                                                             color="BLACK"), ),
                                                        Text("Tue Oct 02 | 09:00AM - 10.00 AM",
                                                             weight=FontWeight.W_500,
                                                             size=12,
                                                             color="BLACK")])),
                              ])),
    pass


class Schedule:
    def __init__(self):
        self.selected_date = datetime.date.today()

    def display_weekly_calendar(self, year, month, day):
        start_of_week = datetime.date(year, month, day) - datetime.timedelta(
            days=datetime.date(year, month, day).weekday())
        end_of_week = start_of_week + datetime.timedelta(days=6)

        week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(7)]

        return week_dates

    def view(self, page: Page, params: Params, basket: Basket, year=None, day=None):
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
        days_of_week = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]

        return View(
            "/schedule",
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
                                                                   on_click=lambda _: page.go(f"/login/homepage")),
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

                            # Display the week's dates with days of the week
                            Container(
                                padding=padding.only(left=10, right=10),
                                # margin=margin.only(left=10, right=10, bottom=10, top=10),
                                content=Row(
                                    alignment=MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        Row(
                                            alignment=alignment.center,
                                            controls=[
                                                Column(
                                                    controls=[
                                                        TextButton(date.strftime('%d'),
                                                                   style=ButtonStyle(shape=CircleBorder(),
                                                                                     color={
                                                                                         MaterialState.HOVERED: colors.WHITE},
                                                                                     overlay_color=colors.INDIGO_400
                                                                                     ),
                                                                   on_click=lambda event: showSchedule(),
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
                            )
                        ]
                    ),
                )])
