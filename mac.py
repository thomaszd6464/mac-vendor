# suscribete! https://www.youtube.com/@hack-redes
import sys
import requests

def get_mac_vendor(mac_address):
    # URL de la API
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        # Realizar la solicitud a la API
        response = requests.get(url)

        # Comprobar el estado de la respuesta
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Error: No encontrado"
    except Exception as e:
        return f"Error al hacer la solicitud: {str(e)}"

def print_table(data):
    # Calcular el ancho de las columnas
    mac_width = max(len(row[0]) for row in data) + 2
    vendor_width = max(len(row[1]) for row in data) + 2

    # Imprimir la cabecera
    print(f"{'Dirección MAC'.ljust(mac_width)} | {'Fabricante'.ljust(vendor_width)}")
    print(f"{'-' * mac_width} + {'-' * vendor_width}")

    # Imprimir cada fila de datos
    for row in data:
        print(f"{row[0].ljust(mac_width)} | {row[1].ljust(vendor_width)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python mac.py <direcciones_mac_coma_separadas>")
        sys.exit(1)

    mac_addresses = sys.argv[1].split(",")  # Dividir las direcciones MAC por coma
    results = []

    for mac in mac_addresses:
        mac = mac.strip()  # Eliminar espacios en blanco adicionales
        vendor = get_mac_vendor(mac)
        results.append([mac, vendor])

    # Mostrar los resultados en un formato de tabla
    print_table(results)

