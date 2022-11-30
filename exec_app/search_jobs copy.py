import os

from googleapiclient.discovery import build
from googleapiclient.errors import Error

client_service = build('jobs', 'v3')
project_id = 'projects/' + os.environ['GOOGLE_CLOUD_PROJECT']

# 1) Define RequestMetadata object
request_metadata = {
    'domain':     'example.com',
    'session_id': 'a5ed434a3f5089b489576cceab824f25',
    'user_id':    '426e428fb99b609d203c0cdb6af3ba36',
}

try:
    # 2) Throw RequestMetadata object in a request
    request = {
        'request_metadata': request_metadata,
    }

    # 3) Make the API call
    response = client_service.projects().jobs().search(
        parent=project_id, body=request).execute()

    # 4) Inspect the results
    if response.get('matchingJobs') is not None:
        print('Search Results:')
        for job in response.get('matchingJobs'):
            print('%s: %s' % (job.get('job').get('title'),
                                job.get('searchTextSnippet')))
    else:
        print('No Job Results')

except Error as e:
    # Alternate 3) or 4) Surface error if things don't work.
    print('Got exception while searching')
    raise e


if __name__ == "__main__":
    search_jobs("searchjobs-357615", "", "backend python")