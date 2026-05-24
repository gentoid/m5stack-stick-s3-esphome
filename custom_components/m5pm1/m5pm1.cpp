#include "m5pm1.h"
#include "esphome/core/log.h"

namespace esphome::m5pm1 {
    static const char *const TAG = "m5pm1";

    void M5PM1Component::setup() {
        ESP_LOGI(TAG, "Initializing M5PM1 Power Management IC...");
    }

    void M5PM1Component::dump_config() {
        ESP_LOGCONFIG(TAG, "M5PM1:");
        LOG_I2C_DEVICE(this);
    }
}
