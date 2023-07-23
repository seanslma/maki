# mms

AEMO tables

https://github-wiki-see.page/m/UNSW-CEEM/NEMOSIS/wiki/AEMO-Tables

http://www.nemweb.com.au/#mms-data-model

http://www.nemweb.com.au/Data_Archive/Wholesale_Electricity/MMSDM/

https://www.aemo.com.au/Electricity/National-Electricity-Market-NEM/Data/Market-Management-System-MMS/Dispatch

files:
http://nemweb.com.au/Reports/CURRENT/

packages:
http://nemweb.com.au/Reports/Current/MMSDataModelReport/Electricity/MMS%20Data%20Model%20Report_files/MMS_2.htm

table def:
https://www.aemo.com.au/energy-systems/electricity/national-electricity-market-nem/data-nem/market-data-nemweb

list of tables:
https://visualisations.aemo.com.au/aemo/nemweb/MMSDataModelReport/Electricity/MMS%20Data%20Model%20Report_files/MMS_470_8.htm

## prdLoader tables
https://visualisations.aemo.com.au/aemo/di-help/Content/pdrLoader/Database_Tables.htm

## demand data
dispatchis.regionsum\\
marketnet.dispatchregionsum

**InitialSupply** =\\
Sum of InitialMW [Over all Regional Scheduled and Semi-scheduled generating units]\\
+ Net MeteredMWFlow into the Region [Over all Interconnectors connected to the region]

**ClearedSupply** =\\
Sum of TotalCleared [Over all Regional Scheduled and Semi-scheduled generating units]\\
+ Net MWFlow into the Region [Over all Interconnectors connected to the region]

## dispatchscada.unit_scada
contains actual generation data for each
- scheduled generation unit,
- semi-scheduled generation unit, and
- non-scheduled generating units or
- non-scheduled generating systems (a non-scheduled generating system comprising non-scheduled generating units).

This file also contains actual load for each scheduled load.

The actual generation and load data in the file is reported under a column headed 'SCADAVALUE'

## next_day_actual_gen
**Non-Scheduled Generation Data**:\\
The metered power outputs from most large non-scheduled generating units and generating systems, in a daily file covering all intervals of the previous trading day.

The output values are sampled from SCADA at 5-minute intervals and reported under the column headed 'MWH_READING'. These figures should be read as instantaneous power in MW rather than MWh.

## dispatch
Public 5 minute dispatch data by region. Data covers interconnector flows, constraints, regional reference price, demand, dispatchable generation, dispatchable load, and ancillary services data.

For the energy market, the regional reference price (**RRP**) is the spot price.

The regional original price (**ROP**) includes the cost of any constraint violations, and can exceed the Market Price Cap (MPC), in which case it will be automatically revised before it is published as the Regional Reference Price (RRP) for the DI.

## trading
Public 30 minute dispatch data by region. Data covers interconnector flows, regional reference price, demand, dispatchable generation, dispatchable load, and ancillary services data.

## p5min
The five-minute predispatch (P5Min) is a MMS system providing projected dispatch for 12 Dispatch cycles (one hour). The 5-minute Predispatch cycle runs every 5-minutes to produce a dispatch and pricing schedule to a 5-minute resolution covering the next hour, a total of twelve periods.

For each interval_datetime there will be 12 runs with the last run_datetime starting from the interval_datetime.

## predispatchis
30 minute predispatch (forecast) data by region to the end of the next market day (from 1 pm why it goes to the next day), and is updated half hourly.

Regional demand can be calculated as total demand plus dispatchable load (i.e. Regional demand =
Total Demand + Dispatchable Load)

## daily
This file is generated daily, shortly after 0400. It contains **previous day** data for all dispatch and trading intervals. Data provided by generating unit includes initial MW, dispatch targets and ramp rates.

tunit: 30min results (trading)
dunit: 5min results (dispatch)

runno:

intervention:

https://github.com/UNSW-CEEM/NEMOSIS/wiki/Column-Summary

## bids
https://www.aemo.com.au/-/media/Files/Electricity/NEM/5MS/Systems-Workstream/2019/Format-and-Validation-for-Energy-FCAS-and-MNSP-Bids-and-Offers.pdf

For bids data the first period is between 4:00 and 4:05, and usually the datetime is the period_ending time.

There are three types of bids or offers to supply – default bids, daily bids, re-bids:
  - **Default bids** are standing bids that apply where no daily bid has been made. These bids are of a ‘commercialin-confidence’ nature and, in general, reflect the base operating levels for generators.
  - **Daily bids** are submitted before 12:30 pm on the day before supply is required, and are reflected in pre-dispatch forecasts.
  - Generators may submit **re-bids** up until approximately five minutes prior to dispatch. In doing so, they can change the volume of electricity from what it was in the original offer, but they cannot change the offer price.

**Closed Bid**: The latest bid close to the dispatch interval. For each DI, go through the duid BidDayOffer bids and find the bid with the highest firstdispatch <= di (dispatch interval), this is the closed bid. A bid with null (DateTime.MinValue) firstdispatch cannot be a closed bid.

**Valid Bid**: Scan through the bids, whatever has a bidofferdate less than or equal to the closed bid's bidofferdate is a valid bid (even if the firstdispatch field is null).

**Closed Bid Capped**: The bid quantities are limited by the max avail. For scheduled load units as the bids are in the reverse order (from the highest price to the lowest price) so the bid should be capped from highest to lowest bands. Also, if fixedload is not zero, fixedload will be for the first band and all other bands should be zero.

**BIDOFFERFILETRK** shows an audit trail of all files submitted containing an FCAS bid, including corrupt bids and rebids.

**BIDDAYOFFER** is a child table to BIDOFFERFILETRK. **BIDDAYOFFER** shows the Energy and Ancillary Service bid data for each Market Day.

**BIDPEROFFER** is a child table of BIDDAYOFFER. **BIDPEROFFER** shows period-based Energy and Ancillary Service bid data.

Empirical observations of bidding patterns in Australia’s National Electricity Market\\
http://www.ceem.unsw.edu.au/sites/default/files/event/documents/Hu_etal_energy_policy2004.pdf\\
Gen can rebid the quantity for a previously bid settlement interval up to 5 min before dispatch, although the price bands are fixed for the entire settlement day.

Bidding-in-energy-only-wholesale-electricity-markets-Final-report.PDF

**bid splitting**:
- bid a reduced capacity at lower price level to ensure continuous dispatch; and
- bid the remaining capacity at the maximum allowable market price

## mcc_dispatch
Comment Results from the Marginal Constraint Cost (MCC) re-run of the dispatch process. The MCC forms part of the AER's
"Electricity transmission network service providers Service target performance incentive Scheme"

## station mapping
marketnet.dudetailsummary provide duid and station mapping

## terms
DISPATCHABLEGENERATION = Dispatched Generation (Sum of dispatched Scheduled and Semischeduled generation)

## nemreview
nemreview uses intervention = 1 data

## PARTICIPANT_REGISTRATION

PUBLIC_DVD_DUDETAIL_201908010000.zip\\
PUBLIC_DVD_DUDETAILSUMMARY_201908010000.zip\\
http://nemweb.com.au/Data_Archive/Wholesale_Electricity/MMSDM/2019/MMSDM_2019_08/MMSDM_Historical_Data_SQLLoader/DATA/

table: DUDETAIL \\
DUDETAIL sets out a records specific details for each unit including start type and whether normally on or off load. Much of this data is **information only** and **is not used in dispatch or settlements**.

table: DUDETAILSUMMARY \\
reducing the need for participants to use the various dispatchable unit detail and owner tables to establish generating unit specific details.
