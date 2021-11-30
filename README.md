# EScafeAPI

## About
This is a simple API to get daily coffee prices in Vitoria - Espirito Santo, Brazil. It was develeped in Pytohn with FastAPI and deployed in Heroku.

EScafeAPI is a project of MAVV for the  Android app [Preço Café](https://play.google.com/store/apps/details?id=com.bortole.precocafe) by Magdo Bartole. 

## Usage
This API is deployed in 'https://escafeapi.herokuapp.com/'. 

### Request by day
You can request coffe's prices of a specific day by adding the date in format `DD-MM-YYYY`.

Example
```
https://escafeapi.herokuapp.com/10-11-2021
```

The response is the following JSON:
```
{"arabica-dura":"R$ 1.208,00","arabica-rio":"R$ 1.136,00","conilon":"R$ 765,00"}
```

This JSON shows prices of three types of coffee:

* `arabica-dura`: Bebida "dura", bica corrida, máx. de 20% de "cata", mín. de 30% de peneira 17 acima.
* `arabica-rio`: Bebida "rio", bica corrida, máx. de 30% de "cata", mín. de 30% de peneira 17 acima.
* `conilon`: Bica corrida, tipo 7/8, com até 13% de umidade e até 5% de broca.

Prices are presented as strings in BRL currency format: `R$ 1.200,00`.

**IMPORTANT NOTE: Only prices for days of the current month can be requested.**

### Request by month
You can request coffe's prices of all days in the current month.

Example
```
https://escafeapi.herokuapp.com/month/
```


The response is the following JSON:
```
{
"1":{"arabica-dura":"1.202,00","arabica-rio":"1.126,00","conilon":"752,00"},
"2":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"3":{"arabica-dura":"1.207,00","arabica-rio":"1.125,00","conilon":"755,00"},
"4":{"arabica-dura":"1.208,00","arabica-rio":"1.131,00","conilon":"759,00"},
"5":{"arabica-dura":"1.190,00","arabica-rio":"1.119,00","conilon":"757,00"},
"6":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"7":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"8":{"arabica-dura":"1.187,00","arabica-rio":"1.117,00","conilon":"751,00"},
"9":{"arabica-dura":"1.208,00","arabica-rio":"1.139,00","conilon":"757,00"},
"10":{"arabica-dura":"1.208,00","arabica-rio":"1.136,00","conilon":"765,00"},
"11":{"arabica-dura":"1.217,00","arabica-rio":"1.144,00","conilon":"767,00"},
"12":{"arabica-dura":"1.238,00","arabica-rio":"1.150,00","conilon":"769,00"},
"13":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"14":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"15":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"16":{"arabica-dura":"1.250,00","arabica-rio":"1.165,00","conilon":"769,00"},
"17":{"arabica-dura":"1.270,00","arabica-rio":"1.180,00","conilon":"772,00"},
"18":{"arabica-dura":"1.255,00","arabica-rio":"1.174,00","conilon":"770,00"},
"19":{"arabica-dura":"1.258,00","arabica-rio":"1.182,00","conilon":"780,00"},
"20":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"21":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"22":{"arabica-dura":"1.270,00","arabica-rio":"1.189,00","conilon":"779,00"},
"23":{"arabica-dura":"1.308,00","arabica-rio":"1.228,00","conilon":"786,00"},
"24":{"arabica-dura":"1.338,00","arabica-rio":"1.248,00","conilon":"791,00"},
"25":{"arabica-dura":"1.355,00","arabica-rio":"1.253,00","conilon":"789,00"},
"26":{"arabica-dura":"1.343,00","arabica-rio":"1.251,00","conilon":"792,00"},
"27":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"28":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"29":{"arabica-dura":"1.308,00","arabica-rio":"1.227,00","conilon":"780,00"},
"30":{"arabica-dura":"-","arabica-rio":"-","conilon":"-"},
"Média Mensal":{"arabica-dura":"1.253,68","arabica-rio":"1.172,84","conilon":"770,53"}
}
```
This JSON shows prices of same three types of coffee per day. Prices are presented in simple strings currency format: `1.200,00` to be easily presented in tables. Prices not reported in the source will be displayed as `'-'`.

## Data source

The data is obtained from official site of Centro do Comércio de Café de Vitória: `https://www.cccv.org.br/`.


## Development

EScafeAPI was develepoed by MAVV - Smart Optimization Consulting.
webpage: [mavvsmart.com](https://mavvsmart.com/)

![](https://mavvsmart.com/wp-content/uploads/2021/11/logo_black2-300x100.png)


