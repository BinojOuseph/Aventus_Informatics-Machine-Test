from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

def validate_file_size(value):
    filesize = value.size

    if filesize > 5 * 1024 * 1024:
        raise ValidationError(_('The maximum file size allowed is 5 MB.'))

class EmployeeMaster(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=250)
    email = models.EmailField(unique=True, blank=False, null=False)
    image = ProcessedImageField(
        upload_to="Employee_Images/",
        format="WEBP",
        options={"quality": 60},
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']),
            validate_file_size
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'EmployeeMaster'
        verbose_name_plural = 'EmployeeMaster'

