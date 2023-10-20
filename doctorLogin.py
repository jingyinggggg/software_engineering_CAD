import flet
from flet import *
from flet_route import Params,Basket

class DoctorLoginPage:
    def __int__(self):
        pass

    def view(self,page:Page, params:Params, basket:Basket):
        # print(params)

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
            "/login",
            controls=[
                Container(padding=padding.symmetric(horizontal=20, vertical=100),
                          width=350,
                          height=700,
                          bgcolor="#FFFFFF",
                          border_radius=30,
                          border=border.all(1, "black"),
                          alignment=alignment.center,
                          # child control
                         content=Column(
                             horizontal_alignment="center",
                             controls=[
                                Container(padding=padding.symmetric(vertical=30),
                                            content=Image(src="pic/loginPageImage.png",
                                                            width=200,
                                                            height=180)),

                                Text("Call A Doctor",
                                    size=24,
                                    font_family="RobotoSlab",
                                    text_align=TextAlign.CENTER,
                                    color="#3386C5"),
                                
                                TextField(
                                        label="Username", 
                                        hint_text="Enter username",
                                        ),
                                
                                TextField(
                                            label="Password", 
                                            password=True, 
                                            hint_text="Enter password",
                                            ),
                                
                                Checkbox(label="Remember Me",
                                         value=False),
                                
                                IconButton(content=Text("Login",
                                                         size=16,
                                                         font_family="RobotoSlab",
                                                         color="WHITE",
                                                         text_align=TextAlign.CENTER),
                                             width=300,
                                             height=45,
                                             style=ButtonStyle(bgcolor={"": "#3386C5"},
                                                               shape={"": RoundedRectangleBorder(radius=7)}
                                                               ),
                                              on_click=lambda _:page.go(f"/login/homepage")
                                             ),
                                
                                Text(disabled=False,
                                     spans=[
                                         TextSpan("forget password?",
                                         TextStyle(decoration=TextDecoration.UNDERLINE),
                                         on_click=lambda _:page.go(f"/login/resetPassword")
                                         ),
                                                                                  
                                        ]  
                                    ),
                                ]
                            )
                        )
            ]
        )