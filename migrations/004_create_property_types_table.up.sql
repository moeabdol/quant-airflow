CREATE TABLE property_types (
	id VARCHAR(100) PRIMARY KEY,
	name_ar VARCHAR(100) NOT NULL,
	name_en VARCHAR(100) NOT NULL,
	category_id VARCHAR(100) NOT NULL REFERENCES categories(id)
);

CREATE INDEX property_types_name_ar_idx ON property_types(name_ar);
CREATE INDEX property_types_name_en_idx ON property_types(name_en);
CREATE INDEX property_types_category_id_idx ON property_types(category_id);
