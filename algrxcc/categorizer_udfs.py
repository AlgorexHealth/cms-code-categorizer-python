import apsw
from . import categorizer as c


def enhance(conn):
    if not isinstance(conn,apsw.Connection):
        raise Exception("this is not a proper connection")
    conn.createscalarfunction("inpatient_mdc_category_by_drg", c.inpatient_mdc_category_by_drg)
    conn.createscalarfunction("inpatient_service_category_by_drg", c.inpatient_service_category_by_drg)
    conn.createscalarfunction("carrier_categorizer_by_hcpc", c.carrier_categorizer_by_hcpc)
    conn.createscalarfunction("outpatient_categorizer_by_hcpc", c.outpatient_categorizer_by_hcpc)
    return conn
