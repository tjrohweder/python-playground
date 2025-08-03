import boto3
import logging
from datetime import date

START_DATE = '2025-01-01'
PERIOD = 'DAILY'
COST_TYPE = 'BlendedCost'

logging.basicConfig(level=logging.INFO, format='%(name)s :: %(levelname)s :: %(message)s')
logger = logging.getLogger(__name__)

today = date.today()
end_date = today.strftime('%Y-%m-%d')


def get_billing(client, start_date, end_date):
    try:
        billing = client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date,
                'End': end_date,
            },
            Granularity=PERIOD,
            Metrics=[
                COST_TYPE,
            ]
        )

        return billing

    except Exception as e:
        logger.error(f'Error fetching billing: {e}')
        return None


def output_format(billing):
    print(f'Date Range | {COST_TYPE} (USD)')
    print('-----------|---------------------')
    for amount in billing['ResultsByTime']:
        start_date = amount['TimePeriod']['Start']
        cost = float(amount['Total'][COST_TYPE]['Amount'])
        print(f'{start_date} | ${cost:,.2f}')


def main():
    client = boto3.client('ce')
    billing = get_billing(client, START_DATE, end_date, PERIOD, COST_TYPE)
    if billing:
        output_format(billing)
    else:
        logger.error('No billing data found')

if __name__ == '__main__':
    main()
