# facebook-dl
> Download facebook videos from your terminal

<p align="center">
<a href="https://asciinema.org/a/n31XoO37sBA2ayX2TLZiNgbWt">
<img src="https://user-images.githubusercontent.com/27065646/42167369-2f894e5a-7e0e-11e8-9f6e-ab15da00283d.png">
</a>
</p>

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
