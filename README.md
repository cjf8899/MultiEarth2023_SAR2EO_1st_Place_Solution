# MultiEarth2023_SAR2EO_1st_Place_Solution

> **1st Place Solution to MultiEarth 2023 Challenge on Multimodal SAR-to-EO Image Translation**
> 
> **CCA: Clean Collector Algorithm for Satellite Image Pre-processing of SAR-to-EO Translation, MDPI Electronics 2024** 
> 
> [Jingi Ju](https://scholar.google.co.kr/citations?user=hlJYrqAAAAAJ&hl), [Hyeoncheol Noh](https://scholar.google.co.kr/citations?user=XTmafQgAAAAJ&hl), [Minwoo Kim](https://scholar.google.com/citations?user=c7el4JwAAAAJ), [Dong-Geol Choi](https://scholar.google.co.kr/citations?user=1498JWoAAAAJ&hl)
> 
> *[arXiv](https://arxiv.org/abs/2306.12626v1)*, *[MDPI Electronics 2024](https://www.mdpi.com/2079-9292/13/22/4529)*
> 
> *[Project Presentations](https://github.com/cjf8899/MultiEarth2023_SAR2EO_1st_Place_Solution/files/11846834/default.pdf)*

## Abstract
The Multimodal Learning for Earth and Environment Workshop (MultiEarth 2023) is the second annual CVPR workshop aimed at the monitoring and analysis of the health of Earth ecosystems by leveraging the vast amount of remote sensing data that is continuously being collected. The primary objective of this workshop is to bring together the Earth and environmental science communities as well as the multimodal representation learning communities to explore new ways of harnessing technological advancements in support of environmental monitoring. The MultiEarth Workshop also seeks to provide a common benchmark for processing multimodal remote sensing information by organizing public challenges focused on monitoring the Amazon rainforest. These challenges include estimating deforestation, detecting forest fires, translating synthetic aperture radar (SAR) images to the visible domain, and projecting environmental trends. This paper presents the challenge guidelines, datasets, and evaluation metrics. Our challenge website is available at [https://sites.google.com/view/rainforest-challenge/multiearth-2023](https://sites.google.com/view/rainforest-challenge/multiearth-2023).

## SAR-to-EO Image Translation task
Numerous research studies have found that climate change has already led to an escalation in the duration of wildfire seasons, the frequency of wildfires, and the amount of land destroyed by fires. The fire detection sub-challenge aims to better understand the Amazon rainforest destroyed by forest fires. By analyzing data from multiple sources, including optical and synthetic aperture radar (SAR) images, participants can track changes in the frequency, intensity, and location of forest fires over time. This information can help identify areas that are particularly susceptible to forest fire, as well as areas where the risk of forest fires is increasing. Automated fire detection system will provide valuable insights into how environmental changes, such as climate change, are impacting the rainforest.

## Ours Methods
We propose the Clean Collector Algorithm (CCA), designed to take full advantage of this cloudless SAR data and eliminate factors that may hinder the data learning process. Subsequently, we applied pix2pixHD for the SAR-to-EO translation and Restormer for image enhancement. In the final evaluation, **the team ‘CDRL’ achieved an MAE of 0.07313, securing the top rank on the leaderboard.**

<p align="center"><img src="https://github.com/cjf8899/MultiEarth2023_SAR2EO_1st_Place_Solution/assets/59816618/649d224b-6803-4d3d-85c4-9b4f5648da1b" width="100%" height="100%" title="70px" alt="memoryblock"></p>



## Thanks to
We would like to thank [Minseok Seo](https://scholar.google.co.kr/citations?user=pOygDIIAAAAJ&hl) and [JongChan Park](https://scholar.google.co.kr/citations?user=jxJw3_oAAAAJ&hl) for their technical assistance during the competition. 

