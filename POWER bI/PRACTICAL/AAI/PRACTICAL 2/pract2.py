import pyshorteners 
def shortener_url(old_url): 
    s = pyshorteners.Shortener() 
    new_url = s.tinyurl.short(old_url) 
    return new_url 
old_url = input("Enter the url:") 
result = shortener_url(old_url) 
print(f"result url=",{result}) 
print("result url = ",result) 
