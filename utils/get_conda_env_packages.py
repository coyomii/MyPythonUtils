import subprocess

import pandas as pd


# 获取所有conda环境的名称
def get_conda_envs():
    result = subprocess.run(['conda', 'env', 'list'], stdout=subprocess.PIPE, text=True)
    envs = [line.split()[0] for line in result.stdout.split('\n') if line and not line.startswith('#') and 'envs' in line]
    envs.append('base')
    return envs

# 获取指定环境中的包
def get_packages(env):
    result = subprocess.run(['conda', 'list', '-n', env], stdout=subprocess.PIPE, text=True)
    packages = []
    for line in result.stdout.split('\n')[3:]:  # 跳过头几行
        if line:
            parts = line.split()
            if len(parts) >= 4:
                packages.append((parts[0], parts[1], parts[2], parts[3], env))
    return packages

# 获取所有环境的包信息
all_packages = []
envs = get_conda_envs()
for env in envs:
    all_packages.extend(get_packages(env))

# 转换为DataFrame并保存为CSV
df = pd.DataFrame(all_packages, columns=['Package', 'Version', 'Build', 'Channel', 'Environment'])
df.to_csv('conda_packages.csv', index=False)
print("Packages list saved to conda_packages.csv")