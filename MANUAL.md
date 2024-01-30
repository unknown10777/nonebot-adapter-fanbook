# Fanbook Adapter 使用指南

**此适配器还在施工中，遇到问题请尽快反馈！**

## 配置 NoneBot

本项目仅为 Nonebot 适配器插件，要搭建 Bot 请先阅读 [Nonebot2 文档](https://v2.nonebot.dev/)

以下内容作为对于 Nonebot 文档的 `driver` 参数和 `adapter` 部分的扩充

## 安装 adapter

请使用 pip 或项目包管理工具进行安装

```shell
pip install nonebot-adapter-fanbook
```

## 配置 Fanbook Bot

### 申请一个 Fanbook 机器人

首先你需要注册 [Fanbook](https://fanbook.idreamsky.com/) 帐号，然后前往[Fanbook 开发者平台](https://open.fanbook.mobi/developers/manage/app)创建一个应用，点击刚刚创建的应用，在左侧边栏寻找机器人，点击创建。创建后需谨慎阅读菜单内所有选项和开关。该方法于2024年1月30日验证有效。

获取流程：应用管理 - 创建应用 - 填入应用名称 - 选择刚创建的应用 - 左侧边栏寻找机器人 - 机器人 - 创建机器人 - 填入机器人的介绍 - 上传图片 - 按需选择权限 - 确认创建 - 复制机器人 Token

本文将以 `<token>` 代替 **机器人的** Token。

本文以该token举例:

`lx6sXzUr7sfuf7`

将这个 token 填入 NoneBot 的`env`文件：

```dotenv
fanbook_bots =[{"token": "lx6sXzUr7sfuf7"}]
```

## 配置驱动器

NoneBot 默认的驱动器为 FastAPI，它是一个服务端类型驱动器（ReverseDriver），而 Fanbook 适配器至少需要一个客户端类型驱动器（ForwardDriver），所以你需要额外安装其他驱动器。

目前推荐 httpx 客户端类型驱动器，你可以使用 nb-cli 进行安装。

```shell
nb driver install httpx
```

别忘了在环境文件中写入配置：

```dotenv
driver=~httpx+~websockets
```

## 第一次对话

```python
import nonebot
from nonebot.adapters.fanbook import Adapter as FanbookAdapter

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(FanbookAdapter)

nonebot.load_builtin_plugins("echo")

nonebot.run()
```

现在，你可以私聊自己的 Fanbook Bot `/echo hello world`，不出意外的话，它将回复你 `hello world`。(如果在频道内请@bot发送)

## 调用 API

（感谢 @DogAddan @ssttkkl 的贡献）

通过调用bot实例方法的形式可以调用 Fanbook 的所有API。

你可以在[Fanbook 开发者平台](https://https://open.fanbook.mobi/document/manage/doc)查看所有的API。API对应方法名参见[源码文件](https://github.com/unknown10777/nonebot-adapter-fanbook/blob/master/nonebot/adapters/Fanbook/api/client.pyi)。

对于`POST asset/create`接口（上传文件/图片），你还可以直接调用`bot.upload_file(file)`方法。
