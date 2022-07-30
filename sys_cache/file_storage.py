from datetime import datetime
import os
import random
from django.core.files.storage import FileSystemStorage


class ImageFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        # 自定义图片名称

        old_name = name.split("/")[-1]

        suffix_name = old_name.split(".")[-1]

        prefix_name = f"IMG_{datetime.now().strftime('%Y%m%d%H%M%S')}{str(random.randint(10000, 99999))}"

        image_path = os.path.dirname(name)

        name = os.path.join(image_path, f"{prefix_name}.{suffix_name}")

        return super()._save(name, content)
