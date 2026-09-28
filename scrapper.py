import requests
from bs4 import BeautifulSoup


def build_search_url(keyword, startno=0):
    return (
        "https://search.incruit.com/list/search.asp"
        f"?col=job&kw={keyword}&startno={startno}"
    )


def search_incruit(keyword, pages = 1):
    jobs = []
    for page in range(pages):
        page = page * 30

        url = build_search_url(keyword, page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("li", class_="c_col")

        for li in lis:
            company = li.find("a", class_="cpname").text
            title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text
            location = li.find("div", class_="cl_md").find_all("span")[0].text
            link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")

            job_data = {
                "company" : company, 
                "title": title, 
                "location": location, 
                "link": link
            }
            jobs.append(job_data)   

    return jobs
