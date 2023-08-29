import json
import nonebot
from anyio import get_current_task
from nonebot.rule import to_me
from pathlib import Path
from nonebot.plugin import PluginMetadata #插件发布用
from .config import Config
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from bardapi import BardCookies

input = on_command("bard")

@input.handle()
async def handle_function(args: Message = CommandArg()):
    if str := args.extract_plain_text():
        await input.send("稍等一下，让我思考一会哦...")
        config = nonebot.get_driver().config
        cookie_dict = config.cookie_dict
        cookie_dict = eval(cookie_dict)
        bard = BardCookies(cookie_dict=cookie_dict)
        answer = bard.get_answer(str)
        await input.finish(answer['content'])

    else:
        await input.finish("请在/bard后输入你的问题哦")


# 插件发布页

__plugin_meta__ = PluginMetadata(
    name="bard_bot",
    description="一个非常简单但是很可用的使得在QQ中可以使用Google Bard的插件",
    usage="""
    使用/bard [文本] 对Google Bard提出问题进行交互
    但请在使用前提前在.env文件中配置好Secure-1PSID，Secure-1PSIDTS和Secure-1PSIDCC
    """,


    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。


    homepage="{项目主页}",
    # 发布必填。


    config=Config,
    # 插件配置项类，如无需配置可不填写。


    supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
)
