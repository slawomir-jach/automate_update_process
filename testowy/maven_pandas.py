import pandas as pd


tables = pd.read_html("https://maven.apache.org/download.cgi")

print(tables[1])

#curl    https://api.github.com/repos/apache/maven/tags/
