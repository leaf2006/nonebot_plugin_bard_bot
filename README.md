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

具体方法参看本文档


