from typing import List, Optional

from pydantic import Field, BaseModel


class BotConfig(BaseModel):
    """
    Fanbook Bot 配置类
    :配置项:
      - ``token``: Fanbook 开发者中心获得
    """

    token: str

    class Config:
        extra = "ignore"
        allow_population_by_field_name = True


class Config(BaseModel):
    """
    Fanbook 配置类

    :配置项:

      - ``Fanbook_bots`` : Fanbook 开发者中心获得
      - ``compress`` : 是否开启压缩, 默认为 False

    :示例:

    .. code-block:: default

        bots = [{"token": "token1"}, {"token": "token2"}]
    """

    Fanbook_bots: List["BotConfig"] = Field(default_factory=list)
    compress: Optional[bool] = Field(default=False)

    class Config:
        extra = "allow"
        allow_population_by_field_name = True
