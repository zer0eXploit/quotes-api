from flask_restful import Resource, reqparse
from models.quote import Quote_Model
from flask_jwt_extended import jwt_required

_parser = reqparse.RequestParser()
_parser.add_argument(
    'quote_description',
    type=str,
    required=True,
    help="Please specify a quote_description."
)
_parser.add_argument(
    'quote_author',
    type=str,
    required=True,
    help="Please specify a quote_author."
)


class Quote_By_Id(Resource):
    def get(self, quote_id):
        try:
            quote = Quote_Model.get_quote_by_id(quote_id)
            if quote:
                return quote.json()

            return {"message": "Quote Not Found."}, 404

        except:
            return {
                "message": "Something went wrong on our server and that's not your fault."
            }, 500

    @jwt_required
    def put(self, quote_id):
        try:
            put_data = _parser.parse_args()

            quote = Quote_Model.get_quote_by_id(quote_id)
            if quote:
                quote.quote_description = put_data["quote_description"]
                quote.quote_author = put_data["quote_author"]
                quote.save_to_db()
                return {"message": "Quote Updated."}, 200

            quote = Quote_Model(**put_data)
            quote.save_to_db()
            return {"message": "Quote Created."}, 201

        except:
            return {
                "message": "Something went wrong on our server and that's not your fault."
            }, 500

    @jwt_required
    def delete(self, quote_id):
        try:
            quote = Quote_Model.get_quote_by_id(quote_id)
            if quote:
                quote.delete_from_db()
                return {"message": "Quote Deleted."}, 200

            return {"message": "Quote Not Found."}, 404

        except:
            return {
                "message": "Something went wrong on our server and that's not your fault."
            }, 500


class Quotes(Resource):
    def get(self):
        try:
            quotes = Quote_Model.find_all()
            return {
                "quotes": [quote.json() for quote in quotes]
            }

        except:
            return {
                "message": "Something went wrong on our server and that's not your fault."
            }, 500

    @jwt_required
    def post(self):
        try:
            quote_data = _parser.parse_args()
            new_quote = Quote_Model(**quote_data)
            new_quote.save_to_db()
            return {"message": "Quote created."}, 201

        except:
            return {
                "message": "Something went wrong on our server and that's not your fault."
            }, 500


class Random_Quote(Resource):
    def get(self):
        try:
            return {
                "quote": Quote_Model.get_random_quote().json()
            }

        except:
            return {
                "message": "Something went wrong on our server and that's not your fault."
            }, 500
