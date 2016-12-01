# -*- coding: utf-8 -*-

"""
Example code to call Rosette API to get de-compounded words from a piece of text.
"""

import argparse
import json
import os

from rosette.api import API, DocumentParameters, MorphologyOutput, RosetteException


def run(key, altUrl='https://api.rosette.com/rest/v1/'):
    # Create an API instance
    api = API(user_key=key, service_url=altUrl)

    morphology_compound_components_data = "Rechtsschutzversicherungsgesellschaften"
    params = DocumentParameters()
    params["content"] = morphology_compound_components_data
    try:
        return api.morphology(params, MorphologyOutput.COMPOUND_COMPONENTS)
    except RosetteException as e:
        print(e)


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description='Calls the ' + os.path.splitext(os.path.basename(__file__))[0] + ' endpoint')
parser.add_argument('-k', '--key', help='Rosette API Key', required=True)
parser.add_argument('-u', '--url', help="Alternative API URL", default='https://api.rosette.com/rest/v1/')

if __name__ == '__main__':
    args = parser.parse_args()
    result = run(args.key, args.url)
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True).encode("utf8"))
