run:
	docker-compose run python python main.py
bash:
	docker-compose run python bash
build:
	docker-compose build

fix-lint:
	docker-compose run python autopep8 --in-place --aggressive --aggressive main.py
lint:
	docker-compose run python pycodestyle main.py

pip-install:
	docker-compose run python pip install -r ./requirements.txt
# 不要なイメージと使われていないvolumeを削除
clean:
	docker image prune
	docker volume prune
	docker rmi -f `docker images -f "dangling=true" -q`