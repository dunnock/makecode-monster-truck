def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_mes_dpad_controller_id_button_1_up():
    wuKong.stop_motor(wuKong.MotorList.M2)
    basic.show_icon(IconNames.SQUARE)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_1_UP,
    on_mes_dpad_controller_id_button_1_up)

def on_mes_dpad_controller_id_button_2_up():
    wuKong.stop_motor(wuKong.MotorList.M2)
    basic.show_icon(IconNames.SQUARE)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_2_UP,
    on_mes_dpad_controller_id_button_2_up)

def on_mes_dpad_controller_id_button_2_down():
    global ServoVelocity
    basic.show_icon(IconNames.COW)
    ServoVelocity = -2
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_2_DOWN,
    on_mes_dpad_controller_id_button_2_down)

def on_mes_dpad_controller_id_button_1_down():
    global ServoVelocity
    basic.show_icon(IconNames.HOUSE)
    ServoVelocity = 2
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_1_DOWN,
    on_mes_dpad_controller_id_button_1_down)

basic.show_icon(IconNames.HEART)
