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

## Example usage and output

```
$ python download.py --url="https://example.com/example.jpeg" --count=5

Usage: download.py [OPTIONS]

Error: Invalid value for "--output": Output path needs to exist and be a directory
```

```
$ mkdir images
```

```
$ python download.py --url="https://example.com/example.jpeg" --count=5

Downloaded file: images/example.jpeg
Will now retry download 5 times, every 2 second(s)
Retrying download with ?count=1 appended to the url
Retrying download with ?count=2 appended to the url
Retrying download with ?count=3 appended to the url
Retrying download with ?count=4 appended to the url
Retrying download with ?count=5 appended to the url
```

```
$ tree images

images
├── example.jpeg
├── 1.jpe
├── 2.jpe
├── 3.jpe
├── 4.jpe
└── 5.jpe

0 directories, 6 files
```

The idea being you can then quickly scan the images to see if any of the retrys are different from the original. We needed to do this because some images were being corrupted at some point by our cache and we needed to see if it happened before or after they were entering the cache.