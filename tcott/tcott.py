"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx


class State(rx.State):
    """The app state."""

    pass


def background():
    return rx.container(
        rx.box(
            id="noise",
            class_name="full-screen",
        ),
        rx.box(
            id="bg",
            class_name="full-screen",
        ),
    )


class Cloud:
    def __init__(self, index: int):
        self.index: int = index

        if self.index > 13:
            raise ValueError(
                "Cloud index must be less than 14. We only got 14 clouds. Sorry, homie pal."
            )

        self.image: str = f"clouds/cloud_{str(self.index).zfill(2)}.png"
        # self.nudge = "33%" if self.index % 2 == 0 else "-33%"
        self.side = "end" if self.index % 2 == 0 else "start"
        self.nudge = "33%" if self.index % 2 == 0 else "-33%"

    def render(self) -> rx.Component:
        return rx.image(
            src=self.image,
            style={
                "opacity": "0.5",
                "mix-blend-mode": "screen",
                "width": "69vw",
                "height": "auto",
                "align-self": self.side,
                "transform": f"translateX({self.nudge})",
                # "border": "1px solid blue",
            },
        )


def cloud_column(cloud_count: int = 1, cloud_seconds: int = 12):
    return rx.flex(
        *[Cloud(i).render() for i in range(cloud_count)],
        direction="column",
        spacing="7",
        style={
            "animation-name": "cloudscroll",
            "animation-duration": f"{cloud_count * cloud_seconds}s",
            "animation-timing-function": "linear",
            "width": "100%",
            # "border": "1px solid red",
        },
    )


@rx.page(route="/", title="The Changing of the Trees")
def landing() -> rx.Component:
    """The landing page."""
    return rx.box(
        background(),
        cloud_column(14),
        style={
            "overflow": "hidden",
            "width": "100vw",
            "height": "100vh",
        },
    )


app = rx.App(stylesheets=config.stylesheets)
