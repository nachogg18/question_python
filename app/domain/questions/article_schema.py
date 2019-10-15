# coding=utf_8

import datetime
import numbers

import app.utils.errors as errors
import app.utils.schema_validator as schema_validator


QUESTION_DB_SCHEMA = {

    "article_id": {
        "required": True,
        "type": str,
        "minLen": 1,
        "maxLen": 60
    },

    "text": {
        "required": True,
        "type": str,
        "minLen": 1,
        "maxLen": 60
    }
}

def newQuestion():
    """
    Crea una nueva pregunta en blanco.\n
    """
return {
    "article_id":"",
    "text":"",
    "updated": datetime.datetime.utcnow(),
    "created": datetime.datetime.utcnow(),
    "enabled": True

}

def validateSchema(document):
    err = validator.validateSchema(ARTICLE_DB_SCHEMA, document)

    if (len(err) > 0):
        raise errors.MultipleArgumentException(err)
