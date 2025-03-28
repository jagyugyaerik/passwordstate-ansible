from ansible.module_utils.basic import *
from ansible.module_utils.urls import fetch_url

import requests

__metaclass__ = type

DOCUMENTATION = r"""
---
module: passwordstate_add_or_update

short_description: Module for adding and updating passwords in Passwordstate.

description: A new Password object can be added by providing the necessary
 fields in the module. The method returns the newly created Password object.
 An existing Password object can be updated by providing the `password_id` field
. Only the specified fields will be modified, while any unspecified fields will
 remain unchanged. It is recommended to include only the fields that need to be
   updated to ensure accurate modifications."

options:
    api_host:
        description: Url of Passwordstate
        required: true
        type: str
    api_key:
        description: API key with permissions to create passwords in the
          Passwordstate folder.
        required: true
        type: str
    password_list_id:
        description: ID of the Passwordstate folder
        required: true
        type: str
    password_id:
        description: ID of an existing password, used when updating it.
        required: true
        type: str
    title:
        description: Title of the password
        required: true
        type: str
    username:
        description: Username
        required: true
        type: str
    password:
        description: Password
        required: true
        type: str
"""

EXAMPLES = r"""
---
- name: Add a new password
  cetinhu.passwordstate.add_or_update:
    api_host: "{{ lookup('ansible.builtin.env', 'API_HOST', default='') }}"
    api_key: "{{ lookup('ansible.builtin.env', 'API_KEY', default='') }}"
    password_list_id: "{{ lookup('ansible.builtin.env', 'LIST_ID', default='') }}"
    title: test-mysql-cluster
    username: service-user
    password: S3rv1ce

- name: Update an existing password
  cetinhu.passwordstate.add_or_update:
    api_host: "{{ lookup('ansible.builtin.env', 'API_HOST', default='') }}"
    api_key: "{{ lookup('ansible.builtin.env', 'API_KEY', default='') }}"
    password_list_id: "{{ lookup('ansible.builtin.env', 'LIST_ID', default='') }}"
    passowrd_id: 137
    password: S3rv1ce
"""

RETURN = r"""return"""


def run_module():
    module_args: dict[str, dict[str, str | bool]] = dict(
        api_host=dict(type="str", required=True),
        api_key=dict(type="str", required=True),
        password_list_id=dict(type="str", required=True),
        title=dict(type="str", required=True,),
        username=dict(type="str", required=True),
        password=dict(type="str", required=True),
        password_id=dict(type="str", required=False, default=""),
        generic_field_1=dict(type="str", required=False, default=""),
        url=dict(type="str", required=False, default=""),
    )

    result: dict[str, bool | str] = dict(changed=False, password="", response="")

    module: AnsibleModule = AnsibleModule(
        argument_spec=module_args, supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    endpoint: str = "passwords"
    url: str = f"{module.params['api_host']}/{endpoint}"
    headers: dict[str, str] = {"APIKey": module.params["api_key"]}
    data: dict[str, str] = {
        "passwordlistid": module.params.get("password_list_id"),
        "title": module.params["title"],
        "username": module.params["username"],
        "password": module.params["password"],
        "genericfield1": module.params["generic_field_1"],
        "url": module.params["url"],
    }

    response: requests.Response = requests.post(
        url=url, headers=headers, data=data
    ).json()

    result["changed"] = True
    result["response"] = response

    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == "__main__":
    main()
