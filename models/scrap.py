
from datetime import datetime
from email import message
from os import link
from flask import Flask, jsonify, request
from scraper import scrap_func
from app import db
import pymongo

class Scrap:

    def scrap(self):
        data = request.get_json(silent=True)
        title = data["title"]
        links = data['links']

        if not title:
            return jsonify({ "error": "Please input all form" }), 400

        results = scrap_func(links)

        # Check for existing books
        results = list(map(add_is_updated, results))

        scrap_logs = []

        for result in results:
            now = datetime.now()
            if (result["is_updated"]):
                db.books.update_one({"_id": result["_id"]}, {"$set": {**result, "last_updated": now}})
            else:
                db.books.insert_one({**result, "created": now, "last_updated": now})

            log = {
                "title": title,
                "status": "Success",
                "book": {
                    "_id": result["_id"],
                    "title": result["title"],
                    "link": result["link"]
                },
                "db_action": "Updated" if result["is_updated"] else "Inserted",
                "created": now
            }

            scrap_logs.append(log)

        db.scrap_logs.insert_many(scrap_logs)

        return jsonify({"message": "Scrap is completed.", "results": results, "scrap_logs": list(map(lambda log : {**log, "_id": str(log["_id"])}, scrap_logs))})


def add_is_updated(book):
    return {**book, "is_updated": True if db.books.find_one({ "_id": book['_id'] }) else False}