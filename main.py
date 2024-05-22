

import flet as ft
import views.store as store
import views.home as home
import views.products as products

            
def main(page: ft.Page):
    page.title = "Routes Example"
    def route_change(route):
        page.views.clear()
        
        page.views.append(
            home.homeView(page)
        )
        
        if page.route == "/store":
            page.views.append(
                store.storeView(page)
            )
            
        if page.route == "/store/products":
            page.views.append(
                products.productsView(page)
            )
            
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    


ft.app(target=main, view=ft.AppView.WEB_BROWSER)


# import flet as ft


# def main(page):

#     page.adaptive = True

#     page.appbar = ft.AppBar(
#         leading=ft.TextButton("New", style=ft.ButtonStyle(padding=0)),
#         title=ft.Text("Adaptive AppBar"),
#         actions=[
#             ft.IconButton(ft.cupertino_icons.ADD, style=ft.ButtonStyle(padding=0))
#         ],
#         bgcolor=ft.colors.with_opacity(0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),
#     )

#     page.navigation_bar = ft.NavigationBar(
#         destinations=[
#             ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
#             ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
#             ft.NavigationDestination(
#                 icon=ft.icons.BOOKMARK_BORDER,
#                 selected_icon=ft.icons.BOOKMARK,
#                 label="Bookmark",
#             ),
#         ],
#         border=ft.Border(
#             top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0)
#         ),
#     )

#     page.add(
#         ft.SafeArea(
#             ft.Column(
#                 [
#                     ft.Checkbox(value=False, label="Dark Mode"),
#                     ft.Text("First field:"),
#                     ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
#                     ft.Text("Second field:"),
#                     ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
#                     ft.Switch(label="A switch"),
#                     ft.FilledButton(content=ft.Text("Adaptive button")),
#                     ft.Text("Text line 1"),
#                     ft.Text("Text line 2"),
#                     # ft.Text("Text line 3"),
#                 ]
#             )
#         )
#     )


# ft.app(target=main,view=ft.AppView.WEB_BROWSER)

# import flet as ft
# import time
# class Task(ft.Row):
#     def __init__(self, text):
#         super().__init__()
#         self.text_view = ft.Text(text)
#         self.text_edit = ft.TextField(text, visible=False)
#         self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
#         self.save_button = ft.IconButton(
#             visible=False, icon=ft.icons.SAVE, on_click=self.save
#         )
#         self.controls = [
#             ft.Checkbox(),
#             self.text_view,
#             self.text_edit,
#             self.edit_button,
#             self.save_button,
#         ]

#     def edit(self, e):
#         self.edit_button.visible = False
#         self.save_button.visible = True
#         self.text_view.visible = False
#         self.text_edit.visible = True
#         self.update()

#     def save(self, e):
#         self.edit_button.visible = True
#         self.save_button.visible = False
#         self.text_view.visible = True
#         self.text_edit.visible = False
#         self.text_view.value = self.text_edit.value
#         self.update()
        
# def main(page: ft.Page):
#     page.add(ft.SafeArea(ft.Text("Hello, Flet!")))

#     page.add(
#         ft.Row(controls=[
#             ft.Text("Take a Sip!"),
#             ft.Text("B"),
#             ft.Text("D")
#         ])
#     # )
#     def add_clicked(e):
#         page.add(Task(text = new_task.value))
#         new_task.value = ""
#         new_task.focus()
#         new_task.update()

#     new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
#     page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    
    

# ft.app(main)


# import flet as ft

# def main(page: ft.Page):
#     page.title = "Flet Chat"

#     # subscribe to broadcast messages
#     def on_message(msg):
#         messages.controls.append(ft.Text(msg))
#         page.update()

#     page.pubsub.subscribe(on_message)

#     def send_click(e):
#         page.pubsub.send_all(f"{user.value}: {message.value}")
#         # clean up the form
#         message.value = ""
#         page.update()

#     messages = ft.Column()
#     user = ft.TextField(hint_text="Your name", width=150)
#     message = ft.TextField(hint_text="Your message...", expand=True)  # fill all the space
#     send = ft.ElevatedButton("Send", on_click=send_click)
#     page.add(messages, ft.Row(controls=[user, message, send]))

# ft.app(target=main, view=ft.AppView.WEB_BROWSER)