# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

import base
import objc
from CoreFoundation import *


#Generated in Mac OS X 10.8.2 using the following command:
#gen_bridge_metadata -c '-l/System/Library/Frameworks/IOKit.framework/IOKit -I/System/Library/Frameworks/IOKit.framework/Headers/ps/' /System/Library/Frameworks/IOKit.framework/Headers/ps/IOPowerSources.h /System/Library/Frameworks/IOKit.framework/Headers/ps/IOPSKeys.h
#
#Following are added manually, because public headers misses their definitions:
#- kIOPMUPSPowerKey
#- kIOPMBatteryPowerKey
#- kIOPMACPowerKey
#They were found at http://opensource.apple.com/source/IOKitUser/IOKitUser-514.16.50/pwr_mgt.subproj/IOPMLibPrivate.h
IO_POWER_SOURCES_BRIDGESUPPORT = """
<?xml version='1.0'?>
<!DOCTYPE signatures SYSTEM "file://localhost/System/Library/DTDs/BridgeSupport.dtd">
<signatures version='1.0'>
    <depends_on path="/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation" />
    <string_constant name='kIOPSACPowerValue' value='AC Power'/>
    <string_constant name='kIOPSBatteryFailureModesKey' value='BatteryFailureModes'/>
    <string_constant name='kIOPSBatteryHealthConditionKey' value='BatteryHealthCondition'/>
    <string_constant name='kIOPSBatteryHealthKey' value='BatteryHealth'/>
    <string_constant name='kIOPSBatteryPowerValue' value='Battery Power'/>
    <string_constant name='kIOPSCheckBatteryValue' value='Check Battery'/>
    <string_constant name='kIOPSCommandDelayedRemovePowerKey' value='Delayed Remove Power'/>
    <string_constant name='kIOPSCommandEnableAudibleAlarmKey' value='Enable Audible Alarm'/>
    <string_constant name='kIOPSCommandStartupDelayKey' value='Startup Delay'/>
    <string_constant name='kIOPSCurrentCapacityKey' value='Current Capacity'/>
    <string_constant name='kIOPSCurrentKey' value='Current'/>
    <string_constant name='kIOPSDeadWarnLevelKey' value='Shutdown Level'/>
    <string_constant name='kIOPSDesignCapacityKey' value='DesignCapacity'/>
    <string_constant name='kIOPSDynamicStorePath' value='/IOKit/PowerSources'/>
    <string_constant name='kIOPSFailureCellImbalance' value='Cell Imbalance'/>
    <string_constant name='kIOPSFailureChargeFET' value='Charge FET'/>
    <string_constant name='kIOPSFailureChargeOverCurrent' value='Charge Over-Current'/>
    <string_constant name='kIOPSFailureChargeOverTemp' value='Charge Over-Temperature'/>
    <string_constant name='kIOPSFailureDataFlushFault' value='Data Flush Fault'/>
    <string_constant name='kIOPSFailureDischargeFET' value='Discharge FET'/>
    <string_constant name='kIOPSFailureDischargeOverCurrent' value='Discharge Over-Current'/>
    <string_constant name='kIOPSFailureDischargeOverTemp' value='Discharge Over-Temperature'/>
    <string_constant name='kIOPSFailureExternalInput' value='Externally Indicated Failure'/>
    <string_constant name='kIOPSFailureFuseBlown' value='Fuse Blown'/>
    <string_constant name='kIOPSFailureOpenThermistor' value='Open Thermistor'/>
    <string_constant name='kIOPSFailurePeriodicAFEComms' value='Periodic AFE Comms'/>
    <string_constant name='kIOPSFailurePermanentAFEComms' value='Permanent AFE Comms'/>
    <string_constant name='kIOPSFailureSafetyOverVoltage' value='Safety Over-Voltage'/>
    <string_constant name='kIOPSFairValue' value='Fair'/>
    <string_constant name='kIOPSGoodValue' value='Good'/>
    <string_constant name='kIOPSHardwareSerialNumberKey' value='Hardware Serial Number'/>
    <string_constant name='kIOPSHealthConfidenceKey' value='HealthConfidence'/>
    <string_constant name='kIOPSInternalBatteryType' value='InternalBattery'/>
    <string_constant name='kIOPSInternalType' value='Internal'/>
    <string_constant name='kIOPSIsChargedKey' value='Is Charged'/>
    <string_constant name='kIOPSIsChargingKey' value='Is Charging'/>
    <string_constant name='kIOPSIsFinishingChargeKey' value='Is Finishing Charge'/>
    <string_constant name='kIOPSIsPresentKey' value='Is Present'/>
    <string_constant name='kIOPSLowWarnLevelKey' value='Low Warn Level'/>
    <string_constant name='kIOPSMaxCapacityKey' value='Max Capacity'/>
    <string_constant name='kIOPSMaxErrKey' value='MaxErr'/>
    <string_constant name='kIOPSNameKey' value='Name'/>
    <string_constant name='kIOPSNetworkTransportType' value='Ethernet'/>
    <string_constant name='kIOPSNotifyLowBattery' value='com.apple.system.powersources.lowbattery'/>
    <string_constant name='kIOPSOffLineValue' value='Off Line'/>
    <string_constant name='kIOPSPermanentFailureValue' value='Permanent Battery Failure'/>
    <string_constant name='kIOPSPoorValue' value='Poor'/>
    <string_constant name='kIOPSPowerAdapterCurrentKey' value='Current'/>
    <string_constant name='kIOPSPowerAdapterFamilyKey' value='FamilyCode'/>
    <string_constant name='kIOPSPowerAdapterIDKey' value='AdapterID'/>
    <string_constant name='kIOPSPowerAdapterRevisionKey' value='AdapterRevision'/>
    <string_constant name='kIOPSPowerAdapterSerialNumberKey' value='SerialNumber'/>
    <string_constant name='kIOPSPowerAdapterSourceKey' value='Source'/>
    <string_constant name='kIOPSPowerAdapterWattsKey' value='Watts'/>
    <string_constant name='kIOPSPowerSourceIDKey' value='Power Source ID'/>
    <string_constant name='kIOPSPowerSourceStateKey' value='Power Source State'/>
    <string_constant name='kIOPSSerialTransportType' value='Serial'/>
    <string_constant name='kIOPSTimeRemainingNotificationKey' value='com.apple.system.powersources.timeremaining'/>
    <string_constant name='kIOPSTimeToEmptyKey' value='Time to Empty'/>
    <string_constant name='kIOPSTimeToFullChargeKey' value='Time to Full Charge'/>
    <string_constant name='kIOPSTransportTypeKey' value='Transport Type'/>
    <string_constant name='kIOPSTypeKey' value='Type'/>
    <string_constant name='kIOPSUPSManagementClaimed' value='/IOKit/UPSPowerManagementClaimed'/>
    <string_constant name='kIOPSUPSType' value='UPS'/>
    <string_constant name='kIOPSUSBTransportType' value='USB'/>
    <string_constant name='kIOPSVendorDataKey' value='Vendor Specific Data'/>
    <string_constant name='kIOPSVoltageKey' value='Voltage'/>
    <string_constant name="kIOPMUPSPowerKey" value="UPS Power" />
    <string_constant name="kIOPMBatteryPowerKey" value="Battery Power" />
    <string_constant name="kIOPMACPowerKey" value="AC Power" />
    <enum name='kIOPSLowBatteryWarningEarly' value='2'/>
    <enum name='kIOPSLowBatteryWarningFinal' value='3'/>
    <enum name='kIOPSLowBatteryWarningNone' value='1'/>
    <enum name='kIOPSTimeRemainingUnknown' value='-1'/>
    <enum name='kIOPSTimeRemainingUnlimited' value='-2'/>
    <function name='IOPSCopyExternalPowerAdapterDetails'>
        <retval type='^{__CFDictionary=}' already_retained='true'/>
    </function>
    <function name='IOPSCopyPowerSourcesInfo'>
        <retval type='@' already_retained='true'/>
    </function>
    <function name='IOPSCopyPowerSourcesList'>
        <arg type='@'/>
        <retval type='^{__CFArray=}' already_retained='true'/>
    </function>
    <function name='IOPSGetBatteryWarningLevel'>
        <retval type='i'/>
    </function>
    <function name='IOPSGetPowerSourceDescription'>
        <arg type='@'/>
        <arg type='@'/>
        <retval type='^{__CFDictionary=}'/>
    </function>
    <function name='IOPSGetProvidingPowerSourceType'>
        <arg type='@'/>
        <retval type='^{__CFString=}'/>
    </function>
    <function name='IOPSGetTimeRemainingEstimate'>
        <retval type='d'/>
    </function>
    <function name='IOPSNotificationCreateRunLoopSource'>
        <arg type='^?' function_pointer='true'>
            <arg type='^v'/>
            <retval type='v'/>
        </arg>
        <arg type='^v'/>
        <retval type='^{__CFRunLoopSource=}' already_retained='true'/>
    </function>
</signatures>
"""

