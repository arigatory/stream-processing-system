import faust
from config import KAFKA_BROKER, TOPICS
from processors.user_blocker import UserBlocker
from processors.message_censor import MessageCensor

app = faust.App("message-processing", broker=KAFKA_BROKER)

# Определение топиков
messages_topic = app.topic(TOPICS["messages"])
filtered_messages_topic = app.topic(TOPICS["filtered_messages"])
blocked_users_topic = app.topic(TOPICS["blocked_users"])
censored_messages_topic = app.topic(TOPICS["censored_messages"])

# Инициализация процессоров
user_blocker = UserBlocker()
message_censor = MessageCensor()


@app.agent(messages_topic)
async def process_message(messages):
    async for message in messages:
        if not user_blocker.is_blocked(message.sender, message.recipient):
            censored_message = message_censor.censor_message(message.content)
            await filtered_messages_topic.send(
                value={
                    "sender": message.sender,
                    "recipient": message.recipient,
                    "content": censored_message,
                }
            )
        else:
            print(
                f"Заблокированное сообщение от {message.sender} к {message.recipient}"
            )


@app.agent(blocked_users_topic)
async def update_blocked_users(blocked_users):
    async for blocked_user in blocked_users:
        user_blocker.block_user(blocked_user.blocker, blocked_user.blocked)


if __name__ == "__main__":
    app.main()
