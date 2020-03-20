import requests
import json
def get_stats(type='latest'):
    if type=='latest':
        URI = 'https://api.rootnet.in/covid19-in/stats/latest'
    else:
        URI = 'https://api.rootnet.in/covid19-in/stats/daily'
    data = requests.get(URI)
    data = json.loads(data.text)
    report_date = data["lastOriginUpdate"][:10]
    data = data["data"]
    return data,report_date




from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    data,report_date = get_stats()
    return render_template('main/index.html',
                           title='COVID19 - THE INDIA STATS',data=data,report_date=report_date)
