import requests
import rest
import urllib
import traceback,sys
from conjunctive_query import ConjunctiveQueryProcessor
from response_converter import DigOutputProcessor,TimeSeries
import json


class TimeSeriesQueryProcessor(object):
    def __init__(self,request,project_name,config_fields,project_root_name,es):
        self.request = request
        self.config = config_fields
        self.es = es
        self.project_root_name = project_root_name
        self.project_name = project_name
        self.cquery = ConjunctiveQueryProcessor(self.request, self.project_name,
                                          self.config,
                                          self.project_root_name, self.es)
        self.field = request.args.get('_group-by')

    def process_ts_query(self):
        '''
        This is the main function in this class. This calls several functions to validate input, set match clauses, set filter clauses
        set sort clauses and finally resolve any nested documents if needed. Finally this function returns the data as a json or json_lines
        joined by a '\n'
        '''
        # valid_input = self.validate_input()
        # if not valid_input:
        #     err_json = {}
        #     err_json['message'] = "Please enter valid query params. Fields must exist for the given project. If not sure, please access http://mydigurl/projects/<project_name>/fields API for reference"
        #     return rest.bad_request(err_json)

        resp = self.cquery.process()[0]
        # ts,dims = DigOutputProcessor(json.dumps(resp['aggregations'][self.field])).process()
        # dimensions = []
        # dimensions.append("DATE")
        # dimensions.append(dims)
        # ts_obj = TimeSeries(ts, {}, dimensions).to_dict()
        return rest.ok(resp)

    def validate_input(self):
        field = self.request.args.get('_group-by',None)
        if field is None:
            return False
        elif not self.config[field]['type'] == "date":
            return False

        return True