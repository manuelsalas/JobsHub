from google.cloud import talent

def sample_list_jobs():
    # Create a client
    client = talent.JobServiceClient()

    # Initialize request argument(s)
    request = talent.ListJobsRequest(
        parent="projects/searchjobs-357615",
        filter="backend python",
    )

    # Make the request
    page_result = client.list_jobs(request=request)

    # Handle the response
    for response in page_result:
        print(response)

if __name__ == "__main__":
    sample_list_jobs()