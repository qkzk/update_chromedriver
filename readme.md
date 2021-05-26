---
title: "Automatically update ChromeDriver"
author: "qkzk"
date: "2021/05/26"

---

# Automatically Update ChromeDriver

Since I use selenium in some scripts and became annoyed to have to update ChromeDriver
in every project as soon as Chrome is updated I wrote this simple script.

It's quite basic, just change the destination folder to what you need and run the script.

```bash
$ python update_chromedriver.py
```

## How to always use the latest downloaded version in your scripts ?

Just create a link to the last file you downloaded to the virtual environment binaries
of your project.

## Credits

[pavelsaman's answer on StackExchange](https://sqa.stackexchange.com/a/41929)


