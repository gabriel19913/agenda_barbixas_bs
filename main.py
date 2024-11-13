from bs4 import BeautifulSoup
import requests

url = "https://linktr.ee/barbixas?fbclid=PAZXh0bgNhZW0CMTEAAaYdK97mfNvlWJBDqro1BqkmSB64QSSVaHv0PKg9C1HVcNF3HV6fkYFaZCM_aem_7T-tKOzy5voRAbwOQ-Dzgw"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

all_classes = soup.find_all('a', class_='sc-pFZIQ sc-idOhPF ldGKnQ gjVUqX group')

final_string = ""
for class_ in all_classes:
    link = class_.attrs['href']
    text = class_.text
    final_string = final_string + f"- {text}\n"
    final_string = final_string + f"  - {link}\n"

print(final_string)