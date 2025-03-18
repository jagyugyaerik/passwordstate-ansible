from ansible.module_utils.basic import *
from ansible.module_utils.urls import fetch_url

import requests


__metaclass__ = type

DOCUMENTATION = r"""
---
"""

EXAMPLES = r"""
---
"""

RETURN = r"""return"""


def run_module():
    module_args = dict(
        api_host=dict(type="str", required=True),
        api_key=dict(type="str", required=True),
        password_list_id=dict(type="str", required=True),
        title=dict(type="str", required=False, default=""),
    )

    result = dict(changed=False, password="", response="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if module.check_mode:
        module.exit_json(**result)

    method = "GET"
    url = f"{module.params['api_host']}/{module.params['password_list_id']}?QueryAll&ExcludePassword=true"
    headers = {"APIKey": module.params["api_key"]}

    # response, info = fetch_url(
    #     module=module, url=url, headers=headers, method=method
    # )

    response = requests.get(url, headers=headers).json()

    result["changed"] = False
    result["response"] = response
    result["url"] = url

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
