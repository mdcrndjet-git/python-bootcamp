speed = float(input("Download Speed (Mbps): "))
file_size = int(input("File Size (MB): "))

# MegaBytes per second (MBps) = Megabits per second (Mbps) / 8
download_speed_MBps = speed / 8

# Download Time (seconds) = File Size (MB) / MegaBytes per second (MBps)
download_time_seconds = file_size / download_speed_MBps

# Download Time (minutes) = Download Time (Seconds) / 60
download_time_minutes = download_time_seconds / 60

print(download_time_minutes)
