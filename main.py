#!/usr/bin/env python3

from datetime import datetime
from lunar_python import Solar, JieQi
from wallpaper import set_wallpaper
import os


def find_wallpaper_path(dir: str, jieqi: JieQi) -> str:
    if not dir or not jieqi:
        return ""
    for root, _, files in os.walk(wallpaper_dir):
        for file in files:
            if not file.startswith(".") and jieqi.toString() in file:
                return os.path.join(root, file)
    return ""


def main():
    wallpaper_dir = os.path.join(os.path.dirname(__file__), '二十四节气')
    lunar_date = Solar.fromDate(datetime.now()).getLunar()
    if not (jieqi := lunar_date.getCurrentJieQi()):
        jieqi = lunar_date.getPrevJieQi()
    wallpaper_path = find_wallpaper_path(wallpaper_dir, jieqi)
    if wallpaper_path:
        set_wallpaper(wallpaper_path)


if __name__ == "__main__":
    main()
