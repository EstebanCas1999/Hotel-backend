import logging
from datetime import datetime as dt
from flask import Flask, request, jsonify
from marshmallow import ValidationError
from http import HTTPStatus

from .config import config_by_name
from . import extensions
from . import modules
from app.main.modules.shared.exceptions import ObjectNotFoundException, InvalidValueError, DuplicateUser, \
    PreconditionFailedException, ConflictException
from .extensions import db


def create_app(config_name) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    extensions.init_app(app)
    modules.init_app(app)
    with app.app_context():
        db.create_all()

    @app.after_request
    def after_request(response):
        logger = logging.getLogger("app.access")
        logger.info(
            "%s [%s] %s %s %s %s %s %s %s",
            request.remote_addr,
            dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
            request.method,
            request.path,
            request.scheme,
            response.status,
            response.content_length,
            request.referrer,
            request.user_agent,
        )
        return response

    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation(err):
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST.value

    @app.errorhandler(ObjectNotFoundException)
    def handle_object_not_found(err):
        response = dict(message=str(err), statusCode=HTTPStatus.NOT_FOUND.value)
        return jsonify(response), HTTPStatus.NOT_FOUND.value

    @app.errorhandler(InvalidValueError)
    def handle_bad_request(err):
        response = dict(message=str(err), statusCode=HTTPStatus.BAD_REQUEST.value)
        return jsonify(response), HTTPStatus.BAD_REQUEST.value

    @app.errorhandler(DuplicateUser)
    def handle_conflict_duplicate_user(err):
        response = dict(message=str(err), statusCode=HTTPStatus.CONFLICT.value)
        return jsonify(response), HTTPStatus.CONFLICT.value

    @app.errorhandler(PreconditionFailedException)
    def precondition_failed(err):
        response = dict(message=str(err), statusCode=HTTPStatus.PRECONDITION_FAILED.value)
        return jsonify(response), HTTPStatus.PRECONDITION_FAILED.value

    @app.errorhandler(ConflictException)
    def handle_conflict(err):
        response = dict(message=str(err), statusCode=HTTPStatus.CONFLICT.value)
        return jsonify(response), HTTPStatus.CONFLICT.value

    return app
