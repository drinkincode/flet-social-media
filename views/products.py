import flet as ft 

def productsView(page):
    return ft.View(
        "/store",
            [
                ft.AppBar(title=ft.Text("Products"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
            ],
    )

