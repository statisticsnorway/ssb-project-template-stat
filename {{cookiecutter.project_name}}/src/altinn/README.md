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

Du må legge inn skjemanummeret som du skal behandle i config/settings.toml.

### Har samme undersøkelse flere skjemaer?

Skal du behandle flere skjemaer må du endre settings.toml og form_processing.py koden til noe som dette:

#### settings.toml
```toml
form_number = ["RAXXXX"] # Gjøres om til en liste
```

#### form_processing.py
```python
for form in settings.form_number: # <- Gjør det til en for-løkke
    processor = DefaultFormProcessor(
        form_name=form,
        form_base_path=f"{settings.form_folder}/{form}", # <- bruk skjemanummeret fra for-løkken istedenfor settings
        extractor=get_extractor(),
        connector=get_storage_connector(),
        alias_mapping={},
        checkbox_mapping=[],
    )
    processor.process_new_forms()
```

## 3. Klargjøring

Her behandles skjemaene med kode og grensesnitt for å bli omgjort til klargjorte data

I app mappen ligger det en standard app som kan tilpasses egne behov.

### App

I mappen src/altinn/app kan du finne en app.py fil som kan kjøres for å starte en applikasjon for å se gjennom dataene dine og ved behov foreta korreksjoner.

Denne appen er med vilje minimal, men designet for å være lett å utvide med mer funksjonalitet.

#### Hvordan legge til moduler fra ssb-dash-framework

Den enkleste måten å legge til flere moduler og skjermbilder i appen er å legge det inn i app.yaml.

Du kan også benytte python for å legge inn moduler og funksjonalitet.

[For veiledning om hvordan, se dokumentasjonen til ssb-dash-framework](https://statisticsnorway.github.io/ssb-dash-framework/) eller direkte i koden [ssb-dash-framework](https://github.com/statisticsnorway/ssb-dash-framework)

#### Lage egne moduler og skjermbilder

ssb-dash-framework er designet for å være utvidbart, så du kan lage egne moduler som du inkluderer i din egen app.

Det anbefales å lage en egen mappe i app mappen hvor du legger egne moduler og tilpasninger.

Se veiledning for å lage moduler i https://github.com/statisticsnorway/ssb-dash-framework/tree/main

### Behandling med kode




## 4. Eksport (form_export.py)

I dette steget eksporteres et klargjort datasett med alle endringene du har gjort.

Hvis du bruker en av de eksisterende eksport-funksjonene i ssb-altinn-form-tools så følger du alle krav og standarder.