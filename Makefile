include .envrc

deletedb:
	rm -f ./dealapp.db

migrateup:
	migrate -path ./migrations -database "$(DB_DIALECT)://$(DB_NAME)?_auth_user=$(DB_USERNAME)&_auth_pass=$(DB_PASSWORD)" -verbose up

migratedown:
	migrate -path ./migrations -database "$(DB_DIALECT)://$(DB_NAME)?_auth_user=$(DB_USERNAME)&_auth_pass=$(DB_PASSWORD)" -verbose down

.PHONY: migrateup migratedown
