# pydisfish
A teeny Tiny module to check URLs against discord's list of phishing domains


# Using
```py
>>> import pydisfish
>>> phisher = pydisfish.Phisherman()
>>> phisher.check("https://google.com")
False
>>> phisher.check("https://discord-gifte.site/playsds/")
True
```