from ..base import _call, _get_read_access_token

'''
All api requests under the companies tab in https://developers.themoviedb.org/3/companies
'''

def details(company_id):
    '''
    Get a companies details by id.

    required: company_id 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/company/{company_id}', headers=headers)

def alternative_names(company_id):
    '''
    Get the alternative names of a company.

    required: company_id 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/company/{company_id}/alternative_names', headers=headers)

def images(company_id):
    '''
    Get a companies logos by id.

    There are two image formats that are supported for companies, PNG's and SVG's.
    You can see which type the original file is by looking at the file_type field.
    We prefer SVG's as they are resolution independent and as such, the width and height are only there to reflect the original asset that was uploaded.
    An SVG can be scaled properly beyond those dimensions if you call them as a PNG.

    For more information about how SVG's and PNG's can be used, take a read through https://developers.themoviedb.org/3/getting-started/images.

    required: company_id 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/company/{company_id}/images', headers=headers)
