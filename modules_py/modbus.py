from pymodbus.client import ModbusTcpClient

def _modbus_connect():
    client_link = ModbusTcpClient(
        host='192.168.4.176',  # IP-адрес устройства
        port=502,  # Стандартный порт Modbus TCP
        timeout=3,  # Таймаут в секундах
        retries=3  # Количество попыток переподключения
    )
    return  client_link

def _modbus_read(client_link):
    if client_link.connect():
        print("Успешное подключение modbus")
    result = client_link.read_discrete_inputs(
        address=0,  # Начальный адрес
        count=8,  # Количество битов (8 bits)
        device_id=1  # ID устройства
    )

    if not result.isError():
        bits = result.bits[:8]
        print(f"Input bits: {bits}")
        print("Состояние input bits:")
        for i, bit in enumerate(bits):
            print(f"Bit {i}: {'ON' if bit else 'OFF'}")
