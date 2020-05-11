# Examples of requests using the aioUAPI module.
# As an example, the interaction with the module "Site News" is presented.
# author Ilya Matthew Kuvarzin <luceo2011@yandex.ru>
# version 1.0 dated April 11, 2020
# Return_value is dict

import aioUAPI
import asyncio

request = aioUAPI.Request('my-site.com', 'https',
                          {
                              'oauth_consumer_key': 'Application id',
                              'oauth_consumer_secret': 'Consumer secret',
                              'oauth_token': 'OAuth token',
                              'oauth_token_secret': 'OAuth token secret'
                          })


async def main():
    return_value = await request.get('/news', {})
    print(return_value)

    return_value = await request.post('/news', {'category': 'CATEGORY-ID', 'title': 'Material name',
                                                'message': 'This is a test material. Request succeeded.'})
    print(return_value)

    return_value = await request.put('/news', {'id': 'MATERIAL-ID', 'message': 'Material successfully changed'})
    print(return_value)

    return_value = await request.delete('/news/posts', {'id': 'MATERIAL-ID'})
    print(return_value)

    await request.close_session()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
