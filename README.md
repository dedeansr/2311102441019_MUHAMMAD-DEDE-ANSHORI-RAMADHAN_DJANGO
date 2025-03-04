# 🚀 Django Project
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](#)
## 🧑🏻‍💻 Description
Project ini adalah perjalanan panjang saya mempelajari Django yang berisikan cara membuat sebuah framework jaringan website, yang digunakan untuk keberlangsungan website itu sendiri.
## 💻 How to run it!
```yaml
name: "size"
on:
  pull_request:
    branches:
      - master
jobs:
  size:
    runs-on: ubuntu-latest
    env:
      CI_JOB_NUMBER: 1
    steps:
      - uses: actions/checkout@v1
      - uses: andresz1/size-limit-action@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
```
## 💡 Fun Fact!
Django digunakan untuk membuat website besar seperti Instagram, Spotify & Dropbox lho. 
