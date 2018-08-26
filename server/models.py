from datetime import datetime
import json

import server.utils as utils

from server.public import db


class BaseModel(object):
    @staticmethod
    def save(item):
        db.session.add(item)
        db.session.commit()

    @staticmethod
    def delete(item):
        db.session.delete(item)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        instance = cls._get_by_id(id)
        return instance

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def _get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


class TestItems(db.Model, BaseModel):
    """this class represents the testitems table, where we store temporary test items"""

    __tablename__ = "testitems"

    id = db.Column(db.Integer, primary_key=True)

    # required fields
    condition = db.Column(db.String, nullable=False)
    listing_name = db.Column(db.String, nullable=False)
    post_link = db.Column(db.String, nullable=False)
    price = db.Column(db.ARRAY(db.Float), nullable=False)
    website = db.Column(db.String, nullable=False)

    # fields generated upon creation
    date_scraped = db.Column(db.ARRAY(db.DateTime), nullable=False)

    # optional fields
    images = db.Column(db.ARRAY(db.String))
    listing_dates = db.Column(db.JSON)
    misc = db.Column(db.JSON)
    post_description = db.Column(db.String(length=500))

    def __init__(self, condition, listing_name, post_link, price, website, images=None,
                 listing_dates=None, misc=None, post_description=None):
        utils.validate_condition(condition)
        self.condition = condition
        utils.validate_listing_name(listing_name)
        self.listing_name = listing_name
        utils.validate_link(post_link)
        self.post_link = post_link
        utils.validate_price(price)
        self.price = [round(float(price), 2)]
        utils.validate_website(website)
        self.website = website

        if images:
            utils.validate_images(images)
            self.images = images
        if listing_dates:
            utils.validate_listing_dates(listing_dates)
            self.listing_dates = listing_dates
        if misc:
            utils.validate_misc(misc)
            self.misc = misc
        if post_description:
            utils.validate_post_description(post_description)
            self.post_description = post_description

        # ensure that no item has the same link
        dups = TestItems.query.filter_by(post_link=post_link).all()
        if dups:
            raise Exception('TestItem with post_link={} already exists'.format(post_link))

        self.date_scraped = [datetime.now()]

    def __repr__(self):
        return json.dumps(self.to_dict())