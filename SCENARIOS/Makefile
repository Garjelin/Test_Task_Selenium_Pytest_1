.PHONY: run html_report clean

run_chrome:
	pytest -o log_cli=true --log-file=test.log main_chrome.py

run_firefox:
	pytest -o log_cli=true --log-file=test.log main_firefox.py

html_report_chrome:
	pytest -o log_cli=true --log-file=test.log --html=report_chrome.html main_chrome.py

html_report_firefox:
	pytest -o log_cli=true --log-file=test.log --html=report_firefox.html main_firefox.py

open_report_chrome:
	xdg-open report_chrome.html

open_report_firefox:
	xdg-open report_firefox.html

clean:
	rm -rf test.log
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf ../LIB_PAGES/__pycache__
	rm -rf assets
	rm -rf report_chrome.html
	rm -rf report_firefox.html
	rm -rf *.exe
