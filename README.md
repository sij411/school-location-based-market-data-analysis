# 초중고 학교 위치 기반 상권 데이터 분석
------------------------------------------------
개인 프로젝트로 진행된 한국외국어대학교 비즈니스 프로그래밍 1의 기말 과제입니다.

## 프로젝트 개요
--------------------------------------------------
해당 프로젝트의 목적은 초등학교, 중학교, 고등학교 위치에 분포해 있는 상권에 대해 파악함으로써 미래의 소비자 층은 알파, Z 세대 그룹의 소비 성향을 파악하기 위함에 있습니다. 청소년들에게 인기 있는 상품 및 서비스는 다른 세대와 차별점이 있을 것이란 가정 하에 진행된 프로젝트이며, 이러한 차이점이 미래 경제에 어떠한 영향을 끼칠 지에 대해 가늠해 보고자 합니다. 

--------------------------------------------------

## 사용한 기술
- Python 3.11.4

## Python Packages & Libraries

- pandas 1.5.3
- geopandas 0.14.1
- folium 0.15.0
- shapely 2.0.2
- matplotlib 3.7.1
- pyproj 3.6.1

## Source Data

경로: "./datasets/rawData/"

- school-region.csv
    - 지방교육재정연구원 초중고 학교 위치(2023)
    - [https://schoolzone.emac.kr/publicData/publicDataView.do]
- region-market.csv
    - 서울시 상권분석서비스(추정매출-상권) (2018-2023) 중에서 2022년 
    - [https://data.seoul.go.kr/dataList/OA-15572/S/1/datasetView.do#]
- seoul-region.csv
    - 서울시 상권분석서비스(영역-상권) (2018-2023)
    - [https://data.seoul.go.kr/dataList/OA-15560/S/1/datasetView.do?tab=A]

## 파일 구조

├── datasets
│   ├── rawData
│   |    ├── cleaneddata1.csv
|   |   └── cleaneddata2.csv
│   ├── cleanedData
│       ├── cleaneddata1.csv
|       └── cleaneddata2.csv
├── codes
│   ├── check-raw-region-market.ipynb
|   ├── check-raq-school-location.ipynb
|   ├── convert-coordination.ipynb
|   ├── markets-near-school-region-analysis.ipynb
|   ├── sales-near-school-analysis.ipynb
│   └── toolkit
|        ├── __init__.py
|        ├── README.md
|        ├── toolkit.py
├── analysis-report.pptx
├── README.md
└── .gitignore