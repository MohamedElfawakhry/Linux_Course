#python code to post on facebook page
import requests
response = requests.post("https://graph.facebook.com/107251262368598/feed?message=My First Post with python!&access_token=EAAOZBlPg2m1YBAMXBvw6ToRjcnLVXuZBpCwkRJuu0iMVhSZA3infwLQjcozXHCq4iTPSQ8Hi84Kv4axgPNTgtlzjaFRBerQfZAvYVwIEcxuzQyXLLfpkba3OnPVYm2RIfLIHXxhZBh5WKuOAxYwuEnqwMTZBfwdZBIkuvXpK9P9gScq3Dk2bpQOcgDFfV5ICTvf4JSJ3qagvKL8yZBQLQoy9")
print(response.json())