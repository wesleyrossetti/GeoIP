import geoip2.database
from collections import defaultdict

# Caminho para seu arquivo mmdb
mmdb_path = "GeoLite2-Country.mmdb"

# Lista de IPs que você quer consultar (pode ser IPs públicos, ranges ou logs)
ips = [
    '8.8.8.8',
    '1.1.1.1',
    '201.48.0.1',
    '91.198.174.192',
    '210.0.0.1',
    '213.180.204.3',
    '45.33.32.156',
    '177.0.0.1',
    '2.16.0.0',
    '23.45.67.89'
]

# Abrir o banco
reader = geoip2.database.Reader(mmdb_path)

# Agrupar IPs por país
countries = defaultdict(list)

for ip in ips:
    try:
        response = reader.country(ip)
        country_name = response.country.name or "Unknown"
        countries[country_name].append(ip)
    except Exception:
        countries["Unknown"].append(ip)

reader.close()

# Salvar em TXT
with open('resultado_paises.txt', 'w', encoding='utf-8') as f:
    for country, ip_list in countries.items():
        f.write(f"País: {country}\n")
        for ip in ip_list:
            f.write(f"  - {ip}\n")
        f.write("\n")

print("Arquivo 'resultado_paises.txt' gerado com sucesso!")
