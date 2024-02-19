import re
import subprocess


def update_packages():
    # 运行 pip freeze 命令并获取输出
    output = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    # 输出从 bytes 转为 string
    package_names = output.stdout.decode("utf-8")
    # 使用正则表达式删除版本号
    names_without_version = re.sub(r"==\d+.\d+(.\d+)?", "", package_names).splitlines()
    # 更新包
    for name in names_without_version:
        subprocess.run(["pip", "install", name, "--upgrade"])


if __name__ == "__main__":
    update_packages()

