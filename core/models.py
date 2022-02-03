from django.db import models
from stdimage import StdImageField
import uuid


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Portfolio(models.Model):
    title = models.CharField('Título', max_length=100)
    url = models.URLField('URL', max_length=150)
    image = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 1400, 'height': 1050, 'crop': True}})

    class Meta:
        verbose_name = 'Portfólio'
        verbose_name_plural = 'Portfólios'

    def __str__(self):
        return self.title
