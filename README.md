# GeoIP — listas de IPs por país

Gera uma lista de redes (CIDR) para cada país a partir do banco **GeoLite2-Country** da MaxMind
e publica os arquivos em um bucket da Cloudflare R2, prontos para uso em firewalls
(pfSense, OPNsense, MikroTik, iptables/ipset etc.).

As listas são atualizadas automaticamente **toda segunda-feira**.

## Como usar

Cada país tem um arquivo `.txt` com uma rede por linha (IPv4 e IPv6):

```
https://listaip.wmanti.com.br/GeoIP-Paises/<País>.txt
```

Exemplo:

```bash
curl https://listaip.wmanti.com.br/GeoIP-Paises/Brazil.txt
```

```
1.178.32.0/20
1.178.95.0/24
2.16.0.0/24
...
```

Regras para o nome do arquivo:

- O nome é o nome do país **em inglês**, como no GeoLite2 (`Brazil`, `United States`, `Germany`).
- Espaços viram `%20` na URL: `https://listaip.wmanti.com.br/GeoIP-Paises/United%20States.txt`.
- Caracteres que não são letra, número, espaço ou `_` são removidos: `Guinea-Bissau` vira `GuineaBissau`,
  `Timor-Leste` vira `TimorLeste`.
- A lista completa dos nomes está em [resultado_paises.txt](resultado_paises.txt).
- A raiz do domínio não lista os arquivos (retorna 404). Use sempre o caminho completo.

### pfSense / OPNsense

1. **Firewall → Aliases → Add**.
2. Tipo: **URL Table (IPs)**.
3. URL: `https://listaip.wmanti.com.br/GeoIP-Paises/Brazil.txt`.
4. Frequência de atualização: **1 dia** (as listas mudam no máximo uma vez por semana).
5. Use o alias nas regras de firewall (bloquear ou permitir o país).

Para vários países, crie um alias por país e agrupe-os em um alias do tipo **Network(s)**.

### Linux (ipset)

```bash
ipset create brasil hash:net
curl -s https://listaip.wmanti.com.br/GeoIP-Paises/Brazil.txt | grep -v ':' | while read net; do
  ipset add brasil "$net"
done
iptables -A INPUT -m set --match-set brasil src -j ACCEPT
```

O `grep -v ':'` remove as redes IPv6, que precisam de um set `family inet6` separado.

## Como funciona

```
GitHub Actions (toda segunda)
   │
   ├─ generate: baixa o GeoLite2-Country (MaxMind) e roda gerador_de_listas.py
   │            → pasta GeoIP_Paises/ com um .txt por país
   │
   └─ upload:   envia os arquivos para o bucket R2 em GeoIP-Paises/
                         │
                         └─ servidos por https://listaip.wmanti.com.br (domínio do bucket)
```

O workflow está em [.github/workflows/geoip.yml](.github/workflows/geoip.yml).

### Executar manualmente

Na aba **Actions** do repositório, selecione **GeoIP → Run workflow**.
Ele também roda sozinho toda segunda-feira às 06:00 UTC (03:00 em Brasília).

> O GitHub desativa workflows agendados em repositórios sem atividade por 60 dias.
> Se isso acontecer, reative em **Actions → GeoIP → Enable workflow**.

## Configuração

### Secrets do GitHub

Em **Settings → Secrets and variables → Actions**:

| Secret | Descrição |
|---|---|
| `MAXMIND_LICENSE_KEY` | Chave de licença da conta MaxMind (GeoLite2) |
| `R2_ACCOUNT_ID` | ID da conta Cloudflare |
| `R2_ACCESS_KEY_ID` | Access Key do token S3 do R2 |
| `R2_SECRET_ACCESS_KEY` | Secret do token S3 do R2 |
| `R2_BUCKET` | Nome do bucket (`geoip`) |

O token S3 do R2 precisa de permissão de escrita no bucket.

### Cloudflare R2

- O bucket tem um **Custom Domain** (`listaip.wmanti.com.br`) para acesso público de leitura.
- O endpoint S3 (`<account>.r2.cloudflarestorage.com`) é privado e usado apenas pelo upload.
- Recomendado: criar uma Cache Rule para o domínio, com Edge TTL de algumas horas.

### Desenvolvimento local

```bash
pip install -r requirements.txt
# coloque GeoLite2-Country.mmdb na raiz do projeto
python gerador_de_listas.py        # gera a pasta GeoIP_Paises/
```

Para testar um IP localmente, use `consultar ips localidade de ips.py`.

Arquivos sensíveis (`.env`, `*.mmdb`) estão no [.gitignore](.gitignore).

## Dependências

Versões fixadas em `requirements.txt` (geração) e `requirements-upload.txt` (upload).
O Dependabot abre PRs semanais para atualizá-las, assim como os actions do workflow.

## Licença dos dados

Os dados vêm do GeoLite2 da MaxMind, sob a
[licença GeoLite2 EULA](https://www.maxmind.com/en/geolite2/eula).
Este produto inclui dados GeoLite2 criados pela MaxMind, disponíveis em https://www.maxmind.com.
