deletedb:
	rm -f "${AIRFLOW_HOME}/dealapp.db"

migrateup:
	migrate -path "${AIRFLOW_HOME}/migrations" -database "${DB_DIALECT}://${DB_NAME}?_auth_user=${DB_USERNAME}&_auth_pass=${DB_PASSWORD}" -verbose up

migratedown:
	migrate -path "${AIRFLOW_HOME}/migrations" -database "${DB_DIALECT}://${DB_NAME}?_auth_user=${DB_USERNAME}&_auth_pass=${DB_PASSWORD}" -verbose down

.PHONY: deletedb migrateup migratedown
