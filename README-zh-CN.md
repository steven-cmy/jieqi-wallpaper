# 节气壁纸

[![Build binaries](https://github.com/steven-cmy/jieqi-wallpaper/actions/workflows/build.yml/badge.svg)](https://github.com/steven-cmy/jieqi-wallpaper/actions/workflows/build.yml)

[ENGLISH](README.md)|中文

节气壁纸是一个提供基于中国传统二十四节气美丽壁纸的项目。

## 功能特色

- 为每个节气提供高质量壁纸。
- 简单易用且便于自定义。

## 使用方法

1. 使用使用预构建的可执行文件:

    1. 前往 [发布页面](https://github.com/steven-cmy/jieqi-wallpaper/releases)

    2. 根据自己的操作系统下载压缩包

    3. 解压并运行

2. 直接运行脚本
   1. 克隆此仓库：

       ```bash
       git clone https://github.com/yourusername/jieqi-wallpaper.git
       ```

   2. 进入项目目录：

       ```bash
       cd jieqi-wallpaper
       ```

   3. 安装依赖：

       ```bash
       pip install -r requirements.txt
       ```

   4. 运行脚本：

       ```bash
       python3 main.py
       ```

### 支持自定义壁纸

> [!IMPORTANT]  
> 请确保自定义壁纸文件名中包含中文的节气名称。

替换二十四节气文件夹中的图像。

## 贡献

欢迎贡献代码！请 fork 本仓库并提交 PR。

## 许可证

本项目采用 [MIT License](LICENSE) 许可证。

## 致谢

灵感来源于中国传统文化之美。

wallpaper.py 文件来自 [1j01/textual-paint](https://github.com/1j01/textual-paint/blob/main/src/textual_paint/wallpaper.py)，遵循 MIT 许可证。
