# Section 6: Automation and Configuration (10%)

**Last reviewed:** 2026-11-07

The two objectives on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/) (checked 2026-11-07) are to manage NVIDIA Spectrum-X switch configurations through NVUE templates and to write Ansible playbooks that automate network setup such as VLAN creation or RoCE configuration. Neither could be run here (no Cumulus Linux switch). The documentation I could read describes the tooling but gives no complete playbook, so the playbook below is my own sketch, labelled as such.

## NVUE: the object model behind the CLI

NVUE is the Cumulus Linux configuration system. The `nv` commands you have seen in this guide (`nv set`, `nv config apply`) edit a configuration, and apply makes it live. The same object model is exposed three ways, per NVIDIA's Data Center Network Automation Quick Start Guide:

- **The CLI**, to "configure, monitor, and manage the Cumulus Linux network elements" (for example `nv config show`).
- **The REST API**, to "run the GET, PATCH, DELETE, and other REST APIs on the NVUE object model endpoints". The page's example: `curl -k -u cumulus:CumulusLinux! -X GET "https://127.0.0.1:8765/nvue_v1/?rev=applied"`. From Cumulus Linux 5.4 the REST API is enabled by linking `/etc/nginx/sites-available/nvue.conf` into `sites-enabled` and restarting nginx.
- **The startup file**: "NVUE saves the configuration in a configuration file called `/etc/nvue.d/startup.yaml`."

**[📖 Automation with Cumulus Linux](https://docs.nvidia.com/networking-ethernet-software/guides/Data-Center-Network-Automation-Quick-Start-Guide/Automation-with-Cumulus-Linux)** - NVUE CLI, REST API, startup.yaml and the Ansible collection

## NVUE templates

A template here means the configuration expressed as data and rendered per switch. The guide says Production Ready Automation "generates the jinja2 template for the startup configuration (`startup.yaml`) that NVUE uses", with a reference topology and playbooks. For features NVUE does not yet model, NVUE snippets let you patch raw YAML into the configuration with `nv config patch`: from the Cumulus Linux docs (search summary), the YAML must use spaces, not tabs, the file must be named with its fully qualified path, NVUE does not parse or validate the snippet's content, and snippets can become invalid as NVUE adds support for a feature.

**[📖 NVUE Snippets](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-Snippets)** - `nv config patch` and the snippet rules

- **NVUE** - NVIDIA User Experience: the Cumulus Linux configuration system, with a CLI, a REST API and a startup.yaml file.
- **startup.yaml** - the file `/etc/nvue.d/startup.yaml` where NVUE saves the configuration applied at boot.
- **NVUE snippet** - raw YAML applied with `nv config patch` for features NVUE does not yet expose; it is not validated by NVUE.

## Ansible with the nvidia.nvue collection

The quick start says the `nvidia.nvue` collection "includes Ansible modules to help you interact with NVIDIA devices managed by NVUE": a **CLI** module (a wrapper around the `nv` command with templating and dialog prompting), a **REST API** module (send and retrieve NVUE configuration), and object-specific modules for bridge, router, interface, evpn, mlag, system, vrf and vxlan. The NVIDIA page says the modules were developed and validated with Ansible 2.11 and Python 3.6 and are supported on Cumulus Linux 5.x. The guide's page has no playbook, so check the collection's own documentation for the parameter names before using the module names below.

Because the documentation I could read gives no playbook, I am not writing one here: an invented module parameter list would look authoritative and could be wrong. What you should be able to describe for the exam is the shape: a play targets the switch group, one task per concern (VLANs and bridge, RoCE QoS, EVPN) calls an `nvidia.nvue` module with the same settings you would type as `nv set` commands, and the apply step makes them live. Read the collection's documentation for the exact parameters.

The reason to automate with these modules instead of shell scripts is idempotence and review: the playbook lives in Git, runs against the whole fabric, and can be tested first in a simulator such as DSX Air (Section 2).

- **nvidia.nvue** - NVIDIA's Ansible collection for devices managed by NVUE, with CLI, REST API and object-specific modules.
- **Production Ready Automation (PRA)** - NVIDIA's reference topology with playbooks and the jinja2 template that renders startup.yaml.

## Check yourself against the objectives

Say the three interfaces to NVUE and where its configuration is stored; say what a snippet is and why it is risky; name the kinds of modules in `nvidia.nvue`; and explain why automation changes are tested in simulation first. Questions are in the [NCP-AIN practice bank](../../../practice-questions/nvidia-ai-networking-professional.md).
