CREATE TABLE categories (
	id VARCHAR(100) PRIMARY KEY,
	name_ar VARCHAR(100) NOT NULL,
	name_en VARCHAR(100) NOT NULL
);

CREATE INDEX categories_name_ar_idx ON categories(name_ar);
CREATE INDEX categories_name_en_idx ON categories(name_en);
