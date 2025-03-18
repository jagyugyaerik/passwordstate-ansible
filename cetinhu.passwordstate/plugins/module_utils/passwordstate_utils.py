


__metaclass__ = type

def passwordstate_common_argument_spec() -> dict[str, dict[str, str | bool]]:
    return dict(
        api_host=dict(type="str", required=True),
        api_key=dict(type="str", required=True),
        password_list_id=dict(type="str", required=True)
    )