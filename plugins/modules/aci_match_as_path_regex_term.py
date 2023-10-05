#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Gaspard Micol (@gmicol) <gmicol@cisco.com>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {"metadata_version": "1.1", "status": ["preview"], "supported_by": "certified"}

DOCUMENTATION = r"""
---
module: aci_match_as_path_regex_term
short_description: Manage Match Regular Expression AS-Path Term (rtctrl:MatchAsPathRegexTerm)
description:
- Manage Match Term Based on Route Regular Expression AS-Path for Match Rule Profiles on Cisco ACI fabrics.
options:
  tenant:
    description:
    - The name of an existing tenant.
    type: str
    aliases: [ tenant_name ]
  match_rule:
    description:
    - The name of an exising match rule profile.
    type: str
    aliases: [ match_rule_name ]
  match_as_path_regex_term:
    description:
    - The name of the match regex AS-Path term.
    type: str
    aliases: [ name, match_as_path_regex_term_name ]
  regex:
    description:
    - The Regular Expression.
    type: str
  description:
    description:
    - The description for the match regex AS-Path term.
    type: str
    aliases: [ descr ]
  state:
    description:
    - Use C(present) or C(absent) for adding or removing.
    - Use C(query) for listing an object or multiple objects.
    type: str
    choices: [ absent, present, query ]
    default: present
  name_alias:
    description:
    - The alias for the current object. This relates to the nameAlias field in ACI.
    type: str
extends_documentation_fragment:
- cisco.aci.aci
- cisco.aci.annotation
- cisco.aci.owner

notes:
- The C(tenant) and the C(match_rule) used must exist before using this module in your playbook.
  The M(cisco.aci.aci_tenant) and the M(cisco.aci.aci_match_rule) modules can be used for this.
seealso:
- module: cisco.aci.aci_tenant
- module: cisco.aci.aci_match_rule
- name: APIC Management Information Model reference
  description: More information about the internal APIC class B(rtctrl:MatchAsPathRegexTerm).
  link: https://developer.cisco.com/docs/apic-mim-ref/
author:
- Gaspard Micol (@gmicol)
"""

EXAMPLES = r"""
- name: Create a match match AS-path regex term
  cisco.aci.match_as_path_regex_term:
    host: apic
    username: admin
    password: SomeSecretPassword
    match_rule: prod_match_rule
    match_as_path_regex_term: prod_match_as_path_regex_term
    regex: .*
    tenant: production
    state: present
  delegate_to: localhost

- name: Delete a match match AS-path regex term
  cisco.aci.match_as_path_regex_term:
    host: apic
    username: admin
    password: SomeSecretPassword
    match_rule: prod_match_rule
    tenant: production
    match_as_path_regex_term: prod_match_as_path_regex_term
    state: absent
  delegate_to: localhost

- name: Query all match AS-path regex terms
  cisco.aci.match_as_path_regex_term:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result

- name: Query a specific match match AS-path regex term
  cisco.aci.match_as_path_regex_term:
    host: apic
    username: admin
    password: SomeSecretPassword
    match_rule: prod_match_rule
    tenant: production
    match_as_path_regex_term: prod_match_as_path_regex_term
    state: query
  delegate_to: localhost
  register: query_result
"""

