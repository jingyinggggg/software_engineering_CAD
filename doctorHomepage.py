from flet import *
from flet_route import Params, Basket

class DoctorHomepage:
    def view(self, page: Page, params: Params, basket: Basket):
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
            "/login/homepage",
            controls=[
                Container(
                    # padding=padding.symmetric(horizontal=20, vertical=100),
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    border=border.all(1, "black"),
                    alignment=alignment.center,
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Container(
                                width=350,
                                height=300,
                                bgcolor="#3386C5",
                                padding=padding.symmetric(horizontal=10, vertical=20),
                            
                                content=Column(
                                    horizontal_alignment="top_left",
                                    controls=[
                                        Image(
                                            src="pic/menu.png",
                                            width=30,
                                            height=30,
                                        ),
                                        
                                        Container(
                                            # width=350,
                                            # height=400,
                                            # bgcolor="#3386C5",
                                            padding=padding.only(left=20,top=60),
                                            
                                            content=Column(
                                                horizontal_alignment="top_left",
                                                controls=[
                                                    Text(
                                                        "Welcome !",
                                                        size=30,
                                                        font_family="RobotoSlab",
                                                        text_align=TextAlign.LEFT,
                                                        color="WHITE"
                                                    ),
                                                    Text(
                                                        "Dr. Shariman",
                                                        size=30,
                                                        font_family="RobotoSlab",
                                                        text_align=TextAlign.LEFT,
                                                        color="WHITE"
                                                    ),
                                                ]
                                            ),
                                        ),
                                        
                                        Container(
                                            # width=350,
                                            # height=400,
                                            # bgcolor="#3386C5",
                                            padding=padding.only(left=80, top=-176),
                                            
                                            content=Row(
                                                # horizontal_alignment="top_left",
                                                controls=[
                                                    Image(
                                                    src="pic/doctor.png",
                                                    width=300,
                                                    height=300
                                                    )
                                                ]
                                            ),
                                        ),
                                        
                                        Container(bgcolor="WHITE",
                                                  padding=padding.only(left=10, top=10),
                                                  border_radius=40,
                                                  content=Column(
                                                      controls=[Text("Our Services",
                                                                size=20,
                                                                font_family="RobotoSlab",
                                                                weight=FontWeight.W_600,
                                                                color="BLACK")]
                                                      
                                                      
                                                  )
                                        )
                                        
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
