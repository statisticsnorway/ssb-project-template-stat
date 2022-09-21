# stat-hurtigstart-template-master
Som en del av hack 2022 opprettes dette repoet som ett forsøk på å definere "standard mappestruktur og verktøysvalg for statistikkproduksjonsløp skrevet i Python".

Gruppedeltagere:
- Miles Winther
- Arne Sørli
- Carl F. Corneil
- Øyvind Bruer-Skarsbø

Valgene som er gjort i templaten kommenteres videre inne i cookie-cutter-template mappen.

Templaten er tenkt brukt som en del av en større "dapla hurtigstart create"-funksjon.\
Det vil være naturlig å produsere flere templates til ulike behov etter hvert som de oppstår og kartlegges.

Om du ønsker å få inn denne templaten direkte via cruft:
`cruft create https://github.com/statisticsnorway/stat-hurtigstart-template-master`


Send inn alle parameterene, uten å skrive de inn, kan gjøres via --no-input og --extra-context.
`cruft create https://github.com/statisticsnorway/stat-hurtigstart-template-master --no-input --extra-context "{\"full_name\":\"Passed In\"}"`
Jsonen som passes til --extra-context må ha doble fnutter, som må være escapet inne i jsonen.\
Om du først gjør dette, vær sikker på at du har dekket alle parametrene satt av cookiecutter.json.