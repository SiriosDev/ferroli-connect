"""Constants for the Ferroli Connect integration."""
from __future__ import annotations

DOMAIN = "ferroli_connect"
PLATFORMS = ["climate", "sensor"]

CONF_CLIENT_ID = "client_id"
CONF_PASSWORD = "password"
CONF_OWNER_SLUG = "owner_slug"
CONF_BRIDGE_ENABLED = "bridge_enabled"
CONF_BRIDGE_HOST = "bridge_host"
CONF_BRIDGE_PORT = "bridge_port"

DEFAULT_BRIDGE_HOST = "18.158.187.64"
# MQTT over TLS. The broker's certificate is checked against BRIDGE_TLS_HOSTNAME:
# we connect by IP because that hostname is redirected to Home Assistant locally.
DEFAULT_BRIDGE_PORT = 8883
BRIDGE_TLS_HOSTNAME = "eu-mqtt.topband-cloud.com"

# dispatcher signal (format with entry_id)
SIGNAL_UPDATE = "ferroli_connect_update_{}"

# device -> cloud (relayed local broker -> Topband)
OUT_TOPICS = ["/dev_realt/#", "/dev2app/#", "/dev2ser_req_info/#"]
# cloud -> device (relayed Topband -> local broker); only this device's topics
# are subscribed and relayed, see FerroliRuntime._relay_allowed
IN_TOPIC_KINDS = ("app2dev", "ser2dev_noti", "ser2dev_res")
