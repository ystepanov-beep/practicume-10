sms = input("")


def check_for_limit(sms: str) -> str:
    """Returns the message if it is within the 160-character limit, otherwise returns the first 160 characters."""

    if len(sms) <= 160:
        return sms
    else:
        return sms[:160]
        
print(check_for_limit(sms))
