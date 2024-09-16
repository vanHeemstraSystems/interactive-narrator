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

If no error, continue:

```
$ pip install -U pip setuptools wheel
```

Install spacy:

```
$ pip install -U spacy
```

Run the following command which will download the [spacy](https://spacy.io/usage/models) NLP language model.

```
$ python -m spacy download en_core_web_md
```

**WARNING**: You may encounter the following:

```
/home/gitpod/.pyenv/versions/3.12.6/bin/python3: No module named spacy
```

If so, make sure you have ran ```$ pip install -U spacy```. Then try again.

OPTIONAL: The [spaCy VSCode Extension](https://github.com/explosion/spacy-vscode) provides additional tooling and features for working with spaCy’s config files. 

Optional, run below command to comply with SpaCy VS Code extension:

```
$ pip install -U pygls
```


MORE