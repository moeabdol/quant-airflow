CREATE TABLE districts (
	id VARCHAR(100) PRIMARY KEY,
	name_ar VARCHAR(100) NOT NULL,
	name_en VARCHAR(100) NOT NULL,
	city_id VARCHAR(100) NOT NULL REFERENCES cities(id),
	region_id VARCHAR(100)
);

CREATE INDEX district_name_ar_idx ON districts(name_ar);
CREATE INDEX district_name_en_idx ON districts(name_en);
CREATE INDEX district_city_id_idx ON districts(city_id);
CREATE INDEX district_region_id_idx ON districts(region_id);