_objc.parseBridgeSupport(IO_POWER_SOURCES_BRIDGESUPPORT,
    globals(),
    _objc.pathForFramework("/System/Library/Frameworks/IOKit.framework"))


POWER_TYPE_MAP = {
    kIOPMACPowerKey: base.POWER_TYPE_AC,
    kIOPMBatteryPowerKey: base.POWER_TYPE_BATTERY,
    kIOPMUPSPowerKey: base.POWER_TYPE_UPS
}


WARNING_LEVEL_MAP = {
    kIOPSLowBatteryWarningNone: base.LOW_BATTERY_WARNING_NONE,
    kIOPSLowBatteryWarningEarly: base.LOW_BATTERY_WARNING_EARLY,
    kIOPSLowBatteryWarningFinal: base.LOW_BATTERY_WARNING_FINAL
}


class PowerManagement(base.PowerManagementBase):
    def get_providing_power_source_type(self):
        providing_source = IOPSCopyPowerSourcesInfo()
        power_type = IOPSGetProvidingPowerSourceType(providing_source)
        return POWER_TYPE_MAP[power_type]

    def get_low_battery_warning_level(self):
        warning_level = IOPSGetBatteryWarningLevel()
        return WARNING_LEVEL_MAP[warning_level]

    def get_time_remaining_estimate(self):
        return int(IOPSGetTimeRemainingEstimate())

    def get_external_power_adapter_info(self):
        return IOPSCopyExternalPowerAdapterDetails()

    def get_power_sources_info(self):
        blob = IOPSCopyPowerSourcesInfo()
        return [IOPSGetPowerSourceDescription(blob, source) for source in IOPSCopyPowerSourcesList(blob)]

    def add_observer(self, observer):
        was_empty = len(self._weak_observers) == 0
        super(PowerManagement, self).add_observer(observer)
        if was_empty:

            @objc.callbackFor(IOPSNotificationCreateRunLoopSource)
            def on_power_sources_change(context):
                for weak_observer in self._weak_observers:
                    observer = weak_observer()
                    if observer:
                        observer.on_power_sources_change(self)

            self._source = IOPSNotificationCreateRunLoopSource(on_power_sources_change, None)
            CFRunLoopAddSource(CFRunLoopGetMain(), self._source, kCFRunLoopDefaultMode)

    def remove_observer(self, observer):
        super(PowerManagement, self).remove_observer(observer)
        if len(self._weak_observers) == 0:
            CFRunLoopRemoveSource(CFRunLoopGetMain(), self._source, kCFRunLoopDefaultMode)
            self._source = None
