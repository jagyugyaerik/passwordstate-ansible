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


def run_module() -> None:
    module_args: dict[str, dict[str, str | bool]] = dict(
        api_host=dict(type="str", required=True),
        api_key=dict(type="str", required=True),
        password_list_id=dict(type="str", required=True),
        password_id=dict(type="str", required=False, default=""),
        title=dict(type="str", required=False, default=""),
    )

    result: dict[str, bool | str] = dict(changed=False, password="", password_id="")

    module: AnsibleModule = AnsibleModule(
        argument_spec=module_args, supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    endpoint: str = "searchpasswords"
    url: str = (
        f"{module.params['api_host']}/{endpoint}/{module.params['password_list_id']}?title={module.params['title']}"
    )
    headers: dict[str, str] = {"APIKey": module.params["api_key"]}

    response: requests.Response = requests.get(url, headers=headers).json()[0]

    result["changed"] = False
    result["password"] = response["Password"]
    result["username"] = response["UserName"]
    result["url"] = response["URL"]
    result["generic_field_1"] = response["GenericField1"]
    result["password_id"] = response["PasswordID"]

    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == "__main__":
    main()
