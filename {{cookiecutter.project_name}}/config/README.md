# Konfigurasjonsfiler

Denne mappen inneholder ferdig oppsett og eksempel på bruk av konfigurasjonsfiler i python.

Konfigurasjonsfiler er tekstfiler som brukes til å lagre innstillinger og
verdier som programmet ditt trenger, for eksempel filstier, perioder og parametre for modeller.
Det er lurt å samle slike variabler på ett sted, i en konfigurasjonsfil, i stedet for at
variablene er spredt rundt omkring i koden.
Da er det kun ett sted man trenger å oppdatere, og koden trenger ikke å endres.

En vanlig type konfigurasjonsfil er [TOML-filer] (Tom's Obvious, Minimal Language).
TOML er et filformat som er enkelt å lese og skrive, og det er populært blant utviklere
for konfigurasjonsformål.
TOML-filer organiseres vanligvis i seksjoner, som hver inneholder nøkkel-verdi-par.
Se eksemplene nedenfor.


## Bruk av dynaconf til å lese konfig-filer

Vi anbefaler bruk av biblioteket [Dynaconf] til å lese og jobbe med konfig-filer i python.
Det støtter blant annet gjenbruk av variabler.
Det vil si at man i en variabel i konfig-filen kan gjenbruke andre variabler.
Et eksempel på dette kan være at man definerer et årstall og så gjenbrukes dette
årstallet i et filnavn.
Dynaconf støtter også validering, bruk av miljøer med mer.

Dynaconf bruker to filer som legges i en `config`-mappe:

```shell
├── config
    ├── settings.toml  # Selve konfigurasjonene
    └── config.py      # Leser inn konfig-filen og gjør variablene tilgjengelig via et settings-objekt.
```

### Eksempel på bruk

`settings.toml`:

```toml
year = 2024
product_root_dir = "/buckets/produkt/metstat"
```

Bruk i din kode:

```python
from config.config import settings

print(f"Year = {settings.year}")
print(f"Product root dir = {settings.product_root_dir}")
```

### Gjenbruk av variabler

Gjenbruk av variable gjøres ved hjelp av en `@format`-syntaks som vist i dette eksemplet:

```toml
dapla_team = "tip-tutorials"
short_name = "metstat"  # statistikkens kortnavn
product_root_dir = "@format gs://ssb-{this.dapla_team}-data-produkt-prod/{this.short_name}"
```

Her blir `settings.product_root_dir` satt til `gs://ssb-tip-tutorials-data-produkt-prod/metstat`.


### Bruk av miljøer

Miljøer kan brukes for å ha forskjellige konfigurasjoner i for eksempel prod og test,
uten å måtte angi alle variable på nytt.
Man trenger bare å overstyre det som er forskjellig.

I eksemplet i denne mappen er det brukt til å angi om man vil bruke bøtte-stier på
formen `/buckets/produkt` eller på formen `gs://ssb-tip-tutorials-data-produkt-prod/`.
Miljøet angir man i form av seksjoner i `settings.toml`-filen, slik som `[default]`
og `[gsbuckets]` i eksemplet her:

```toml
[default]
dapla_team = "tip-tutorials"
short_name = "metstat"  # statistikkens kortnavn
kildedata_root_dir = "@format /buckets/kilde/{this.short_name}"
product_root_dir = "@format /buckets/produkt/{this.short_name}"
inndata_dir = "@format {this.product_root_dir}/inndata"
klargjort_dir = "@format {this.product_root_dir}/klargjorte-data"
statistikk_dir = "@format {this.product_root_dir}/statistikk"
utdata_dir = "@format {this.product_root_dir}/utdata"

[gsbuckets]
kildedata_root_dir = "@format gs://ssb-{this.dapla_team}-data-kilde-prod/{this.short_name}"
product_root_dir = "@format gs://ssb-{this.dapla_team}-data-produkt-prod/{this.short_name}"
```

Merk at man bare trenger å angi kildedata_root_dir og product_root_dir under
`[gsbuckets]`-seksjonen.
De andre variablene blir automatisk ekspandert med riktig root_dir når man overstyrer
kildedata_root_dir og product_root_dir.

#### Valg av miljø

Hvilket miljø du ønsker å bruke velger du filen `config.py`, som vist her:

```python
settings = Dynaconf(
    settings_files=["settings.toml"],
    envvar_prefix="DYNACONF",
    environments=True,
    env="default",  # Change this to gsbuckets for use with google storage buckets
)
```

[Dynaconf]: https://www.dynaconf.com/
[tech-coach-stat repoet]: https://github.com/statisticsnorway/tech-coach-stat/tree/main/config
[TOML-filer]: https://toml.io/en/
