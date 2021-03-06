from __future__ import absolute_import

# This should be exactly the same as `django.db.migrations.writer.py.MIGRATION_TEMPLATE`,
# except that we add
# - `atomic = False`
# - `is_dangerous = False`
# to the class definition. Compare this template after each Django version bump to make
# sure we're not missing any important changes.
SENTRY_MIGRATION_TEMPLATE = """\
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
%(imports)s

class Migration(migrations.Migration):
    # This flag is used to mark that a migration shouldn't be automatically run in
    # production. We set this to True for operations that we think are risky and want
    # someone from ops to run manually and monitor.
    # General advice is that if in doubt, mark your migration as `is_dangerous`.
    # Some things you should always mark as dangerous:
    # - Adding indexes to large tables. These indexes should be created concurrently,
    #   unfortunately we can't run migrations outside of a transaction until Django
    #   1.10. So until then these should be run manually.
    # - Large data migrations. Typically we want these to be run manually by ops so that
    #   they can be monitored. Since data migrations will now hold a transaction open
    #   this is even more important.
    # - Adding columns to highly active tables, even ones that are NULL.
    is_dangerous = False

%(replaces_str)s
    dependencies = [
%(dependencies)s\
    ]

    operations = [
%(operations)s\
    ]
"""
