# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/23 22:37

import wandb
import random

wandb.login(key='754a44c84ce131b6c2f664c9e7f626393b4b03d3')

# start a new wandb run to track this script
wandb.init(
    # set the wandb project where this run will be logged
    project="my-awesome-project",

    # track hyperparameters and run metadata
    config={
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    }
)

# simulate training
epochs = 10
offset = random.random() / 5
for epoch in range(2, epochs):
    acc = 1 - 2 ** -epoch - random.random() / epoch - offset
    loss = 2 ** -epoch + random.random() / epoch + offset

    # log metrics to wandb 将度量记录到wandb
    wandb.log({"acc": acc, "loss": loss})

# [optional] finish the wandb run, necessary in notebooks
# [可选]完成wandb，这在笔记本电脑中是必要的
wandb.finish()
