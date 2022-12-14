# global settlement and UFE
https://www.aemc.gov.au/sites/default/files/2018-12/Global%20Settlement%20and%20Market%20Reconciliation%20-%20For%20publication.pdf

https://aemo.com.au/initiatives/major-programs/nem-five-minute-settlement--program-and-global-settlement/global-settlement/how-gs-will-work

https://aemo.com.au/-/media/files/electricity/nem/data/metering/ufe/2022/ufe-report-june-2022.pdf?la=en

## UFE calculation
In accordance with NER 3.15.5, for each local area, the UFE amount for each trading interval is determined by the following formula:
```
UFE = TME – DDME – ADME
```
Where:
- `UFE` is total unaccounted for energy for a local area,
- `TME` is total energy inflows into a local area from transmission connection points,
- `DDME` is cross boundary energy flow between adjacent distribution networks. DDME is a positive value for the supplying distribution local area and a negative value for the receiving distribution local area, and
- `ADME` is the aggregate of energy flows for each connection point in a local area.
UFE, TME, DDME and ADME information is available from the RM 46 Report for financially responsible Market Participants (FRMPs) and Local Network Service Provides (LNSPs).

## UFE allocation
The allocation of UFE for every distribution network connection point in a local area is determined by the following formula:
```
UFEA = UFE x (DME/ADMELA)
```
Where:
- `UFEA` is the allocation of local area unaccounted for energy for a connection point,
- `DME` is the load component (ME- x DLF) at a connection point in the local area,
- `ME-` is load component as recorded in the metering data at a connection point in the local area,
- `DLF` is the distribution loss factor applicable at a connection point in the local area, and
- `ADMELA` is the aggregate of all DME amounts in a local area for which a Market Customer is financially responsible

## UFE Factor (UFEF)
The UFE Factor (UFEF) is used to facilitate the allocation of UFE to individual connection points.
```
UFEF = UFE/ADMELA
```
Where:
- `UFE` is total unaccounted for energy for a local area, and
- `ADMELA` is the aggregate of all DME amounts in a local area for which a Market Customer is financially responsible
- `UFEA = UFE x (DME/ADMELA)`, or can be expressed as `UFEA = DME x (UFE/ADMELA)`, therefore `UFEA = DME x UFEF`
UFEF and ADMELA are available from the RM 46 Report. UFEF is also available from the RM 43 Report.
