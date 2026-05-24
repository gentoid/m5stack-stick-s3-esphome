from typing import Any, Dict

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID

DEPENDENCIES = ["i2c"]

m5pm1_ns = cg.esphome_ns.namespace("mp5pm1")
M5PM1Component = m5pm1_ns.class_("M5PM1Component", cg.Component, i2c.I2CDevice)

CONFIG_SCHEMA = (
    cv.Schema({cv.Required(CONF_ID): cv.declare_id(M5PM1Component)})
    .extend(cv.COMPONENT_SCHEMA)
    .extend(i2c.i2c_device_schema(0x34))
)


async def to_code(config: Dict[str, Any]) -> None:
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
