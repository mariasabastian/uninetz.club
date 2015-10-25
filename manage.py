#!/usr/bin/env python

from migrate.versioning.shell import main
import config

if __name__ == '__main__':
  print (config.SQLALCHEMY_DATABASE_URI)
  main(debug='False', url=config.SQLALCHEMY_DATABASE_URI, repository='./migrations/')
