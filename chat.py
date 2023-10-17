from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class Chat:
    def __init__(self):
        self.show_navigation_button = False

    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "dark"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        return View(
            "/chat",
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
                                            height=80,
                                            alignment=alignment.center,
                                            bgcolor="#3386C5",
                                            content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                        controls=[
                                                            IconButton(icons.ARROW_BACK_ROUNDED,
                                                                       icon_size=30,
                                                                       icon_color="WHITE",
                                                                       on_click=lambda _: page.go(f"/login/homepage")),
                                                            Text("Chat",
                                                                 color="WHITE",
                                                                 text_align=TextAlign.CENTER,
                                                                 size=20,
                                                                 font_family="RobotoSlab",
                                                                 weight=FontWeight.BOLD)]
                                                        )
                                        )
                                    ])]))])



