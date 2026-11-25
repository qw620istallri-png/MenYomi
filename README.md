# Menyomi めん読み

Apprendre à lire les kanji écrits à la main sur les menus japonais : révisions espacées, menus générés, écriture simulée au pinceau.

Site : https://qw620istallri-png.github.io/MenYomi/

- `index.html` : l'application complète (données incluses, fonctionne hors ligne une fois installée).
- `src/template.html` : interface et moteur d’écriture. `progress.js` : validation,
  fusion et transaction de progression. `learning.js` : favoris et bilan quotidien.
- `src/data.json` et `src/kanji.json` : données de tracés, dictionnaire et explications
  conservées depuis l’application livrée. `menudata.py` reste la source du vocabulaire.

## Construire et tester

Python 3.10+ suffit pour construire le site depuis un clone propre, sans téléchargement :

```sh
python src/build.py
python src/build.py --check
python -m http.server 8765 --bind 127.0.0.1
```

Ouvrir ensuite http://127.0.0.1:8765/ . Le build est déterministe : sa version dépend
du contenu des sources. `sitebuild.py` reste un alias de compatibilité.

Tests de progression, de génération et du service worker (Node 24) :

```sh
node --test tests/*.test.cjs
```

Tests des règles dans un projet de démonstration local (Node 24, Java 21) :

```sh
npm ci --ignore-scripts
npm run test:rules
```

Ces dépendances servent uniquement aux tests ; aucun paquet npm n’est livré dans l’app.
La CI vérifie les fichiers générés et les tests avant chaque déploiement. Elle publie
uniquement les ressources nécessaires au fonctionnement via `python src/package.py`.

## Progression et synchronisation

Les sauvegardes locales existantes et les codes `MENYOMI1` sont conservés. L’import
valide le contenu et fusionne les cartes, après avoir créé une copie locale sous
`menyomi.beforeImport`. Une sauvegarde locale illisible est préservée sous
`menyomi.recovery` ; les erreurs d’enregistrement sont signalées dans l’interface.
Exporter régulièrement avec le bouton **i → Transférer par code → Télécharger**.

Les nouvelles écritures cloud utilisent une transaction Firestore et conservent les
modifications faites localement pendant la requête. Hors ligne, la progression reste
locale ; la synchronisation est retentée au retour de la connexion. Les annulations
de cartes et retraits de favoris ont des marqueurs horodatés pour résister à la fusion.

`firestore.rules` limite la lecture et l’écriture de `users/{uid}` à son propriétaire,
et valide l’enveloppe du document. Ces règles sont testées dans l’émulateur, mais ne
sont **pas déployées automatiquement** par GitHub Pages. Pour les publier sur le
projet Firebase existant, après vérification de son identifiant :

```sh
npx firebase deploy --only firestore:rules --project menyomi
```

## Données et contenus

Le build courant n’exige ni base externe ni génération audio. `builddata.py` est un
outil optionnel de réimport : il attend `src/kvgall/kanji/` (KanjiVG) et
`dl/jamdict.db` (données KANJIDIC). Sauvegarder les données canoniques avant un réimport.
Les sources, licences et procédures de génération des voix doivent être conservées
si l’audio ou les tracés sont renouvelés ; les sorties existantes restent utilisables.

Les variantes de papier et de notes restent procédurales, sans photographies.
Les sept fonds doux et les treize scènes d’ombres tournent sur des cycles distincts,
selon le jour civil local et la section (y compris « La main »). Chaque écran a son
propre fond ; les 91 associations fond/ombre se renouvellent sans modifier le SRS.
Les scènes de lanternes contiennent toujours trois à cinq lanternes. Le bois reprend
une tranche plus dense et une ombre portée, avec une oscillation très discrète.
Le scotch et les coins pliés des notes sont déterministes pour un mot et un jour.
Dans l’atelier, les reflets de l’encre fraîche suivent les traits et disparaissent
pendant le séchage ; le papier lui-même ne change pas de luminosité.
Le décor n’est pas atténué pendant l’étude. Le tutoriel garde l’ordre écriture,
découverte du mot, puis reconnaissance sur menu. La version texte propose un
exercice alternatif en japonais imprimé aux contenus dessinés sur canvas.

Tracés : KanjiVG © Ulrich Apel, CC BY-SA 3.0. Sens et lectures : KANJIDIC2 (EDRDG), CC BY-SA 4.0.
