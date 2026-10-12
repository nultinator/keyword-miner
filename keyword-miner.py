import requests, json, time, random, string
from brightdata import SyncBrightDataClient

#initialize a variable to hold your api key
API_KEY = ""

#store your creds in a JSON file, i know everyone else uses environment variables. i don't like os-level global variables
with open("creds.json", "r") as file:
    data = json.load(file)
    #assign your API key to the variable we created
    API_KEY = data["bright_data_api_key"]

#call google's autocomplete for a list of words
def suggest(query, client="firefox", hl="en", gl="us"):
    r = requests.get(
        "https://suggestqueries.google.com/complete/search",
        params={"client": client, "q": query, "hl": hl, "gl": gl},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()[1]


#using a single seed query, generate a list of related queries
def expand(seed, verbose=False):
    results = set(suggest(seed))
    # suffix: "sola scriptura a" ... "sola scriptura z"
    for letter in string.ascii_lowercase:
        results.update(suggest(f"{seed} {letter}"))
        time.sleep(random.uniform(0.3, 0.8))
    # prefix modifiers: question and comparison style keywords
    for mod in ["why", "how", "can", "is", "does", "best", "vs"]:
        results.update(suggest(f"{mod} {seed}"))
        time.sleep(random.uniform(0.3, 0.8))
    sorted_results = sorted(results)
    if verbose:
        print(sorted_results)
    return sorted_results


#for a given query, fetch the top 10 google results
def find_top_ranking_pages(search_query, verbose=False):

    with SyncBrightDataClient(token=API_KEY) as client:

        results = client.search.google(
            query=search_query,
            location="United States",
            language="en",
            num_results=10
        )
        if verbose:
            print(results.data)
        return results.data


#input a list of keywords, find top ranked results, output a list of keywords with their corresponding google results
def mine_top_results(keyword_list, verbose=False):
    final_list = []

    for query in keyword_list:
        top_pages = find_top_ranking_pages(query, verbose=verbose)
        harvested_query = {
            "query": query,
            "top_pages": top_pages
        }
        final_list.append(harvested_query)
    return final_list


#self explanatory: input a base keyword, output a huge list of related keywords and their search results
def generate_keyword_list(base_keyword, verbose=False):
    keywords = expand(base_keyword, verbose=verbose)
    harvested_queries = mine_top_results(keywords, verbose=verbose)
    return harvested_queries


#main program
if __name__ == "__main__":

    #change this to whatever keyword you want
    BASE_KEYWORD = "demonology in the book of enoch"

    #create a full list of keywords and search results
    harvested_queries = generate_keyword_list(BASE_KEYWORD, verbose=True)

    #dump the harvested queries to a json file
    with open("output.json", "w", encoding="utf-8") as file:
        json.dump(harvested_queries, file, indent=4, ensure_ascii=False)