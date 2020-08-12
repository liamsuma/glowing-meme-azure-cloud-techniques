# Two ways of messging via Azure Service Bus are queues and topics & subscriptions 
# Queues offer FIFO message delivery to one or more competing consumers 
# Topics and subscriptions provide a one-to-many form of communication instead, especially useful for scaling to large numbers of receipients 

# Topics and subscriptions example 

from azure.servicebus.control_client import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME

conString = '<connection string>' # unique identifier to your organization 

azure_namespace = 'abc'
key_name = 'xyz'
key_value = '1q2w3e4r5t6y7u8i9o='

bus_service = ServiceBusService(
    service_namespace=azure_namespace,
    shared_access_key_name=key_name,
    shared_access_key_value=key_value)
    
conTopic = 'mytopic'
conSubscription = 'mysubscription'

# send message to a topic 
for i in range(5):
    msg = Message('Msg {0}'.format(i).encode('utf-8'))
    bus_service.send_topic_message(conTopic, msg)
    
# receive messages from a subscription 
msg = bus_service.receive_subscription_message(conTopic, conSubscription)
print(msg.body) 

# Queues example 

msg = Message('Hello Azure!')
bus_service.send_queue_message('taskqueue', msg)
