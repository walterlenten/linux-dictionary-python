import tkinter as tk
from tkinter import ttk

# Data for Linux distros and their developers
distros = [
    ("Ubuntu", "Canonical Ltd."),
    ("Debian", "Debian Project"),
    ("Fedora", "Fedora Project (sponsored by Red Hat)"),
    ("Arch Linux", "Judd Vinet, Aaron Griffin"),
    ("Manjaro", "Manjaro GmbH & Co. KG"),
    ("Gentoo", "Gentoo Foundation"),
    ("openSUSE", "openSUSE Project"),
    ("Slackware", "Patrick Volkerding"),
    ("CentOS", "Community, Red Hat"),
    ("Elementary OS", "Daniel Foré and the Elementary OS Team"),
    ("Linux Mint", "Clement Lefebvre"),
    ("Kali Linux", "Offensive Security"),
    ("Zorin OS", "Zorin Group"),
    ("Pop!_OS", "System76"),
    ("Red Hat Enterprise Linux (RHEL)", "Red Hat, Inc."),
    ("Mageia", "Mageia.Org"),
    ("PCLinuxOS", "Texstar"),
    ("ClearOS", "ClearFoundation"),
    ("Qubes OS", "Invisible Things Lab"),
    ("Tails", "The Tor Project"),
    ("Alpine Linux", "Natanael Copa"),
    ("Bodhi Linux", "Jeff Hoogland"),
    ("Solus", "Ikey Doherty"),
    ("NixOS", "NixOS Foundation"),
    ("Parrot OS", "Parrot Security"),
    ("Deepin", "Wuhan Deepin Technology Co., Ltd."),
    ("Lubuntu", "Lubuntu Team"),
    ("Xubuntu", "Xubuntu Team"),
    ("Kubuntu", "Kubuntu Team"),
    ("MX Linux", "MX Dev Team"),
    ("Void Linux", "The Void Linux Team"),
    ("Puppy Linux", "Barry Kauler"),
    ("Tiny Core Linux", "Robert Shingledecker"),
    ("SparkyLinux", "SparkyLinux Team"),
    ("Peppermint OS", "Peppermint OS Team"),
    ("Feren OS", "Feren OS Team"),
    ("KaOS", "KaOS Community"),
    ("ExTiX", "Arne Exton"),
    ("OpenMandriva", "OpenMandriva Association"),
    ("Sabayon", "Sabayon Team"),
    ("Trisquel", "Trisquel Project"),
    ("Devuan", "Devuan Developers"),
    ("PureOS", "Purism"),
    ("Slax", "Tomas Matejicek"),
    ("Salix OS", "Salix Team"),
    ("Bluestar Linux", "Bluestar Linux Team"),
    ("RebornOS", "RebornOS Team"),
    ("Artix Linux", "Artix Linux Team"),
    ("Lakka", "Lakka Team"),
    ("Knoppix", "Klaus Knopper"),
    ("Damn Small Linux", "John Andrews"),
    ("Freespire", "Freespire Team"),
    ("Linspire", "PC/OpenSystems LLC"),
    ("Garuda Linux", "Garuda Team"),
    ("Enso OS", "Enso OS Team"),
    ("Neptune OS", "Leszek Lesner"),
    ("GhostBSD", "GhostBSD Project"),
    ("FuryBSD", "FuryBSD Team"),
    ("Netrunner", "Netrunner Team"),
    ("Parabola GNU/Linux-libre", "Parabola Project"),
    ("Antergos", "Antergos Team"),
    ("Calculate Linux", "Alexander Tratsevskiy"),
    ("ChaletOS", "Dejan Petrovic"),
    ("BackBox", "BackBox Team"),
    ("Rescatux", "Adrian Raulete"),
    ("ALT Linux", "ALT Linux Team"),
    ("ROSA Linux", "ROSA Laboratory"),
    ("Pinguy OS", "Antoni Norman"),
    ("Nitrux", "Nitrux Latinoamericana S.C."),
    ("ArcoLinux", "Erik Dubois"),
    ("Namib GNU/Linux", "Namib Team"),
    ("Hyperbola GNU/Linux-libre", "Hyperbola Project"),
    ("Septor", "Septor Team"),
    ("Zenwalk", "Jean-Philippe Guillemin"),
    ("CRUX", "Per Liden"),
    ("Funtoo", "Daniel Robbins"),
    ("Korora", "Korora Project"),
    ("UberStudent", "Stephen Ewen"),
    ("GoboLinux", "GoboLinux Team"),
    ("BunsenLabs Linux", "BunsenLabs Team"),
    ("MakuluLinux", "Jacque Montague Raymer"),
    ("Nexenta OS", "Nexenta Systems, Inc."),
    ("NuTyX", "NuTyX Team"),
    ("Peppermint", "Peppermint OS LLC"),
    ("Remix OS", "Jide Technology"),
    ("Void", "Void Linux Team"),
    ("Robolinux", "John Martinson"),
    ("ALT", "BaseALT Ltd."),
    ("PureOS", "Purism"),
    ("Siduction", "Ferdinand Thommes"),
    ("Clear", "Intel Corporation"),
    ("SteamOS", "Valve Corporation"),
    ("Quirky", "Barry Kauler"),
    ("LFS", "Gerard Beekmans"),
    ("Porteus", "Porteus Team"),
    ("Enlightenment", "Enlightenment Foundation"),
    ("Source Mage", "Source Mage Team"),
    ("SUSE Linux Enterprise", "SUSE LLC"),
    ("SliTaz", "Christophe Lincoln"),
    ("RasPlex", "RasPlex Team")
]

# Function to show distro details in a new window
def show_distro_details(distro_name):
    for distro, developer in distros:
        if distro.lower() == distro_name.lower():
            details_window = tk.Toplevel(root)
            details_window.title(distro)
            
            name_label = tk.Label(details_window, text=distro, font=("Arial", 20, "bold"))
            name_label.pack(pady=10)
            
            developer_label = tk.Label(details_window, text=developer, font=("Arial", 12))
            developer_label.pack(pady=5)
            break

# Function to update suggestions based on input
def update_suggestions(event):
    input_text = entry.get().lower()
    suggestions = [distro for distro, _ in distros if input_text in distro.lower()]
    
    listbox.delete(0, tk.END)
    for suggestion in suggestions:
        listbox.insert(tk.END, suggestion)

# Function to handle Enter key press
def on_enter(event):
    selected_distro = listbox.get(tk.ACTIVE)
    show_distro_details(selected_distro)

# Create the main window
root = tk.Tk()
root.title("Linux Distros and Their Developers")

# Create the text entry for input
entry = tk.Entry(root, width=50)
entry.pack(pady=20)
entry.bind("<KeyRelease>", update_suggestions)
entry.bind("<Return>", on_enter)

# Create a listbox for suggestions
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Initial population of the listbox with all distros
for distro, _ in distros:
    listbox.insert(tk.END, distro)

# Run the application
root.mainloop()