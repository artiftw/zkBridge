from utils import *
from config import *

def main():
    wallets,results = [],[]
    print(f'\n{" " * 32}автор - https://t.me/iliocka{" " * 32}\n')
    for key in keys:
        if proxies:
            proxy = random.choice(proxies)
        else:
            proxy = None

        if TYPE == 'nftbridger':
            zk = ZkBridge(key,DELAY,chain,to,MORALIS_API_KEY, MODE,proxy)
            res = zk.claim_on_destinaton()
            wallets.append(res[0]), results.append(res[1])

        if TYPE == 'messenger':
            zk = ZkMessage(key,chain,to,DELAY,proxy)
            res = zk.send_msg()
            wallets.append(res[0]), results.append(res[1])

    res = {'address': wallets, 'result': results}
    df = pd.DataFrame(res)
    df.to_csv('results.csv', mode='a', index=False)
    logger.success('Минетинг закончен...')
    print(f'\n{" " * 32}автор - https://t.me/{" " * 32}\n')
    print(f'\n{" " * 32}донат - 0x{" " * 32}\n')


if __name__ == '__main__':
    main()