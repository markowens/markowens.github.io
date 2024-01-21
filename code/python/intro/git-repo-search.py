import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"


def create_stars_query(languages, min_stars=10000):
    query = f"stars:>{min_stars} "
    for language in languages:
        query += f"language:{language} "
    # a sample query looks like: "stars:>50 language:python language:javascript"
    return query

def create_forks_query(languages, min_forks=1000):
    query = f"forks:>{min_forks} "
    for language in languages:
        query += f"language:{language} "
    # a sample query looks like: "stars:>50 language:python language:javascript"
    return query

def repos_with_most_stars(languages, sort="stars", order="desc"):
    query = create_stars_query(languages)
    params = {"q": query, "sort": sort, "order": order}
    response = requests.get(GITHUB_API_URL, params=params)
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Code: {status_code}.")
    else:
        response_json = response.json()
        return response_json["items"]    

def repos_with_most_forks(languages, sort="forks", order="desc"):
    query = create_forks_query(languages)
    params = {"q": query, "sort": sort, "order": order}
    response = requests.get(GITHUB_API_URL, params=params)
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Code: {status_code}.")
    else:
        response_json = response.json()
        return response_json["items"]  


if __name__ == "__main__":
    #languages = ["python", "javascript", "java"]
    languages = ["python"]
    fork_results = repos_with_most_forks(languages)
    star_results = repos_with_most_stars(languages)

    for result in star_results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]
        print(f"-> {name} is a {language} repo with {stars} stars.")        

    print("-------------------------------")

    for result in fork_results:
        language = result["language"]
        forks = result["forks_count"]
        name = result["name"]
        print(f"-> {name} is a {language} repo with {forks} forks.")                