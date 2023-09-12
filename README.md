# ssb-project-template-stat

Et template repo, egnet som utgangspunkt for statistikkproduksjon.

Repoet er typisk brukt sammen med kommandolinjeverktøyet [`ssb-project`](https://github.com/statisticsnorway/ssb-project-cli). Når man bruker `ssb-project` for å opprette et nytt prosjekt (f.eks `ssb-project create mitt-prosjekt`) så er dette repoet standardvalget som mal.

## Oppdateringer

Det er spesifisert avhengigheter i dette repoet, som må oppdateres jevnlig for å få med sikkerhetsoppdateringer. For å oppdatere kan man:

1. Instansiere malen med f.eks `ssb-project create temp`
1. `cd temp`
1. `poetry update`
1. Kopiere så den resulterende `poetry.lock` fil til dette repoet
1. Åpne en PR med de eventuelle endringene
