CREATE TABLE cities (
	id VARCHAR(100) PRIMARY KEY,
	name_ar VARCHAR(100) NOT NULL,
	name_en VARCHAR(100) NOT NULL
);

CREATE INDEX name_ar_idx ON cities(name_ar);
CREATE INDEX name_en_idx ON cities(name_en);

INSERT INTO cities(id, name_ar, name_en) VALUES
("6009d941950ada00061eeeab", "الرياض", "riyadh"),
("6009d942950ada00061eeeac", "جده", "jeddah"),
("5dd49004af8af4002cbfae3a", "الدمام", "dammam"),
("5dd49004af8af4002cbfae4c", "الخبر", "khobar"),
("5dd49004af8af4002cbfae33", "مكة المكرمة", "mekkah"),
("5dd49004af8af4002cbfae3b", "المدينة المنورة", "medina"),
("5dd49004af8af4002cbfae38", "بريدة", "buraidah"),
("5dd49004af8af4002cbfae32", "الطائف", "taif"),
("5dd49004af8af4002cbfae3c", "أبها", "abha"),
("5dd49005af8af4002cbfbc7a", "الأحساء", "ahsa"),
("5dd49004af8af4002cbfae9e", "الجبيل", "jubail"),
("5dd49004af8af4002cbfae6b", "خميس مشيط", "khamis mushait");
