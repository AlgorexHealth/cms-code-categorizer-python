# cms-code-categorizer-python
##  A set of python functions for categorizing HCPC codes and DRG codes

![ explanation ](cms-categorizer.png)

## Motivation:
Medical claims data often comes with a set of codes:
  * ICD-9 Procedure Codes
  * HCPC/CPT Procedure Codes
  * DRG Codes

These codes are useful for allowing health systems and payers to understand cost.
However as these codes are at a granular level sometimes there is a need to agglomerate
them into coarser-grain categories.

Once established, these categories represent a new dimension upon which standard reporting
may be run (e.g. `select sum(cost),category from outpatient_billing group by category`).

This package is a set of python functions that take in these codes and provide
a category according to a deterministic mapping.

## Mapping Types
Though the concept of a mapping is sufficiently easy to understand, there will
be many options to choose from due to the multiplicative nature of the type of mapping
and the source and version of the mapping rules.

The rules by which these categories are established can be found in many publications.  

### Source(s)
Our current source for this library is: 
  * **HCIC Source**:  [Health Care Cost and Utilization Report: 2011](http://www.healthcostinstitute.org/files/HCCI_HCCUR2011.pdf)

### Mapping Type
Currently we support:
  * DRG -> MDC (Medical Diagnostic Category)
  * DRG -> Inpatient Service Category
  * HCPC -> Outpatient Service Category
  * HCPC -> Professional Services Category (for carrier files) 

## Function Mapping and API

The following tables list the relevant python functions found in `categorizer.py` that you, as a developer, will need.  All you need to do is pass in your appropriate code.

The API is fairly simple and relies on strings:
```
category = carrier_categorizer_by_hcpc("0016T")
```

The above snippet of code will return the category `Surgery` (as a string) as per the HCIC2011 specification.

### DRG
<table>
  <th>Source</th>
  <th>Inpatient Service Category</th>
  <th>Medical Diagnostic Category</th>
  <tr>
    <td>HCIC2011</td>
    <td><code>inpatient_service_category_by_drg(drg)</code></td>
    <td><code>inpatient_mdc_category_by_drg(drg)</code></td>
  </tr>
</table>

### HCPC
<table>
  <th>Source</th>
  <th>Outpatient Service Category</th>
  <th>Professional Services Category</th>
  <tr>
    <td>HCIC2011</td>
    <td><code>outpatient_categorizer_by_hcpc(hcpc)</code></td>
    <td><code>carrier_categorizer_by_hcpc(hcpc)</code></td>
  </tr>
</table>

## Lower level API and Creating and Contributing your own Mapping

![ yourown ](creating-your-own.png)
