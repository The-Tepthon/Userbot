@zedub.on(events.NewMessage(pattern='.تحميل (.*)'))
async def download_video(event):
    # تحقق مما إذا كان المرسل هو الحساب المنصب فقط
    if event.sender_id != Config.OWNER_ID:  # استبدل Config.OWNER_ID بمعرف صاحب الحساب
        return

    video_url = event.pattern_match.group(1)
    await event.reply(f"࿊ مرحبًــا بـك عزيزي المنصـب، جاري التحميـل من: {video_url}...")

    # إعداد خيارات yt-dlp
    ydl_opts = {
        "format": "best",
        "outtmpl": "%(title)s.%(ext)s",
        "cookiefile": get_cookies_file(),
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video_url, download=True)

            # تحقق من وجود 'title' في المعلومات المستخرجة
            if 'title' not in info or 'ext' not in info:
                await event.reply("❌ لم أتمكن من استخراج معلومات الفيديو.")
                return

            title = info['title']
            filename = f"{title}.{info['ext']}"

            await event.reply(f"࿊ تم تحميـل الفيديو: {title}\n⇜ انتظـر المعالجة جارية...")

            # إرسال الملف إلى تيليجرام
            await zedub.send_file(event.chat_id, filename)

            # حذف الملف بعد الإرسال
            os.remove(filename)
        except Exception as e:
            await event.reply(f"خطـــأ ❌: {e}")
