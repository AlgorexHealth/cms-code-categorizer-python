# cms-code-categorizer-python
##  A set of python functions for categorizing HCPC codes and DRG codes

![ explanation ](cms-categorizer.png)

## Motivation:
Medical claims data often comes with a set of codes:
  * ICD-9 Procedure Codes
  * HCPC/CPT Procedure Codes
  * DRG Codes

These codes are useful for allowing health systems and payers to understand cost.
However, these codes are at too granular a level, so there is a need to agglomerate
these codes into coarser-grain categories.

Once established, these categories represent a new dimension upon which standard reporting
may be run (e.g. `select sum(cost),category from outpatient_billing group by category`).


## Current Mappings Supported:
### From Source
The rules by which these categories are established can be found in many publications.  Our current source for this library is: 
  * [Health Care Cost and Utilization Report: 2011](http://www.healthcostinstitute.org/files/HCCI_HCCUR2011.pdf)

### Mapping Type
Currently we support:
  * DRG -> 
