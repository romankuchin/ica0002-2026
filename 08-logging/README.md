# Lab 8

In this lab we will setup centralized logging.

## Task 1: Install Loki

Follow the official install guide:
https://grafana.com/docs/loki/latest/setup/install/local/#install-using-apt-or-rpm-package-manager.

Use host group named `loki_servers`, and VM that doesn't have Prometheus installed.

Change a few aspects of default Loki behavior (update the Loki configuration file):
 - Disable debug logging (`server.log_level`) -- Loki own logs can be noisy, and `log_level: warn` will be enough
 - Disable gRPC -- we won't use it; set `server.grpc_listen_port: 0`
 - Disable rules -- we won't use it; remove `ruler.alertmanager_url` block

Loki configuration reference: https://grafana.com/docs/loki/latest/configure/.

Loki is listening on 0.0.0.0:3100 by default -- don't change it.

## Task 2: Install Alloy

Install it to all VMs; use `init` role for that.

Guide: https://grafana.com/docs/alloy/latest/set-up/install/linux/

Files to read:

  - /var/log/syslog
  - /var/log/uwsgi/app/agama.log
  - /var/log/nginx/access.log
  - /var/log/nginx/error.log

Read only the files that are expected to be on VM.

Guide: https://grafana.com/docs/alloy/latest/monitor/monitor-logs-from-file/#configure-logging

Make sure that `alloy` user is in `adm` group for syslog access.

Allow members of `adm` group to read `/var/log/uwsgi/app/agama.log`. Do not change the file permissions.

Send logs from these files to Loki.

## Task 3: Create new dashboard with Agama logs

Agama logs are in `/var/log/uwsgi/app/agama.log`.

Make sure developers can use this dashboard without authentication.

Don't forget to add the new JSON file to your Ansible repo.

Don't forget to add Loki to provisioned datasources in Grafana.

## Task 4: Add Promtail and Loki monitoring to main Grafana dashboard

Make sure that you gather metrics from Alloy and Loki:
 - Add Prometheus target named `alloy`
 - Add Prometheus target named `loki`

Add to main dashboard rate of `loki_distributor_lines_received_total` for Loki performance monitoring.

Add rate of `loki_source_file_read_lines_total`, sum per VM, for Alloy performance monitoring.

Don't forget to update JSON file in your Ansible repo.

## Task 5: Create docs/slo.md

Prepare documentation for SRE team. Write at least 2 user journeys for main Agama page. Describe SLIs and SLOs.

Must have SLI types:
  - availability
  - latency

If you feel that something is missing - add it.

Docs for inspiration: https://sre.google/resources/practices-and-processes/art-of-slos/

Example from worksheet:

Make sure that your SLIs have an event, a success criterion, and specify where and 
how you record success or failure. Describe your specification as the proportion of 
events that were good. Make sure that your SLO specifies both a target and a 
measurement window.

User Journey:

SLI Type:

SLI Specification:

SLI Implementations:

SLO:

## Task 6: Setup SLI tracking

Configure Nginx logs for Agama SLI tracking and start collecting them into Loki.

Make sure you're collecting only `valid` events (requests to Prometheus or Grafana are not considered valid for main Agama page SLI)!
Separate Nginx `access_log` for Agama requests will make it much easier.

Adjust Grafana main dashboard, add SLO as thresholds to SLI tracking panels.

Examples of LogQL queries for all events (not only valid ones):

    avg_over_time(
    {filename="/var/log/nginx/agama.log"}
    | regexp "(?P<latency>\d+\.\d+)$"
    | unwrap latency
    [10m]
    )

    100 * (
    rate({filename="/var/log/nginx/agama.log"} 
    |~ `^[23]\\d\\d ` [10m])
    / rate({filename="/var/log/nginx/agama.log"}[10m]))

Don't forget to add Loki to provisioned datasources in Grafana.

Useful docs: https://docs.nginx.com/nginx/admin-guide/monitoring/logging/.

## Task 7: Test your SLO

1. Drop `agama` database in MySQL to verify that availability goes down.
2. Add latency between VMs with

        tc qdisc add dev ens3 root netem delay 100ms 50ms

    this will add 100 ±50ms to every outgoing packet, including `ping` and SSH! Rollback:

        tc qdisc del dev ens3 root

## Expected result

Your repository contains these files and directories:

    ansible.cfg
	docs/slo.md
    group_vars/all.yaml
    infra.yaml
    roles/loki/tasks/main.yaml

Your repository also contains all the required files from the previous labs.

Your repository **does not contain** Ansible Vault master password.

Everything is installed and configured with this command:

	ansible-playbook infra.yaml

Running the same command again does not make any changes to any of the managed hosts.

After playbook execution you should be able to see all logs in Grafana->Drilldown->Logs.

All the tests pass successfully:

    ./run-tests.sh
