import os
import re
import argparse
import shutil
import subprocess
from sys import platform
from shutil import copytree
from pathlib import Path

if platform == "win32":
    burpsuite_path = os.path.join(str(os.getenv("APPDATA")), "BurpSuite")
elif platform == "linux" or platform == "darwin":
    burpsuite_path = os.path.join(str(os.getenv("HOME")), ".BurpSuite")
else:
    print("Unsuported platform")
    exit()


def cmdline_args():
    parser = argparse.ArgumentParser(description="Burp Browser Profiles")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-P", "--profile", help="Create or open a profile")
    group.add_argument(
        "-p",
        "--proxy",
        nargs="?",
        action="store",
        const="127.0.0.1:8080",
        help="Specify a proxy server to use, will use 127.0.0.1:8080 by default",
        default="",
    )
    parser.add_argument(
        "-c",
        "--color",
        choices=["blue", "cyan", "green", "yellow", "orange", "red", "magenta", "pink"],
        help="Specify a color to use",
    )
    parser.add_argument("-u", "--user-agent", help="Specify an user agent to use")
    group.add_argument(
        "-x", "--disable-proxy", action="store_true", help="Disable the proxy"
    )
    parser.add_argument(
        "-d",
        "--enable-remote-debugging",
        action="store_true",
        help="Enable remote debugging",
    )
    parser.add_argument(
        "-L", "--list-profiles", action="store_true", help="Disable the proxy"
    )
    parser.add_argument("-D", "--delete-profile", help="Delete a profile")

    ar = parser.parse_args()

    if not (ar.profile or ar.list_profiles or ar.delete_profile):
        parser.print_help()
        exit()

    if (
        ar.proxy
        or ar.color
        or ar.user_agent
        or ar.disable_proxy
        or ar.disable_remote_debugging
    ) and ar.profile is None:
        parser.error("-P/--profile is required when using this argument")
    else:
        return ar


def profiles_dir_does_not_exist():
    profiles_dir = os.path.join(burpsuite_path, "burp-browser-profiles")
    if os.path.exists(profiles_dir):
        return False
    else:
        return True


def profiles_data_dir_does_not_exist():
    profiles_dir = os.path.join(burpsuite_path, "burp-browser-profiles_data")
    if os.path.exists(profiles_dir):
        return False
    else:
        return True


def setup_profiles_dir_and_data():
    os.mkdir(os.path.join(burpsuite_path, "burp-browser-profiles"))
    if profiles_data_dir_does_not_exist():
        os.mkdir(os.path.join(burpsuite_path, "burp-browser-profiles_data"))
        copytree(
            "burp-browser-profiles-theme",
            os.path.join(
                burpsuite_path,
                "burp-browser-profiles_data",
                "burp-browser-profiles-theme",
            ),
        )
        copytree(
            "burp-browser-profiles-extension",
            os.path.join(
                burpsuite_path,
                "burp-browser-profiles_data",
                "burp-browser-profiles-extension",
            ),
        )
    return


def setup_profile(profile_name):
    if (
        os.path.exists(
            os.path.join(burpsuite_path, "burp-browser-profiles", profile_name)
        )
        is False
    ):
        copytree(
            os.path.join(burpsuite_path, "pre-wired-browser"),
            os.path.join(burpsuite_path, "burp-browser-profiles", profile_name),
        )
        copytree(
            os.path.join(
                burpsuite_path,
                "burp-browser-profiles_data",
                "burp-browser-profiles-theme",
            ),
            os.path.join(
                burpsuite_path,
                "burp-browser-profiles",
                profile_name,
                "burp-browser-profiles-theme",
            ),
        )
        copytree(
            os.path.join(
                burpsuite_path,
                "burp-browser-profiles_data",
                "burp-browser-profiles-extension",
            ),
            os.path.join(
                burpsuite_path,
                "burp-browser-profiles",
                profile_name,
                "burp-browser-profiles-extension",
            ),
        )


def list_profiles():
    for profile in os.listdir(os.path.join(burpsuite_path, "burp-browser-profiles")):
        print(profile)


def delete_profile(profile_name):
    if (
        os.path.exists(
            os.path.join(burpsuite_path, "burp-browser-profiles", profile_name)
        )
        is True
    ):
        shutil.rmtree(
            os.path.join(burpsuite_path, "burp-browser-profiles", profile_name)
        )


def prepare_colors(color_name):
    if color_name == "blue":
        return "blue:[0,0,255]"
    if color_name == "cyan":
        return "cyan:[0,255,255]"
    if color_name == "green":
        return "green:[0,255,0]"
    if color_name == "yellow":
        return "yellow:[255,255,0]"
    if color_name == "orange":
        return "orange:[255,140,0]"
    if color_name == "red":
        return "red:[255,0,0]"
    if color_name == "pink":
        return "pink:[255,105,180]"
    if color_name == "magenta":
        return "magenta:[128,0,128]"


