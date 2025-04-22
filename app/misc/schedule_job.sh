#!/bin/bash

# Agendando execucao de teste para cada 3h.

CRON_LINE="55 */3 * * * /app/app/misc/send_invoice_batch_demo.sh"
TEMP_CRON_FILE="/tmp/temp_cron"

# Ler o crontab atual (se existir) e redirecionar para um arquivo temporário
crontab -l > "$TEMP_CRON_FILE" 2>/dev/null || true

# Adicionar a nova linha ao arquivo temporário
echo "$CRON_LINE" >> "$TEMP_CRON_FILE"

# Aplicar o novo crontab a partir do arquivo temporário
crontab "$TEMP_CRON_FILE"

# Remover o arquivo temporário
rm "$TEMP_CRON_FILE"

echo "Job cron agendado para rodar send_invoice_batch_demo.sh a cada 3 horas."