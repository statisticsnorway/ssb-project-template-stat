# Behandling av altinn skjemaer

## Bruksanvisning for startpakke

Pakken består av følgende funksjoner. Generelt anbefales det å endre minst mulig, men i "Avansert" er det beskrevet hvordan du kan tilpasse produksjonen til eget skjema. Det står også mer utfyllende om hvert steg lenger nede.

| Komponent | Plassering | Forklaring | Avansert |
|---|---|---|---|
| get_extractor() | src/altinn/processing/form_processing.py | Her settes hvilken type Extractor skjemaet ditt bruker. | Hvis du trenger at skjemaet ditt flates ut på en annen måte enn det som er standard, så kan du skifte ut hva slags Extractor som returneres her. |
| get_storage_connector() | src/altinn/processing/form_processing.py | Denne funksjonen setter opp koblingen til datalagringen din. | Her kan du bestemme hvordan dataene dine som kommer fra Extractor skal lagres. Pakken starter med Parquedit koblingen, men denne kan skiftes til det som passer din undersøkelse. |
| main_process_forms() | src/altinn/processing/form_processing.py | Dette er prosesseringskoden som syr sammen Extractor og StorageConnector for å først flate ut skjemaene og så lagre de. | Hvis du har flere skjemaer i samme repo/datalagring, se beskrivelse nedenfor. Har du veldig spesielle behov kan du erstatte DefaultFormProcessor med en som arver fra MetaFormProcessor. |
| app.py | src/altinn/app/app.py | Her ligger editeringsappen din. Du kan kjøre den som en hvilken som helst python fil og den starter opp appen din. Den er utformet med beskrivelse for hvor du kan legge inn egne endringer, dette for å redusere støy og unødvendige konflikter ved oppdatering av malen. | For å utvide og tilpasse appen din kan du bruke fortrinssvis yaml filer eller alternativt python kode for å legge til funksjonalitet. Du kan også lage helt egne skreddersydde komponenter om det er nødvendig. Se veiledning i [ssb-dash-framework sin dokumentasjon](https://github.com/statisticsnorway/ssb-dash-framework)
| app.yaml | src/altinn/app/app-config/app.yaml | Her er basisoppsett for en yaml basert app. Her kan du utvide med flere moduler og bygge ut appen din. | Se [ssb-dash-framework sin yaml spesifikke dokumentasjon](https://github.com/statisticsnorway/ssb-dash-framework/blob/main/docs/yaml_reference.md) for hvordan moduler settes opp. Alle moduler i ssb-dash-framework som arver fra ModuleBase er mulig å konfigurere med yaml. Du kan også bruke denne base classen for å gjøre dine egne skreddersydde moduler konfigurerbare. |
| export_forms() | src/altinn/form_export.py | Her er kode for å eksportere data fra lagringen din. Denne er mest relevant om du bruker en lagring som parquedit eller en database. | Om du ønsker spesifikk prosessering gjort etter eksport, for eksempel utledning av hjelpevariabler eller beregning av summer o.l. så er dette en fin plass å legge det inn. | 

## 1. Overføring fra Suv bøtte og kildomat

Mottatte skjemaer anbefales å flyttes til produkt bøtta uendret og legges i en mappe under inndata/temp/altinn/skjemanummer

Eksempel: ledstill/inndata/temp/altinn/RA0678/

Mal for kildomat kan du se her:

```python
import gcsfs
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fs = gcsfs.GCSFileSystem()

destination_root = "{PROD_BUCKET_NAME}/{SHORTNAME}/inndata/altinn/{FORM_NUMBER}"

def main(source_file):
    logger.info(f"Kjører på: {source_file}")
    if source_file.endswith(".xml") or source_file.endswith(".json"):        
        relative_path = source_file.split("/altinn/", 1)[1]        
        dest = f"gs://{dest_root}/{relative_path}"
        logger.info(f"Kopierer {source_file} til {dest}")
        fs.copy(source_file, dest)
    else:
        logger.debug(f"Skipping file '{source_file}'")
```

## 2. Prosessering av skjemaene

Dette steget tar seg av:
- utflating av mottatte skjemaer
- nødvendige omkodinger
- innlasting til database/lagringssystem

Du må legge inn skjemanummeret som du skal behandle i config/settings.toml.

Prosesseringen i dette steget baserer seg på pakken **ssb-altinn-form-tools** som tilbyr en standard-prosessering og har muligheter for å skreddersy deler av prosessen ved behov, med minimalt av endringer. Se [ssb-altinn-form-tools repoet for mer dokumentasjon.](https://github.com/statisticsnorway/ssb-altinn-form-tools)

### Har samme undersøkelse flere skjemaer?

Skal du behandle flere skjemaer må du endre settings.toml og form_processing.py koden til noe som dette:

#### settings.toml

```toml
form_number = ["ra-XXXX"] # Gjøres om til en liste
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

I mappen src/altinn/app kan du finne en app.py fil som kan kjøres for å starte en applikasjon for å se gjennom dataene dine og ved behov foreta korreksjoner. Denne appen er bygd med **ssb-dash-framework** som er et bibliotek med modul-baserte skjermbilder som du kan bygge appen din med. Det er sentralt forvaltet og laget for å kunne tilpasses hver enkelt sitt behov og utvides over tid med mer funksjonalitet.

Denne appen er med vilje minimal, men designet for å være lett å utvide med mer funksjonalitet. En generell anbefaling er å se på DataEditor modulen først.

Se demoer/eksempler i [ssb-dash-framework/tree/main/demo](https://github.com/statisticsnorway/ssb-dash-framework/tree/main/demo) og dokumentasjon i [ssb-dash-framework/tree/main/docs](https://github.com/statisticsnorway/ssb-dash-framework/tree/main/docs).

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