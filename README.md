# 由于Google Gimini的发布，本项目不再维护。但是其作为我在nonebot2学习道路上的第一个小项目，对我的影响深远.

# nonebot_plugin_bard_bot
一个非常简单但是很可用的使得在QQ中可以使用Google Bard的插件，基于nonebot2

## Required

- Python >= 3.8（不然你nonebot2都运行不起来）
- 知道如何科学上网（Google Bard国内用不了）
- 拥有Google账号（Google Bard需要登录Google账号）

## Getting started

使用方式如下：

* #### 使用pip安装

在你的nonebot机器人目录下使用以下命令：

```sh
pip3 install nonebot-plugin-bard-bot
```

如果你使用的是虚拟环境，**请切换至虚拟环境安装，不然无法使用**

```sh
cd .venv/bin # 具体看你的.venv文件在哪
./pip3 install nonebot-plugin-bard-bot
```

然后在机器人目录下的**pyproject.toml**文件中添加以下语句

```toml
... # 此处省略其他内容
plugins = ["你安装的其他插件...", "nonebot_plugin_bard_bot"]
... # 此处省略其他内容
```

## 使用

使用本机器人首先你要知道如何使用Google Bard。因为本机器人基于bardapi库，需要获取cookies中的**Secure-1PSID，Secure-1PSIDTS和Secure-1PSIDCC**后才能使用

然后，请打开.**env**文件进行配置，在文件中写入以下语句：

```
COOKIE_DICT={
    "__Secure-1PSID": "Your __Secure-1PSID",
    "__Secure-1PSIDTS": "Your __Secure-1PSIDTS",
    "__Secure-1PSIDCC": "Your __Secure-1PSIDCC"
}
```

随后启动机器人，使用`/bard [空格] 问题`来对Google Bard询问，Google Bard会做出回答，具体思考时间取决于你的网速。

