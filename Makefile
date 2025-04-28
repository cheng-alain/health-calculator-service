.PHONY: init run test build clean

init:
	pip install -r requirements.txt

run:
	python app.py

test:
	python -m unittest test.py

build:
	docker build -t health-calculator-app .

docker-run:
	docker run -p 8000:8000 health-calculator-app

clean:
	rm -rf __pycache__ *.pyc
	rm -f health_app.log

test-bmi:
	curl -X POST -H "Content-Type: application/json" -d '{"height": 1.75, "weight": 70}' http://localhost:8000/bmi

test-bmr:
	curl -X POST -H "Content-Type: application/json" -d '{"height": 175, "weight": 70, "age": 30, "gender": "male"}' http://localhost:8000/bmr