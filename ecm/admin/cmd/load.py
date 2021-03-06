# Copyright (c) 2010-2012 Robin Jarry
#
# This file is part of EVE Corporation Management.
#
# EVE Corporation Management is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# EVE Corporation Management is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# EVE Corporation Management. If not, see <http://www.gnu.org/licenses/>.

from __future__ import with_statement

__date__ = '2012 5 18'
__author__ = 'diabeteman'

import os
import shutil
import urllib2
import tempfile
from optparse import OptionParser
from ConfigParser import SafeConfigParser

from ecm.lib.subcommand import Subcommand
from ecm.admin.util import pipe_to_dbshell, expand
from ecm.admin.util import log


CCP_DATA_DUMPS = {
    'django.db.backends.postgresql_psycopg2': {
        'PATCH': 'eve_ecm_patch_psql.sql',
        'DROP': 'drop_eve_tables_psql.sql',
    },
    'django.db.backends.mysql': {
        'PATCH': 'eve_ecm_patch_mysql.sql',
        'DROP': 'drop_eve_tables_mysql.sql',
    },
    'django.db.backends.sqlite3': {
        'PATCH': 'eve_ecm_patch_sqlite.sql',
        'DROP': None,
    },
}


#-------------------------------------------------------------------------------
def sub_command():
    # INIT
    description = 'Load official EVE data dump into the instance database.'
    
    load_cmd = Subcommand('load',
                          parser=OptionParser(usage='%prog [OPTIONS] instance_dir datadump'),
                          help=description,
                          callback=run)
    load_cmd.parser.description = description + ' "datadump" can be either a URL or a local path. '\
                                 'It can also be an archive file (bz2, gz, zip).'

    return load_cmd

#-------------------------------------------------------------------------------
SQL_ROOT = os.path.abspath(os.path.dirname(__file__))
def run(command, global_options, optionsd, args):
    
    if not args:
        command.parser.error('Missing instance directory.')
    instance_dir = args.pop(0)
    if not args:
        command.parser.error('Missing datadump.')
    datadump = args.pop(0)
    
    config = SafeConfigParser()
    if config.read([os.path.join(instance_dir, 'settings.ini')]):
        db_engine = config.get('database', 'ecm_engine')
        db_password = config.get('database', 'ecm_password')
    else:
        command.parser.error('Could not read "settings.ini" in instance dir.')
    try:
        sql = CCP_DATA_DUMPS[db_engine]
    except KeyError:
        command.parser.error('Cannot load datadump with database engine %r. '
                             'Supported engines: %r' % (db_engine, CCP_DATA_DUMPS.keys()))

    try:
        tempdir = tempfile.mkdtemp()
        
        if not os.path.exists(datadump):
            # download from URL
            dump_archive = os.path.join(tempdir, os.path.basename(datadump))
            log('Downloading EVE original dump from %r to %r...', datadump, dump_archive)
            req = urllib2.urlopen(datadump)
            with open(dump_archive, 'wb') as fp:
                shutil.copyfileobj(req, fp)
            req.close()
            log('Download complete.')
        else:
            dump_archive = datadump
        
        extension = os.path.splitext(dump_archive)[-1]
        if extension in ('.bz2', '.gz', '.zip'):
            # decompress archive
            log('Expanding %r to %r...', dump_archive, tempdir)
            dump_file = expand(dump_archive, tempdir)
            log('Expansion complete to %r.' % dump_file)
        else:
            dump_file = dump_archive
        
        log('Patching and importing data (this can be long)...')
        if 'sqlite' in db_engine:
            import sqlite3
            with open(os.path.join(SQL_ROOT, sql['PATCH'])) as f:
                sql_script = f.read() 
            connection = sqlite3.connect(os.path.join(instance_dir, 'db/ecm.sqlite'))
            cursor = connection.cursor()
            cursor.execute('ATTACH DATABASE \'%s\' AS "eve";' % dump_file)
            cursor.executescript(sql_script)
            cursor.execute('DETACH DATABASE "eve";')
            cursor.close()
            connection.commit()
        else:
            pipe_to_dbshell(dump_file, instance_dir, password=db_password)
            pipe_to_dbshell(os.path.join(SQL_ROOT, sql['PATCH']), instance_dir, password=db_password)
            pipe_to_dbshell(os.path.join(SQL_ROOT, sql['DROP']), instance_dir, password=db_password)
        
        log('EVE data successfully imported.')
    finally:
        log('Removing temp files...')
        shutil.rmtree(tempdir)
        log('done')

#-------------------------------------------------------------------------------
def print_load_message(instance_dir, db_engine):
    
    if 'mysql' in db_engine:
        engine = 'mysql'
    elif 'sqlite' in db_engine:
        engine = 'sqlite'
    else:
        engine = 'psql'
    
    log('')
    log('Now you need to load your database with EVE static data.')
    log('Please execute `ecm-admin load %s <official_dump_file>` to do so.' % instance_dir)
    log('You will find official dump conversions here http://releases.eve-corp-management.org/eve_sde/')
    log('Be sure to take the latest one matching your db engine "%s".' % engine)
