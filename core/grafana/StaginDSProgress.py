from requests import post, get
from json import loads
from core.settings.local import GRAFANA as token
from django.http import JsonResponse
from core.views import login_customrequired, initRequest,  DateTimeEncoder
from core.libs.exlib import dictfetchall
from django.db import connection
from django.utils import timezone
from datetime import timedelta
from core.settings import defaultDatetimeFormat


def run_query(rules):
    base = "https://monit-grafana.cern.ch"
    url = "api/datasources/proxy/8428/_msearch"

    rulequery = ""
    for rule in rules:
        rulequery += " data.rule_id: %s OR" % rule

    rulequery = rulequery[:-3]
    paramQuery = """{"filter":[{"query_string":{"analyze_wildcard":true,"query":"data.event_type:rule_progress AND (%s)"}}]}""" % rulequery
    query = """{"search_type":"query_then_fetch","ignore_unavailable":true,"index":["monit_prod_rucio_raw_events*"]}\n{"size":500,"query":{"bool":"""+paramQuery+"""},"sort":{"metadata.timestamp":{"order":"desc","unmapped_type":"boolean"}},"script_fields":{},"docvalue_fields":["metadata.timestamp"]}\n"""
    headers = token
    request_url = "%s/%s" % (base, url)
    r = post(request_url, headers=headers, data=query)
    resultdict = {}
    if r.ok:
        results = loads(r.text)['responses'][0]['hits']['hits']
        for result in results:
            dictEntry = resultdict.get(result['_source']['data']['rule_id'], {})
            dictEntry[result['_source']['data']['created_at']] = result['_source']['data']['progress']
            resultdict[result['_source']['data']['rule_id']] = dictEntry
        result = resultdict
    else:
        result = None
    return result

def __getRucioRuleByTaskID(taskid):
    new_cur = connection.cursor()
    new_cur.execute(""" SELECT RSE FROM ATLAS_DEFT.T_DATASET_STAGING where DATASET IN (select PRIMARY_INPUT FROM ATLAS_DEFT.t_production_task where TASKID=%i)""" % int(taskid))
    rucioRule = dictfetchall(new_cur)
    if rucioRule and len(rucioRule) > 0:
        return rucioRule[0]['RSE']
    else:
        return None


def __getRucioRulesBySourceSEAndTimeWindow(source, hours):
    new_cur = connection.cursor()
    new_cur.execute(""" SELECT RSE FROM ATLAS_DEFT.T_DATASET_STAGING where SOURCE_RSE='%s' 
    and START_TIME>TO_DATE('%s','YYYY-mm-dd HH24:MI:SS')""" % (source, (timezone.now() - timedelta(hours=hours)).strftime(defaultDatetimeFormat)))
    rucioRulesRows = dictfetchall(new_cur)
    rucioRules = []
    if rucioRulesRows and len(rucioRulesRows) > 0:
        for rucioRulesRow in rucioRulesRows:
            rucioRules.append(rucioRulesRow['RSE'])
        return rucioRules
    else:
        return None



@login_customrequired
def getStageProfileData(request):
    valid, response = initRequest(request)
    RRules = []
    if 'jeditaskid' in request.session['requestParams']:
        rucioRule = __getRucioRuleByTaskID(int(request.session['requestParams']['jeditaskid']))
        if rucioRule:
            RRules.append(rucioRule)
    elif ('source' in request.session['requestParams'] and 'hours' in request.session['requestParams']):
        RRules = __getRucioRulesBySourceSEAndTimeWindow(
            request.session['requestParams']['source'].strip().replace("'","''"),
            int(request.session['requestParams']['hours']))
    chunksize = 50
    chunks = [RRules[i:i + chunksize] for i in range(0, len(RRules), chunksize)]
    resDict = {}
    for chunk in chunks:
        resDict = {**resDict, **run_query(chunk)}

    return JsonResponse(resDict)

