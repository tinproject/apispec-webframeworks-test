# apispec-webframeworks Documented Blueprint test

This is a dumb repo with some code to test and look the DocumentedBlueprint feature proposed at https://github.com/marshmallow-code/apispec-webframeworks/pull/27


### How to run:
```bash
python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=app
export FLASK_ENVIRONMENT=development

flask run
```

Open http://localhost:5000/url-map in a browser.
