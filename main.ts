bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Diamond)
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_1_UP, function () {
    wuKong.stopMotor(wuKong.MotorList.M2)
    basic.showIcon(IconNames.Meh)
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_2_UP, function () {
    wuKong.stopMotor(wuKong.MotorList.M2)
    basic.showIcon(IconNames.Silly)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(100)
    basic.showIcon(IconNames.Giraffe)
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_2_DOWN, function () {
    wuKong.setMotorSpeed(wuKong.MotorList.M2, -20)
    basic.showIcon(IconNames.Yes)
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_1_DOWN, function () {
    wuKong.setMotorSpeed(wuKong.MotorList.M2, 50)
    basic.showIcon(IconNames.Happy)
})
basic.showIcon(IconNames.Surprised)
