@echo off
echo "Listing all sessions (including remote):"
wmic /NODE:"localhost" COMPUTERSYSTEM GET UserName