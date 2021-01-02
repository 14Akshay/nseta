import click
from nseta.common.history import historicaldata
from nseta.common.log import tracelog, default_logger
from nseta.cli.inputs import *
from datetime import datetime

__all__ = ['history', 'pe_history']

@click.command(help='Get price history of a security for given dates')
@click.option('--symbol', '-S',  help='Security code')
@click.option('--start', '-s', help='Start date in yyyy-mm-dd format')
@click.option('--end', '-e', help='End date in yyyy-mm-dd format')
@click.option('--file', '-o', 'file_name',  help='Output file name')
@click.option('--index/--no-index', default=False, help='--index if security is index else --no-index')
@click.option('--format', '-f', default='csv',  type=click.Choice(['csv', 'pkl']),
				help='Output format, pkl - to save as Pickel and csv - to save as csv')
@tracelog
def history(symbol, start, end, file_name, index, format): #, futures, expiry, option_type, strike):
	if not validate_inputs(start, end, symbol):
		print_help_msg(history)
		return
	sd = datetime.strptime(start, "%Y-%m-%d").date()
	ed = datetime.strptime(end, "%Y-%m-%d").date()
	df = None
	try:
		historyinstance = historicaldata()
		df = historyinstance.daily_ohlc_history(symbol, sd, ed)
		click.echo(df.head())
	except Exception as e:
		default_logger().debug(e, exc_info=True)
		click.secho('Failed to fetch history', fg='red', nl=True)
		return
	except SystemExit:
		pass
	if not file_name:
		file_name = symbol + '.' + format
	if format == 'csv':
		df.to_csv(file_name)
	else:
		df.to_pickle(file_name)
	default_logger().info('Saved to: {}'.format(file_name))
	click.secho('Saved to: {}'.format(file_name), fg='green', nl=True)

@click.command(help='Get PE history of a security for given dates')
@click.option('--symbol', '-S',  help='Index code')
@click.option('--start', '-s', help='Start date in yyyy-mm-dd format')
@click.option('--end', '-e', help='End date in yyyy-mm-dd format')
@click.option('--format', '-f', default='csv',  type=click.Choice(['csv', 'pkl']),
				help='Output format, pkl - to save as Pickel and csv - to save as csv')
@click.option('--file', '-o', 'file_name',  help='Output file name')
@tracelog
def pe_history(symbol, start, end, format, file_name):
	if not validate_inputs(start, end, symbol):
		print_help_msg(pe_history)
		return
	sd = datetime.strptime(start, "%Y-%m-%d").date()
	ed = datetime.strptime(end, "%Y-%m-%d").date()
	try:
		historyinstance = historicaldata()
		df = historyinstance.get_index_pe_history(symbol, sd, ed)
		click.echo(df.head())
	except Exception as e:
		default_logger().debug(e, exc_info=True)
		click.secho('Failed to fetch PE history.', fg='red', nl=True)
		return
	except SystemExit:
		pass

	if not file_name:
		file_name = symbol + '.' + format

	if format == 'csv':
		df.to_csv(file_name)
	else:
		df.to_pickle(file_name)
	default_logger().info('Saved to: {}'.format(file_name))
	click.secho('Saved to: {}'.format(file_name) , fg='green', nl=True)
