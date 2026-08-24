# Behandling av altinn skjemaer



## 1. Overføring fra Suv bøtte og kildomat

Mottatte skjemaer anbefales å flyttes til produkt bøtta uendret og legges i en mappe under inndata/temp/altinn/skjemanummer

Eksempel: ledstill/inndata/temp/altinn/RA0678/

Mal for kildomat kan du se her: TODO

## 2. Prosessering av skjemaene

Dette steget tar seg av:
- utflating av mottatte skjemaer
- nødvendige omkodinger
- innlasting til database/lagringssystem

Du må legge inn skjemanummerne som du skal behandle i config/settings.toml.

## 3. Klargjøring

Her behandles skjemaene med kode og grensesnitt for å bli omgjort til klargjorte data

I app mappen ligger det en standard app som kan tilpasses egne behov.

### Behandling med kode



### App

I mappen src/altinn/app kan du finne en app.py fil som kan kjøres for å starte en applikasjon for å se gjennom dataene dine og ved behov foreta korreksjoner.

Denne appen er med vilje minimal, men designet for å være lett å utvide med mer funksjonalitet.

#### Legge til moduler fra ssb-dash-framework

Den enkleste måten å legge til flere moduler og skjermbilder i appen er å legge det inn i app.yaml.

#### Lage egne moduler og skjermbilder

ssb-dash-framework er designet for å være utvidbart, så du kan lage egne moduler som du inkluderer i din egen app.

Det anbefales å lage en egen mappe i app mappen hvor du legger egne moduler og tilpasninger.

Se veiledning for å lage moduler i https://github.com/statisticsnorway/ssb-dash-framework/tree/main

## 4. Eksport (form_export.py)

I dette steget eksporteres et klargjort datasett med alle endringene du har gjort.

Hvis du bruker en av de eksisterende eksport-funksjonene i ssb-altinn-form-tools så følger du alle krav og standarder.