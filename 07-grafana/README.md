# Lab 7

In this lab we will continue with monitoring. The goal of this lab is to create a place where everyone can get overview of your infrastructure state.

## Task 1: Install MySQL exporter

Create MySQL user named `exporter`. This user should be only able to log in from the same host, but not from the other hosts.

Install MySQL exporter from Ubuntu package repository.

Docs: https://github.com/prometheus/mysqld_exporter.

Use `~/.my.cnf` file for passing authentication data to MySQL exporter. Find under what user it runs and what folder is a home folder for that user. Nobody except the user itself and `root` should be able to read this file. Nobody (except `root`) should be able to change the file.

Content of `~/.my.cnf`:

    [client]
    user = exporter
    password = {{ ... }}

Make sure that exporter will be restarted in case username/password change.

**No clear text passwords in Git repository!**

Exporter tasks should be a part of `mysql` role.

Add Prometheus target named `mysql`.

Check your solution: execute `mysql_up` query in the Prometheus Graph interface; one element should be listed, value should be 1.

## Task 2: Install Bind9 exporter

Install Bind9 exporter from Ubuntu package repository.

Expose Bind9 statistics for the exporter on local interface.

Docs: https://github.com/prometheus-community/bind_exporter.

Exporter tasks should be a part of `bind` role.

Add Prometheus target named `bind`.

Check your solution: execute `bind_up` query in the Prometheus Graph interface; one element should be listed, value should be 1.

## Task 3: Install Nginx exporter

Install Nginx exporter from Ubuntu package repository.

Make sure that Nginx exposes statistics to exporter on local interface.

Docs: https://github.com/nginx/nginx-prometheus-exporter.

Exporter tasks should be a part of `nginx` role.

Add Prometheus target named `nginx`.

Check your solution: execute `nginx_up` query in the Prometheus Graph interface; two elements should be listed, both values should be 1.

## Task 4: Install Grafana

Docs: https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/#install-from-apt-repository.

Use steps for Grafana OSS stable. Be patient, Grafana process may take some time to start for the first time.

Ansible modules to use: `apt_key`, `apt_repository`, `apt`.

Host group in the inventory should be named `grafana_servers`. Note that you don't need to change anything for that if you are using [dynamic inventory](https://github.com/romankuchin/ica0002-2026/tree/main/03-web-server#this-year-experiment-dynamic-inventory) already.

## Task 5: Configure reverse proxy

Add necessary locations to the Nginx config:

    - location /grafana -> localhost:(grafana_port)
    
Helpful docs for Grafana: https://grafana.com/tutorials/run-grafana-behind-a-proxy.

In Nginx don't add locations that point to non-existing services. You can use this code for checking if we should expect some path on this VM or not:

    {% if 'prometheus' in group_names %}
    location /prometheus {
        proxy_pass http://localhost:xyz/...;
    }
    {% endif %}

## Task 6: Create dashboard in Grafana

Create Grafana `Main` dashboard that will show:
 - CPU utilisation on every VM
 - Memory consumption on every VM
 - Bind9 status + amount of A DNS queries per minute (`bind_resolver_queries_total`)
 - MySQL status + amount of selects per minute (`mysql_global_status_commands_total`)
 - Nginx status + amount of requests per minute (`nginx_http_requests_total`)

Use Prometheus as a datasource.

## Task 7: Configure Grafana provisioning

To avoid manual operations every time do the following during Grafana installation:

 - Configure Prometheus as default datasource (https://grafana.com/docs/grafana/latest/administration/provisioning/#data-sources)
 - Precreate `Main` dashboard (https://grafana.com/docs/grafana/latest/administration/provisioning/#dashboards)
 - Precreate user (your GitHub username) and password

**No clear text passwords in Git repository!**

## Task 8: Allow anonymous access to Grafana dashboards

Make it possible to review your dashboards without authentication. Docs: https://grafana.com/docs/grafana/latest/setup-grafana/configure-access/configure-authentication/anonymous-auth/

Should be read only, you still must login to make any changes.

## Expected result

Your repository contains these files and directories:

    ansible.cfg
    group_vars/all.yaml
    hosts
    infra.yaml
	roles/grafana/files/main.json
    roles/grafana/tasks/main.yaml

Your repository also contains all the required files from the previous labs.

Your repository **does not contain** Ansible Vault master password.

Grafana, exporters and reverse proxy are installed and configured with this command:

	ansible-playbook infra.yaml

Running the same command again does not make any changes to any of the managed
hosts.

After playbook execution you should be able to:

1. See Grafana dashboard by using \<your_VM_http_link\>/grafana.
2. Check your Prometheus web interface by using \<your_VM_http_link\>/prometheus (lab 6).
3. Access Agama by using \<your_VM_http_link\> (lab 4).
