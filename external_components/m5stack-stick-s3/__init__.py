from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, cast

import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.loader as loader
from esphome.components import i2c
from esphome.const import (
    CONF_FREQUENCY,
    CONF_I2C_ID,
    CONF_ID,
    CONF_SCAN,
    CONF_SCL,
    CONF_SDA,
)
from esphome.core import CORE, ConfigType

if TYPE_CHECKING:
    import m5pm1 as m5pm1_module


AUTO_LOAD = ["i2c", "m5pm1"]
DOMAIN = "m5stack_stick_s3"


@dataclass
class StickS3Data:
    bus_initialized = False


def _get_data() -> StickS3Data:
    if DOMAIN not in CORE.data:
        CORE.data[DOMAIN] = StickS3Data()
    return CORE.data[DOMAIN]


CONFIG_SCHEMA = cv.Schema({cv.GenerateID(): cv.declare_id(cg.Component)}).extend(
    cv.COMPONENT_SCHEMA
)


async def to_code(config: Dict[str, Any]) -> None:
    data = _get_data()

    if data.bus_initialized:
        return

    i2c_bus_id = "global_i2c_bus"
    pm1_id = "m5_power_ic"

    i2c_config = {
        CONF_ID: cv.declare_id(i2c.I2CBus)(i2c_bus_id),
        CONF_SDA: 47,
        CONF_SCL: 48,
        CONF_FREQUENCY: 100_000,
        CONF_SCAN: True,
    }

    if CORE.config is None:
        CORE.config = ConfigType()

    if "i2c" not in CORE.config:
        CORE.config["i2c"] = []

    i2c_list = cast(List[Dict[str, Any]], CORE.config["i2c"])
    i2c_list.append(i2c_config)

    pm1_config = {
        CONF_ID: cv.declare_id(cg.MockObj)(pm1_id),
        CONF_I2C_ID: cv.declare_id(i2c.I2CBus)(i2c_bus_id),
    }

    m5pm1_manifest = loader.get_component("m5pm1")
    if m5pm1_manifest is None:
        return

    if not TYPE_CHECKING:
        m5pm1_module = m5pm1_manifest.module

    if m5pm1_module is None:
        return

    await m5pm1_module.to_code(pm1_config)

    data.bus_initialized = True
