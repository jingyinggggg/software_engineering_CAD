from _pydecimal import Overflow

from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class ChatInfo:
    def __init__(self):
        self.message_input = ""  # Initialize the message input
        self.conversation = []  # Initialize an empty list to store the conversation

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

            return fullName

        fullName = get_doctor_details()

        def send_message():
            # Implement the logic to send the message here
            # You can access the message from self.message_input
            message = self.message_input
            # Perform the necessary actions to send the message

            # Add the sent message to the conversation
            self.conversation.append({
                "sender": "Doctor",  # You can change this to the actual sender's name
                "message": message
            })

            # Clear the message input field after sending
            self.message_input = ""

            # Update the page to reflect the sent message
            page.update()

        # Build the conversation based on the stored messages
        conversation_controls = []
        for message_data in self.conversation:
            # Create a container for each message in the conversation
            message_container = Container(
                bgcolor="#3386C5",  # Blue background for the doctor's messages
                border_radius=20,
                padding=padding.all(10),
                content=Text(message_data["message"], color="WHITE"),
            )

            conversation_controls.append(message_container)

        conversation = Column(controls=conversation_controls)

        return View(
            "/chat_info/:user_id",
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
                                        padding=padding.only(right=160),
                                        width=350,
                                        height=60,
                                        alignment=alignment.center,
                                        bgcolor="WHITE",
                                        border=border.all(color="#666666"),
                                        content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        IconButton(icons.ARROW_BACK_ROUNDED,
                                                                   icon_size=20,
                                                                   icon_color="BLACK",
                                                                   on_click=lambda _: page.go(
                                                                       f"/chat/{user_id}")),

                                                        Text("Melody Wong Yi Yi",
                                                             color="BLACK",
                                                             text_align=TextAlign.CENTER,
                                                             size=16,
                                                             font_family="RobotoSlab",
                                                             weight=FontWeight.BOLD)
                                                    ])
                                    )
                                ]),

                            # Sample Conversation with sender's and receiver's messages
                            Column(controls=[
                                # Sender's message on the right
                                Row(
                                    alignment=MainAxisAlignment.END,  # Align to the right
                                    controls=[
                                        Container(
                                            bgcolor="#3386C5",
                                            border_radius=20,
                                            padding=padding.all(10),
                                            content=Text("Hello Melody!", color="WHITE"),
                                        )
                                    ]
                                ),
                                # Receiver's message on the left
                                Row(
                                    alignment=MainAxisAlignment.START,  # Align to the left
                                    controls=[
                                        Container(
                                            bgcolor="#EFEFEF",
                                            border_radius=20,
                                            padding=padding.all(10),
                                            content=Text("Hi there!", color="BLACK"),
                                        )
                                    ]
                                ),
                                conversation,
                                # Add input field for writing messages
                                Container(margin=margin.only(top=320),
                                          content=Row(
                                              alignment=MainAxisAlignment.END,  # Align to the center

                                              controls=[
                                                  Container(
                                                            width=280,
                                                            content=TextField(
                                                                label="Write your message",
                                                                value=self.message_input,
                                                                on_change=lambda text: setattr(self, "message_input",
                                                                                               text),
                                                                border_color="#3386C5",
                                                                border_radius=10,
                                                                text_style=TextStyle(size=14, color=colors.BLACK),
                                                                height=40
                                                            )),
                                                  IconButton(
                                                      icons.SEND,
                                                      on_click=send_message,
                                                      icon_size=24,
                                                      icon_color="#3386C5",
                                                      width=50,
                                                      height=40
                                                  )
                                              ]
                                          ))
                            ])
                        ]
                    )
                )
            ]
        )
