from GUIs.OTsUI_main import *
from pyqtgraph import PlotWidget, AxisItem, setConfigOption
from PyQt5.Qt import QStyle, QFileDialog
from PyQt5.QtWidgets import QMainWindow
import PyQt5
import configparser as cfg
import numpy as np
from os import sep
from GUIs.configUI_deriv import configDial

try:
    import epz as tempEpz
    import inspect
    _,_,keys,_ = inspect.getargspec(tempEpz.CMD.__init__())
    if 'tag' not in keys:
        import libs.epz as tempEpz
    epz = tempEpz
except:
    from libs import epz

setConfigOption('background', 'w')
setConfigOption('foreground', (120,120,120))

INCR = 0.01


class OTsUI(QMainWindow,Ui_OTsUI_main):

    def __init__(self, parent=None):

        super(OTsUI, self).__init__(parent)
        self.setupUi(self)
        self.cfgFile = QFileDialog.getOpenFileName(self,'Select a configuration file',filter='Ini (*.ini)')[0]
        if self.cfgFile == '':
            self.cfgFile = 'config/defaultCfg.ini'
        self.kx = -1
        self.ky = -1
        self.kz = -1
        self.sx = -1
        self.sy = -1
        self.sz = -1
        self.logDir = ''
        self.dataDir = ''
        self.parDir = ''

        # epz objects

        self.otsuiEnv = epz.Environment()

        #######################################################################

        # Plot items
        
        self.trapPadPlot.plotItem.showAxis('top', show=True)
        self.trapPadPlot.plotItem.showAxis('right', show=True)
        self.trapPadPlot.plotItem.showGrid(True, True, 1)
        self.trapPadPlot.setMaximumSize(QtCore.QSize(180, 180))
        
        self.trapPosXYPlot.plotItem.showAxis('top', show=True)
        self.trapPosXYPlot.plotItem.showAxis('right', show=True)
        self.trapPosXYPlot.plotItem.showGrid(True, True, 1)
        self.trapPosXYPlot.setEnabled(True)
        
        self.trapPosZPlot.plotItem.hideAxis('left')
        self.trapPosZPlot.plotItem.showAxis('right', show=True)
        
        #######################################################################
        
        # Set num controls

        self.parDict = self.getParamsDict()
        
        ctrls = ['xyPNumDbl',
                'xyINumDbl',
                'xyPDial',
                'xyIDial',
                'zPNumDbl',
                'zINumDbl',
                'zPDial',
                'zIDial',
                'xSpeedTrapPadNumDbl',
                'ySpeedTrapPadNumDbl',
                'xSpeedTrapPadSlider',
                'ySpeedTrapPadSlider',
                'xOffSetNumDbl',
                'yOffSetNumDbl',
                'zOffSetNumDbl',
                'xOffSetDial',
                'yOffSetDial',
                'zOffSetDial',
                'passiveCalDurNumDbl',
                'passiveCalMaxFreqNumDbl',
                'passiveCalAvgNum',
                'activeCalXAmplNumDbl',
                'activeCalYAmplNumDbl',
                'activeCalZAmplNumDbl',
                'activeCalXFreqNumDbl',
                'activeCalYFreqNumDbl',
                'activeCalZFreqNumDbl',
                'activeCalDurNumDbl',
                'activeCalMaxFreqNumDbl',
                'activeCalAvgNum',
                'radiusNumDbl',
                'dynViscNumDbl',
                'kxNumDbl',
                'kyNumDbl',
                'kzNumDbl',
                'SxNumDbl',
                'SyNumDbl',
                'SzNumDbl',
                'stdExpXSetPntNumDbl',
                'stdExpYSetPntNumDbl',
                'stdExpZSetPntNumDbl',
                'stdExpDurNumDbl',
                'fbSchedNumIntNum',
                'fbSchedOnDurNumDbl',
                'fbSchedOffDurNumDbl',
                'customExpXNumIntNum',
                'customExpXOnDurNumDbl',
                'customExpXOffDurNumDbl',
                'customExpXAmplNumDbl',
                'customExpXFreqNumDbl',
                'customExpYNumIntNum',
                'customExpYOnDurNumDbl',
                'customExpYOffDurNumDbl',
                'customExpYAmplNumDbl',
                'customExpYFreqNumDbl',
                'customExpZNumIntNum',
                'customExpZOnDurNumDbl',
                'customExpZOffDurNumDbl',
                'customExpZAmplNumDbl',
                'customExpZFreqNumDbl']
        
        cfgCtrls = ['XYP',
                   'XYI',
                   'XYP',
                   'XYI',
                   'ZI',
                   'ZP',
                   'ZI',
                   'ZP',
                   'XSPEED',
                   'YSPEED',
                   'XSPEED',
                   'YSPEED',
                   'XO',
                   'YO',
                   'ZO',
                   'XO',
                   'YO',
                   'ZO',
                   'DUR',
                   'MAXFREQ',
                   'AVG',
                   'XAMPL',
                   'YAMPL',
                   'ZAMPL',
                   'XFREQ',
                   'YFREQ',
                   'ZFREQ',
                   'DUR',
                   'MAXFREQ',
                   'AVG',
                   'RADIUS',
                   'DYNVISC',
                   'KX',
                   'KY',
                   'KZ',
                   'SX',
                   'SY',
                   'SZ',
                   'XSP',
                   'YSP',
                   'ZSP',
                   'DUR',
                   'INTNUM',
                   'ONDUR',
                   'OFFDUR',
                   'XINTNUM',
                   'XONDUR',
                   'XOFFDUR',
                   'XAMPL',
                   'XFREQ',
                   'YINTNUM',
                   'YONDUR',
                   'YOFFDUR',
                   'YAMPL',
                   'YFREQ',
                   'ZINTNUM',
                   'ZONDUR',
                   'ZOFFDUR',
                   'ZAMPL',
                   'ZFREQ']
        
        cfgKeys = ['PI',
                   'PI',
                   'PI',
                   'PI',
                   'PI',
                   'PI',
                   'PI',
                   'PI',
                   'PAD',
                   'PAD',
                   'PAD',
                   'PAD',
                   'OFFSET',
                   'OFFSET',
                   'OFFSET',
                   'OFFSET',
                   'OFFSET',
                   'OFFSET',
                   'PASSIVECALIB',
                   'PASSIVECALIB',
                   'PASSIVECALIB',
                   'ACTIVECALIB',
                   'ACTIVECALIB',
                   'ACTIVECALIB',
                   'ACTIVECALIB',
                   'ACTIVECALIB',
                   'ACTIVECALIB',
                   'ACTIVECALIB',
                   'ACTIVECALIB',
                   'ACTIVECALIB',
                   'GENPAR',
                   'GENPAR',
                   'CALRESULTS',
                   'CALRESULTS',
                   'CALRESULTS',
                   'CALRESULTS',
                   'CALRESULTS',
                   'CALRESULTS',
                   'STDEXP',
                   'STDEXP',
                   'STDEXP',
                   'STDEXP',
                   'FBSCHED',
                   'FBSCHED',
                   'FBSCHED',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP',
                   'CUSTEXP']
        
        #for i in range(len(ctrls)):
            #self.configNum(ctrls[i], cfgCtrls[i], cfgKeys[i])
            
        #################################################################################

        self.numConnections()
        self.cmbBoxConnections()
        self.pathConnections()
        self.actionConnections()


    def getParamsDict(self):

        baseDict = {PyQt5.QtWidgets.QSpinBox:['NUM','.value()','.setValue(',[]],PyQt5.QtWidgets.QDoubleSpinBox:['DBL','.value()','.setValue(',[]],
                    PyQt5.QtWidgets.QLineEdit:['LINE','.text()','.setText(',[]],PyQt5.QtWidgets.QCheckBox:['CKBOX','.isChecked()','.setChecked(',[]]}

        for d in dir(self):
            dObj = getattr(self, d)
            try:
                if dObj.isReadOnly():
                    continue
            except:
                pass
            if type(dObj) in baseDict.keys():
                baseDict[type(dObj)][3].append(d)
            else:
                pass

        return baseDict


    def configNum(self,numName,cfgName,cfgKey):
        
        culprit = getattr(self, numName)
        scale = (1/INCR) if (type(culprit) == PyQt5.QtWidgets.QDial or type(culprit) == PyQt5.QtWidgets.QSlider) else 1
        getattr(self, numName).setMaximum(float(self.cfgParse[cfgKey][cfgName+'MAX'])*scale)
        getattr(self, numName).setMinimum(float(self.cfgParse[cfgKey][cfgName+'MIN'])*scale)
        getattr(self, numName).setSingleStep(INCR*scale)
        getattr(self, numName).setValue(float(self.cfgParse[cfgKey][cfgName])*scale)
        
    
    def changeCmbGrMem(self):
        sendCmb = self.sender()
        fatherCmb = sendCmb.parentWidget()
        listCmbChild = [c for c in fatherCmb.children() if (type(c)==PyQt5.QtWidgets.QComboBox and c is not sendCmb)]
        equalValCmb = [l for l in listCmbChild if l.currentIndex()==sendCmb.currentIndex()][0]
        elements = list(range(sendCmb.count()))
        elements.remove(sendCmb.currentIndex())
        listOtherChild = [c for c in listCmbChild if c is not equalValCmb]
        for c in listOtherChild:
            elements.remove(c.currentIndex())
        equalValCmb.blockSignals(True)
        equalValCmb.setCurrentIndex(elements[0])
        equalValCmb.blockSignals(False)
        
    
    def setScaledValue(self,rec):
        culprit = self.sender()
        scale = rec.singleStep() if (type(culprit) == PyQt5.QtWidgets.QDial or type(culprit) == PyQt5.QtWidgets.QSlider) else 1/culprit.singleStep()
        rec.blockSignals(True)
        rec.setValue(culprit.value()*scale)
        rec.blockSignals(False)
        
        
    def selectDir(self,displayLine):
        
        displayLine.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
        
    
    def updateDirObj(self,dir):
        
        culprit = self.sender()
        dir = culprit.text()
        dir=dir.replace('/',sep)
        
    
    def saveParams(self):
        for k in self.attribDict.keys():
            self.paramSaveParser.add_section(str(k))


    def showDial(self):

        culprit = self.sender()

        if culprit is self.action_Config_File:
            self.cfgDial = configDial(self.cfgFile,self)
            self.cfgDial.exec_()


    def numConnections(self):

        # Setting up the interconnection between UI numeric controls

        self.zPNumDbl.valueChanged.connect(lambda: self.setScaledValue(self.zPDial))
        self.zPDial.valueChanged.connect(lambda: self.setScaledValue(self.zPNumDbl))

        self.zINumDbl.valueChanged.connect(lambda: self.setScaledValue(self.zIDial))
        self.zIDial.valueChanged.connect(lambda: self.setScaledValue(self.zINumDbl))

        self.xyPNumDbl.valueChanged.connect(lambda: self.setScaledValue(self.xyPDial))
        self.xyPDial.valueChanged.connect(lambda: self.setScaledValue(self.xyPNumDbl))

        self.xyINumDbl.valueChanged.connect(lambda: self.setScaledValue(self.xyIDial))
        self.xyIDial.valueChanged.connect(lambda: self.setScaledValue(self.xyINumDbl))

        self.zOffSetNumDbl.valueChanged.connect(lambda: self.setScaledValue(self.zOffSetDial))
        self.zOffSetDial.valueChanged.connect(lambda: self.setScaledValue(self.zOffSetNumDbl))

        self.xOffSetNumDbl.valueChanged.connect(lambda: self.setScaledValue(self.xOffSetDial))
        self.xOffSetDial.valueChanged.connect(lambda: self.setScaledValue(self.xOffSetNumDbl))

        self.yOffSetNumDbl.valueChanged.connect(lambda: self.setScaledValue(self.yOffSetDial))
        self.yOffSetDial.valueChanged.connect(lambda: self.setScaledValue(self.yOffSetNumDbl))

        self.xSpeedTrapPadSlider.valueChanged.connect(lambda: self.setScaledValue(self.xSpeedTrapPadNumDbl))
        self.xSpeedTrapPadNumDbl.valueChanged.connect(lambda: self.setScaledValue(self.xSpeedTrapPadSlider))

        self.ySpeedTrapPadSlider.valueChanged.connect(lambda: self.setScaledValue(self.ySpeedTrapPadNumDbl))
        self.ySpeedTrapPadNumDbl.valueChanged.connect(lambda: self.setScaledValue(self.ySpeedTrapPadSlider))

        ######################################


    def cmbBoxConnections(self):

        # Setting Plot combo boxes

        self.sig1selCmb.currentIndexChanged.connect(self.changeCmbGrMem)
        self.sig2selCmb.currentIndexChanged.connect(self.changeCmbGrMem)
        self.sig3selCmb.currentIndexChanged.connect(self.changeCmbGrMem)

        self.ps1selCmb.currentIndexChanged.connect(self.changeCmbGrMem)
        self.ps2selCmb.currentIndexChanged.connect(self.changeCmbGrMem)
        self.ps3selCmb.currentIndexChanged.connect(self.changeCmbGrMem)

        #################################################################################


    def pathConnections(self):

        # Set directories selection

        self.logDirBtn.clicked.connect(lambda: self.selectDir(self.logDirLine))
        self.parDirBtn.clicked.connect(lambda: self.selectDir(self.parDirLine))
        self.dataDirBtn.clicked.connect(lambda: self.selectDir(self.dataDirLine))
        self.logDirLine.textChanged.connect(lambda: self.updateDirObj(self.logDir))
        self.parDirLine.textChanged.connect(lambda: self.updateDirObj(self.parDir))
        self.dataDirLine.textChanged.connect(lambda: self.updateDirObj(self.dataDir))

        #################################################################################


    def actionConnections(self):

        self.action_Config_File.triggered.connect(self.showDial)

        
    