from Common.utils.SmsUtil import SmsUtil

if __name__ == "__main__":
    print('start...')

    SmsUtil.get_sms('19900030001', 4)
    SmsUtil.get_sms('19900030001')

    SmsUtil.get_sms('19900030001', 1)
    SmsUtil.get_sms('19900030001', 2)
