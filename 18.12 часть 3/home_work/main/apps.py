from django.apps import AppConfig
from django.db.models.signals import post_migrate


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self):
        post_migrate.connect(create_groups, sender=self)


def create_groups(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from .models import Book, Reader

    librarians, _ = Group.objects.get_or_create(name="Librarians")
    admins, _ = Group.objects.get_or_create(name="Administrators")

    book_ct = ContentType.objects.get_for_model(Book)
    reader_ct = ContentType.objects.get_for_model(Reader)

    view_perms = Permission.objects.filter(
        content_type__in=[book_ct, reader_ct],
        codename__startswith="view_"
    )

    all_perms = Permission.objects.filter(
        content_type__in=[book_ct, reader_ct]
    )

    librarians.permissions.set(view_perms)
    admins.permissions.set(all_perms)
