# Backup SLA

## Coverage

We back up services that satisfy at least one of these criteria:
 - are primary source of truth for particular data
 - contain customer and/or client data
 - are not feasible (or very costly) to restore by other means

Services that are backed up:
 - [___(service_name)___]
 - [___(service_name)___]
 - [___(service_name)___]


## Schedule

[___(service_name)___] backups are created every [___(time_period)___]. It takes up to [___(time_period)___] to create and store the backup.

[___(service_name)___] backups are created every [___(time_period)___]. It takes up to [___(time_period)___] to create and store the backup.

[___(service_name)___] backups are created every [___(time_period)___]. It takes up to [___(time_period)___] to create and store the backup.

All backups are started automatically by [___(service_name)___].

Backup RPO (recovery point objective) is:
 - [___(service_name)___] for [___(time_period)___]
 - [___(service_name)___] for [___(time_period)___]
 - [___(service_name)___] for [___(time_period)___]


## Storage

[___(service_name)___] and [___(service_name)___] backups are uploaded to the backup server.

[___(service_name)___] is mirrored to the internal Git server.

Backup data from both servers will be synchronized to encrypted AWS S3 bucket in future (work in progress).


## Retention

[___(service_name)___] backups are stored for [___(time_period)___]; [___(number)___] versions (recovery points) are available to restore.

[___(service_name)___] backups are stored for [___(time_period)___]; [___(number)___] versions are available to restore.

[___(service_name)___] backups are stored for [___(time_period)___]; [___(number)___] versions are available to restore.


## Usability checks

[___(service_name)___] backups are verified every [___(time_period)___] by [___(whom_or_waht___].

[___(service_name)___] backups are verified every [___(time_period)___] by [___(whom_or_waht___].

[___(service_name)___] backups are verified every [___(time_period)___] by [___(whom_or_waht___].


## Restore process

Service is recovered from the backup in case of an incident, and when service cannot be restored in any other way.

RTO (recovery time objective) is:
 - [___(time_period)___] for [___(service_name)___]
 - [___(time_period)___] for [___(service_name)___]
 - [___(time_period)___] for [___(service_name)___]

Detailed backup restore procedure is documented in the [backup_restore.md](./backup_restore.md).
