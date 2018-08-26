import http.client

import urllib

import server.constants as constants


class NotFound(Exception):
    status_code = http.client.NOT_FOUND

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class BadRequest(Exception):
    status_code = http.client.BAD_REQUEST

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def validate_condition(condition):
    if not isinstance(condition, str):
        raise Exception('condition must be str')
    elif condition not in constants.VALID_CONDITIONS:
        raise Exception('condition must be one of {}'.format(constants.VALID_CONDITIONS))


def validate_listing_name(name):
    if not isinstance(name, str):
        raise Exception('listing_name must be str')


def validate_link(link):
    if not isinstance(link, str):
        raise Exception('link must be str')
    if urllib.parse.urlparse(link).scheme not in ['http', 'https']:
        raise Exception('link must begin with \'http\' or \'https\'')


def validate_price(price):
    if isinstance(price, str):
        try:
            price = float(price)
            if not price > 0:
                raise Exception
        except Exception as e:
            raise Exception('price must be able to be cast to a positive float')
    elif type(price) in [int, float]:
        if not price > 0:
            raise Exception('price must be a positive float')


def validate_website(website):
    if not isinstance(website, str):
        raise Exception('website must be str')
    elif website not in constants.VALID_WEBSITES:
        raise Exception('website must be one of {}'.format(constants.VALID_WEBSITES))


def validate_images(images):
    if not isinstance(images, list):
        raise Exception('images must be a list of str')
    else:
        for item in images:
            validate_link(item)


def validate_listing_dates(dates):
    if not isinstance(dates, dict):
        raise Exception('listing_dates must be {date_listed: ..., date_sold: ...}')
    else:
        required_keys = {'date_listed', 'date_sold'}
        given_keys = dates.keys()

        if not required_keys == given_keys:
            raise Exception('listing_dates must be {date_listed: ..., date_sold: ...}')


def validate_misc(misc):
    if not isinstance(misc, dict):
        raise Exception('mist must be dict')


def validate_post_description(description):
    if not isinstance(description, str):
        raise Exception('post_description must be str')