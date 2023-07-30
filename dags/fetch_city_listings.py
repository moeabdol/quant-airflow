"""
Fetch listings per city
"""
import json
from sqlalchemy import create_engine, text, insert, Table, Column, Integer, String, MetaData, Boolean, JSON
from requests import get


meta = MetaData()

property_listings_table = Table(
    'property_listings', meta,
    Column('id', String, primary_key=True),
    Column('title', String),
    Column('area', Integer),
    Column('code', Integer),
    Column('is_authorize_with_rega', Boolean),
    Column('payment_method', String),
    Column('price', Integer),
    Column('price_type', String),
    Column('purpose', String),
    Column('details', JSON),
    Column('category_id', String),
    Column('property_type_id', String),
    Column('city_id', String),
    Column('district_id', String)
)

def fetch_city_listings(name):
    """ fetch_city_listings() Task """
    engine = create_engine("sqlite+pysqlite:////home/moeabdol/Documents/quant-airflow/dealapp.db", echo=True)
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT id FROM cities where name_en='{name}'"))
        city_id, *_ = result.first()
        result = conn.execute(text(f"SELECT id FROM districts where city_id='{city_id}'"))
        district_ids = result.all()

        for did in district_ids:
            district_id, *_ = did
            has_next = True
            next_page = 1
            limit = 10
            while has_next:
                params = {
                    "page": next_page,
                    "limit": limit,
                    "city": city_id,
                    "district": district_id,
                }
                url = "https://dealapp.sa/api/ad"
                res = get(url=url, params=params, timeout=5)
                data = json.loads(res.text)["data"]

                for d in data:
                    stmt = insert(property_listings_table).values(
                        id=d.get("_id"),
                        title=d.get("title"),
                        area=d.get("area"),
                        code=d.get("code"),
                        is_authorize_with_rega=d.get("isAuthorizedWithREGA"),
                        payment_method=d.get("paymentMethod"),
                        price=d.get("price"),
                        price_type=d.get("priceType"),
                        purpose=d.get("purpose"),
                        details=d.get("relatedQuestions"),
                        category_id=d.get("propertyType").get("category").get("_id"),
                        property_type_id=d.get("propertyType").get("_id"),
                        city_id=city_id,
                        district_id=district_id
                    )
                    conn.execute(stmt)

                if res.json()["hasNextPage"] == "true":
                    has_next = True
                    next_page = res.json()["nextPage"]
                else:
                    has_next = False


if __name__ == "__main__":
    fetch_city_listings("riyadh")
