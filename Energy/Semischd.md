# Semi-Scheduled

**Semi-scheduled generating units** are those generating units registered in accordance with NER clause 2.2.7. Generally these generating units will be:
- Greater than 30 MW and
- Intermittent generation (typically, **wind and solar farms**)

The dispatch instruction for a semi-scheduled generating unit requires that unit’s active power output to be capped at the dispatch level set by AEMO only when its semi-dispatch interval flag is set to ‘TRUE’. This is called its “semi-dispatch cap”.

NER 4.9.5(a)(3) also requires AEMO to specify a ramp rate or a specific target time to reach the outcome specified in the dispatch instruction. Absent a specified ramp rate, the semi-scheduled generating unit is expected to ramp linearly from its initial active power output to its semi-dispatch cap applying at the end of the 5-minute dispatch interval, subject to energy availability.

This requirement applies to semi-scheduled generating units that have an active power control system capable of linear ramping as agreed in the relevant performance standard. When the semi-dispatch interval flag is set to ‘FALSE’ the semi-scheduled generating unit is free to generate at any level.
