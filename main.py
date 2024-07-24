import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

class LinuxDistroApp:
    def __init__(self, master):
        self.master = master
        self.master.title("DistroDictionary")
        self.master.geometry("400x500")

        self.create_widgets()

    def create_widgets(self):
        # Search frame
        search_frame = ttk.Frame(self.master)
        search_frame.pack(pady=10, padx=10, fill=tk.X)

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_list)
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side=tk.LEFT, padx=(0, 10))


        # Listbox
        self.listbox = tk.Listbox(self.master, width=50, height=20)
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Populate listbox with 100 distros
        self.distros = [
    ("Ubuntu", "Canonical Ltd.", "UK"),
    ("Fedora", "Red Hat", "USA"),
    ("Debian", "Debian Project", "Global"),
    ("Arch Linux", "Arch Linux Team", "Canada"),
    ("Linux Mint", "Linux Mint Team", "Ireland"),
    ("openSUSE", "openSUSE Project", "Germany"),
    ("Manjaro", "Manjaro GmbH & Co. KG", "Germany"),
    ("CentOS", "The CentOS Project", "USA"),
    ("Elementary OS", "elementary, Inc.", "USA"),
    ("Zorin OS", "Zorin Group", "Ireland"),
    ("Solus", "Solus Project", "Ireland"),
    ("Kali Linux", "Offensive Security", "USA"),
    ("Puppy Linux", "Barry Kauler & Community", "Australia"),
    ("MX Linux", "MX Dev Team", "Greece"),
    ("Deepin", "Wuhan Deepin Technology Co.", "China"),
    ("Tails", "The Tails Project", "Global"),
    ("Pop!_OS", "System76", "USA"),
    ("Lubuntu", "Lubuntu Team", "Global"),
    ("Xubuntu", "Xubuntu Team", "Global"),
    ("Kubuntu", "Kubuntu Team", "Global"),
    ("Gentoo", "Gentoo Foundation", "USA"),
    ("Slackware", "Patrick Volkerding", "USA"),
    ("antiX", "antiX Team", "Greece"),
    ("PCLinuxOS", "PCLinuxOS Team", "USA"),
    ("Mageia", "Mageia Community", "France"),
    ("Peppermint", "Peppermint Team", "USA"),
    ("KDE neon", "KDE", "Global"),
    ("LXLE", "LXLE Team", "USA"),
    ("Bodhi Linux", "Bodhi Linux Team", "USA"),
    ("Q4OS", "Q4OS Team", "Czech Republic"),
    ("Void Linux", "Void Linux Team", "Global"),
    ("Sabayon", "Sabayon Team", "Italy"),
    ("Knoppix", "Klaus Knopper", "Germany"),
    ("ReactOS", "ReactOS Team", "Global"),
    ("Alpine Linux", "Alpine Linux Development Team", "Global"),
    ("Parrot OS", "Parrot Security Team", "Italy"),
    ("Tiny Core Linux", "Team Tiny Core", "USA"),
    ("Porteus", "Porteus Team", "Poland"),
    ("SparkyLinux", "SparkyLinux Team", "Poland"),
    ("4MLinux", "4MLinux Team", "Poland"),
    ("Nitrux", "Nitrux Development Team", "Nicaragua"),
    ("Qubes OS", "Invisible Things Lab", "Poland"),
    ("Clear Linux", "Intel Corporation", "USA"),
    ("Endless OS", "Endless Mobile, Inc.", "USA"),
    ("NixOS", "NixOS Foundation", "Netherlands"),
    ("OpenMandriva", "OpenMandriva Association", "France"),
    ("Feren OS", "Feren OS Team", "UK"),
    ("Netrunner", "Blue Systems", "Germany"),
    ("Endeavour OS", "EndeavourOS Team", "Global"),
    ("Devuan", "Devuan Team", "Global"),
    ("ROSA", "ROSA Company", "Russia"),
    ("Parabola GNU/Linux-libre", "Parabola Team", "Global"),
    ("Artix Linux", "Artix Linux Team", "Global"),
    ("Hyperbola GNU/Linux-libre", "Hyperbola Project", "Global"),
    ("PureOS", "Purism", "USA"),
    ("Raspbian", "Raspberry Pi Foundation", "UK"),
    ("BlackArch Linux", "BlackArch Team", "Global"),
    ("GhostBSD", "GhostBSD Project", "Canada"),
    ("Trisquel", "The Trisquel Project", "Spain"),
    ("Dragora GNU/Linux-Libre", "Dragora Project", "Argentina"),
    ("Guix System", "GNU Project", "Global"),
    ("Armbian", "Armbian Team", "Global"),
    ("KaOS", "KaOS Team", "Global"),
    ("AV Linux", "Glen MacArthur", "Canada"),
    ("Scientific Linux", "Fermilab", "USA"),
    ("Pardus", "TÜBİTAK ULAKBİM", "Turkey"),
    ("Chakra Linux", "Chakra Project", "Global"),
    ("Linspire", "PC/OpenSystems LLC", "USA"),
    ("Oracle Linux", "Oracle Corporation", "USA"),
    ("Apricity OS", "Apricity OS Team", "USA"),
    ("Maui Linux", "Maui Project", "Global"),
    ("SteamOS", "Valve Corporation", "USA"),
    ("Lakka", "Lakka Team", "France"),
    ("Batocera.linux", "Batocera Team", "France"),
    ("OpenMediaVault", "Volker Theile", "Germany"),
    ("OpenWrt", "OpenWrt Project", "Global"),
    ("pfSense", "Netgate", "USA"),
    ("OPNsense", "Deciso B.V.", "Netherlands"),
    ("Proxmox VE", "Proxmox Server Solutions GmbH", "Austria"),
    ("CoreOS", "Red Hat", "USA"),
    ("Quirky Linux", "Barry Kauler", "Australia"),
    ("Bedrock Linux", "Bedrock Linux Team", "USA"),
    ("Redcore Linux", "Redcore Linux Team", "Romania"),
    ("Exherbo", "Exherbo Team", "Global"),
    ("GoboLinux", "GoboLinux Team", "Brazil"),
    ("Parted Magic", "Patrick Verner", "USA"),
    ("Pentoo", "Pentoo Team", "Global"),
    ("Porteus Kiosk", "Tomasz Jokiel", "Poland"),
    ("Revenge OS", "Revenge OS Team", "USA"),
    ("Robolinux", "Robolinux Team", "USA"),
    ("Slax", "Tomas Matejicek", "Czech Republic"),
    ("SliTaz", "SliTaz Association", "Switzerland"),
    ("SwagArch", "SwagArch Team", "Global"),
    ("SystemRescue", "SystemRescue Team", "France"),
    ("Ultimate Edition", "TheeMahn", "USA"),
    ("Zenwalk", "Jean-Philippe Guillemin", "France"),
    ("Antergos", "Antergos Developers", "Global"),
    ("Archlabs", "Archlabs Team", "Global"),
    ("Aurora OS", "Aurora Open Source Software", "Russia"),
    ("BackBox", "BackBox Team", "Italy"),
    ("Bicom Systems PBXware", "Bicom Systems", "UK"),
    ("Bio-Linux", "Environmental Omics Synthesis Centre", "UK"),
    ("Caixa Mágica", "Caixa Mágica Software", "Portugal"),
    ("Calculate Linux", "Calculate Ltd.", "Russia"),
    ("ClearOS", "ClearCenter", "USA"),
    ("Clonezilla", "NCHC Free Software Labs", "Taiwan"),
    ("Cucumber Linux", "Scott Court", "USA"),
    ("Daphile", "Daphile Team", "Global"),
    ("DietPi", "DietPi Team", "Global"),
    ("Dyson", "Dyson Team", "Global"),
    ("EasyOS", "Barry Kauler", "Australia"),
    ("Elastix", "3CX", "Germany"),
    ("Elive", "Elive Team", "Global"),
    ("Emmabuntüs", "Emmabuntüs Collective", "France"),
    ("Endian Firewall", "Endian", "Italy"),
    ("Finnix", "Ryan Finnie", "USA"),
    ("Fuduntu", "Fuduntu Team", "Global"),
    ("Garuda Linux", "Garuda Linux Team", "India"),
    ("Gecko Linux", "Gecko Linux Team", "Global"),
    ("Greenie Linux", "Stanislav Hoferek", "Slovakia"),
    ("Grml", "Grml Solutions", "Austria"),
    ("Hamara Linux", "Hamara Linux Team", "India"),
    ("HandyLinux", "HandyLinux Team", "France"),
    ("Hannah Montana Linux", "Hannah Montana Linux Team", "Global"),
    ("Hybryde", "Hybryde Team", "France"),
    ("Iglunix", "Iglunix Team", "Global"),
    ("IPFire", "IPFire Team", "Germany"),
    ("Jarro Negro", "Jarro Negro Team", "Argentina"),
    ("Kali NetHunter", "Offensive Security", "USA"),
    ("KolibriOS", "KolibriOS Team", "Russia"),
    ("Kwort", "David Cortarello", "Argentina"),
    ("LibreELEC", "LibreELEC Team", "Global"),
    ("Lite", "Lite Linux Team", "Global"),
    ("Lunar Linux", "Lunar Linux Team", "Global"),
    ("Mabox Linux", "Mabox Linux Team", "Poland"),
    ("Macpup", "Macpup Team", "Global"),
    ("Madbox", "Madbox Team", "France"),
    ("Mangaka", "Animesoft International", "France"),
    ("Matriux", "Matriux Team", "India"),
    ("MidnightBSD", "Lucas Holt", "USA"),
    ("MiniNo", "MiniNo Team", "Spain"),
    ("Momonga Linux", "Momonga Project", "Japan"),
    ("Musix", "Musix Team", "Argentina"),
    ("Mythdora", "Mythdora Team", "Global"),
    ("NayuOS", "Nexedi", "France"),
    ("NetBSD", "The NetBSD Foundation", "USA"),
    ("Netrunner Rolling", "Blue Systems", "Germany"),
    ("NomadBSD", "NomadBSD Team", "Germany"),
    ("Nova", "University of Information Sciences", "Cuba"),
    ("NST (Network Security Toolkit)", "NST Team", "USA"),
    ("Obarun", "Obarun Team", "France"),
    ("OpenBSD", "OpenBSD Project", "Canada"),
    ("OpenIndiana", "OpenIndiana Team", "Global"),
    ("openmamba", "openmamba Team", "Italy"),
    ("OpenMandriva Lx", "OpenMandriva Association", "Global"),
    ("Ophcrack", "Objectif Sécurité", "Switzerland"),
    ("Oracle Solaris", "Oracle Corporation", "USA"),
    ("OSGeoLive", "OSGeo", "Global"),
    ("Otaku", "Otaku Team", "Global"),
    ("Overclockix", "Overclockix Team", "Global"),
    ("Parsix GNU/Linux", "Parsix Team", "Iran"),
    ("Pear OS", "Pear Team", "France"),
    ("Peach OSI", "Peach Open Source", "USA"),
    ("Pinguy OS", "Pinguy OS Team", "UK"),
    ("Plamo Linux", "Plamo Linux Project", "Japan"),
    ("Plop Linux", "Elmar Hanlhofer", "Austria"),
    ("Point Linux", "Peter Ryzhenkov", "Russia"),
    ("Pogo Linux", "Pogo Linux, Inc.", "USA"),
    ("Poseidon Linux", "Poseidon Linux Team", "Brazil"),
    ("PrimTux", "PrimTux Team", "France"),
    ("Privatix", "Privatix Team", "Germany"),
    ("ProxmoxVE", "Proxmox Server Solutions GmbH", "Austria"),
    ("Puppy Studio", "Puppy Studio Team", "Global"),
    ("PureOS", "Purism", "USA"),
    ("Qubes OS", "Invisible Things Lab", "Poland"),
    ("Quirky", "Barry Kauler", "Australia"),
    ("RancherOS", "Rancher Labs", "USA"),
    ("Raspberry Slideshow", "Raspberry Slideshow Team", "Global"),
    ("Raspup", "Raspup Team", "Global"),
    ("Redo Rescue", "Redo Rescue Team", "Global"),
    ("Refracta", "Refracta Team", "Global"),
    ("Rescatux", "Rescatux Team", "Spain"),
    ("RISC OS", "RISC OS Open Limited", "UK"),
    ("RoboLinux", "RoboLinux Team", "USA"),
    ("Rocks Cluster Distribution", "UC San Diego", "USA"),
    ("Runtu", "Runtu Team", "Russia"),
    ("Salix", "Salix Team", "Global"),
    ("Satux", "Satux Team", "Global"),
    ("SchilliX", "Jörg Schilling", "Germany"),
    ("Sculpt OS", "Genode Labs", "Germany"),
    ("Secure-K OS", "Mon-K Data Protection", "Italy"),
    ("Semplice Linux", "Semplice Team", "Italy"),
    ("Septor", "Septor Team", "Global"),
    ("Shabdix", "Shabdix Team", "Iran"),
    ("Shells", "Shells, Inc.", "USA"),
    ("Siduction", "Siduction Team", "Germany"),
    ("Simplicity Linux", "Simplicity Linux Team", "UK"),
    ("SME Server", "Koozali Foundation", "USA"),
    ("Smoothwall", "Smoothwall Ltd.", "UK"),
    ("Snowlinux", "Snowlinux Team", "Germany"),
    ("SolydXK", "SolydXK Team", "Netherlands"),
    ("Sophos UTM", "Sophos Group plc", "UK"),
    ("Source Mage GNU/Linux", "Source Mage Team", "Global"),
    ("Springdale Linux", "Princeton University", "USA"),
    ("Star", "Star Labs Systems", "UK"),
    ("Stratux", "Stratux Team", "USA"),
    ("SuperGamer", "SuperGamer Team", "Global"),
    ("SuperX", "Libresoft", "India"),
    ("SwagArch", "SwagArch Team", "Global"),
    ("Symphony OS", "Symphony OS Team", "USA"),
    ("SythOS", "SythOS Team", "Global"),
    ("T2 SDE", "T2 Team", "Germany"),
    ("Tails", "The Tails Project", "Global"),
    ("Thinstation", "Thinstation Team", "Global"),
    ("Tilix", "Tilix Team", "Global"),
    ("ToOpPy Linux", "ToOpPy Team", "France"),
    ("Toutou Linux", "Toutou Linux Team", "France"),
    ("Trident", "Project Trident", "USA"),
    ("TrueNAS", "iXsystems", "USA"),
    ("TrueOS", "iXsystems", "USA"),
    ("Tugux", "Tugux Team", "Tunisia"),
    ("Turnkey Linux", "Turnkey Linux Team", "Australia"),
    ("Untangle", "Untangle, Inc.", "USA"),
    ("VectorLinux", "VectorLinux Team", "Canada"),
    ("Vine Linux", "Vine Linux Project", "Japan"),
    ("Vinux", "Vinux Project", "UK"),
    ("VyOS", "VyOS Project", "Global"),
    ("Webconverger", "Webconverger", "Singapore"),
    ("Whonix", "Whonix Team", "Global"),
    ("Wifislax", "Wifislax Team", "Spain"),
        ]

        for distro in self.distros:
            self.listbox.insert(tk.END, distro[0])

        # Bind events
        self.listbox.bind("<Double-1>", self.show_info)
        self.listbox.bind("<Return>", self.show_info)

    def update_list(self, *args):
        search_term = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        for distro in self.distros:
            if search_term in distro[0].lower():
                self.listbox.insert(tk.END, distro[0])

    def show_info(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            distro_name, developers, location = self.distros[index]
            
            info_window = tk.Toplevel(self.master)
            info_window.title(distro_name)
            info_window.geometry("300x200")

            frame = ttk.Frame(info_window, padding="20")
            frame.pack(expand=True, fill=tk.BOTH)

            name_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
            dev_font = tkfont.Font(family="Helvetica", size=12, slant="italic")
            loc_font = tkfont.Font(family="Helvetica", size=10)

            name_label = ttk.Label(frame, text=distro_name, font=name_font, anchor="center")
            name_label.pack(pady=(0, 5))

            dev_label = ttk.Label(frame, text=developers, font=dev_font, anchor="center")
            dev_label.pack(pady=(0, 5))

            loc_label = ttk.Label(frame, text=location, font=loc_font, anchor="center")
            loc_label.pack(pady=(0, 5))

            for label in (name_label, dev_label, loc_label):
                label.pack(expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = LinuxDistroApp(root)
    root.mainloop()