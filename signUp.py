import flet
from flet import *
from flet_route import Params,Basket

class SignUpPage:
    def __int__(self):
        pass

    def view(self, page:Page, params:Params, basket:Basket):
        page.title = "Call A Doctor"
        page.window_width = 380
        page.window_height = 900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.theme_mode = "light"

        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

        return View(
            "/signUp",
            controls=[
                Container(padding=padding.symmetric(horizontal=20, vertical=20),
                          width=350,
                          height=700,
                          bgcolor="#D0DCEE",
                          border_radius=30,
                          border=border.all(1, "black"),
                          alignment=alignment.center,
                          # child control
                          content=Column())

            ]
        )