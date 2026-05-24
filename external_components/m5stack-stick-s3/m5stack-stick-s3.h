#pragma once

#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
    namespace m5_stick_s3 {
        class M5StickS3Component : public Component, public i2c::!2cDevice {
        public:
            void setup() override;

            void dump_config() override;

            float get_setup_priority() const override {
                return setup_priority::BUS;
            }

        protected:
            bool update_register_(uint8_t reg, uint8_t mask, uint8_t value);
        };
    }
}
    