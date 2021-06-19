# TsDownloader
Example usage

1. Play video in e.g. Google Chrome
2. Ctrl + Shift + I -> Network tab
3. Find an example of a repeating request to .ts file containing an incrementing id, copy this url
4. Replace id by '{}' (without quotes) and insert -u flag with this url

E.g.
```bash
python3 TsDownloader.py -u "https://tmg-nl-ams-p15-am3.cdn.streamgate.nl/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTg3MDc4NTksInVyaSI6Ilwvdm9kXC90bWdcL3MxXC9KSUpnZklFSzFNUUVcL2hsc1wvS3pwb2VkNUkzZWFHXC9LenBvZWQ1STNlYUdfdjE2MTUzMTI1MjcuaXNtIiwiY2xpZW50X2lwIjoiNzguMjEuMTAwLjE4NSIsInZpZXdlciI6InNhbS1yZWRpcmVjdC1zZXJ2aWNlIiwicmlkIjoiYWRiZWU4NiJ9.5fc3GaphmwTlMlgx5NuPRkTQj355MvHohCQ9nXWtGnc/vod/tmg/s1/JIJgfIEK1MQE/hls/Kzpoed5I3eaG/Kzpoed5I3eaG_v1615312527.ism/Kzpoed5I3eaG-1615312527-audio=128000-video=2200000-{}.ts?v=1615312527" -s {} -o "output.mp4"
```
