pages-help:
	python -m htmlscreenshot

pages-demo:
	python -m htmlscreenshot 'sample.txt'


page-help:
	python -m htmlscreenshot.scrape

page-demo:
	python -m htmlscreenshot.scrape 'https://www.python.org'
