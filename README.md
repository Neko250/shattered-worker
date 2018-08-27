# shattered-worker

this little worker will perform some management tasks for [my blog](https://shatteredcontinuum.tumblr.com)

## setup

- go to [tumblr api console](https://api.tumblr.com/console)
- create an app and retrieve consumer credentials
- return to the tumblr api console
- provide consumer credentials to obtain oauth tokens
- then:

```bash
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
cp config.template.json config.json
vim config.json
python shattered-worker.py
```
