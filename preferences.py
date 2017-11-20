import os
from config import get_preferences_path, get_preferences_backup_dir
from utils import execute_shell


def backup():
    print ''
    print 'Backuping preferences (.plist)...'
    domains = execute_shell(["defaults", "domains"])
    domains = domains.split("\n")[0].split(", ")
    domains = ["NSGlobalDomain"] + domains
    for domain in domains:
        filepath = get_preferences_path(domain)
        print "Backing up: " + domain + " to " + filepath
        execute_shell(["defaults", "export", domain, filepath])


def restore():
    print ''
    print 'Restoring preferences (.plist)...'
    backup_dir = get_preferences_backup_dir()
    domains = get_domains()
    for domain in domains:
        filename = domain + ".plist"
        print "Importing: " + domain
        execute_shell(["defaults", "import", domain,
                       os.path.join(backup_dir, filename)])

def get_domains():
    domains = []
    backup_dir = get_preferences_backup_dir()
    for filename in sorted(os.listdir(backup_dir)):
        if ".plist" in filename:
            domains.append(filename.replace(".plist", ""))
    return domains
