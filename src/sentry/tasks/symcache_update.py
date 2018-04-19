from __future__ import absolute_import

from sentry.tasks.base import instrumented_task
from sentry.models import Project, ProjectDSymFile


@instrumented_task(
    name='sentry.tasks.symcache_update',
    time_limit=65,
    soft_time_limit=60,
)
def symcache_update(project_id, debug_ids, **kwargs):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return

    ProjectDSymFile.dsymcache.update_symcaches(project, debug_ids)
