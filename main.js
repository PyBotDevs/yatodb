function rd(target) {
    // Redirects the user to a subpage, or another page.
    if (target == "invite") {window.location = "https://discord.com/api/oauth2/authorize?client_id=1103327777467420723&permissions=274877908992&scope=bot%20applications.commands";}
    else if (target == "git") {window.location = "https://github.com/PyBotDevs/YAToDB";}
    else if (target == "commands") {window.location = "";}
    else if (target == "changelog") {window.location = "https://github.com/PyBotDevs/YAToDB/releases/latest";}
    else if (target == "server") {window.location = "https://discord.gg/b5pz8T6Yjr";}
    else {console.error("Page target does not exist.");}
}
