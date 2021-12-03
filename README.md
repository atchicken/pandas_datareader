# pandas_datareader
Get Stock Price from "Stooq"

## How to Use

・Get Stock Price Data(Input Date: YYYYMMDD)
```bash:bash
python downloadStooq.py [Start Date] [End Date] -b [Stock Brand] -s [Save CSV Path] 
```

・Create Graph(Input Date: YYYYMMDD)
```
python createGraph.py [CSV Path] [Start Date] [End Date] -b [Stock Brand] -s [Save Image Path] 
```

## Example of CSV to Get
```
Date,Open,High,Low,Close,Volume
2021-10-29,1081.86,1115.21,1073.205,1114.0,29918417
2021-10-28,1068.305,1081.0,1054.2,1077.04,27213173
2021-10-27,1039.66,1070.88,1030.78,1037.86,38526459
2021-10-26,1024.69,1094.94,1001.44,1018.43,62414968
...
```

## Detailed Explanation(Japanese)

・[Blog](https://atchicken.com/stooq_download/)




## Results
```bash:bash
python createGraph.py
```

![graph](https://user-images.githubusercontent.com/93382642/139573722-d2cb6256-447c-4237-8980-a57dc0ff1ca6.png)
