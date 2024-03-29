import reflex as rx

config = rx.Config(
    app_name="tcott",
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="medium",
        accent_color="pink",
        gray_color="slate",
    ),
    stylesheets=["landing.css"],
)
