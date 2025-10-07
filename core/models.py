from django.db import models

class CotacaoDolar(models.Model):
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name="Valor da Cotação (R$/US$)"
    )

    data_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data e Hora do Registro"
    )
    fonte = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Fonte da Cotação"
    )


    def __str__(self):
        return f"Dólar: R${self.valor} em {self.data_registro.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Cotação do Dólar"
        verbose_name_plural = "Cotações do Dólar"
        ordering = ['-data_registro']