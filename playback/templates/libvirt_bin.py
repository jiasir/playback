conf_libvirt_bin = """# Defaults for libvirt-bin initscript (/etc/init.d/libvirt-bin)
# This is a POSIX shell fragment

# Start libvirtd to handle qemu/kvm:
start_libvirtd="yes"

# options passed to libvirtd, add "-l" to listen on tcp
libvirtd_opts="-l -d -f /etc/libvirt/libvirtd.conf"

# pass in location of kerberos keytab
#export KRB5_KTNAME=/etc/libvirt/libvirt.keytab
"""
