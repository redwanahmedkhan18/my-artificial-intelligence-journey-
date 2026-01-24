def notify(email_body=None, sms_body=None, *, priority='high', retry=True, **kwargs):
    # Simulate sending logic (replace with actual API calls)
    email_sent = f"Email sent with body: '{email_body}'" if email_body else "No email sent"
    sms_sent = f"SMS sent with body: '{sms_body}'" if sms_body else "No SMS sent"

    # Process extra config
    user_id = kwargs.get('user_id', 'N/A')
    template = kwargs.get('template', 'default')

    # Prepare structured summary
    summary = {
        'status': 'success',  # In real life, this would change if errors occurred
        'channels': {
            'email': email_sent,
            'sms': sms_sent,
        },
        'config': {
            'priority': priority,
            'retry': retry,
            'user_id': user_id,
            'template': template
        },
        'message': 'Notification process completed.'
    }
    return summary


# Basic usage
print(notify("Hello User!", "Hi there!", priority='medium'))

# With extra kwargs
print(notify(
    email_body="Your order #123 is confirmed.",
    sms_body="Order 123 confirmed.",
    priority='urgent',
    user_id='user456',
    template='order_confirmation'
))

# Only sending one channel
print(notify(sms_body="Quick update!", priority='low', retry=False, source='system'))
