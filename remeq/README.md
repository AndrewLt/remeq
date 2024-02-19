# REMEQ
It is a simple library for creating message queue based on Redis and its channels

# How can I use it?
First of all import MessageQueue object into your code.

    from remeq import MessageQueue

and create new queue

    redis_message_queue = MessageQueue(
        queue_name=YOUR_CHANNEL_NAME,
        queue_method='FIFO',
        host=REDIS_HOST,
        port=REDIS_PORT,
        decode_responses=True
    )

where
* _queue_name_ - is the name of your channel where you want to store messages
* _queue_method_ - is how the message will be added to the channel and how its message will be taken from the channel, FIFO or LIFO
* _host, port, decode_response_ - are standard settings of Redis object 

So, to send a message into the channel use _send_massage_ method
    
    redis_message_queue.send_message("YOUR_MESSAGE_TEXT")

And if you want to get the message from the channel, use _get_message_ method

    redis_message_queue.get_message()

That's all. Good luck :)