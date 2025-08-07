# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url`

ind_com = url.index(".com")
ind_https = url.index("://")

# Extract the website name in `url` and display it

print(url[ind_https+3:ind_com])