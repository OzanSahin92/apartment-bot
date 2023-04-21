# apartment-bot
==============================

Simple python bot to check known sites for apartments

Project Organization
------------

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── pyproject.toml     <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with poetry
    │
    └── apartment_bot      <- Source code for use in this project.
        └── __init__.py    <- Makes apartment-bot a Python module
 


--------

## python

* install conda with

```
 wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh

 bash Anaconda3-2020.11-Linux-x86_64.sh
```

* after that, the following should be in .bashrc

```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('~/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "~/anaconda3/etc/profile.d/conda.sh" ]; then
        . "~/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="~/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```
* this could lead to conda activating automatically, which can be stopped with the following command

```
conda config --set auto_activate_base false
```

* now, create a conda env based on environment.yml and the installation dependencies in it

```
conda env create -f environment.yml
```
* the created env can now be activated or deactivated
```
conda activate <name of env in environment.yml>

conda deactivate
``` 

## important links

- https://pretagteam.com/question/python-selenium-solve-geetest-captcha-how-to-use-callback-function-to-submit-answer

## to-dos
- solve CAPTCHA with selenium 

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a> and the <a target="_blank" href="https://github.com/khuyentran1401/data-science-template">cookiecutter data science project template by khuyentran1401</a>. #cookiecutterdatascience</small></p>