def setup_color(color_name, profile_name):
    frame_color = str(prepare_colors(color_name)).split(":")[1]
    extension_color = str(prepare_colors(color_name)).split(":")[0]

    with open(
        os.path.join(
            burpsuite_path,
            "burp-browser-profiles",
            profile_name,
            "burp-browser-profiles-theme",
            "manifest.json",
        ),
        "r",
        encoding="utf-8",
    ) as theme_file:
        data = theme_file.readlines()
    data[8] = '"frame" : ' + frame_color + "\n"

    with open(
        os.path.join(
            burpsuite_path,
            "burp-browser-profiles",
            profile_name,
            "burp-browser-profiles-theme",
            "manifest.json",
        ),
        "w",
        encoding="utf-8",
    ) as theme_file:
        theme_file.writelines(data)

    with open(
        os.path.join(
            burpsuite_path,
            "burp-browser-profiles",
            profile_name,
            "burp-browser-profiles-extension",
            "background.js",
        ),
        "r",
        encoding="utf-8",
    ) as extension_file:
        data = extension_file.readlines()

    data[0] = "var color = '" + extension_color + "';\n"

    with open(
        os.path.join(
            burpsuite_path,
            "burp-browser-profiles",
            profile_name,
            "burp-browser-profiles-extension",
            "background.js",
        ),
        "w",
        encoding="utf-8",
    ) as extension_file:
        extension_file.writelines(data)


def reset_profile_color(profile_name):
    if os.path.exists(
        os.path.join(
            burpsuite_path,
            "burp-browser-profiles",
            profile_name,
            "Default",
            "Preferences",
        )
    ):
        with open(
            os.path.join(
                burpsuite_path,
                "burp-browser-profiles",
                profile_name,
                "Default",
                "Preferences",
            ),
            "r",
            encoding="utf-8",
        ) as preferences_file:
            data = preferences_file.read()
        data = re.sub(r"\"theme[^}]*}}", '"theme":{"use_system":true}', data)
        with open(
            os.path.join(
                burpsuite_path,
                "burp-browser-profiles",
                profile_name,
                "Default",
                "Preferences",
            ),
            "w",
            encoding="utf-8",
        ) as preferences_file:
            preferences_file.write(data)


def chrome_binary_path():
    path = sorted(
        filter(
            os.path.isdir, Path(os.path.join(burpsuite_path, "burpbrowser")).iterdir()
        ),
        key=os.path.getmtime,
        reverse=True,
    )
    if platform == "win32":
        return os.path.join(path[0], "chrome.exe")
    if platform == "darwin":
        return os.path.join(path[0], "Chromium.app", "Contents", "MacOS", "Chromium")
    if platform == "linux":
        return os.path.join(path[0], "chrome")


if __name__ == "__main__":
    args = cmdline_args()

    if profiles_dir_does_not_exist():
        setup_profiles_dir_and_data()
    if args.list_profiles:
        list_profiles()
        exit()
    if args.delete_profile:
        delete_profile(args.delete_profile)
        exit()
    if args.profile:
        setup_profile(args.profile)

    command = [str(chrome_binary_path())]

    proxy = "--proxy-server=127.0.0.1:8080"
    if args.proxy:
        proxy = "--proxy-server=" + args.proxy

    if not args.disable_proxy:
        command.append(proxy)

    remote_debugging = "--remote-debugging-port=0"
    if args.enable_remote_debugging:
        command.append(remote_debugging)

    if args.user_agent:
        user_agent = "--user-agent=" + args.user_agent
        command.append(user_agent)

    data_dir = "--user-data-dir=" + os.path.join(
        burpsuite_path, "burp-browser-profiles", args.profile
    )
    command.append(data_dir)

    extensions_path = "--load-extension=" + os.path.join(
        burpsuite_path, "burp-chromium-extension"
    )

    if args.color:
        setup_color(args.color, args.profile)
        extensions_path = (
            extensions_path
            + ","
            + os.path.join(
                burpsuite_path,
                "burp-browser-profiles",
                args.profile,
                "burp-browser-profiles-extension",
            )
            + ","
            + os.path.join(
                burpsuite_path,
                "burp-browser-profiles",
                args.profile,
                "burp-browser-profiles-theme",
            )
        )
    reset_profile_color(args.profile)
    command.append(extensions_path)

    other_startup_args = [
        "--disable-ipc-flooding-protection",
        "--disable-xss-auditor",
        "--disable-bundled-ppapi-flash",
        "--disable-plugins-discovery",
        "--disable-default-apps",
        "--disable-prerender-local-predictor",
        "--disable-sync",
        "--disable-breakpad",
        "--disable-crash-reporter",
        "--disable-prerender-local-predictor",
        "--disk-cache-size=0",
        "--disable-settings-window",
        "--disable-notifications",
        "--disable-speech-api",
        "--disable-file-system",
        "--disable-presentation-api",
        "--disable-permissions-api",
        "--disable-new-zip-unpacker",
        "--disable-media-session-api",
        "--no-experiments",
        "--no-events",
        "--no-first-run",
        "--no-default-browser-check",
        "--no-pings",
        "--no-service-autorun",
        "--media-cache-size=0",
        "--use-fake-device-for-media-stream",
        "--dbus-stub",
        "--disable-background-networking",
        "--disable-features=ChromeWhatsNewUI,HttpsUpgrades",
        "--proxy-bypass-list=<-loopback>",
        "--disable-background-networking",
        "--ignore-certificate-errors",
        "chrome://newtab",
    ]
    command = command + other_startup_args
    if platform == "win32":
        subprocess.Popen(command, creationflags=0x00000008)
    else:
        subprocess.Popen(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
