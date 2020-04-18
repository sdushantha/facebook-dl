# facebook-dl
<p align="center">
  Very <b>minimal</b> Facebook downloader written in <b>28 lines</b> of Python code (not including comments and blank spaces)
 </p>

<p align="center">
<img src="https://user-images.githubusercontent.com/27065646/79065713-ba4f3f00-7cb2-11ea-9c08-61842fcc6791.gif" width="90%" height="90%">
</p>

[![Support me!](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/XoJfSVI)

## Installation

```bash
# clone the repo
$ git clone https://github.com/sdushantha/facebook-dl.git

# install the requirements
$ pip3 install -r requirements.txt
```

## Usage
```
usage: facebook-dl.py [-h] url [resolution]
```

---
Download video in High Definition.
```bash
$ python3 facebook-dl.py https://www.facebook.com/nike/videos/10155846581253445/ hd
```
OR
```bash
# Without mentioning the resolution will also download in HD
$ python3 facebook-dl.py https://www.facebook.com/nike/videos/10155846581253445/
```
Download video in Standard Definition.
```bash
$ python3 facebook-dl.py https://www.facebook.com/nike/videos/10155846581253445/ sd
```

## License
MIT License

Copyright (c) 2018 Siddharth Dushantha