RETURN = r"""
current:
  description: The existing configuration from the APIC after the module has finished
  returned: success
  type: list
  sample:
    [
        {
            "fvTenant": {
                "attributes": {
                    "descr": "Production environment",
                    "dn": "uni/tn-production",
                    "name": "production",
                    "nameAlias": "",
                    "ownerKey": "",
                    "ownerauto_continue": ""
                }
            }
        }
    ]
error:
  description: The error information as returned from the APIC
  returned: failure
  type: dict
  sample:
    {
        "code": "122",
        "text": "unknown managed object class foo"
    }
raw:
  description: The raw output returned by the APIC REST API (xml or json)
  returned: parse error
  type: str
  sample: '<?xml version="1.0" encoding="UTF-8"?><imdata totalCount="1"><error code="122" text="unknown managed object class foo"/></imdata>'
sent:
  description: The actual/minimal configuration pushed to the APIC
  returned: info
  type: list
  sample:
    {
        "fvTenant": {
            "attributes": {
                "descr": "Production environment"
            }
        }
    }
previous:
  description: The original configuration from the APIC before the module has started
  returned: info
  type: list
  sample:
    [
        {
            "fvTenant": {
                "attributes": {
                    "descr": "Production",
                    "dn": "uni/tn-production",
                    "name": "production",
                    "nameAlias": "",
                    "ownerKey": "",
                    "ownerauto_continue": ""
                }
            }
        }
    ]
proposed:
  description: The assembled configuration from the user-provided parameters
  returned: info
  type: dict
  sample:
    {
        "fvTenant": {
            "attributes": {
                "descr": "Production environment",
                "name": "production"
            }
        }
    }
filter_string:
  description: The filter string used for the request
  returned: failure or debug
  type: str
  sample: ?rsp-prop-include=config-only
method:
  description: The HTTP method used for the request to the APIC
  returned: failure or debug
  type: str
  sample: POST
response:
  description: The HTTP response from the APIC
  returned: failure or debug
  type: str
  sample: OK (30 bytes)
status:
  description: The HTTP status from the APIC
  returned: failure or debug
  type: int
  sample: 200
url:
  description: The HTTP url used for the request to the APIC
  returned: failure or debug
  type: str
  sample: https://10.11.12.13/api/mo/uni/tn-production.json
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.aci.plugins.module_utils.aci import ACIModule, aci_argument_spec, aci_annotation_spec, aci_owner_spec


def main():
    argument_spec = aci_argument_spec()
    argument_spec.update(aci_annotation_spec())
    argument_spec.update(aci_owner_spec())
    argument_spec.update(
        tenant=dict(type="str", aliases=["tenant_name"]),  # Not required for querying all objects
        match_rule=dict(type="str", aliases=["match_rule_name"]),  # Not required for querying all objects
        match_as_path_regex_term=dict(type="str", aliases=["name", "match_as_path_regex_term_name"]),
        regex=dict(type="str"),
        description=dict(type="str", aliases=["descr"]),
        name_alias=dict(type="str"),
        state=dict(type="str", default="present", choices=["present", "absent", "query"]),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ["state", "absent", ["match_as_path_regex_term", "tenant"]],
            ["state", "present", ["match_as_path_regex_term", "tenant"]],
        ],
    )

    match_as_path_regex_term = module.params.get("match_as_path_regex_term")
    description = module.params.get("description")
    regex = module.params.get("regex")
    state = module.params.get("state")
    tenant = module.params.get("tenant")
    match_rule = module.params.get("match_rule")
    name_alias = module.params.get("name_alias")

    aci = ACIModule(module)

    aci.construct_url(
        root_class=dict(
            aci_class="fvTenant",
            aci_rn="tn-{0}".format(tenant),
            module_object=tenant,
            target_filter={"name": tenant},
        ),
        subclass_1=dict(
            aci_class="rtctrlSubjP",
            aci_rn="subj-{0}".format(match_rule),
            module_object=match_rule,
            target_filter={"name": match_rule},
        ),
        subclass_2=dict(
            aci_class="rtctrlMatchAsPathRegexTerm",
            aci_rn="aspathrxtrm-{0}".format(match_as_path_regex_term),
            module_object=match_as_path_regex_term,
            target_filter={"name": match_as_path_regex_term},
        ),
    )

    aci.get_existing()

    if state == "present":
        aci.payload(
            aci_class="rtctrlMatchAsPathRegexTerm",
            class_config=dict(
                name=match_as_path_regex_term,
                regex=regex,
                descr=description,
                nameAlias=name_alias,
            ),
        )

        aci.get_diff(aci_class="rtctrlMatchAsPathRegexTerm")

        aci.post_config()

    elif state == "absent":
        aci.delete_config()

    aci.exit_json()


if __name__ == "__main__":
    main()