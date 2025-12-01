# Predispatch

## 30-minute Predispatch (Predispatch)
- https://www.aemo.com.au/-/media/files/electricity/nem/security_and_reliability/power_system_ops/procedures/so_op_3704-predispatch.pdf?la=en
- Runs and is published every 30 minutes
- forecasts out to the end of the next market day (4 AM the following day). It can cover a period of up to 48 hours or more.

## 5-minute Predispatch (P5MIN)
- Runs and is published every 5 minutes
- Forecasts for the next 12 dispatch cycles (one hour)

## Extended Predispatch (PD7Day)
https://www.aemo.com.au/-/media/Files/Electricity/NEM/Emergency_Management/2017/Guide-to-Extended-Predispatch-Report.pdf

## Total demand
https://aemo.com.au/-/media/files/electricity/nem/security_and_reliability/dispatch/policy_and_process/demand-terms-in-emms-data-model.pdf?la=en

Table `dispatchregionsum`:
- NetInterchange: negative for import
- `Gen - NetInterchange(export) = TotalDemand + Load - WDR_Dispatched + AllocatedInterconnectorLosses`

## Energy reserve
`Reserve = AvailGen - NetInterchange (Export) - TotalDemand`

Table `predispatchregionsum`, `p5min_regionsolution`, `dispatchregionsum`: 
- `TOTALDEMAND`: forecast total demand in MW (less normally on loads)
- `AVAILABLEGENERATION`: aggregate generation bid available in the region (MW), the sum of all generation units' available capacity.
- `AVAILABLELOAD`: aggregate load bid available in the region (MW). This primarily refers to `dispatchable load` or `interruptible load` that can be reduced to help balance supply and demand.
- `PREDISPATCHSEQNO` format: `yyyymmddxx`
- `RUN_DATETIME` format: `yyyy-mm-dd 24hh:mi:ss`
- `SETTLEMENT_DATE` format: `yyyy-mm-dd 24hh:mi:ss`

## Regional excess supply
https://www.aemo.com.au/-/media/files/electricity/nem/security_and_reliability/power_system_ops/reserve-level-declaration-guidelines.pdf
Mainland regions:
```
RXS
= + Aggregate Non-Energy Limited Capacity
  + Aggregate Energy Limited Capacity
  - Aggregate Semi-Scheduled Output
  - Net Interconnector Export
  + Aggregate Semi-Scheduled Output
  - Scheduled Demand
= + AvailGen
  - NetInterchange (Export)
  - TotalDemand
```
