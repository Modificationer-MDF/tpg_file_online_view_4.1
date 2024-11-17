# -*- coding: utf-8 -*-
import sys
import time as t
import random
import os

def char(string, time):
    if time == None:
        time = 0.05
    time = float(time)
    for i in string:
        print(i, end="", flush=True)
        t.sleep(time)
    input()

def keyin(string, time, holder):
    if time == None:
        time = 0.05
    time = float(time)
    for i in string:
        print(i, end="", flush=True)
        t.sleep(time)
    print()
    a = input(holder)
    return a

def main():
    os.system("@echo off")
    os.system("title 你好！")
    os.system("cls")
    os.system("color b")
    char("""
        你好！欢迎运行 The Play Games 0.9 中的第 9 个文件！
        当你坐在一个比较偏僻的位置时，你是否想要检查会不会有人发现这个文件？
        没问题！本程序将为你提供像样的程序。

        按任意键继续……
    """, 0.05)
    os.system("title 首先")
    os.system("cls")
    os.system("color 1")
    char("""
        首先，我们需要结束老师的控制。
        假设学校正在使用 “极域电子课堂”。
        接下来我将给你几种选择。
    """, 0.03)
    print()
    res = keyin("""
        1 - 使用 taskkill 命令结束进程；
        2 - 使用 resmon.exe 结束 / 挂起（暂停）进程；
        3 - 我将为你返回 StudentMain.exe 的 tasklist 信息，并打开 CMD.exe；
        4 - 打开 regedit.exe 查看 HKEY_LOCAL_MACHINE\\SOFTWARE\\TopSomain\\e-Learning Class Standard\\1.00\\uninstallpasswd（大概率会失败）。
    """, 0.03, "请输入你的选择：")
    match res:
        case "1":
            os.system("taskkill /f /im StudentMain.exe")
            os.system("cls")
            os.system("color 4")
            char("你选择了使用 taskkill 命令结束进程。", 0.06)
        case "2":
            os.system("resmon.exe")
            os.system("cls")
            os.system("color 3")
            char("请在 resmon.exe 中选择结束 / 挂起（暂停） StudentMain.exe 的进程。", 0.03)
        case "3":
            os.system("tasklist | findstr StudentMain.exe")
            os.system("cmd.exe")
            os.system("cls")
            os.system("color 3")
            char("请尽快在 CMD 中结束 StudentMain.exe 的进程。", 0.03)
        case "4":
            os.system("regedit.exe")
            os.system("cls")
            os.system("color 3")
            char("请在 regedit.exe 中查看 HKEY_LOCAL_MACHINE\\SOFTWARE\\TopSomain\\e-Learning Class Standard\\1.00\\uninstallpasswd。", 0.03)
        case _:
            os.system("cls")
            os.system("color 4")
            char("你没有选择任何选项。", 0.06)
    os.system("pause")

main()