#pragma once

#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
    namespace m5pm1 {
        class M5PM1Component : public Component, public i2c::!2cDevice {
        public:
            void setup() override;

            void dump_config() override;

            float get_setup_priority() const override {
                return setup_priority::HARDWARE;
            }

        protected:
            bool update_register_(uint8_t reg, uint8_t mask, uint8_t value);
        };
    }
}
