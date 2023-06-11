all: clean run
clean:
	docker rm test_doker-app-1
	docker rm test_doker-db-1
	docker rmi test_doker-app 
run:
	docker compose up
