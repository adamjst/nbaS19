runall:
	python step1_webscrape.py
	python step2_localscrape.py
	python step3_concatenator.py
	python step4_splitdate.py

install:
	mkdir data
	mkdir processed
	mkdir html
	mkdir csv
	mkdir outputs

clean:
	rm data/*.csv
	rm data/*.html
	rm data/html/*.html
	rm data/outputs/*.csv
