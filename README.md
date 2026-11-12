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

<p>
<a href="https://github.com/luchocomputor/flow-state-uqam"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/titles/uqam-dark.svg">
  <img alt="Can EEG tell when a player is in the zone? UQAM, Montréal, research internship, 2026" src="assets/titles/uqam-light.svg">
</picture></a>
</p>

26 skilled players, about 4 hours of *Apex Legends* each, recorded with a 16-channel EEG headset at Ubisoft La Forge. Flow state has no ground truth, so we built the labels from behaviour: small targets appeared at the edge of the screen, and a long run of missed targets marked a player fully absorbed in the game, contrasted with lobby rest between matches.

Absorbed play vs. rest decodes well across subjects (F1 = 0.76, leave-one-subject-out). Control analyses with eye-tracking, permutation tests and self-supervised probes then showed what the model actually reads: a broad play-vs-rest arousal shift rather than a marker of flow itself. The paper therefore frames the target as **attentional engagement**, not flow.

`EEG-Conformer` `self-supervised learning` `EfficientNet` `Riemannian geometry` `multivariate EMD` `Wigner-Ville` `PyTorch`

**First-author paper submitted to IEEE ISCAS 2027.**

<p>
<a href="https://github.com/luchocomputor/flow-state-uqam"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/code-dark.svg"><img height="30" alt="Code" src="assets/buttons/code-light.svg"></picture></a>
</p>

<br>

<p>
<a href="https://github.com/luchocomputor/Medical-Time-Series-Research-Project"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/titles/granger-dark.svg">
  <img alt="How do brain regions drive each other during sleep? École des Ponts, with CNRS and Max Planck researchers, 2024-25" src="assets/titles/granger-light.svg">
</picture></a>
</p>

Full-night EEG from the PhysioNet 2018 Challenge database (MGH Sleep Lab, 1,985 subjects). VAR models give temporal and spectral (Geweke) Granger causality between EEG channels, and wavelets make it time-resolved, to follow how these directed interactions change across sleep stages.

`Granger causality` `VAR models` `wavelets` `time-frequency analysis` `sleep EEG`

**First-author poster at the International Summer Institute on Network Physiology, Lake Como, 2025.**

<p>
<a href="https://github.com/luchocomputor/Medical-Time-Series-Research-Project"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/repo-dark.svg"><img height="30" alt="Repo" src="assets/buttons/repo-light.svg"></picture></a>&nbsp;
<a href="https://github.com/luchocomputor/Medical-Time-Series-Research-Project/blob/main/POSTER.pdf"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/poster-dark.svg"><img height="30" alt="Poster" src="assets/buttons/poster-light.svg"></picture></a>
</p>

<br>

## Projects

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/titles/challenge-dark.svg">
  <img alt="EEG/EMG Foundation Challenge 2026: EEG-to-Image. Meta, Muse and Yneuro, in progress" src="assets/titles/challenge-light.svg">
</picture>
</p>

Decoding which image a person is looking at from their EEG, on public datasets through Meta's NeuralBench framework. First submissions: ridge regression from EEG to image embeddings, fitted on about a million EEG epochs from Alljoined.

`EEG decoding` `image embeddings` `ridge regression` `NeuralBench`

<p>
<a href="https://neural-interfaces26.github.io/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/challenge-dark.svg"><img height="30" alt="Challenge website" src="assets/buttons/challenge-light.svg"></picture></a>
</p>

<br>

<p>
<a href="https://github.com/luchocomputor/martha"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/titles/martha-dark.svg">
  <img alt="Martha. Personal project, iOS, 2025-26" src="assets/titles/martha-light.svg">
</picture></a>
</p>

Native app that digitises a wardrobe from photos and suggests outfits with vision and language models. About 22k lines of Swift, from data model and backend to interface.

`SwiftUI` `CoreData` `Supabase` `Gemini vision`

<p>
<a href="https://github.com/luchocomputor/martha"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/repo-dark.svg"><img height="30" alt="Repo" src="assets/buttons/repo-light.svg"></picture></a>
</p>

<br>

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/titles/qrt-dark.svg">
  <img alt="QRT Data Challenge 2025. QRT and Institut Gustave Roussy, 2025" src="assets/titles/qrt-light.svg">
</picture>
</p>

Overall survival prediction for leukaemia patients from clinical and molecular data.

`survival analysis` `Cox models` `random survival forests` `LightGBM` `scikit-survival`

**IPCW C-index of 0.755 on the public leaderboard.**


<br>

## Experience

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/titles/cdc-dark.svg">
  <img alt="Caisse des Dépôts. Machine learning intern, Paris, 2025" src="assets/titles/cdc-light.svg">
</picture>
</p>

Learning-to-rank (LambdaMART) to allocate across emerging-market equity indices, with purged, embargoed time-series cross-validation against look-ahead bias.

<br>

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/titles/sopra-dark.svg">
  <img alt="Sopra Steria. Data science intern, Paris, 2024" src="assets/titles/sopra-light.svg">
</picture>
</p>

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

<p>
<a href="https://github.com/luchocomputor/cv/blob/main/cv.pdf"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/cv-dark.svg"><img height="30" alt="CV" src="assets/buttons/cv-light.svg"></picture></a>&nbsp;
<a href="https://www.linkedin.com/in/louis-almairac"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/linkedin-dark.svg"><img height="30" alt="LinkedIn" src="assets/buttons/linkedin-light.svg"></picture></a>&nbsp;
<a href="mailto:louis.almairac@enpc.fr"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/email-dark.svg"><img height="30" alt="Email" src="assets/buttons/email-light.svg"></picture></a>
</p>
