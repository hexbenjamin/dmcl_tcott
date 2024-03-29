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
        self.image: str = f"clouds/cloud_{str(self.index).zfill(2)}.png"
        self.nudge = "-33%" if self.index % 2 == 0 else "33%"

    def render(self) -> rx.Component:
        return rx.image(
            src=self.image,
            style={
                "opacity": "0.5",
                "width": "50vw",
                "height": "auto",
                "transform": f"translateX({self.nudge})",
            },
        )


def cloud_column(cloud_count: int = 1):
    return rx.flex(
        *[Cloud(i).render() for i in range(cloud_count)],
        direction="column",
    )


@rx.page(route="/", title="The Changing of the Trees")
def landing() -> rx.Component:
    """The landing page."""
    cloud1 = Cloud(1)
    return rx.container(
        background(),
        cloud_column(3),
        class_name="full-screen",
    )


app = rx.App(stylesheets=config.stylesheets)
