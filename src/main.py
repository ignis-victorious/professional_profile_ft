#  _________________________
#  Import LIBRARIES
import flet as ft
from flet import (
    Page,
    app,
    Container,
    Icon,
    TextField,
    Dropdown,
    Text,
    OutlinedButton,
    Column,
    Row,
    Divider,
    ResponsiveRow,
)
from datetime import datetime
import re
#  Import FILES
#  _________________________


class ProfileApp:
    def _init_(self) -> None:
        self.profile_data: dict[str, str | int | None] = {}

    def main(self, page: Page) -> None:
        page.title = "Profile Demo"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 20
        page.scroll = ft.ScrollMode.ALWAYS

        self.profile_pic = Container(
            content=Icon(name=ft.Icons.PERSON, size=80, color=ft.Colors.WHITE),
            width=120,
            height=120,
            bgcolor=ft.Colors.BLUE_400,
            border_radius=60,
            alignment=ft.alignment.center,
        )

        self.first_name = TextField(
            label="First Name",
            hint_text="Enter Your first name",
            prefix_icon=ft.Icons.PERSON,
            border_radius=10,
        )
        self.last_name = TextField(
            label="Last Name",
            hint_text="Enter Your last name",
            prefix_icon=ft.Icons.PERSON_OUTLINE,
            border_radius=10,
        )
        self.email = TextField(
            label="Email",
            hint_text="Enter Your Email name",
            prefix_icon=ft.Icons.EMAIL,
            border_radius=10,
        )
        self.phone = TextField(
            label="Phone Number",
            hint_text="Enter Your phone number",
            prefix_icon=ft.Icons.PHONE,
            border_radius=10,
            keyboard_type=ft.KeyboardType.PHONE,
        )

        self.birth_data = TextField(
            label="Birth Date",
            hint_text="DD/MM/YY",
            prefix_icon=ft.Icons.CALENDAR_TODAY,
            border_radius=10,
        )

        self.gender: Dropdown = Dropdown(
            label="Gender",
            hint_text="Select your Gender",
            options=[
                ft.dropdown.Option(key="Male"),
                ft.dropdown.Option(key="Female"),
                ft.dropdown.Option(key="Other"),
                ft.dropdown.Option(key="Prefer not to say"),
            ],
            border_radius=10,
        )

        self.occupation = TextField(
            label="Occupation",
            hint_text="Enter Your occupation",
            prefix_icon=ft.Icons.WORK,
            border_radius=10,
        )

        self.bio = TextField(
            label="Bio",
            hint_text="Tell us about ourself ... ",
            prefix_icon=ft.Icons.BIOTECH,
            border_radius=10,
            min_lines=3,
            max_lines=5,
            multiline=True,
        )

        self.country = Dropdown(
            label="Country",
            hint_text="Select your country",
            options=[
                ft.dropdown.Option(key="United Sates"),
                ft.dropdown.Option(key="United Kingdom"),
                ft.dropdown.Option(key="Canada"),
                ft.dropdown.Option(key="Iraq"),
                ft.dropdown.Option(key="Suriye"),
                ft.dropdown.Option(key="Australia"),
                ft.dropdown.Option(key="Germany"),
                ft.dropdown.Option(key="France"),
                ft.dropdown.Option(key="Iran"),
                ft.dropdown.Option(key="Japan"),
                ft.dropdown.Option(key="Saudi Arabia"),
                ft.dropdown.Option(key="Kuwait"),
                ft.dropdown.Option(key="Qatar"),
            ],
            border_radius=10,
        )
        self.status_message = Text(
            value="", color=ft.Colors.GREEN, size=14, weight=ft.FontWeight.BOLD
        )
        self.create_btn = OutlinedButton(
            text="Create Profile",
            icon=ft.Icons.SAVE,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
                padding=ft.padding.symmetric(horizontal=30, vertical=15),
            ),
            on_click=self.create_profile,
        )
        self.clear_btn = OutlinedButton(
            text="Clear Form",
            icon=ft.Icons.CLEAR,
            style=ft.ButtonStyle(
                color=ft.Colors.RED_400,
                padding=ft.padding.symmetric(horizontal=30, vertical=15),
            ),
            on_click=self.clear_form_func,
        )
        self.profile_display = Container(
            content=Text(value="Profile will appear here after creation...."),
            bgcolor=ft.Colors.GREY_300,
            border_radius=10,
            padding=20,
            visible=False,
        )

        page.add(
            Container(
                content=Column(
                    controls=[
                        Row(
                            controls=[
                                Icon(
                                    name=ft.Icons.ACCOUNT_CIRCLE,
                                    size=40,
                                    color=ft.Colors.BLUE_400,
                                ),
                                Text(
                                    value="Create Your Profile",
                                    size=32,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLUE_400,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        Divider(height=20, color=ft.Colors.TRANSPARENT),
                        Row(
                            controls=[self.profile_pic],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        #
                        Divider(height=20, color=ft.Colors.TRANSPARENT),
                        ResponsiveRow(
                            controls=[
                                Container(
                                    content=self.first_name, col={"sm": 12, "md": 6}
                                ),
                                Container(
                                    content=self.last_name, col={"sm": 12, "md": 6}
                                ),
                            ]
                        ),
                        ResponsiveRow(
                            controls=[
                                Container(content=self.email, col={"sm": 12, "md": 6}),
                                Container(content=self.phone, col={"sm": 12, "md": 6}),
                            ]
                        ),
                        ResponsiveRow(
                            controls=[
                                Container(
                                    content=self.birth_data, col={"sm": 12, "md": 6}
                                ),
                                Container(content=self.gender, col={"sm": 12, "md": 6}),
                                Container(
                                    content=self.country, col={"sm": 12, "md": 6}
                                ),
                            ]
                        ),
                        self.occupation,
                        self.bio,
                        self.status_message,
                        Row(
                            controls=[self.create_btn, self.clear_btn],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        Divider(height=20, color=ft.Colors.TRANSPARENT),
                        self.profile_display,
                    ],
                    spacing=15,
                ),
                padding=20,
            )
        )

    def validate_email(self, email: str) -> bool:
        pattern: str = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        return re.match(pattern=pattern, string=email) is not None

    def validate_date(self, date_str: str) -> bool:
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def create_profile(self, e: ft.ControlEvent) -> None:
        error: list[str] = []
        if not self.first_name.value:
            error.append("First name required")
        if not self.last_name.value:
            error.append(" required")
        if not self.email.value:
            error.append("email required")

        if self.birth_data.value and not self.validate_date(
            date_str=self.birth_data.value
        ):
            error.append("Invalid date format")
        if error:
            self.status_message.value = "Error:" + "".join(error)
            self.status_message.color = ft.Colors.RED
        else:
            self.profile_data = {
                "first_name": self.first_name.value,
                "last_name": self.last_name.value,
                "email": self.email.value,
                "phone": self.phone.value or "Not provided",
                "birth_date": self.birth_data.value,
                "gender": self.gender.value or "Not Specified",
                "occupation": self.occupation.value or "Not Specified",
                "bio": self.bio.value or "No bio provided",
                "country": self.country.value or "Not specefied",
            }
            self.status_message.value = "Profile Created succefully!"
            self.status_message.color = ft.Colors.GREEN

            self.profile_displays()
        e.page.update()

    def profile_displays(self):
        profile_content: Column = Column(
            controls=[
                Text(
                    value="Profile Summary",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="blue",
                ),
                Divider(),
                Row(
                    controls=[
                        Text(value="Name:", weight=ft.FontWeight.BOLD, width=120),
                        Text(
                            value=f"{self.profile_data['first_name']}{self.profile_data['last_name']}"
                        ),
                    ]
                ),
                Row(
                    controls=[
                        Text(value="Email:", weight=ft.FontWeight.BOLD, width=120),
                        Text(value=str(self.profile_data["email"])),
                    ]
                ),
                Row(
                    controls=[
                        Text(value="Phone:", weight=ft.FontWeight.BOLD, width=120),
                        Text(value=str(self.profile_data["phone"])),
                    ]
                ),
                Row(
                    controls=[
                        Text(value="Birth Date:", weight=ft.FontWeight.BOLD, width=120),
                        Text(value=str(self.profile_data["birth_date"])),
                    ]
                ),
                Row(
                    controls=[
                        Text(value="Gender:", weight=ft.FontWeight.BOLD, width=120),
                        Text(value=str(self.profile_data["gender"])),
                    ]
                ),
                Row(
                    controls=[
                        Text(value="Country:", weight=ft.FontWeight.BOLD, width=120),
                        Text(value=str(self.profile_data["country"])),
                    ]
                ),
                Row(
                    controls=[
                        Text(value="Occupation:", weight=ft.FontWeight.BOLD, width=120),
                        Text(value=str(self.profile_data["occupation"])),
                    ]
                ),
                Column(
                    controls=[
                        Text(value="bio:", weight=ft.FontWeight.BOLD),
                        Text(value=str(self.profile_data["bio"]), max_lines=None),
                    ],
                    spacing=5,
                ),
            ]
        )
        self.profile_display.content = profile_content
        self.profile_display.visible = True

    def clear_form_func(self, e: ft.ControlEvent) -> None:
        self.first_name.value = ""
        self.last_name.value = ""
        self.email.value = ""
        self.phone.value = ""
        self.birth_data.value = ""
        self.gender.value = None
        self.occupation.value = ""
        self.bio.value = ""
        self.country.value = None
        self.status_message.value = ""
        self.profile_display.visible = False

        e.page.update()


def main(page: Page) -> None:
    apps: ProfileApp = ProfileApp()
    apps.main(page=page)


if __name__ == "__main__":
    app(target=main)


#  _________________________
#  Import LIBRARIES
#  Import FILES
#  _________________________
