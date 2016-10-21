from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse


from .utils.update import update


class ProjectManager(models.Manager):
    def featured(self):
        return super(ProjectManager, self).filter(featured=True)

    def not_featured(self):
        return super(ProjectManager, self).filter(featured=False)


class Project (models.Model):
    username = models.CharField(max_length=128)
    repository = models.CharField(max_length=128)
    slug = models.SlugField(max_length=64)
    featured = models.BooleanField(default=False)
    readme = models.TextField(blank=True, help_text="Please update this on github!")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    sha = models.CharField(max_length=64, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    download_url = models.URLField(blank=True)
    language = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    objects = ProjectManager()

    def get_absolute_link(self):
        return reverse("projects:view", kwargs={"slug": self.slug})

    class Meta:
        unique_together = ('username', 'repository', )


def create_slug(instance):
    slug = slugify(instance.repository)
    if Project.objects.filter(slug=slug).exists():
        slug = "%s-%s" % (slug, instance.id)

    return slug


def pre_save_port_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    update(instance, False)

pre_save.connect(pre_save_port_receiver, sender=Project)
