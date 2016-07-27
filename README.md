## INTRODUCTION

Some Expect scripts with a Python wrapper that collect configuration from multiple network devices. Similar to fetchconfig[1] but can connect to the devices with ssh.

It can fetch the configuration from Cisco, Juniper, RedBack devices. See expect/* for a full list of devices and operating systems.

It saves the configurations in configs/*, in seperate daily folders.

## REQUIREMENTS
- Python 2
- Expect 5+

## USAGE

- Edit getconfig.ini.
- Add devices to device_list.ini.

```
[DEVICE-NAME]
type=The Device type. Files in expect/* are types. Ex: cisco-nxos-7k
ip=127.0.0.1
user=USERNAME
password=PASSWORD
enable=FALSE or the enable password
```

- Start the getconfig.sh script.
- If it encounters an error during fetch it will try to send an email through localhost.

## LICENSE
Public Domain - Creative Commons CC0 1.0 Universal (CC-0)


[1] https://github.com/udhos/fetchconfig
