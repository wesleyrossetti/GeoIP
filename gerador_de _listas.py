import maxminddb
import os

# Defina o caminho do seu GeoLite2
mmdb_path = "GeoLite2-Country.mmdb"
output_dir = r'GeoIP_Paises'  # Pasta onde criar os arquivos

# Criar pasta de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Abrir o MMDB
reader = maxminddb.open_database(mmdb_path)

# Dicionário para guardar IPs por país
country_ips = {}

# Vamos percorrer todas as redes armazenadas
for network, record in reader:
    country_name = None
    try:
        country_name = record['country']['names']['en']
    except KeyError:
        continue  # Se não tiver país, pula

    if country_name not in country_ips:
        country_ips[country_name] = []

    country_ips[country_name].append(str(network))

reader.close()

# Agora gerar os arquivos
for country, ips in country_ips.items():
    # Remover caracteres inválidos de nomes de arquivos
    safe_country = "".join(c for c in country if c.isalnum() or c in (" ", "_")).rstrip()
    output_file = os.path.join(output_dir, f"{safe_country}.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        for ip in ips:
            f.write(ip + "\n")

print(f"Arquivos gerados em: {output_dir}")
