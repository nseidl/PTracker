import datetime
import http.client
import os

from flask import request, jsonify, render_template
from flask_api import FlaskAPI
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from server.configs import app_config
from server.custom_logging import get_logger
from server.utils import BadRequest, NotFound


logger = get_logger(module='PTracker Server', warn_list=['werkzeug'])

db = SQLAlchemy()


def create_app(config_name):
    from server.models import TestItems

    app = FlaskAPI(__name__, static_folder=os.path.relpath('../dist/static'), template_folder=os.path.relpath('../dist'))
    app.config.from_object(app_config[config_name])
    app.debug = True
    CORS(app)
    db.app = app
    db.init_app(app)
    db.create_all()

    @app.before_request
    def print_request():
        logger.info('[{}] {}'.format(request.method, request.url))

    @app.route('/', methods=['GET'])
    def root():
        return render_template('index.html'), http.client.OK

    @app.route('/<path:path>', methods=['GET'])
    def any_path(path):
        return render_template('index.html'), http.client.OK

    @app.route('/api/date', methods=['GET'])
    def get_date():
        now = datetime.datetime.now()
        return {'date': now.strftime('%Y-%m-%d %H:%M')}

    @app.route('/api/test_items', methods=['GET'])
    def get_test_items():
        item_id = request.args.get('test_item_id')

        if item_id:
            item = TestItems.get_by_id(item_id)
            if item:
                return item.to_dict(), http.client.OK
            else:
                raise NotFound('item_id={} not found'.format(item_id))

        items = dict()
        items_found = TestItems.get_all()
        for item in items_found:
            items[item.id] = item.to_dict()

        return items, http.client.OK

    @app.route('/api/test_items', methods=['POST'])
    def add_test_items():
        items = request.json
        if items:
            try:
                for item_info in items:
                    new_item = TestItems(item_info.get('condition'), item_info.get('listing_name'),
                                         item_info.get('post_link'), item_info.get('price'),
                                         item_info.get('website'), item_info.get('images'),
                                         item_info.get('listing_dates'), item_info.get('misc'),
                                         item_info.get('post_description'))
                    TestItems.save(new_item)

                return {'message': 'all items added successfully'}, http.client.CREATED
            except Exception as e:
                msg = 'error creating new test_item: {}'.format(e)
                logger.warning(msg)
                raise BadRequest(msg)
        else:
            msg = 'body json must be provided'
            logger.warning(msg)
            raise BadRequest(msg)

    @app.route('/api/test_items/<int:item_id>', methods=['delete'])
    def delete_test_item(item_id):
        test_item = TestItems.get_by_id(item_id)
        if test_item:
            TestItems.delete(test_item)
            return test_item.to_dict(), http.client.OK
        else:
            raise NotFound('test_item_id={} not found'.format(item_id))

    @app.route('/test/<int:custom_id>', methods=['POST'])
    def handle_data(custom_id):
        args = request.args
        form_data = request.form

        result = {
            'custom_id': custom_id,
            'args': args,
            'form_data': form_data
        }

        return result, http.client.OK

    @app.after_request
    def allow_requests(response):
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        return response

    @app.errorhandler(NotFound)
    def handle_not_found(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.errorhandler(BadRequest)
    def handle_bad_request(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app