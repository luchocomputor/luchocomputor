<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Louis Almairac, machine learning for time series and EEG" src="assets/banner-light.svg">
</picture>
</p>

I'm in the **MVA master (Mathématiques, Vision, Apprentissage) at ENS Paris-Saclay**, as the final year of my engineering degree at École Nationale des Ponts et Chaussées. I work on machine learning for time series and biosignals, mostly EEG.

**Looking for a 6-month research internship from April 2027.**

<br>

## Research

### Can EEG tell when a player is in the zone?
<sub>UQAM, MONTRÉAL &nbsp;·&nbsp; RESEARCH INTERNSHIP &nbsp;·&nbsp; 2026</sub>

26 skilled players, about 4 hours of *Apex Legends* each, recorded with a 16-channel EEG headset at Ubisoft La Forge. Flow state has no ground truth, so we built the labels from behaviour: small targets appeared at the edge of the screen, and a long run of missed targets marked a player fully absorbed in the game, contrasted with lobby rest between matches.

Absorbed play vs. rest decodes well across subjects (F1 = 0.76, leave-one-subject-out). Control analyses with eye-tracking, permutation tests and self-supervised probes then showed what the model actually reads: a broad play-vs-rest arousal shift rather than a marker of flow itself. The paper therefore frames the target as **attentional engagement**, not flow.

`EEG-Conformer` `self-supervised learning` `EfficientNet` `Riemannian geometry` `multivariate EMD` `Wigner-Ville` `PyTorch`

**First-author paper submitted to IEEE ISCAS 2027.**

### How do brain regions drive each other during sleep?
<sub>ÉCOLE DES PONTS &nbsp;·&nbsp; WITH CNRS AND MAX PLANCK RESEARCHERS &nbsp;·&nbsp; 2024-25 &nbsp;·&nbsp; <a href="https://github.com/luchocomputor/Medical-Time-Series-Research-Project">REPO ↗</a></sub>

Full-night EEG from the PhysioNet 2018 Challenge database (MGH Sleep Lab, 1,985 subjects). VAR models give temporal and spectral (Geweke) Granger causality between EEG channels, and wavelets make it time-resolved, to follow how these directed interactions change across sleep stages.

`Granger causality` `VAR models` `wavelets` `time-frequency analysis` `sleep EEG`

**First-author [preprint on HAL](https://hal.science/hal-05377253) and poster at the International Summer Institute on Network Physiology, Lake Como, 2025.**

<br>

## Projects

### EEG/EMG Foundation Challenge 2026: EEG-to-Image
<sub>META, MUSE AND YNEURO &nbsp;·&nbsp; IN PROGRESS</sub>

Decoding which image a person is looking at from their EEG, on public datasets through Meta's NeuralBench framework. First submissions: ridge regression from EEG to image embeddings, fitted on about a million EEG epochs from Alljoined.

`EEG decoding` `image embeddings` `ridge regression` `NeuralBench`

### QRT Data Challenge 2025
<sub>QRT AND INSTITUT GUSTAVE ROUSSY &nbsp;·&nbsp; 2025 &nbsp;·&nbsp; <a href="https://github.com/luchocomputor/QRT_DataChallenge2025">REPO ↗</a></sub>

Overall survival prediction for leukaemia patients from clinical and molecular data.

`survival analysis` `Cox models` `random survival forests` `LightGBM` `scikit-survival`

**IPCW C-index of 0.755 on the public leaderboard.**

### Martha
<sub>PERSONAL PROJECT &nbsp;·&nbsp; iOS &nbsp;·&nbsp; 2025-26 &nbsp;·&nbsp; <a href="https://github.com/luchocomputor/martha">REPO ↗</a></sub>

Native app that digitises a wardrobe from photos and suggests outfits with vision and language models. About 22k lines of Swift, from data model and backend to interface.

`SwiftUI` `CoreData` `Supabase` `Gemini vision`

<br>

## Experience

### Caisse des Dépôts
<sub>MACHINE LEARNING INTERN &nbsp;·&nbsp; PARIS &nbsp;·&nbsp; 2025</sub>

Learning-to-rank (LambdaMART) to allocate across emerging-market equity indices, with purged, embargoed time-series cross-validation against look-ahead bias.

### Sopra Steria
<sub>DATA SCIENCE INTERN &nbsp;·&nbsp; PARIS &nbsp;·&nbsp; 2024</sub>

Root-cause analysis of metro delays for an RATP line-automation project.

<br>

## Activity

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/luchocomputor/luchocomputor/output/contrib-dark.svg">
  <img alt="Contribution graph over the last year" src="https://raw.githubusercontent.com/luchocomputor/luchocomputor/output/contrib-light.svg">
</picture>
</p>

<br>

## Tools

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=py%2Cpytorch%2Csklearn%2Cswift%2Csupabase%2Clatex%2Cgit&theme=dark">
  <img alt="Python, PyTorch, scikit-learn, Swift, Supabase, LaTeX, Git" src="https://skillicons.dev/icons?i=py%2Cpytorch%2Csklearn%2Cswift%2Csupabase%2Clatex%2Cgit&theme=light">
</picture>
</p>

<br>

**[CV](https://github.com/luchocomputor/cv/blob/main/cv.pdf)** &nbsp;·&nbsp; **[LinkedIn](https://www.linkedin.com/in/louis-almairac)** &nbsp;·&nbsp; **[louis.almairac@enpc.fr](mailto:louis.almairac@enpc.fr)**
