import wikipedia 

def scrape(name='Microsoft', length=2):
    result = wikipedia.summary(name, sentences=length)
    return result

print(scrape("facebook", 3))
