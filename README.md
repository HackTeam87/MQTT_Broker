# MQTT_Broker Заметки
apt  install mosquitto mosquitto-clients -y \
pip install -r requirements.txt \
- client:
mosquitto_pub -h localhost -t userloc -m 1KM
- server:
mosquitto_sub -h learnlinux.golden.net.ua -t userloc -v