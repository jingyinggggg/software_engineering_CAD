import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class HistoryPage:
    def __init__(self):
        pass

    def get_appointments(self, filter_option, value):
        appointments = [
            {"date": "Tue Oct 02 | 09:00AM - 10.00 AM", "patient": "Melody Wong Yi Yi", "type": "Consultation"},
            {"date": "Wed Oct 03 | 10:00AM - 11.00 AM", "patient": "John Doe", "type": "Follow up"},
            # Add more appointments here
        ]

        if filter_option == "Consultation":
            return value == "Consultation"
        elif filter_option == "Follow up":
            return value == "Follow up"
        else:
            return appointments

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
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

        # def on_filter_selected(option):
        #     nonlocal filter_option
        #     filter_option = option

        def get_doctor_details():
            c = db.cursor()
            c.execute("SELECT * FROM doctors WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]
            username = record[0][2]

            return fullName, username

        fullName, username = get_doctor_details()

        return View(
            "/history/:user_id",
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
                                    # top bar container
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
                                                                   on_click=lambda _: page.go(f"/login/homepage/{user_id}")),
                                                        Text("History",
                                                             color="WHITE",
                                                             text_align=TextAlign.CENTER,
                                                             size=20,
                                                             font_family="RobotoSlab",
                                                             weight=FontWeight.BOLD),
                                                        IconButton(icons.SEARCH_OUTLINED,
                                                                   icon_color="WHITE")]
                                                    )
                                    )]),

                            Container(
                                padding=padding.only(left=10),
                                content=Column(
                                    controls=[
                                        Dropdown(
                                            dense=True,
                                            label_style=TextStyle(size=14,
                                                                  weight=FontWeight.W_500,
                                                                  color="#3386C5"),
                                            label="Filter by category",
                                            hint_text="Select a category",
                                            hint_style=TextStyle(color="#71839B",
                                                                 size=14,
                                                                 italic=True),
                                            text_style=TextStyle(size=14,
                                                                 weight=FontWeight.W_500),
                                            options=[
                                                dropdown.Option("All"),
                                                dropdown.Option("Consultation"),
                                                dropdown.Option("Follow up")
                                            ],
                                            border_radius=10,
                                            border_color="#3386C5",
                                            color='BLACK',
                                            autofocus=True,
                                            width=320,
                                            height=80,
                                            focused_color="#71839B",
                                            text_size=12,
                                            content_padding=10,
                                        )
                                    ]
                                )
                            ),

                            Container(alignment=alignment.center,
                                      border_radius=8,
                                      padding=padding.only(left=10),
                                      margin=margin.only(left=10, top=-30),
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

                                                      Container(
                                                          content=Row(alignment=alignment.center,
                                                                      controls=[Container(
                                                                          Image(src="pic/patient.png",
                                                                                border_radius=20,
                                                                                width=65,
                                                                                height=65), ),
                                                                          Text("Melody Wong Yi Yi",
                                                                               weight=FontWeight.W_500,
                                                                               size=14,
                                                                               color="BLACK"),
                                                                      ])),
                                                      Container(margin=margin.only(left=75, top=-35),
                                                                content=Column(alignment=alignment.center,
                                                                               controls=[Container(
                                                                                   Text("Consultation",

                                                                                        color="#979797"))])),

                                                      Container(margin=margin.only(left=200, top=-20),
                                                                content=Column(alignment=alignment.center,
                                                                               controls=[Container(
                                                                                   TextButton("more >>",
                                                                                              on_click=lambda _: page.go(f"/appointmentDetail/{user_id}"))

                                                                               )]))

                                                      ])),

                            Container(alignment=alignment.center,
                                      border_radius=8,
                                      padding=padding.only(left=10),
                                      margin=margin.only(left=10),
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

                                                      Container(
                                                          content=Row(alignment=alignment.center,
                                                                      controls=[Container(
                                                                          Image(src="pic/patient.png",
                                                                                border_radius=20,
                                                                                width=65,
                                                                                height=65), ),
                                                                          Text("Melody Wong Yi Yi",
                                                                               weight=FontWeight.W_500,
                                                                               size=14,
                                                                               color="BLACK"),
                                                                      ])),

                                                      Container(margin=margin.only(left=75, top=-35),
                                                                content=Column(alignment=alignment.center,
                                                                               controls=[Container(
                                                                                   Text(value="Follow up",
                                                                                        color="#979797"))])),

                                                      Container(margin=margin.only(left=200, top=-20),
                                                                content=Column(alignment=alignment.center,
                                                                               controls=[Container(
                                                                                   TextButton("more >>",
                                                                                              on_click=lambda _: page.go(f"/appointmentDetail/{user_id}"))

                                                                               )]))

                                                      ])),

                            Container(alignment=alignment.center,
                                      border_radius=8,
                                      padding=padding.only(left=10),
                                      margin=margin.only(left=10),
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

                                                      Container(
                                                          content=Row(alignment=alignment.center,
                                                                      controls=[Container(
                                                                          Image(src="pic/patient.png",
                                                                                border_radius=20,
                                                                                width=65,
                                                                                height=65), ),
                                                                          Text("Melody Wong Yi Yi",
                                                                               weight=FontWeight.W_500,
                                                                               size=14,
                                                                               color="BLACK"),
                                                                      ])),
                                                      Container(margin=margin.only(left=75, top=-35),
                                                                content=Column(alignment=alignment.center,
                                                                               controls=[Container(
                                                                                   Text("Consultation",
                                                                                        color="#979797"))])),

                                                      Container(margin=margin.only(left=200, top=-20),
                                                                content=Column(alignment=alignment.center,
                                                                               controls=[Container(
                                                                                   TextButton("more >>",
                                                                                              on_click=lambda _: page.go(f"/appointmentDetail/{user_id}"))

                                                                               )]))

                                                      ])),
                        ]))])
