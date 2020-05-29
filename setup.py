import cx_Freeze

executables = [cx_Freeze.Executable("game_proj.py")]

cx_Freeze.setup(
    name="The Burninator",
    options={"build_exe": {"packages":["pygame"],
                        "include_files":["music/", "hero/", "tree/", "george/", "dragon/", "bg_bg1.png", "castle.gif", "classes.py", "grassbg.png", "testbg.jpg"]}},
    executables = executables

    )

