
from google.cloud import talent
import six

def list_tenants(project_id):
    """List Tenants"""

    client = talent.TenantServiceClient()

    # project_id = 'searchjobs-357615'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode("utf-8")
    parent = f"projects/{project_id}"

    # Iterate over all results
    for response_item in client.list_tenants(parent=parent):
        print(f"Tenant Name: {response_item.name}")
        print(f"External ID: {response_item.external_id}")

if __name__ == "__main__":
    list_tenants('searchjobs-357615')