# Dependencies
  * TravisPy (pip install travispy)
  * Requests (pip install requests)
  * BeautifulSoup4 (pip install beautifulsoup4)<br>
 
 Python version used 2.7
 
# Info
Regarding temporary testing codes,

the script named google_log_extractor.py is basically a google crawler that fetches the url corresponding to a perticular error type and stores it in a file named result.txt

log_reader then reads the file result.txt fetches the job_id, build_id, repository and logs corresponding to a perticular url.<br>
later on, these logs can be searched for errors + line number in which error exist.

then in order to find corresponding code, github api can be used to fetch code snippet belonging to that build_id. 
