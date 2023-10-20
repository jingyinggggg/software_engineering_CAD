from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class AppointmentDetail:
    def __init__(self):
        self.show_navigation_button = False

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        grey = "#71839B"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        def handle_dropdown_change(value):
            if value == "Completed":
                # Show the navigation button when "Completed" is selected
                self.show_navigation_button = True
            else:
                # Hide the navigation button for other options
                self.show_navigation_button = False

        return View(
            "/appointmentDetail",
            controls=[Container(
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
                                    padding=padding.only(right=120),
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
                                                    Text("Appointment",
                                                         color="WHITE",
                                                         text_align=TextAlign.CENTER,
                                                         size=20,
                                                         font_family="RobotoSlab",
                                                         weight=FontWeight.BOLD)]
                                                )
                                )
                            ]),

                        Container(alignment=alignment.center,
                                  border_radius=8,
                                  padding=padding.only(left=10),
                                  margin=margin.only(left=10, top=10),
                                  border=border.all(color="BLACK"),
                                  width=320,
                                  height=150,
                                  content=Stack(
                                      # Stacking the image and text
                                      [
                                          Image(src="pic/patient.png",
                                                width=150,
                                                height=150),
                                          Column(controls=[
                                              Row(alignment=MainAxisAlignment.START,
                                                  controls=[Container(
                                                      alignment=alignment.top_left,
                                                      content=
                                                      Text("Patient Details",
                                                           font_family="RobotoSlab",
                                                           weight=FontWeight.BOLD,
                                                           size=14,
                                                           color="#979797"))]
                                                  ),
                                              Container(
                                                  margin=margin.only(left=160, top=-5),
                                                  content=Column(controls=[
                                                      Text("Name: ", color="BLACK", size=12, weight=FontWeight.BOLD),
                                                      Text("D.O.B: ", color="BLACK", size=12, weight=FontWeight.BOLD),
                                                      Text("Age: ", color="BLACK", size=12, weight=FontWeight.BOLD),
                                                      Text("Gender: ", color="BLACK", size=12, weight=FontWeight.BOLD)
                                                  ])
                                              )
                                          ]

                                          )
                                      ]
                                  )),
                        Container(
                            margin=margin.only(left=10, top=10),
                            alignment=alignment.top_left,
                            content=
                            Text("Appointment Details",
                                 font_family="RobotoSlab",
                                 weight=FontWeight.BOLD,
                                 size=14,
                                 color="#979797")),
                        Container(margin=margin.only(left=10),
                                  content=Row(controls=[
                                      Text("Appointment Date: ", color="BLACK", font_family="RobotoSlab",
                                           weight=FontWeight.BOLD, size=12),
                                      # get from database
                                      Text()
                                  ])),
                        Container(margin=margin.only(left=10),
                                  content=Row(controls=[
                                      Text("Appointment Time: ", color="BLACK", font_family="RobotoSlab",
                                           weight=FontWeight.BOLD, size=12),
                                      # get from database
                                      Text()
                                  ])),
                        Container(margin=margin.only(left=10),
                                  content=Row(controls=[
                                      Text("Type of appointment: ", color="BLACK", font_family="RobotoSlab",
                                           weight=FontWeight.BOLD, size=12),
                                      # get from database
                                      Text()
                                  ])),
                        Container(margin=margin.only(left=10),
                                  content=Row(controls=[
                                      Text("Appointment Location: ", color="BLACK", font_family="RobotoSlab",
                                           weight=FontWeight.BOLD, size=12),
                                      # get from database
                                      Text()
                                  ])),
                        Container(margin=margin.only(left=10),
                                  content=Row(controls=[
                                      Text("Appointment Status: ", color="BLACK", font_family="RobotoSlab",
                                           weight=FontWeight.BOLD, size=12),
                                      # get from database
                                      Dropdown(label="Update status",
                                               hint_text="e.g. scheduled/checked-in/completed",
                                               hint_style=TextStyle(color=grey,
                                                                    size=14,
                                                                    italic=True),
                                               options=[
                                                   dropdown.Option("Scheduled"),
                                                   dropdown.Option("Checked-in"),
                                                   dropdown.Option("Completed")],
                                               on_change=handle_dropdown_change,
                                               width=190,
                                               # height=50,
                                               content_padding=10,
                                               color='BLACK',
                                               autofocus=True,
                                               text_size=12,
                                               border_color="#3386C5",
                                               label_style=TextStyle(size=14,
                                                                     weight=FontWeight.W_500,
                                                                     color="#3386C5"),
                                               dense=True,
                                               text_style=TextStyle(size=14,
                                                                    weight=FontWeight.W_500),
                                               focused_color=grey,
                                               )

                                  ])),
                        Container(margin=margin.only(left=10),
                                  content=Row(controls=[
                                      Text("Reason for visit: ", color="BLACK", font_family="RobotoSlab",
                                           weight=FontWeight.BOLD, size=12),
                                      # get from database
                                      Text()
                                  ])),

                        Container(margin=margin.only(left=80, top=50),
                                  content=Row(controls=[
                                      FilledTonalButton("Write Prescription",
                                                        on_click=lambda _: page.go("/prescription"),
                                                        visible=self.show_navigation_button),
                                      # get from database
                                      Text()
                                  ])),

                        # Show the button only when self.show_navigation_button is True
                        # FilledTonalButton("Write Prescription",
                        #                   on_click=lambda _: page.go("/prescription"),
                        #                   visible=self.show_navigation_button),

                    ]
                ))
            ]
        )
