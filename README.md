# README

```
Usage: download.py [OPTIONS]

  Simple program to repeatedly download a file while appending a unique
  query string

Options:
  --url TEXT       URL to download  [required]
  --count INTEGER  Number of times to repeat the download (default: 50).
  --pause INTEGER  Number of seconds to pause between downloads (default: 2).
  --param TEXT     Query param to append to url on each retry (default:
                   count).
  --output TEXT    Where to output the resulting files (default: ./images).
  --help           Show this message and exit.
```