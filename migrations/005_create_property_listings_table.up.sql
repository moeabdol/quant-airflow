CREATE TABLE property_listings (
	id VARCHAR(100) PRIMARY KEY,
	title TEXT,
	area INT,
	code INT,
	is_authorize_with_rega BOOLEAN,
	payment_method VARCHAR(100),
	price INT,
	price_type VARCHAR(100),
	purpose VARCHAR(100),
	details JSONB,
	category_id VARCHAR(100) NOT NULL REFERENCES categories(id),
	property_type_id VARCHAR(100) NOT NULL REFERENCES property_types(id),
	city_id VARCHAR(100) NOT NULL REFERENCES cities(id),
	district_id VARCHAR(100) NOT NULL REFERENCES districts(id)
);

CREATE INDEX property_listings_category_idx ON property_listings(category_id);
CREATE INDEX property_listings_property_type_idx ON property_listings(property_type_id);
CREATE INDEX property_listings_city_idx ON property_listings(city_id);
CREATE INDEX property_listings_district_idx ON property_listings(district_id);
