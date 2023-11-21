import flet
from flet import *
from flet_route import Params, Basket
import sqlite3
import datetime

db = sqlite3.connect("cad.db", check_same_thread=False)


class HealthTipsPage:
    def __init__(self):
        self.show_sidebar = False

    def view(self, page: Page, params: Params, basket: Basket):
        # print(params)
        user_id = int(params.user_id)

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

        return View(
            "/healthTips/:user_id",
            controls=[
                Container(width=350,
                          height=700,
                          bgcolor=colors.WHITE,
                          border_radius=30,
                          # child control
                          content=Column(
                              scroll=True,
                              horizontal_alignment="center",
                              controls=[

                                  Container(width=350,
                                            height=70,
                                            bgcolor=blue,
                                            alignment=alignment.top_center,
                                            padding=padding.only(left=10, right=10, bottom=0),
                                            content=Row(
                                                controls=[
                                                    Container(padding=padding.only(top=25),
                                                              content=Image(
                                                                  src="pic/back.png",
                                                                  color=colors.WHITE,
                                                                  width=20,
                                                                  height=20
                                                              ),
                                                              on_click=lambda _: page.go(f"/homepage/{user_id}")
                                                              ),

                                                    Container(padding=padding.only(left=90, top=25),
                                                              content=Text(
                                                                  value="Health Tips",
                                                                  size=20,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.WHITE,
                                                                  text_align=TextAlign.CENTER)
                                                              ),

                                                ]
                                            )
                                            ),

                                  Container(
                                      margin=margin.only(left=10, right=10, top=10, bottom=20),
                                      padding=padding.only(left=10, right=10, top=10, bottom=10),
                                      border_radius=0,
                                      # width=320,
                                      border=border.all(2, lightBlue),
                                      bgcolor=lightBlue,
                                      content=Column(
                                          controls=[
                                              Row(
                                                  controls=[
                                                      Text(
                                                          value="💡",
                                                          size=14
                                                      ),

                                                      Container(
                                                          width=265,
                                                          content=Text(
                                                              value=f"TIPS FOR MAINTAINING A HEALTHY LIFESTYLE",
                                                              size=14,
                                                              font_family="RobotoSlab",
                                                              color=colors.BLACK,
                                                              text_align=TextAlign.JUSTIFY,
                                                              weight=FontWeight.W_600

                                                          )
                                                      )
                                                  ]
                                              ),

                                              Container(
                                                  margin=margin.only(top=10),
                                                  padding=padding.only(left=5),
                                                  content=Row(
                                                      controls=[
                                                          Text(
                                                              value="1.",
                                                              size=11,
                                                              color=colors.BLACK,
                                                              font_family="RobotoSlab",
                                                              weight=FontWeight.W_600
                                                          ),

                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Limit Unhealthy Foods and Eat Healthy Meals",
                                                                  size=11,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY,
                                                                  weight=FontWeight.W_600

                                                              )
                                                          )
                                                      ]
                                                  ),
                                              ),

                                              Container(
                                                  margin=margin.only(top=-5),
                                                  padding=padding.only(left=24),
                                                  content=Row(
                                                      controls=[
                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Do not forget to eat breakfast and choose a "
                                                                        f"nutritious meal with more protein and fiber "
                                                                        f"and less fat, sugar, and calories.",
                                                                  size=9,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY

                                                              )
                                                          )
                                                      ]
                                                  )
                                              ),

                                              Container(
                                                  margin=margin.only(top=10),
                                                  padding=padding.only(left=5),
                                                  content=Row(
                                                      controls=[
                                                          Text(
                                                              value="2.",
                                                              size=11,
                                                              color=colors.BLACK,
                                                              font_family="RobotoSlab",
                                                              weight=FontWeight.W_600
                                                          ),

                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Take Multivitamin Supplements",
                                                                  size=11,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY,
                                                                  weight=FontWeight.W_600

                                                              )
                                                          )
                                                      ]
                                                  ),
                                              ),

                                              Container(
                                                  margin=margin.only(top=-5),
                                                  padding=padding.only(left=24),
                                                  content=Row(
                                                      controls=[
                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"To make sure you have sufficient levels of "
                                                                        f"nutrients, taking a daily multivitamin "
                                                                        f"supplement is a good idea, especially when "
                                                                        f"you do not have a variety of vegetables and "
                                                                        f"fruits at home.",
                                                                  size=9,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY

                                                              )
                                                          )
                                                      ]
                                                  )
                                              ),

                                              Container(
                                                  margin=margin.only(top=10),
                                                  padding=padding.only(left=5),
                                                  content=Row(
                                                      controls=[
                                                          Text(
                                                              value="3.",
                                                              size=11,
                                                              color=colors.BLACK,
                                                              font_family="RobotoSlab",
                                                              weight=FontWeight.W_600
                                                          ),

                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Drink Water and Limit Sugared Beverages",
                                                                  size=11,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY,
                                                                  weight=FontWeight.W_600

                                                              )
                                                          )
                                                      ]
                                                  ),
                                              ),

                                              Container(
                                                  margin=margin.only(top=-5),
                                                  padding=padding.only(left=24),
                                                  content=Row(
                                                      controls=[
                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Drink water regularly to stay healthy, but "
                                                                        f"there is NO evidence that drinking water "
                                                                        f"frequently (e.g. every 15 minutes) can help "
                                                                        f"prevent any viral infection.",
                                                                  size=9,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY

                                                              )
                                                          )
                                                      ]
                                                  )
                                              ),

                                              Container(
                                                  margin=margin.only(top=10),
                                                  padding=padding.only(left=5),
                                                  content=Row(
                                                      controls=[
                                                          Text(
                                                              value="4.",
                                                              size=11,
                                                              color=colors.BLACK,
                                                              font_family="RobotoSlab",
                                                              weight=FontWeight.W_600
                                                          ),

                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Reduce Sitting and Screen Time ",
                                                                  size=11,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY,
                                                                  weight=FontWeight.W_600

                                                              )
                                                          )
                                                      ]
                                                  ),
                                              ),

                                              Container(
                                                  margin=margin.only(top=-5),
                                                  padding=padding.only(left=24),
                                                  content=Row(
                                                      controls=[
                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"You could consider taking breaks from "
                                                                        f"sedentary time, such as walking around the "
                                                                        f"office/room a couple of times in a day. ",
                                                                  size=9,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY

                                                              )
                                                          )
                                                      ]
                                                  )
                                              ),

                                              Container(
                                                  margin=margin.only(top=10),
                                                  padding=padding.only(left=5),
                                                  content=Row(
                                                      controls=[
                                                          Text(
                                                              value="5.",
                                                              size=11,
                                                              color=colors.BLACK,
                                                              font_family="RobotoSlab",
                                                              weight=FontWeight.W_600
                                                          ),

                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Get Enough Good Sleep ",
                                                                  size=11,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY,
                                                                  weight=FontWeight.W_600

                                                              )
                                                          )
                                                      ]
                                                  ),
                                              ),

                                              Container(
                                                  margin=margin.only(top=-5),
                                                  padding=padding.only(left=24),
                                                  content=Row(
                                                      controls=[
                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"There is a very strong connection between "
                                                                        f"sleep quality and quantity and your immune "
                                                                        f"system. You can keep your immune system "
                                                                        f"functioning properly by getting seven to "
                                                                        f"eight hours of sleep each night.",
                                                                  size=9,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY

                                                              )
                                                          )
                                                      ]
                                                  )
                                              ),

                                              Container(
                                                  margin=margin.only(top=10),
                                                  padding=padding.only(left=5),
                                                  content=Row(
                                                      controls=[
                                                          Text(
                                                              value="6.",
                                                              size=11,
                                                              color=colors.BLACK,
                                                              font_family="RobotoSlab",
                                                              weight=FontWeight.W_600
                                                          ),

                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Go Easy on Alcohol and Stay Sober",
                                                                  size=11,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY,
                                                                  weight=FontWeight.W_600

                                                              )
                                                          )
                                                      ]
                                                  ),
                                              ),

                                              Container(
                                                  margin=margin.only(top=-5),
                                                  padding=padding.only(left=24),
                                                  content=Row(
                                                      controls=[
                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Drinking alcohol does not protect you from "
                                                                        f"the coronavirus infection. Don’t forget "
                                                                        f"that those alcohol calories can add up "
                                                                        f"quickly. Alcohol should always be consumed "
                                                                        f"in moderation.",
                                                                  size=9,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY

                                                              )
                                                          )
                                                      ]
                                                  )
                                              ),

                                              Container(
                                                  margin=margin.only(top=10),
                                                  padding=padding.only(left=5),
                                                  content=Row(
                                                      controls=[
                                                          Text(
                                                              value="7.",
                                                              size=11,
                                                              color=colors.BLACK,
                                                              font_family="RobotoSlab",
                                                              weight=FontWeight.W_600
                                                          ),

                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"Find Ways to Manage Your Emotions",
                                                                  size=11,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY,
                                                                  weight=FontWeight.W_600

                                                              )
                                                          )
                                                      ]
                                                  ),
                                              ),

                                              Container(
                                                  margin=margin.only(top=-5),
                                                  padding=padding.only(left=24),
                                                  content=Row(
                                                      controls=[
                                                          Container(
                                                              width=270,
                                                              content=Text(
                                                                  value=f"It is common for people to have feelings of "
                                                                        f"fear, anxiety, sadness, and uncertainty "
                                                                        f"in their work and study.",
                                                                  size=9,
                                                                  font_family="RobotoSlab",
                                                                  color=colors.BLACK,
                                                                  text_align=TextAlign.JUSTIFY

                                                              )
                                                          )
                                                      ]
                                                  )
                                              ),



                                          ]
                                      )
                                  ),

                              ]
                          )
                          )
            ]
        )
