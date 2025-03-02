import flet as ft


def main(page: ft.Page):
    page.window.bgcolor = ft.Colors.TRANSPARENT  # Macht den Fensterhintergrund transparent
    page.window.frameless = True  # Entfernt den Rahmen (nur für Desktop-Apps)

    page.add(ft.Text("Schwebender Text!"))
    page.update()


ft.app(target=main)
