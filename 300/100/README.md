# 100 - Installation

From the root of the repository (opened in GitPod) run the following command which will install all the required packages):

```
$ pip install -r requirements.txt
```

**WARNING**: You may encounter the following: 

```
AttributeError: module 'configparser' has no attribute 'SafeConfigParser'. Did you mean: 'RawConfigParser'?
```

We do **not** have a solution for above error as of yet. :(

If not error, continue:

Run the following command which will download the [spacy](https://spacy.io/usage/models) NLP language model.

```
$ python -m spacy download en_core_web_md
```

**WARNING**: You may encounter the following:

```
/home/gitpod/.pyenv/versions/3.12.6/bin/python3: No module named spacy
```

We do **not** have a solution for above error as of yet. :(



MORE