import flet as ft 

def storeView(page):
    return ft.View(
        "/store",
            [
                ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ft.ElevatedButton("Products", on_click=lambda _: page.go("/store/products")),
            ],
    )

