import flet
from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ChatInfo:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        user_id = int(params.user_id)
        patient_id = int(params.patient_id)

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

        def get_user_name():
            c = db.cursor()
            c.execute("SELECT fullName FROM doctors WHERE id = ?", (user_id,))
            record = c.fetchone()

            username = record[0]
            return username

        username = get_user_name()

        def get_initials(name):
            return name[:1].capitalize()

        def get_patient_name():
            c = db.cursor()
            c.execute("SELECT fullName FROM users WHERE id = ?", (patient_id,))
            record = c.fetchone()

            name = record[0]
            # print(name)
            return name

        name = get_patient_name()

        # Chat messages
        chat = ListView(
            expand=True,
            spacing=10,
            auto_scroll=True,
            controls=[
                Container(
                    margin=margin.only(top=10, left=40),
                    width=240,
                    # alignment=alignment.center_right,
                    content=Row(
                        # vertical_alignment="center",
                        controls=[
                            Column(
                                controls=[
                                    Text(
                                        width=235,
                                        value=f"{name}",
                                        weight="bold",
                                        color=colors.BLACK,
                                        font_family="RobotoSlab",
                                        size=14,
                                        text_align=TextAlign.RIGHT
                                    ),

                                    Container(
                                        padding=padding.only(top=10, left=10, right=10, bottom=10),
                                        bgcolor=lightBlue,
                                        border_radius=10,
                                        # width=220,
                                        content=Text(
                                            width=220,
                                            value=f"Hi, Dr. Johnson, I am {name} and I would like to ask you something...",
                                            size=12,
                                            text_align=TextAlign.JUSTIFY,
                                            color=colors.BLACK,
                                            font_family="RobotoSlab"
                                        )
                                    )

                                ],

                                tight=True,
                                spacing=3
                            ),

                            CircleAvatar(
                                content=Text(get_initials(name)),
                                color=colors.WHITE,
                                bgcolor=blue
                            ),
                        ]
                    )

                )
            ]
        )

        new_message = TextField(
            width=240,
            # height=40,
            dense=True,
            border_width=1,
            border_color=blue,
            multiline=True,
            text_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 font_family="RobotoSlab"
                                 ),
            hint_text="Write a message...",
            hint_style=TextStyle(size=12,
                                 color=colors.GREY_800,
                                 font_family="RobotoSlab"),
            autofocus=True,
        )

        def send_click(e):
            message = new_message.value
            if message.strip():
                chat.controls.append(
                    Container(
                        width=220,
                        margin=margin.only(top=10, left=20),
                        content=Row(
                            controls=[
                                CircleAvatar(
                                    content=Text(get_initials(username)),
                                    color=colors.WHITE,
                                    bgcolor="#87CEEC"
                                ),

                                Column(
                                    controls=[
                                        Text(
                                            value=f"Dr. {username}",
                                            weight="bold",
                                            color=colors.BLACK,
                                            font_family="RobotoSlab",
                                            size=14,
                                        ),

                                        Container(
                                            padding=padding.only(top=10, left=10, right=10, bottom=10),
                                            bgcolor=lightBlue,
                                            border_radius=10,
                                            content=Text(
                                                width=190,
                                                value=new_message.value,
                                                size=12,
                                                text_align=TextAlign.JUSTIFY,
                                                color=colors.BLACK,
                                                font_family="RobotoSlab"
                                            )
                                        )

                                    ],

                                    tight=True,
                                    spacing=3
                                )
                            ]
                        )

                    )

                )
                new_message.value = ""
                new_message.error_text = None
                page.update()
            else:
                new_message.error_text = "You are not allowed to send an empty message..."
                new_message.error_style = TextStyle(font_family="RobotoSlab",
                                                    color="#FF0000",
                                                    size=8)
                page.update()
                # new_message.error_text("You are not allowed to send empty message..."),
                # new_message.error_style(TextStyle(font_family="RobotoSlab"))

        return View(
            "/chat_info/:user_id:patient_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              horizontal_alignment="center",
                              controls=[
                                  Container(width=350,
                                            height=70,
                                            bgcolor=blue,
                                            alignment=alignment.top_center,
                                            padding=padding.only(left=10, right=10, bottom=0),
                                            content=Row(
                                                alignment="spaceBetween",
                                                controls=[
                                                    Container(padding=padding.only(top=25),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ),
                                                              on_click=lambda _: page.go(f"/chat/{user_id}{patient_id}")
                                                              ),

                                                    Container(padding=padding.only(top=25),
                                                              content=Text(
                                                                  value="Chat",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),

                                                    Container(
                                                        padding=padding.only(top=25),
                                                        content=IconButton(
                                                            icons.CALL,
                                                            icon_color=colors.WHITE,
                                                            icon_size=20,
                                                            on_click=lambda _: page.go(f"/doctorCallInterface/{user_id}{patient_id}")
                                                        )
                                                    )
                                                ]
                                            )
                                            ),

                                  chat,

                                  Container(
                                      width=300,
                                      # alignment=alignment.center,
                                      margin=margin.only(bottom=20),
                                      content=Row(
                                          vertical_alignment=CrossAxisAlignment.CENTER,
                                          controls=[
                                              new_message,

                                              Container(
                                                  content=TextButton(
                                                      content=Text("Send",
                                                                   size=10,
                                                                   font_family="RobotoSlab",
                                                                   color=blue,
                                                                   text_align=TextAlign.CENTER),
                                                      style=ButtonStyle(bgcolor={"": lightBlue},
                                                                        shape={
                                                                            "": RoundedRectangleBorder(
                                                                                radius=15)},
                                                                        ),
                                                      on_click=send_click
                                                  ),
                                              )

                                          ]
                                      )
                                  )

                              ]
                          )
                          )
            ]
        )