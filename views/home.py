import flet as ft 

def homeView(page):
    return ft.View(
                "/",
                [   
                    ft.AppBar(
                        leading=ft.Icon(ft.icons.PALETTE),
                        leading_width=40,
                        title=ft.Text("AppBar Title"),
                        center_title=False,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        actions=[
                            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                            ft.IconButton(ft.icons.FILTER_3),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text="Store"),
                                    ft.PopupMenuItem(),  # divider
                                    ft.PopupMenuItem(
                                        text="Checked item",
                                        checked=False,
                                    ),
                                ]
                            ),
                        ],
                    ),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )

