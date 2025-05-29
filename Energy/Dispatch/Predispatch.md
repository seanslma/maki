# Predispatch

## 30-minute Predispatch (Predispatch)
- Runs and is published every 30 minutes
- forecasts out to the end of the next market day (4 AM the following day). It can cover a period of up to 48 hours or more.

## 5-minute Predispatch (P5MIN)
- Runs and is published every 5 minutes
- Forecasts for the next 12 dispatch cycles (one hour)

## Energy reserve
`Reserve = AvailGen + AvailLoad - TotalDemand`

Table `predispatchregionsum`, `p5min_regionsolution`, `dispatchregionsum`: 
- `TOTALDEMAND`: forecast total demand in MW (less normally on loads)
- `AVAILABLEGENERATION`: aggregate generation bid available in the region (MW), the sum of all generation units' available capacity.
- `AVAILABLELOAD`: aggregate load bid available in the region (MW). This primarily refers to `dispatchable load` or `interruptible load` that can be reduced to help balance supply and demand.
- `PREDISPATCHSEQNO` format: `yyyymmddxx`
- `RUN_DATETIME` format: `yyyy-mm-dd 24hh:mi:ss`
- `SETTLEMENT_DATE` format: `yyyy-mm-dd 24hh:mi:ss`
