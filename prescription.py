from datetime import date

from flet import *
from flet_route import Params, Basket
import sqlite3

db = sqlite3.connect("cad.db", check_same_thread=False)


class Prescription:
    def __init__(self):
        self.selected_date = date.today()
        self.show_confirmation = False
        self.show_alert = False
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

        def close_alert_dialog(_):
            page.dialog = alert_dialog
            alert_dialog.open = False
            page.update()

        # Create an alert dialog
        alert_dialog = AlertDialog(
            modal=True,
            title=Text("Alert", text_align=TextAlign.CENTER),
            content=Text("Prescription generated successfully!",
                         text_align=TextAlign.CENTER),
            actions=[TextButton("OK", on_click=close_alert_dialog)],
            actions_alignment=MainAxisAlignment.CENTER,
            open=False
        )

        def open_alert_dialog(_):
            page.dialog = alert_dialog
            alert_dialog.open = True
            page.update()

        return View(
            "/prescription/:user_id",
            controls=[
                Container(
                    width=350,
                    height=700,
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Row(alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        padding=padding.only(right=60),
                                        width=350,
                                        height=80,
                                        alignment=alignment.center,
                                        bgcolor="#3386C5",
                                        content=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        IconButton(icons.ARROW_BACK_ROUNDED,
                                                                   icon_size=30,
                                                                   icon_color="WHITE",
                                                                   on_click=lambda _: page.go(
                                                                       f"/appointmentDetail/{user_id}")),
                                                        Text("Generate Prescription",
                                                             color="WHITE",
                                                             text_align=TextAlign.CENTER,
                                                             size=20,
                                                             font_family="RobotoSlab",
                                                             weight=FontWeight.BOLD)]
                                                    )
                                    )
                                ]),
                            Container(padding=padding.only(left=10),
                                      content=Column(controls=[
                                          Text("Patient's Name:", color="#666666", size=14,
                                               weight=FontWeight.BOLD),
                                          Row(
                                              alignment=MainAxisAlignment.START,
                                              controls=[
                                                  TextField(
                                                      label="First Name",
                                                      read_only=True,
                                                      value="Wong",
                                                      width=150,
                                                      height=35,
                                                      label_style=TextStyle(color="BLACK"),
                                                      border_color=colors.BLACK,
                                                      bgcolor="#D1D1D1",
                                                      text_style=TextStyle(size=12, color=colors.BLACK)
                                                  ),
                                                  TextField(
                                                      label="Last Name",
                                                      read_only=True,
                                                      value="Yi Yi",
                                                      width=150,
                                                      height=35,
                                                      label_style=TextStyle(color="BLACK"),
                                                      border_color=colors.BLACK,
                                                      bgcolor="#D1D1D1",
                                                      text_style=TextStyle(size=12, color=colors.BLACK)
                                                  )
                                              ]
                                          ),
                                          Text("Patient's Age", color="#666666", size=14, weight=FontWeight.BOLD),
                                          Row(
                                              alignment=MainAxisAlignment.START,
                                              controls=[
                                                  TextField(
                                                      label="Age",
                                                      read_only=True,
                                                      value="40",
                                                      width=310,
                                                      height=35,
                                                      label_style=TextStyle(color="BLACK"),
                                                      border_color=colors.BLACK,
                                                      bgcolor="#D1D1D1",
                                                      text_style=TextStyle(size=12, color=colors.BLACK)
                                                  ),
                                              ]),
                                          Text("Treatment", color="#666666", size=14, weight=FontWeight.BOLD),
                                          Text("Rx: Medication / Strength / Frequency", color="#666666", size=12,
                                               weight=FontWeight.W_600),
                                          Row(
                                              alignment=MainAxisAlignment.START,
                                              controls=[
                                                  TextField(
                                                      value="",
                                                      width=310,
                                                      height=35,
                                                      label_style=TextStyle(color="BLACK"),
                                                      border_color=colors.BLACK,
                                                      text_style=TextStyle(size=12, color=colors.BLACK)
                                                  )
                                              ]
                                          ),
                                          # OutlinedButton(text="Add More", width=310,
                                          #                style=ButtonStyle(color="#3D3F99",
                                          #                                  side=BorderSide(1, color="#3386C5"))),
                                          Text("Medical Notes", color="#666666", size=14, weight=FontWeight.BOLD),
                                          Row(
                                              alignment=MainAxisAlignment.START,
                                              controls=[
                                                  TextField(
                                                      value="",
                                                      width=310,
                                                      height=70,
                                                      label_style=TextStyle(color="BLACK"),
                                                      border_color=colors.BLACK,
                                                      text_style=TextStyle(size=14, color=colors.BLACK)
                                                  )
                                              ]
                                          ),
                                          # Checkbox(label="Test & Lab Result (optional)")
                                          Text("Date Signed", color="#666666", size=14, weight=FontWeight.BOLD),
                                          TextField(
                                              label="Select Date:",
                                              suffix_icon=icons.DATE_RANGE,
                                              width=310,
                                              height=35,
                                              label_style=TextStyle(color="BLACK"),
                                              border_color=colors.BLACK,
                                              text_style=TextStyle(size=12, color=colors.BLACK),
                                              value=self.selected_date.strftime('%d/%m/%Y'),
                                              # Display selected date in the TextField

                                          ),
                                          Text("Physician's Signature", color="#666666", size=14,
                                               weight=FontWeight.BOLD),
                                          Row(
                                              alignment=MainAxisAlignment.START,
                                              controls=[
                                                  TextField(
                                                      value="",
                                                      width=310,
                                                      height=70,
                                                      label_style=TextStyle(color="BLACK"),
                                                      border_color=colors.BLACK,
                                                      text_style=TextStyle(size=12, color=colors.BLACK)
                                                  )
                                              ]
                                          ),
                                          Container(padding=padding.only(left=70),
                                                    margin=margin.only(top=-20),
                                                    content=Column(controls=[
                                                        # Your other controls here
                                                        FilledButton(text="Generate", width=200,
                                                                     on_click=open_alert_dialog)
                                                    ]))
                                      ]))]))])
