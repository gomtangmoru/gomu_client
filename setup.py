from cx_Freeze import setup, Executable

build_options = {
    "packages": ["tkinter", "logging", "shit"],
    "excludes": [],
    "includes": [
        "shit.jjampu",
        "shit.moru",
        "shit.use_potato",
        "shit.wireguard",

    ]
}

executables = [
    Executable(
        "main.py",
        base="Win32GUI",
        target_name="GOMUSTORAGE.exe",
    )
]

setup(
    name="MyApp",
    version="1.0",
    options={"build_exe": build_options},
    executables=executables,
)