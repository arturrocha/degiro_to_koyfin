# degiro_to_koyfin
Converts the csv from degiro to be able to be uploaded to koyfin MP.  
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
`koyfin.csv` is going to be created under `src`
