# tomarkdown

## Getting Started

### Installation

```bash
git clone https://gitlab.com/berlinade/tomarkdown.git
cd tomarkdown
pip install -e .
```

### Usage

... *under construction*

but in short: **look at** demo1.py as well as my_script.py in the "demo" folder. 
The demo1.py scripts imports and initiates the tomarkdown package to generate:

  - my_script.md
  - my_script.TopLevel.md
  - my_script.TopLevel.MidLevel.md

for the documentation of my_script.py.
Finally the mkdocs.yml has been adjusted by hand to include the generated markdown scripts and then Mkdocs does its thing.
You can see teh results for yourself here: [https://berlinade.gitlab.io/tomarkdown](https://berlinade.gitlab.io/tomarkdown/)

## Return to repo

the repository can be found here: [tomarkdown](https://gitlab.com/berlinade/tomarkdown)

## License

this version of the "tomarkdown" has been published under GPLv3 (see [LICENSE](https://gitlab.com/berlinade/tomarkdown/-/blob/main/LICENSE)). 
