from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Summary:
    - Custom user model extending
      Django's built-in user.
    """

    is_validated = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        """
        Summary:
        - Django model configuration.
        """

        ordering = [
            "username"
        ]

        verbose_name = "User"

        verbose_name_plural = "Users"

    def __str__(self):
        """
        Summary:
        - String representation
          of the user.
        """

        return (
            f"{self.username}"
        )