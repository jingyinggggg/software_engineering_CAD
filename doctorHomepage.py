from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class DoctorHomepage:
    def __init__(self):
        pass

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

        def get_doctor_details():
            c = db.cursor()
            c.execute("SELECT * FROM doctors WHERE id = ?", (user_id,))
            record = c.fetchall()

            fullName = record[0][1]
            username = record[0][2]

            return fullName, username

        fullName, username = get_doctor_details()

        # phone container
        return View(
            "/login/homepage/:user_id",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,

                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.START,
                        controls=[
                            Container(
                                width=350,
                                height=250,
                                bgcolor="#3386C5",
                                padding=padding.symmetric(horizontal=10, vertical=20),

                                content=Column(
                                    controls=[
                                        Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                Container(
                                                    content=IconButton(icons.MENU,
                                                                       icon_color="WHITE",
                                                                       on_click=lambda _: page.go(f"/sideBar"))),
                                                Row(controls=[IconButton(icons.CIRCLE_NOTIFICATIONS_ROUNDED,
                                                                         icon_color="WHITE",
                                                                         on_click=lambda _: page.go(
                                                                             f"/notification/{user_id}"))])]),

                                        Text(value="Welcome !",
                                             size=30,
                                             font_family="RobotoSlab",
                                             weight=FontWeight.BOLD,
                                             color="WHITE"),

                                        Text(value=f"Dr. {fullName}",
                                             size=30,
                                             font_family="RobotoSlab",
                                             weight=FontWeight.BOLD,
                                             color="WHITE"),

                                        Container(
                                            padding=padding.only(left=100, top=-140),

                                            content=Row(
                                                # horizontal_alignment="top_left",
                                                controls=[
                                                    Image(
                                                        src="pic/doctor.png",
                                                        width=280,
                                                        height=280
                                                    )
                                                ])),

                                        Container(bgcolor="WHITE",
                                                  padding=padding.only(top=10, left=10),
                                                  alignment=alignment.top_left,
                                                  width=800,
                                                  height=800,
                                                  margin=margin.only(top=-100, left=-10, right=-10),
                                                  border_radius=30,
                                                  content=Column(
                                                      controls=[Text("Our Services",
                                                                     text_align=TextAlign.CENTER,
                                                                     size=16,
                                                                     font_family="RobotoSlab",
                                                                     weight=FontWeight.W_500,
                                                                     color="BLACK"),
                                                                ])

                                                  ),

                                    ])),
                            Container(
                                alignment=alignment.center,
                                margin=margin.only(top=10),
                                content=Row(
                                    alignment=MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        Container(
                                            content=IconButton(
                                                icons.HISTORY,
                                                icon_color="#3D3F99",
                                                icon_size=45,
                                                tooltip="view history",
                                                on_click=lambda _: page.go(f"/history/{user_id}")
                                            ),
                                            border_radius=50,
                                            border=border.all(1, "#000000"),
                                            height=60,
                                            width=60,

                                        ),

                                        Container(
                                            content=IconButton(
                                                icons.DATE_RANGE_ROUNDED,
                                                icon_color="#3D3F99",
                                                icon_size=45,
                                                tooltip="view schedule",
                                                on_click=lambda _: page.go(f"/schedule/{user_id}")
                                            ),
                                            border_radius=50,
                                            border=border.all(1, "#000000"),
                                            height=60,
                                            width=60
                                            # Add border here
                                        ),
                                        Container(
                                            content=IconButton(
                                                icons.WECHAT,
                                                icon_color="#3D3F99",
                                                icon_size=45,
                                                tooltip="view chat",
                                                on_click=lambda _: page.go(f"/chat/{user_id}")
                                            ),
                                            border_radius=50,
                                            border=border.all(1, "#000000"),
                                            height=60,
                                            width=60
                                            # Add border here
                                        )
                                    ]
                                )
                            ),
                            Container(alignment=alignment.center,
                                      content=Row(alignment=MainAxisAlignment.SPACE_EVENLY,
                                                  controls=[Container(
                                                      content=Text("History",
                                                                   font_family="RobotoSlab",
                                                                   size=14,
                                                                   color="BLACK"),
                                                  ),
                                                      Text("Schedule",
                                                           font_family="RobotoSlab",
                                                           size=14,
                                                           color="BLACK"),
                                                      Text("Chat",
                                                           font_family="RobotoSlab",
                                                           size=14,
                                                           color="BLACK")])),

                            Container(alignment=alignment.center,
                                      padding=padding.only(left=10, top=30, right=10),
                                      content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                  controls=[Container(
                                                      content=Text("Appointment",
                                                                   font_family="RobotoSlab",
                                                                   color="BLACK",
                                                                   size=16,
                                                                   weight=FontWeight.W_500)),
                                                      Text(disabled=False,
                                                           spans=[TextSpan(
                                                               "see more",
                                                               TextStyle(
                                                                   decoration=TextDecoration.UNDERLINE,
                                                                   color="#3386C5"),
                                                               on_click=lambda _: page.go(f"/schedule/{user_id}"))])

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

                                                      Container(margin=margin.only(left=220, top=-20),
                                                                content=Column(alignment=alignment.center,
                                                                               controls=[Container(
                                                                                   TextButton("more >>",
                                                                                              on_click=lambda _: page.go(f"/appointmentDetail/{user_id}"))

                                                                               )]))

                                                      ])),

                            # ResponsiveRow([Container(Text())])
                        ]))])
