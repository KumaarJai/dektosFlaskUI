'''
Created on Feb 8, 2019
@author: Ajay_Rabidas

UI for configuring devices
Server page
'''
from modbusInterface import dektosExternalPackageInstaller as DEKTOS_INSTALLER
from dektosFlaskUI import app


if __name__ == '__main__':
#     DEKTOS_INSTALLER.installPackage('flask')
#     DEKTOS_INSTALLER.installPackage('flask_wtf')
#     DEKTOS_INSTALLER.installPackage('flask_sqlalchemy')
    app.run(debug=True)
    
    