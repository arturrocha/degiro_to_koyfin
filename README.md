# degiro_to_koyfin
Converts the csv from degiro to be able to be uploaded to koyfin [Model Portfolio](https://www.koyfin.com/help/release-notes/v3-23-model-portfolios/).  
You can pass multiple portifolios, they are going to be added together.  


# usage
```
git clone https://github.com/rocartur/degiro_to_koyfin.git  
cd degiro_to_koyfin  
python3 -m venv env  
source env/bin/activate  
pip install -r requirements.txt
cd src
python3 dtk.py --input_csv ~/Documents/Portfolio.csv
```
`koyfin.csv` is going to be created under `src` with format...
```
isin,weight,date
US02079K3059,0.01,01/01/2023
US03212B1035,0.01,01/01/2023
US03940R1077,0.06,01/01/2023
...
NL0010273215,0.03,01/01/2023
```
