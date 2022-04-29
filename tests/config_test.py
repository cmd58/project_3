"""This is the configuration test"""
# project/tests/test_config.py
#import logging
#import os

#import app.config

"""This is the Development Configuration Test"""
def test_development_config(application):
    application.config.from_object('app.config.DevelopmentConfig')

    assert application.config['DEBUG']
    assert not application.config['TESTING']

"""This is the Testing Configuration Test"""
def test_testing_config(application):
    application.config.from_object('app.config.TestingConfig')
    assert application.config['DEBUG']
    assert application.config['TESTING']
    assert not application.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'

"""This is the Production Configuration Test"""
def test_production_config(application):
    application.config.from_object('app.config.ProductionConfig')
    assert not application.config['DEBUG']
    assert not application.config['TESTING']
