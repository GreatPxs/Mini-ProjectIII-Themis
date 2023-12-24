The link for Tasks-#2141 is https://github.com/tasks/tasks/issues/2141

The link for AntennaPod-#6311 is https://github.com/AntennaPod/AntennaPod/issues/6311

#2141号bug涉及到设置页面中语言的修改，python脚本难以完成，可能需要手动复现。步骤如下：
1.创建一些任务，直至排序界面出现“My Order”或者“我的顺序”选项；
2.在设置-系统-语言设置中找到阿拉伯语或波斯语等非英语体系语言，设置为系统语言；
3.回到tasks，选择My Order排序已经较为卡顿，退出重新进入时发生crash，无法打开。

#6120号bug的脚本运行不太顺利，可能与bug复现为概率问题有关，需要添加并播放含有连续章节的剧集，在播放界面点击“章节”或者“Chapter”按键，系统卡顿无反应，crash。
