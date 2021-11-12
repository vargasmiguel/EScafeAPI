# EScafeAPI

## About
This is a simple API to get coffe prices in Vitoria Espiritu Santo, Brazil. It was develeped in Pytohn with FastAPI and deployed in Heroku.

##Usage
The API is deployed in 'https://escafeapi.herokuapp.com/'. You can request coffe's prices of a specific day by adding the date in format `DD-MM-YYYY`.

Example
```
https://escafeapi.herokuapp.com/10-11-2021
```

The response is the following JSON:
```
{"arabica-dura":"R$ 1.208,00","arabica-rio":"R$ 1.136,00","conilon":"R$ 765,00"}
```

This JSON shows prices of three types of coffee:

*`arabica-dura`: Bebida "dura", bica corrida, máx. de 20% de "cata", mín. de 30% de peneira 17 acima.
*`arabica-rio`: Bebida "rio", bica corrida, máx. de 30% de "cata", mín. de 30% de peneira 17 acima.
*`conilon`: Bica corrida, tipo 7/8, com até 13% de umidade e até 5% de broca.

Prices are presented as strings in BRL currency format: `R$ 1.200,00`.

**IMPORTANT NOTE: Only prices for days of the current month can be requested. **

## Data

The data is obtained from official site of Centro do Comércio de Café de Vitória: `https://www.cccv.org.br/`

