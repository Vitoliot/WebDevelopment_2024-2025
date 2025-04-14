# mainapp/models.py
from django.db import models


class Feedback(models.Model):
    SPECIALTY_CHOICES = [
        ('frontend', 'Frontend-разработка'),
        ('backend', 'Backend-разработка'),
        ('data_science', 'Data Science'),
        ('devops', 'DevOps'),
        ('other', 'Другое')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email")
    message = models.TextField("Сообщение")

    specialty = models.CharField(
        "Специальность",
        max_length=20,
        choices=SPECIALTY_CHOICES,
        default='frontend'
    )
    rating = models.PositiveIntegerField("Оценка сайту (1–10)", default=5)

    created_at = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Feedback from {self.name} ({self.email})"
