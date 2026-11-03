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

## Endpoints disponíveis

Base: `https://listaip.wmanti.com.br/GeoIP-Paises/`

Todos os **250 endpoints** abaixo foram testados em 03/11/2026 e responderam **HTTP 200** com conteúdo
(total de 1.063.785 redes). A coluna *Redes* é a quantidade de linhas (CIDRs) de cada lista na data do teste e muda a cada atualização.

> **User-Agent:** a Cloudflare responde **403** ao User-Agent padrão do `urllib` do Python. O `curl` (testado)
> funciona normalmente. Em scripts Python, envie um cabeçalho `User-Agent`. Se o firewall receber 403 ao
> baixar a lista, esse é o motivo.

<details>
<summary>Ver os 250 endpoints</summary>

| País | Endpoint | Redes |
|---|---|---:|
| Afghanistan | [Afghanistan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Afghanistan.txt) | 722 |
| Albania | [Albania.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Albania.txt) | 1.479 |
| Algeria | [Algeria.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Algeria.txt) | 407 |
| American Samoa | [American%20Samoa.txt](https://listaip.wmanti.com.br/GeoIP-Paises/American%20Samoa.txt) | 437 |
| Andorra | [Andorra.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Andorra.txt) | 378 |
| Angola | [Angola.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Angola.txt) | 592 |
| Anguilla | [Anguilla.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Anguilla.txt) | 146 |
| Antarctica | [Antarctica.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Antarctica.txt) | 800 |
| Antigua and Barbuda | [Antigua%20and%20Barbuda.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Antigua%20and%20Barbuda.txt) | 264 |
| Argentina | [Argentina.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Argentina.txt) | 5.574 |
| Armenia | [Armenia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Armenia.txt) | 774 |
| Aruba | [Aruba.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Aruba.txt) | 159 |
| Australia | [Australia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Australia.txt) | 18.460 |
| Austria | [Austria.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Austria.txt) | 6.938 |
| Azerbaijan | [Azerbaijan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Azerbaijan.txt) | 681 |
| Bahamas | [Bahamas.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bahamas.txt) | 278 |
| Bahrain | [Bahrain.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bahrain.txt) | 456 |
| Bangladesh | [Bangladesh.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bangladesh.txt) | 4.818 |
| Barbados | [Barbados.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Barbados.txt) | 278 |
| Belarus | [Belarus.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Belarus.txt) | 775 |
| Belgium | [Belgium.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Belgium.txt) | 7.491 |
| Belize | [Belize.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Belize.txt) | 301 |
| Benin | [Benin.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Benin.txt) | 185 |
| Bermuda | [Bermuda.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bermuda.txt) | 432 |
| Bhutan | [Bhutan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bhutan.txt) | 255 |
| Bolivia | [Bolivia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bolivia.txt) | 597 |
| Bonaire Sint Eustatius and Saba | [Bonaire%20Sint%20Eustatius%20and%20Saba.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bonaire%20Sint%20Eustatius%20and%20Saba.txt) | 114 |
| Bosnia and Herzegovina | [Bosnia%20and%20Herzegovina.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bosnia%20and%20Herzegovina.txt) | 457 |
| Botswana | [Botswana.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Botswana.txt) | 232 |
| Bouvet Island | [Bouvet%20Island.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bouvet%20Island.txt) | 38 |
| Brazil | [Brazil.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Brazil.txt) | 24.216 |
| British Indian Ocean Territory | [British%20Indian%20Ocean%20Territory.txt](https://listaip.wmanti.com.br/GeoIP-Paises/British%20Indian%20Ocean%20Territory.txt) | 102 |
| British Virgin Islands | [British%20Virgin%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/British%20Virgin%20Islands.txt) | 582 |
| Brunei | [Brunei.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Brunei.txt) | 192 |
| Bulgaria | [Bulgaria.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Bulgaria.txt) | 3.250 |
| Burkina Faso | [Burkina%20Faso.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Burkina%20Faso.txt) | 248 |
| Burundi | [Burundi.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Burundi.txt) | 132 |
| Cabo Verde | [Cabo%20Verde.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Cabo%20Verde.txt) | 172 |
| Cambodia | [Cambodia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Cambodia.txt) | 745 |
| Cameroon | [Cameroon.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Cameroon.txt) | 289 |
| Canada | [Canada.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Canada.txt) | 27.244 |
| Cayman Islands | [Cayman%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Cayman%20Islands.txt) | 244 |
| Central African Republic | [Central%20African%20Republic.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Central%20African%20Republic.txt) | 119 |
| Chad | [Chad.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Chad.txt) | 165 |
| Chile | [Chile.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Chile.txt) | 9.627 |
| China | [China.txt](https://listaip.wmanti.com.br/GeoIP-Paises/China.txt) | 19.559 |
| Christmas Island | [Christmas%20Island.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Christmas%20Island.txt) | 72 |
| Cocos Keeling Islands | [Cocos%20Keeling%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Cocos%20Keeling%20Islands.txt) | 39 |
| Colombia | [Colombia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Colombia.txt) | 3.866 |
| Comoros | [Comoros.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Comoros.txt) | 112 |
| Congo DRC | [Congo%20DRC.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Congo%20DRC.txt) | 387 |
| Congo Republic | [Congo%20Republic.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Congo%20Republic.txt) | 171 |
| Cook Islands | [Cook%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Cook%20Islands.txt) | 115 |
| Costa Rica | [Costa%20Rica.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Costa%20Rica.txt) | 944 |
| Croatia | [Croatia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Croatia.txt) | 1.162 |
| Cuba | [Cuba.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Cuba.txt) | 185 |
| Curaçao | [Cura%C3%A7ao.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Cura%C3%A7ao.txt) | 204 |
| Cyprus | [Cyprus.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Cyprus.txt) | 1.437 |
| Czechia | [Czechia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Czechia.txt) | 5.776 |
| Denmark | [Denmark.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Denmark.txt) | 5.082 |
| Djibouti | [Djibouti.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Djibouti.txt) | 149 |
| Dominica | [Dominica.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Dominica.txt) | 164 |
| Dominican Republic | [Dominican%20Republic.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Dominican%20Republic.txt) | 1.076 |
| Ecuador | [Ecuador.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Ecuador.txt) | 1.348 |
| Egypt | [Egypt.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Egypt.txt) | 988 |
| El Salvador | [El%20Salvador.txt](https://listaip.wmanti.com.br/GeoIP-Paises/El%20Salvador.txt) | 444 |
| Equatorial Guinea | [Equatorial%20Guinea.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Equatorial%20Guinea.txt) | 122 |
| Eritrea | [Eritrea.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Eritrea.txt) | 122 |
| Estonia | [Estonia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Estonia.txt) | 1.744 |
| Eswatini | [Eswatini.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Eswatini.txt) | 149 |
| Ethiopia | [Ethiopia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Ethiopia.txt) | 198 |
| Falkland Islands | [Falkland%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Falkland%20Islands.txt) | 94 |
| Faroe Islands | [Faroe%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Faroe%20Islands.txt) | 112 |
| Federated States of Micronesia | [Federated%20States%20of%20Micronesia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Federated%20States%20of%20Micronesia.txt) | 152 |
| Fiji | [Fiji.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Fiji.txt) | 205 |
| Finland | [Finland.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Finland.txt) | 46.715 |
| France | [France.txt](https://listaip.wmanti.com.br/GeoIP-Paises/France.txt) | 40.742 |
| French Guiana | [French%20Guiana.txt](https://listaip.wmanti.com.br/GeoIP-Paises/French%20Guiana.txt) | 173 |
| French Polynesia | [French%20Polynesia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/French%20Polynesia.txt) | 231 |
| French Southern Territories | [French%20Southern%20Territories.txt](https://listaip.wmanti.com.br/GeoIP-Paises/French%20Southern%20Territories.txt) | 22 |
| Gabon | [Gabon.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Gabon.txt) | 148 |
| Gambia | [Gambia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Gambia.txt) | 158 |
| Georgia | [Georgia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Georgia.txt) | 747 |
| Germany | [Germany.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Germany.txt) | 73.123 |
| Ghana | [Ghana.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Ghana.txt) | 582 |
| Gibraltar | [Gibraltar.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Gibraltar.txt) | 227 |
| Greece | [Greece.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Greece.txt) | 2.522 |
| Greenland | [Greenland.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Greenland.txt) | 257 |
| Grenada | [Grenada.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Grenada.txt) | 191 |
| Guadeloupe | [Guadeloupe.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Guadeloupe.txt) | 317 |
| Guam | [Guam.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Guam.txt) | 263 |
| Guatemala | [Guatemala.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Guatemala.txt) | 751 |
| Guernsey | [Guernsey.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Guernsey.txt) | 181 |
| Guinea | [Guinea.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Guinea.txt) | 154 |
| GuineaBissau | [GuineaBissau.txt](https://listaip.wmanti.com.br/GeoIP-Paises/GuineaBissau.txt) | 128 |
| Guyana | [Guyana.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Guyana.txt) | 145 |
| Haiti | [Haiti.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Haiti.txt) | 205 |
| Heard and McDonald Islands | [Heard%20and%20McDonald%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Heard%20and%20McDonald%20Islands.txt) | 36 |
| Honduras | [Honduras.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Honduras.txt) | 605 |
| Hong Kong | [Hong%20Kong.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Hong%20Kong.txt) | 15.973 |
| Hungary | [Hungary.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Hungary.txt) | 2.917 |
| Iceland | [Iceland.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Iceland.txt) | 829 |
| India | [India.txt](https://listaip.wmanti.com.br/GeoIP-Paises/India.txt) | 21.414 |
| Indonesia | [Indonesia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Indonesia.txt) | 11.084 |
| Iran | [Iran.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Iran.txt) | 2.775 |
| Iraq | [Iraq.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Iraq.txt) | 1.636 |
| Ireland | [Ireland.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Ireland.txt) | 8.862 |
| Isle of Man | [Isle%20of%20Man.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Isle%20of%20Man.txt) | 347 |
| Israel | [Israel.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Israel.txt) | 4.258 |
| Italy | [Italy.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Italy.txt) | 13.460 |
| Ivory Coast | [Ivory%20Coast.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Ivory%20Coast.txt) | 469 |
| Jamaica | [Jamaica.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Jamaica.txt) | 363 |
| Japan | [Japan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Japan.txt) | 18.075 |
| Jersey | [Jersey.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Jersey.txt) | 219 |
| Jordan | [Jordan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Jordan.txt) | 602 |
| Kazakhstan | [Kazakhstan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Kazakhstan.txt) | 2.371 |
| Kenya | [Kenya.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Kenya.txt) | 1.321 |
| Kiribati | [Kiribati.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Kiribati.txt) | 188 |
| Kosovo | [Kosovo.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Kosovo.txt) | 108 |
| Kuwait | [Kuwait.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Kuwait.txt) | 600 |
| Kyrgyzstan | [Kyrgyzstan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Kyrgyzstan.txt) | 508 |
| Laos | [Laos.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Laos.txt) | 271 |
| Latvia | [Latvia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Latvia.txt) | 1.802 |
| Lebanon | [Lebanon.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Lebanon.txt) | 622 |
| Lesotho | [Lesotho.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Lesotho.txt) | 146 |
| Liberia | [Liberia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Liberia.txt) | 172 |
| Libya | [Libya.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Libya.txt) | 233 |
| Liechtenstein | [Liechtenstein.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Liechtenstein.txt) | 491 |
| Lithuania | [Lithuania.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Lithuania.txt) | 5.263 |
| Luxembourg | [Luxembourg.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Luxembourg.txt) | 1.951 |
| Macao | [Macao.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Macao.txt) | 752 |
| Madagascar | [Madagascar.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Madagascar.txt) | 191 |
| Malawi | [Malawi.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Malawi.txt) | 222 |
| Malaysia | [Malaysia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Malaysia.txt) | 3.906 |
| Maldives | [Maldives.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Maldives.txt) | 236 |
| Mali | [Mali.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Mali.txt) | 153 |
| Malta | [Malta.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Malta.txt) | 417 |
| Marshall Islands | [Marshall%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Marshall%20Islands.txt) | 120 |
| Martinique | [Martinique.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Martinique.txt) | 254 |
| Mauritania | [Mauritania.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Mauritania.txt) | 146 |
| Mauritius | [Mauritius.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Mauritius.txt) | 641 |
| Mayotte | [Mayotte.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Mayotte.txt) | 128 |
| Mexico | [Mexico.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Mexico.txt) | 6.401 |
| Moldova | [Moldova.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Moldova.txt) | 2.768 |
| Monaco | [Monaco.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Monaco.txt) | 328 |
| Mongolia | [Mongolia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Mongolia.txt) | 494 |
| Montenegro | [Montenegro.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Montenegro.txt) | 246 |
| Montserrat | [Montserrat.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Montserrat.txt) | 91 |
| Morocco | [Morocco.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Morocco.txt) | 717 |
| Mozambique | [Mozambique.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Mozambique.txt) | 270 |
| Myanmar | [Myanmar.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Myanmar.txt) | 780 |
| Namibia | [Namibia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Namibia.txt) | 223 |
| Nauru | [Nauru.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Nauru.txt) | 112 |
| Nepal | [Nepal.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Nepal.txt) | 752 |
| New Caledonia | [New%20Caledonia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/New%20Caledonia.txt) | 181 |
| New Zealand | [New%20Zealand.txt](https://listaip.wmanti.com.br/GeoIP-Paises/New%20Zealand.txt) | 3.933 |
| Nicaragua | [Nicaragua.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Nicaragua.txt) | 291 |
| Niger | [Niger.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Niger.txt) | 140 |
| Nigeria | [Nigeria.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Nigeria.txt) | 1.675 |
| Niue | [Niue.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Niue.txt) | 96 |
| Norfolk Island | [Norfolk%20Island.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Norfolk%20Island.txt) | 107 |
| North Korea | [North%20Korea.txt](https://listaip.wmanti.com.br/GeoIP-Paises/North%20Korea.txt) | 545 |
| North Macedonia | [North%20Macedonia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/North%20Macedonia.txt) | 412 |
| Northern Mariana Islands | [Northern%20Mariana%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Northern%20Mariana%20Islands.txt) | 108 |
| Norway | [Norway.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Norway.txt) | 4.358 |
| Oman | [Oman.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Oman.txt) | 741 |
| Pakistan | [Pakistan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Pakistan.txt) | 2.042 |
| Palau | [Palau.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Palau.txt) | 112 |
| Palestine | [Palestine.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Palestine.txt) | 464 |
| Panama | [Panama.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Panama.txt) | 977 |
| Papua New Guinea | [Papua%20New%20Guinea.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Papua%20New%20Guinea.txt) | 361 |
| Paraguay | [Paraguay.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Paraguay.txt) | 683 |
| Peru | [Peru.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Peru.txt) | 1.796 |
| Philippines | [Philippines.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Philippines.txt) | 3.388 |
| Pitcairn Islands | [Pitcairn%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Pitcairn%20Islands.txt) | 36 |
| Poland | [Poland.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Poland.txt) | 11.749 |
| Portugal | [Portugal.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Portugal.txt) | 3.212 |
| Puerto Rico | [Puerto%20Rico.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Puerto%20Rico.txt) | 1.007 |
| Qatar | [Qatar.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Qatar.txt) | 823 |
| Romania | [Romania.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Romania.txt) | 5.401 |
| Russia | [Russia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Russia.txt) | 25.419 |
| Rwanda | [Rwanda.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Rwanda.txt) | 197 |
| Réunion | [R%C3%A9union.txt](https://listaip.wmanti.com.br/GeoIP-Paises/R%C3%A9union.txt) | 306 |
| Saint Barthélemy | [Saint%20Barth%C3%A9lemy.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Saint%20Barth%C3%A9lemy.txt) | 107 |
| Saint Kitts and Nevis | [Saint%20Kitts%20and%20Nevis.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Saint%20Kitts%20and%20Nevis.txt) | 160 |
| Saint Lucia | [Saint%20Lucia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Saint%20Lucia.txt) | 177 |
| Saint Martin | [Saint%20Martin.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Saint%20Martin.txt) | 149 |
| Saint Pierre and Miquelon | [Saint%20Pierre%20and%20Miquelon.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Saint%20Pierre%20and%20Miquelon.txt) | 122 |
| Saint Vincent and the Grenadines | [Saint%20Vincent%20and%20the%20Grenadines.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Saint%20Vincent%20and%20the%20Grenadines.txt) | 142 |
| Samoa | [Samoa.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Samoa.txt) | 141 |
| San Marino | [San%20Marino.txt](https://listaip.wmanti.com.br/GeoIP-Paises/San%20Marino.txt) | 170 |
| Saudi Arabia | [Saudi%20Arabia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Saudi%20Arabia.txt) | 2.586 |
| Senegal | [Senegal.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Senegal.txt) | 235 |
| Serbia | [Serbia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Serbia.txt) | 1.394 |
| Seychelles | [Seychelles.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Seychelles.txt) | 4.927 |
| Sierra Leone | [Sierra%20Leone.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Sierra%20Leone.txt) | 169 |
| Singapore | [Singapore.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Singapore.txt) | 14.688 |
| Sint Maarten | [Sint%20Maarten.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Sint%20Maarten.txt) | 110 |
| Slovakia | [Slovakia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Slovakia.txt) | 1.925 |
| Slovenia | [Slovenia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Slovenia.txt) | 1.541 |
| Solomon Islands | [Solomon%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Solomon%20Islands.txt) | 122 |
| Somalia | [Somalia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Somalia.txt) | 190 |
| South Africa | [South%20Africa.txt](https://listaip.wmanti.com.br/GeoIP-Paises/South%20Africa.txt) | 5.780 |
| South Georgia and the South Sandwich Islands | [South%20Georgia%20and%20the%20South%20Sandwich%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/South%20Georgia%20and%20the%20South%20Sandwich%20Islands.txt) | 30 |
| South Korea | [South%20Korea.txt](https://listaip.wmanti.com.br/GeoIP-Paises/South%20Korea.txt) | 5.612 |
| South Sudan | [South%20Sudan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/South%20Sudan.txt) | 176 |
| Spain | [Spain.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Spain.txt) | 14.780 |
| Sri Lanka | [Sri%20Lanka.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Sri%20Lanka.txt) | 464 |
| St Helena | [St%20Helena.txt](https://listaip.wmanti.com.br/GeoIP-Paises/St%20Helena.txt) | 34 |
| Sudan | [Sudan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Sudan.txt) | 207 |
| Suriname | [Suriname.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Suriname.txt) | 142 |
| Svalbard and Jan Mayen | [Svalbard%20and%20Jan%20Mayen.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Svalbard%20and%20Jan%20Mayen.txt) | 43 |
| Sweden | [Sweden.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Sweden.txt) | 14.437 |
| Switzerland | [Switzerland.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Switzerland.txt) | 12.087 |
| Syria | [Syria.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Syria.txt) | 402 |
| São Tomé and Príncipe | [S%C3%A3o%20Tom%C3%A9%20and%20Pr%C3%ADncipe.txt](https://listaip.wmanti.com.br/GeoIP-Paises/S%C3%A3o%20Tom%C3%A9%20and%20Pr%C3%ADncipe.txt) | 117 |
| Taiwan | [Taiwan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Taiwan.txt) | 4.882 |
| Tajikistan | [Tajikistan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Tajikistan.txt) | 257 |
| Tanzania | [Tanzania.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Tanzania.txt) | 533 |
| Thailand | [Thailand.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Thailand.txt) | 4.300 |
| The Netherlands | [The%20Netherlands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/The%20Netherlands.txt) | 78.550 |
| TimorLeste | [TimorLeste.txt](https://listaip.wmanti.com.br/GeoIP-Paises/TimorLeste.txt) | 170 |
| Togo | [Togo.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Togo.txt) | 145 |
| Tokelau | [Tokelau.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Tokelau.txt) | 106 |
| Tonga | [Tonga.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Tonga.txt) | 120 |
| Trinidad and Tobago | [Trinidad%20and%20Tobago.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Trinidad%20and%20Tobago.txt) | 284 |
| Tunisia | [Tunisia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Tunisia.txt) | 330 |
| Turkmenistan | [Turkmenistan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Turkmenistan.txt) | 152 |
| Turks and Caicos Islands | [Turks%20and%20Caicos%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Turks%20and%20Caicos%20Islands.txt) | 126 |
| Tuvalu | [Tuvalu.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Tuvalu.txt) | 106 |
| Türkiye | [T%C3%BCrkiye.txt](https://listaip.wmanti.com.br/GeoIP-Paises/T%C3%BCrkiye.txt) | 6.085 |
| Uganda | [Uganda.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Uganda.txt) | 375 |
| Ukraine | [Ukraine.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Ukraine.txt) | 7.868 |
| United Arab Emirates | [United%20Arab%20Emirates.txt](https://listaip.wmanti.com.br/GeoIP-Paises/United%20Arab%20Emirates.txt) | 6.475 |
| United Kingdom | [United%20Kingdom.txt](https://listaip.wmanti.com.br/GeoIP-Paises/United%20Kingdom.txt) | 51.085 |
| United States Minor Outlying Islands | [United%20States%20Minor%20Outlying%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/United%20States%20Minor%20Outlying%20Islands.txt) | 84 |
| United States | [United%20States.txt](https://listaip.wmanti.com.br/GeoIP-Paises/United%20States.txt) | 262.974 |
| Uruguay | [Uruguay.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Uruguay.txt) | 426 |
| US Virgin Islands | [US%20Virgin%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/US%20Virgin%20Islands.txt) | 266 |
| Uzbekistan | [Uzbekistan.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Uzbekistan.txt) | 782 |
| Vanuatu | [Vanuatu.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Vanuatu.txt) | 291 |
| Vatican City | [Vatican%20City.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Vatican%20City.txt) | 112 |
| Venezuela | [Venezuela.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Venezuela.txt) | 1.633 |
| Vietnam | [Vietnam.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Vietnam.txt) | 3.877 |
| Wallis and Futuna | [Wallis%20and%20Futuna.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Wallis%20and%20Futuna.txt) | 92 |
| Western Sahara | [Western%20Sahara.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Western%20Sahara.txt) | 43 |
| Yemen | [Yemen.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Yemen.txt) | 231 |
| Zambia | [Zambia.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Zambia.txt) | 272 |
| Zimbabwe | [Zimbabwe.txt](https://listaip.wmanti.com.br/GeoIP-Paises/Zimbabwe.txt) | 334 |
| Åland Islands | [%C3%85land%20Islands.txt](https://listaip.wmanti.com.br/GeoIP-Paises/%C3%85land%20Islands.txt) | 169 |

</details>

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
