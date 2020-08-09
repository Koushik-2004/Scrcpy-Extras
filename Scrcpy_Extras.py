import datetime
import tkinter as tk

from ppadb.client import Client

devices = Client(host='127.0.0.1', port=5037).devices()

if len(devices) == 0:
    print()
    print('No Devices Connected')
    print()
    quit()

device = devices[0]


#########################################################Functions######################################################
def install():
    def install_apk():
        try:
            install.title('Installer(ADB Based)')
            install_bttn['fg'] = 'black'
            device.install(package_file_path.get())
            print('[ALERT] Package Installed [ALERT]')
            install_bttn['fg'] = 'green'
        except:
            print('[ALERT] Failed to Install Package [ALERT]')
            install.title('Error! Invalid Path or Package Already Installed')
            install_bttn['fg'] = 'red'

    install = tk.Tk()
    install.title('Installer(ADB Based)')

    tk.Label(install, text='# ----- Android Package Path ----- #').grid(pady=2)
    package_file_path = tk.Entry(install, width=80)
    package_file_path.grid()
    install_bttn = tk.Button(install, text='Install', fg='black', command=install_apk)
    install_bttn.grid()

    install.mainloop()


def reboot():
    device.reboot()
    print('[0] Reboot Initiated [0]')


def screenshot():
    try:
        image_name = 'Screenshots/' + str(datetime.datetime.now()).replace(':', '.') + '.png'
        image = open(image_name, 'wb')
        image.write(device.screencap())
        image.close()
        print('[INFO] Screenshot saved in ' + image_name)
    except RuntimeError:
        print('[ALERT] Device not found or disconnected [ALERT]')


def sys_info():
    def load_info():
        try:
            properties = Client(host='127.0.0.1', port=5037).devices()[0].get_properties()
            d_m['text'], maker['text'], s_v['text'], s_p['text'], c_a['text'] = properties['ro.product.model'], \
                                                                                properties['ro.product.manufacturer'], \
                                                                                properties['ro.build.version.sdk'], \
                                                                                properties[
                                                                                    'ro.build.version.security_patch'], \
                                                                                properties['ro.product.cpu.abi']
            sys_info.title('About ' + properties['ro.product.model'])
            if load['text'] == 'Reload':
                print('[ALERT] Info Reloaded [ALERT]')
            else:
                print('[ALERT] Info Loaded [ALERT]')
                load['text'] = 'Reload'
        except:
            sys_info.title('About')
            d_m['text'], maker['text'], s_v['text'], s_p['text'], c_a[
                'text'] = 'Error! Fetching Data', 'Error! Fetching Data', 'Error! Fetching Data', 'Error! Fetching Data', 'Error! Fetching Data'
            print('[ALERT] Error! Fetching Data [ALERT]')

    sys_info = tk.Tk()
    sys_info.title('')
    sys_info.minsize(width=230, height=130)
    sys_info.minsize(width=230, height=130)

    frame = tk.Frame(sys_info, relief=tk.SUNKEN, borderwidth=1)

    tk.Label(frame, text='Device Model: ').grid(row=0, column=0, sticky='e')
    d_m = tk.Label(frame, text='NaN')
    d_m.grid(row=0, column=1, sticky='w')

    tk.Label(frame, text='Manufacturer: ').grid(row=1, column=0, sticky='e')
    maker = tk.Label(frame, text='NaN')
    maker.grid(row=1, column=1, sticky='w')

    tk.Label(frame, text='SDK Version: ').grid(row=2, column=0, sticky='e')
    s_v = tk.Label(frame, text='NaN')
    s_v.grid(row=2, column=1, sticky='w')

    tk.Label(frame, text='Security Patch: ').grid(row=3, column=0, sticky='e')
    s_p = tk.Label(frame, text='NaN')
    s_p.grid(row=3, column=1, sticky='w')

    tk.Label(frame, text='CPU Architecture: ').grid(row=4, column=0, sticky='e')
    c_a = tk.Label(frame, text='NaN')
    c_a.grid(row=4, column=1, sticky='w')

    frame.pack(fill=tk.BOTH)

    load = tk.Button(sys_info, text='Load', width=7, height=1, command=load_info)
    load.pack()

    sys_info.mainloop()


def macro():
    print('[#/3] Function Not Added Yet')
    pass  # Will add later if I have time and some idea  # Anyway feel free to improve this one. It is not that great


########################################################################################################################

extra_control_panel = tk.Tk()
extra_control_panel.title("Scrcpy Extra's")
extra_control_panel.minsize(width=241, height=124)
extra_control_panel.maxsize(width=241, height=124)

menu_bttns = tk.Frame(extra_control_panel, relief=tk.SUNKEN, borderwidth=1)

tk.Button(menu_bttns, text='ScreenShot', width=10, height=2, bg='grey', command=screenshot).grid(row=0, column=1)
tk.Button(menu_bttns, text='Reboot', width=10, height=2, bg='grey', command=reboot).grid(row=1, column=0)
tk.Button(menu_bttns, text='Install', width=10, height=2, bg='grey', command=install).grid(row=1, column=1)
tk.Button(menu_bttns, text='About', width=10, height=2, bg='grey', command=sys_info).grid(row=1, column=2)
tk.Button(menu_bttns, text='Macro', width=10, height=2, bg='grey', command=macro).grid(row=2, column=1)

menu_bttns.grid()

extra_control_panel.mainloop()
