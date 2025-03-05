from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message
from users.models import User


@shared_task
def schedule_send_telegram_message():
    """Запланированная задача для отправки сообщений в Telegram."""
    habits = Habit.objects.filter(is_pleasant=False)
    users = User.objects.all()
    for user in users:
        chat_id = user.tg_chat_id
        message = "Ваши привычки:\n"
        for habit in habits:
            message += f"- {habit.action} в {habit.time.strftime('%H:%M')}\n"
        send_telegram_message(chat_id, message)
