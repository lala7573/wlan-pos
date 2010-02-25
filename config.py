DATPATH = 'dat/'
RAWSUFFIX = '.raw'
RMPSUFFIX = '.rmp'
#INTERSIZE = 10
CLUSTERKEYSIZE = 4
KNN = 4

# DB related configuration.
db_config = {
    'hostname' : 'localhost',
    'username' : 'pos',
    'password' : 'pos',
    'dbname' : 'wlanpos' }
# SQL table related data structs.
tbl_names = { 'cidaps':'cidaps', 
                'cfps':'cfps' }
tbl_field = { 'cidaps':'(cid, keyaps)',
                'cfps':'(cid, spid, lat, lon, rsss)' }
tbl_forms = { 'cidaps':""" (
                     cid SMALLINT NOT NULL, 
                  keyaps VARCHAR(71),
                   INDEX icid (cid)
                )""", 
              'cfps':""" (
                     cid SMALLINT NOT NULL,
                    spid SMALLINT NOT NULL,
                     lat DOUBLE(9,6),
                     lon DOUBLE(9,6),
                    rsss VARCHAR(59),
                   INDEX icid (cid)
                )""" }
tbl_files = { 'cidaps':'tbl/cidaps.tbl', 
                'cfps':'tbl/cfprints.tbl' }
# SQL statements.
SQL_DROP = 'DROP TABLE IF EXISTS %s'
SQL_CREATE = 'CREATE TABLE IF NOT EXISTS %s %s'
SQL_CSVIN = """
        LOAD DATA LOCAL INFILE "%s" INTO TABLE %s 
        FIELDS TERMINATED BY ',' 
        LINES TERMINATED BY '\\n' 
        %s"""
SQL_SELECT = 'SELECT %s FROM %s'
SQL_SELECT_WHERE = 'SELECT %s FROM %s WHERE %s'

# String length of 179 and 149 chars are used for each intersection set to have 
# at most INTERSET APs, which should be enough for classification, very ugly though.
dt_rmp_nocluster = {'names':('spid','lat','lon','macs','rsss'), 
                       'formats':('i4','f4','f4','S179','S149')}
WLAN_FAKE = {
        2: #home
            [ ['00:25:86:23:A4:48', '-86'], ['00:24:01:FE:0F:20', '-90'], 
              ['00:0B:6B:3C:75:34', '-89'] ],
        5: #home-only 1 visible
            [ ['00:0B:6B:3C:75:34', '-89'] ],
        4: #cmri-only 1 visible
            [ ['00:15:70:9E:91:60', '-53'] ],
        3: #cmri-fail
            [ ['00:15:70:9F:7D:88', '-82'], ['00:15:70:9F:7D:89', '-77'],
              ['00:15:70:9F:7D:8A', '-77'], ['00:23:89:3C:BD:F2', '-81'],
              ['00:11:B5:FD:8B:6D', '-81'], ['00:23:89:3C:BE:10', '-70'],
              ['00:23:89:3C:BE:11', '-70'], ['00:23:89:3C:BE:13', '-71'],
              ['00:15:70:9E:91:62', '-72'], ['00:15:70:9E:91:60', '-49'],
              ['00:23:89:3C:BD:32', '-75'], ['00:15:70:9E:91:61', '-50'],
              ['00:23:89:3C:BE:12', '-75'], ['00:23:89:3C:BD:33', '-76'],
              ['00:14:BF:1B:A5:48', '-79'], ['00:15:70:9E:6C:6D', '-68'],
              ['00:15:70:9E:6C:6C', '-68'], ['00:15:70:9E:6C:6E', '-68'],
              ['00:23:89:3C:BD:30', '-75'], ['00:23:89:3C:BD:31', '-75'],
              ['00:23:89:3C:BC:90', '-79'], ['00:23:89:3C:BC:93', '-75'],
              ['00:11:B5:FE:8B:6D', '-88'], ['00:23:89:3C:BC:91', '-80'],
              ['00:23:89:3C:BC:92', '-81'], ['00:23:89:3C:BD:F1', '-80']],
        1: #cmri-ok-part
            [ ['00:15:70:9F:7D:8A', '-76'], ['00:15:70:9F:7D:88', '-77'],
              ['00:15:70:9F:7D:89', '-80'], ['00:11:B5:FD:8B:6D', '-79'],
              ['00:23:89:3C:BC:90', '-75'], ['00:23:89:3C:BC:91', '-76'],
              ['00:23:89:3C:BC:92', '-76'], ['00:23:89:3C:BC:93', '-75'],
              ['00:23:89:3C:BE:12', '-73'], ['00:23:89:3C:BE:10', '-75'],
              ['00:23:89:3C:BE:11', '-69'], ['00:15:70:9E:91:61', '-63'],
              ['00:23:89:3C:BE:13', '-71'], ['00:15:70:9E:91:62', '-61'],
              ['00:15:70:9E:91:60', '-62'], ['00:14:BF:1B:A5:48', '-81'],
              ['00:23:89:3C:BD:33', '-73'], ['00:15:70:9E:6C:6C', '-67'],
              ['00:15:70:9E:6C:6D', '-68'], ['00:15:70:9E:6C:6E', '-67']],
        6: #cmri-ok-full
            [ ['00:11:B5:FD:8B:6D', '-69'], ['00:15:70:9E:91:60', '-52'], 
              ['00:15:70:9E:91:61', '-53'], ['00:15:70:9F:73:64', '-78'], 
              ['00:15:70:9F:73:66', '-75'], ['00:15:70:9E:91:62', '-55'],
              ['00:23:89:3C:BE:10', '-74'], ['00:23:89:3C:BE:11', '-78'], 
              ['00:23:89:3C:BE:12', '-78'], ['00:11:B5:FE:8B:6D', '-80'], 
              ['00:15:70:9E:6C:6C', '-65'], ['00:15:70:9E:6C:6D', '-60'],
              ['00:15:70:9E:6C:6E', '-70'], ['00:15:70:9F:76:E0', '-81'], 
              ['00:15:70:9F:7D:88', '-76'], ['00:15:70:9F:73:65', '-76'], 
              ['00:23:89:3C:BD:32', '-75'], ['00:23:89:3C:BD:30', '-78'],
              ['02:1F:3B:00:01:52', '-76'] ]
}
icon_encrypton = '/kml/encrypton.png'
icon_encryptoff = '/kml/encryptoff.png'
icon_other = '/kml/reddot.png'
dict_encrypt_icon = { 'on': [ '"encrypton"',  icon_encrypton ],
                     'off': [ '"encryptoff"', icon_encryptoff],
                   'other': [ '"reddot"',     icon_other] }
