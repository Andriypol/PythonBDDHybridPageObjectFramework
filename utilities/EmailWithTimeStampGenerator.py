from datetime import datetime


def get_new_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "ahrnot" + time_stamp + "@ukr.net"