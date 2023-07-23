# dispatch

when a unit failed to conform (compliance) the dispatch target, it may need pay infringement notice.

Two trigger mechanisms are utilised to identify the severity of Non-Compliance. These are the Small Error Trigger and the Large Error Trigger.

## pre-dispatch process
https://www.aemo.com.au/media/Files/Other/electricityops/0140-0040%20pdf.pdf

## The semi-dispatch process
why solar farms are only subject to the ramp down constraint, not the ramp up constraint in dispatch?

why most of the time of solar farm's output is constrained by the dispatch target, seems there are no binding constraints?

https://www.aemo.com.au/-/media/Files/Electricity/NEM/Security_and_Reliability/Power_System_Ops/Procedures/SO_OP_3705---Dispatch.pdf

The National Electricity Market Dispatch Engine (NEMDE) will dispatch the semi-scheduled generating unit in a similar manner to a normal scheduled generating unit based on the **bid** information provided and the **UIGF** provided from AWEFS/ASEFS, with the only difference being that a **semi-scheduled cap flag** (semi-dispatch interval flag) will also be provided. This flag may be set on the basis of constraint limitations or bidding reasons.

If this cap is set to false then the intermittent generator is not required to follow dispatch targets and will not be considered by the non-compliance monitor. If the flag is set to true then the intermittent generator is required to follow the dispatch target only in that its output must not exceed the dispatch target value and will be monitored by the non-compliance monitor.

The “semi-dispatch compliance” requirement flag is set when either one of the following conditions is satisfied:
  * Dispatch Cap limited by Binding or Violated Network or FCAS Constraint
  * The generating unit’s forecast output (its dispatch cap) is explicitly limited by any binding or violated network or FCAS constraint equation, and if the actual output were to exceed the dispatch cap value this would result in violating (or further violating) that network or FCAS constraint equation; OR
  * Dispatch Cap otherwise below the Unit’s unconstrained intermittent generation forecast
    * The generating unit’s forecast output (its dispatch cap) is not explicitly limited by a binding or violated network constraint equation, BUT
    * The generating unit’s dispatch cap is less than its unconstrained intermittent generation forecast as a result of either a purely inter-regional limitation, or an offer or marketrelated limitation, the latter including:
      * Unit Ramp Rate
      * Unit Fixed Loading Level
      * Non-dispatch of uneconomic price bands
      * Marginal dispatch of economic price bands

if uigf (forecast, avail) is too low, the target (totalcleared) will be constrainted by ramp down rate, so target > avail. In this interval, the semicap flag = false, the actual generation can be lower or higher than the target.

## terms
**INITIALMW** is the SCADA metered value nearest to the 5-minute interval at the time of running NEMDE.

**TOTALCLEARED** is the dispatch target for the end of this dispatch interval (DI).

**AVAILABILITY** appears to be the Australian Solar Energy Forecasting System (ASEFS) forecast for the next 5-minutes ahead
