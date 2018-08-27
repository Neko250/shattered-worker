# shattered-worker

this little worker will perform some management tasks for [my blog](https://shatteredcontinuum.tumblr.com)

## setup

```bash
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
cp config.template.json config.json
vim config.json
python shattered-worker.py
```
