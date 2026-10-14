## Installation

Clone the repo

```shell
git clone https://github.com/nultinator/keyword-miner/
```

`cd` into the project folder.

```shell
cd keyword-miner
```
Install dependencies

```shell
pip install -r requirements.txt
```

Make sure to swap out the API key with your own.

If you need a Bright Data API key, you can get one [here](https://get.brightdata.com/serp-api-jake-nulty). Full disclosure, I do get a commission for referrals.

```json
{
    "bright_data_api_key": "<your-bright-data-api-key>"
}
```

## Running the keyword miner

Run the script and pass your seed phrase in as an argument.

```shell
python keyword-miner.py "book of enoch"
```


## Output

Each run generates a report with a JSON list of keywords with actual search rankings.

If your list of generated keywords is long, it may be as short as two minutes or as long as an hour.

Total runtime is completely dependent on the size of the expanded keyword list.

```json
[
    {
        "query": "and the book of enoch",
        "top_pages": [
            {
                "position": 1,
                "title": "The Complete Book of Enoch, Standard English Version",
                "url": "https://ia800903.us.archive.org/25/items/TheCompleteBookOfEnochStandardEnglishVersionJayWinter/The%20Complete%20Book%20of%20Enoch%2C%20Standard%20English%20Version%20-%20Jay%20Winter.pdf",
                "description": "The theme of the Book of Enoch dealing with the nature and deeds of the fallen angels. The book written by Enoch − Enoch indeed wrote this complete doctrine of ...",
                "displayed_url": "https://ia800903.us.archive.org › items › The Co..."
            },
            {
                "position": 2,
                "title": "Book of Enoch",
                "url": "https://en.wikipedia.org/wiki/Book_of_Enoch",
                "description": "The Book of Enoch contains unique material on the origins of demons and Nephilim, why some angels fell from heaven, an explanation of why the Genesis flood was ...Read more",
                "displayed_url": "https://en.wikipedia.org › wiki › Book_of_Enoch"
            },
...
```
