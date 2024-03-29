
from google.cloud import talent
import six

def search_jobs(project_id, tenant_id, query):
    """
    Search Jobs with histogram queries

    Args:
      query Histogram query
      More info on histogram facets, constants, and built-in functions:
      https://godoc.org/google.golang.org/genproto/googleapis/cloud/talent/v4beta1#SearchJobsRequest
    """

    client = talent.JobServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # query = 'count(base_compensation, [bucket(12, 20)])'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode("utf-8")
    if isinstance(tenant_id, six.binary_type):
        tenant_id = tenant_id.decode("utf-8")
    if isinstance(query, six.binary_type):
        query = query.decode("utf-8")
    #parent = f"projects/{project_id}/tenants/{tenant_id}"
    parent = f"projects/{project_id}"
    domain = "www.example.com"
    session_id = "Hashed session identifier"
    user_id = "Hashed user identifier"
    request_metadata = {"domain": domain, "session_id": session_id, "user_id": user_id}
    #histogram_queries_element = {"histogram_query": query}
    #histogram_queries = [histogram_queries_element]

    # Iterate over all results
    results = []
    request = talent.SearchJobsRequest(
        parent=parent,
        #query=query,
        request_metadata=request_metadata,
        #histogram_queries=histogram_queries,
    )
    for response_item in client.search_jobs(request=request).matching_jobs:
        print("Job summary: {response_item.job_summary}")
        print("Job title snippet: {response_item.job_title_snippet}")
        job = response_item.job
        #results.append(job)
        print("Job name: {job.name}")
        print("Job title: {job.title}")
    return results




if __name__ == "__main__":
    search_jobs("searchjobs-357615", "", "backend python")