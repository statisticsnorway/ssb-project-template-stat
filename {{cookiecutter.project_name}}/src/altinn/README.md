# Behandling av altinn skjemaer

## 1. Kildomat

TODO:

## 2. Prosessering (form_processing.py)

Dette steget tar seg av:
- utflating av mottatte skjemaer
- nødvendige omkodinger
- innlasting til database/lagringssystem

## 3. Behandling (app.py)

Her behandles skjemaene med kode og grensesnitt for å bli omgjort til klargjorte data

I app mappen ligger det en standard app som kan tilpasses egne behov.

### Legge til moduler fra ssb-dash-framework

Den enkleste måten å legge til flere moduler og skjermbilder i appen er å legge det inn i app.yaml.

### Lage egne moduler og skjermbilder

ssb-dash-framework er designet for å være utvidbart, så du kan lage egne moduler som du inkluderer i din egen app.

Det anbefales å lage en egen mappe i app mappen hvor du legger egne moduler og tilpasninger.

Se veiledning for å lage moduler i https://github.com/statisticsnorway/ssb-dash-framework/tree/main

## 4. Eksport (form_export.py)

I dette steget eksporteres et klargjort datasett med alle endringene du har gjort.

Hvis du bruker en av de eksisterende eksport-funksjonene i ssb-altinn-form-tools så følger du alle krav og standarder.