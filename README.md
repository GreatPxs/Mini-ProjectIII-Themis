The link for Tasks-#2141 is https://github.com/tasks/tasks/issues/2141

The link for AntennaPod-#6311 is https://github.com/AntennaPod/AntennaPod/issues/6120

#6311号bug涉及到设置页面中语言的修改，python脚本难以完成，可能需要手动复现。步骤如下：
1.创建一些任务，直至排序界面出现“My Order”或者“我的顺序”选项；
2.在设置-系统-语言设置中找到阿拉伯语或波斯语等非英语体系语言，设置为系统语言；
3.回到tasks，选择My Order排序已经较为卡顿，退出重新进入时发生crash，无法打开。
