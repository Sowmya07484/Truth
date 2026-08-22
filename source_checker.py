from urllib.parse import urlparse

trusted_sources = [
    "bbc.com",
    "reuters.com",
    "theguardian.com",
    "nytimes.com",
    "cnn.com",
    "aljazeera.com",
    "washingtonpost.com",
    "bloomberg.com",
    "forbes.com",
    "economist.com",
    "abcnews.go.com",
    "nbcnews.com",
    "cbsnews.com",
    "apnews.com",
    "newsweek.com",
    "time.com",
    "thehindu.com",
    "timesofindia.indiatimes.com",
    "hindustantimes.com",
    "indianexpress.com",
    "deccanchronicle.com",
    "telegraphindia.com",
    "theprint.in",
    "scroll.in",
    "firstpost.com",
    "ndtv.com",
    "indiatoday.in",
    "aajtak.in",
    "republicworld.com",
    "zeenews.india.com",
    "news18.com",
    "timesnownews.com",
    "wionews.com",
    "tv9telugu.com",
    "tv9.com",
    "tv5news.in",
    "ntvtelugu.com",
    "sakshi.com",
    "abntelugutv.com",
    "eenadu.net",
    "v6velugu.com",
    "dailyhunt.in",
    "inshorts.com"
]

unreliable_sources = [
    "fakenews.com",
    "clickbaitnews.com",
    "rumornews.net",
    "viraltruthdaily.com",
    "shockingnews247.com",
    "worldrumorsdaily.net",
    "instantviralnews.com",
    "globalviralstories.com",
    "buzzbreakingnews.com",
    "dailyviralnow.com"
]

def check_source(url):

    try:
        domain = urlparse(url).netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        for site in trusted_sources:
            if site in domain:
                return "✅ Trusted News Source"

        for site in unreliable_sources:
            if site in domain:
                return "⚠️ Potentially Unreliable Source"

        return "ℹ️ Source not in database — verify manually"

    except:
        return "❌ Invalid URL"