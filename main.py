#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
import sys
from lunar_python import Solar, JieQi
from wallpaper import set_wallpaper
import os

def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and PyInstaller) """
    if getattr(sys, 'frozen', False):
        # Running as bundled executable
        base_path = Path(sys.executable).parent
    else:
        # Running as script
        base_path = Path(__file__).parent

    return base_path / relative_path

def find_wallpaper_path(dir: str, jieqi: JieQi) -> str:
    if not dir or not jieqi:
        return ""
    for root, _, files in os.walk(dir):
        for file in files:
            if not file.startswith(".") and jieqi.toString() in file:
                return os.path.join(root, file)
    return ""


def main():
    wallpaper_dir = resource_path('二十四节气')
    lunar_date = Solar.fromDate(datetime.now()).getLunar()
    if not (jieqi := lunar_date.getCurrentJieQi()):
        jieqi = lunar_date.getPrevJieQi()
    wallpaper_path = find_wallpaper_path(wallpaper_dir, jieqi)
    if wallpaper_path:
        set_wallpaper(wallpaper_path)


if __name__ == "__main__":
    main()
