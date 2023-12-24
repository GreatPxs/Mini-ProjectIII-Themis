# bug reproduction script for bug #2141 of tasks
#2141号bug涉及到设置页面中语言的修改，python脚本难以完成，可能需要手动复现。步骤如下：
#1.创建一些任务，直至排序界面出现“My Order”或者“我的顺序”选项；
#2.在设置-系统-语言设置中找到阿拉伯语或波斯语等非英语体系语言，设置为系统语言；
#3.回到tasks，选择My Order排序已经较为卡顿，退出重新进入时发生crash，无法打开。
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    d.app_start("de.rampro.activitydiary.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "de.rampro.activitydiary.debug":
            break
        time.sleep(2)
    wait()

    # click the Navigation
    out = d(className="android.widget.ImageButton", description="Open navigation").click()
    if not out:
        print("Success: press Navigation")
    wait()

    # click the Settings
    out = d(className="android.widget.CheckedTextView", text="Settings").click()
    if not out:
        print("Success: press Settings")
    wait()

    # scroll down the settings
    out = d(className="android.support.v7.widget.RecyclerView", resourceId="de.rampro.activitydiary.debug:id/recycler_view").swipe("up")
    if out:
        print("Success: Scroll down")
    wait()

    # scroll down the settings
    out = d(className="android.support.v7.widget.RecyclerView",
            resourceId="de.rampro.activitydiary.debug:id/recycler_view").swipe("up")
    if out:
        print("Success: scroll down")
    wait()

    # click Location Service
    out = d(className="android.widget.TextView", text="Location Service").click()
    if not out:
        print("Success: press Location Service")
    wait()

    # click Network
    out = d(className="android.widget.CheckedTextView", text="Network").click()
    if not out:
        print("Success: press Network")
    wait()

    # click Update period
    out = d(className="android.widget.TextView", text="Update period").click()
    if not out:
        print("Success: press update period")
    wait()

    # set the edittext to empty
    out = d(className="android.widget.EditText").set_text(text="")
    if out:
        print("Success: set text to empty")
    wait()

    # click Ok
    out = d(className="android.widget.Button", text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
