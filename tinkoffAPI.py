
from tinkoff.invest import Client
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX

TOKEN = 't.Drcafjn6oaMz2zBgmHmSXD87nDQp17nEN0V1QpcRuEM7H1PfgkaUPCgPUJYWvYt8ruz4v8jMDL1TiZAMYbaCAQ'

with Client(TOKEN, target=INVEST_GRPC_API_SANDBOX ) as client:
    print(client.users.get_accounts())