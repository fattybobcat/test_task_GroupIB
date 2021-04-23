import aiohttp
import asyncio
import homoglyphs as hg
import string
from itertools import product

domains = ("com", "ru", "net", "org", "info", "cn", "es", "top", "au", "pl",
           "it", "uk", "tk", "ml", "ga", "cf", "us", "xyz", "top", "site",
           "win", "bid")


def add_symbol(word, domains):
    l = [(word+c+"."+dom) for c in string.ascii_lowercase for dom in domains]
    print(l)
    print(len(l))

def lomoglyphs_str(word):
    print("word", word)
    homoglyphs = hg.Homoglyphs(languages={"en"}, strategy=hg.STRATEGY_LOAD)
    return homoglyphs.to_ascii('ХР123.')
   # print("word", word, homoglyphs.to_ascii("asvdsv01"))

    #return homoglyphs.to_ascii(word)

def allocation_subdomain(word):
    l = [word[:i]+'.'+word[i:] for i in range(1,len(word))
         if word[i].isalnum() and word[i-1].isalnum()]
    return l


def del_symbol(word, domains):
    l = [word[:i]+word[i+1] for i in range(len(word))]
    print(l)

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


loop = asyncio.get_event_loop()

coroutines = [get("http://example.com") for _ in range(8)]

results = loop.run_until_complete(asyncio.gather(*coroutines))

print("Results: %s" % results)

w = "dog"
add_symbol(w, domains)

c = "group-ib"
print(allocation_subdomain(c))
asd = 'ХР123.'
print(lomoglyphs_str(asd))

domain_tl = tuple(['.']) + tuple([asd[len(asd) - 1]])
glyphs = []
for c in asd:
    glyphs.append(hg.Homoglyphs(languages={'en'},
                              #  alphabet={"en"},
                                ascii_strategy=hg.STRATEGY_REMOVE,
                               ascii_range=range(ord('0'), ord('z')),
                                ).get_combinations(c))


print(glyphs)
result = []
#if args.idna == "on":
for l in product(*glyphs):
    e = ''.join(l + domain_tl)
    if e not in result:
        result.append(e)
# else:
#     for l in product(*glyphs):
#         e = ''.join(l + domain_tl)
#         if e not in result:
#             result.append(e)


print(result)
print("end")
homoglyphs = hg.Homoglyphs(languages={'en'},
                           strategy=hg.STRATEGY_IGNORE,
                            ascii_strategy=hg.STRATEGY_LOAD,
                           ascii_range=range(ord('0'), ord('z')),
                           )
print(homoglyphs.to_ascii('ХРoO0123.'))
