from module_utils.passwordstate_utils import passwordstate_common_argument_spec

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
    module_args: dict[str, dict[str, str | bool]] = passwordstate_common_argument_spec()
    module_args.update(
        dict(
            password_id=dict(type="str", required=False, default=""),
            title=dict(type="str", required=False, default=""),
            username=dict(type="str", required=False, default=""),
            password=dict(type="str", required=False, default=""),
        )
    )

    result: dict[str, bool | str] = dict(changed=False, password="", response="")

    module: AnsibleModule = AnsibleModule(
        argument_spec=module_args, supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    method: str = "GET"
    endpoint: str = "searchpasswords"
    url: str = (
        f"{module.params['api_host']}/{endpoint}/{module.params['password_list_id']}?title={module.params['title']}"
    )
    headers: dict[str, str] = {"APIKey": module.params["api_key"]}

    response: requests.Response = requests.get(
        url, headers=headers, method=method
    ).json()

    result["changed"] = False
    result["response"] = response

    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == "__main__":
    main()
