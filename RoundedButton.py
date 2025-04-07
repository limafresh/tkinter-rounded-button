"""
Version: 0.1.1
License: Unlicense
"""

from tkinter import Canvas


class RoundedButton(Canvas):
    def __init__(
        self,
        parent,
        width=150,
        height=30,
        text="RoundedButton",
        font=None,
        radius=13,
        bg_color="green",
        fg_color="white",
        command=None,
        cursor="hand2",
        **kwargs,
    ):
        Canvas.__init__(
            self,
            parent,
            width=width,
            height=height,
            bg=parent["bg"],
            highlightthickness=0,
            **kwargs,
        )

        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.radius = radius
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.command = command
        self.cursor = cursor

        self.delete("all")
        self._create_button()

        self.bind("<ButtonRelease-1>", self._on_release)

    def _create_button(self):
        r, w, h = self.radius, self.width, self.height
        self.create_arc(
            (0, 0, r * 2, r * 2),
            start=90,
            extent=90,
            fill=self.bg_color,
            outline=self.bg_color,
            tags="button",
        )
        self.create_arc(
            (w - 2 * r, 0, w, r * 2),
            start=0,
            extent=90,
            fill=self.bg_color,
            outline=self.bg_color,
            tags="button",
        )
        self.create_arc(
            (0, h - 2 * r, r * 2, h),
            start=180,
            extent=90,
            fill=self.bg_color,
            outline=self.bg_color,
            tags="button",
        )
        self.create_arc(
            (w - 2 * r, h - 2 * r, w, h),
            start=270,
            extent=90,
            fill=self.bg_color,
            outline=self.bg_color,
            tags="button",
        )

        self.create_rectangle(
            (r, 0, w - r, h), fill=self.bg_color, outline=self.bg_color, tags="button"
        )
        self.create_rectangle(
            (0, r, w, h - r), fill=self.bg_color, outline=self.bg_color, tags="button"
        )

        if self.font is None:
            self.create_text(
                w / 2, h / 2, text=self.text, fill=self.fg_color, tags="button"
            )
        elif isinstance(self.font, tuple):
            self.create_text(
                w / 2,
                h / 2,
                text=self.text,
                font=self.font,
                fill=self.fg_color,
                tags="button",
            )
        else:
            self.create_text(
                w / 2,
                h / 2,
                text=self.text,
                font=(None, self.font),
                fill=self.fg_color,
                tags="button",
            )

        self.configure(cursor=self.cursor)

    def _on_release(self, event):
        if self.command:
            self.command()

    def config(self, **kwargs):
        self.delete("button")
        if "width" in kwargs:
            self.width = kwargs["width"]
            self.configure(width=self.width)
        if "height" in kwargs:
            self.height = kwargs["height"]
            self.configure(height=self.height)
        if "text" in kwargs:
            self.text = kwargs["text"]
        if "font" in kwargs:
            self.font = kwargs["font"]
        if "radius" in kwargs:
            self.radius = kwargs["radius"]
        if "bg_color" in kwargs:
            self.bg_color = kwargs["bg_color"]
        if "fg_color" in kwargs:
            self.fg_color = kwargs["fg_color"]
        if "command" in kwargs:
            self.command = kwargs["command"]
        if "cursor" in kwargs:
            self.cursor = kwargs["cursor"]
        self._create_button()

    def cget(self, key):
        if key == "width":
            return self.width
        elif key == "height":
            return self.height
        elif key == "text":
            return self.text
        elif key == "font":
            return self.font
        elif key == "radius":
            return self.radius
        elif key == "bg_color":
            return self.bg_color
        elif key == "fg_color":
            return self.fg_color
        elif key == "command":
            return self.command
        elif key == "cursor":
            return self.cursor
        else:
            raise KeyError(f"Unknown option: '{key}'")
