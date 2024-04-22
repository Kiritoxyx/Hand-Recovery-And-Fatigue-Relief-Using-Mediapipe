import pygame

from ball import Ball


class Collision:
    @staticmethod
    def collide_with_element(ball, enemy_group,game):
        """
        检测ball与enemy组中任一enemy是否发生碰撞
        :param ball: Ball的实例
        :param enemy_group: Enemy的精灵组
        :return: 如果发生碰撞，返回True，否则返回False
        """
        collided_enemies = pygame.sprite.spritecollide(ball, enemy_group, False)
        for enemy in collided_enemies:
            if Ball.get_card_type(ball) == 'card_golden' and not enemy.collided and not enemy.enchanted:
                enemy.enchanted = True
                ball.clear_image()
                game.score += 10  # 增加分数
                if enemy.frozen:  # 如果enemy被冻结
                    enemy.frozen = False  # 解冻enemy
            elif Ball.get_card_type(ball) == 'card_fire':
                enemy.kill()  # 直接杀死enemy
                game.score += 10  # 增加分数
                ball.clear_image()
                if enemy.frozen:  # 如果enemy被冻结
                    enemy.frozen = False  # 解冻enemy
            elif Ball.get_card_type(ball) == 'card_ice' and not enemy.frozen:
                enemy.frozen = True
                ball.clear_image()
            elif Ball.get_card_type(ball) == 'card_ground' and ball.effected_by_card_ground and enemy.affected_by_card_ground:
                if ball.rect.x >= 1050:  # 检查enemy是否到达lane的最右边
                    # enemy.move_right = lambda: None  # 停止enemy的移动
                    ball.kill()  # 移除card_ground
                else:
                    enemy.move_right()
                ball.effected_by_card_ground = False
                enemy.affected_by_card_ground = False
            elif Ball.get_card_type(
                    ball) == 'card_ground' and ball.effected_by_card_ground == False and enemy.affected_by_card_ground == False:
                if ball.rect.x >= 1050:  # 检查enemy是否到达lane的最右边
                    # enemy.move_right = lambda: None  # 停止enemy的移动
                    ball.kill()  # 移除card_ground
                else:
                    enemy.move_right()
                # enemy.move_right()
        return False

    def enemy_turned(self, enemy_group):
        """
        处理被魅惑的enemy向右走的逻辑，并检测碰撞
        :param enemy_group: Enemy的精灵组
        """
        for enemy in enemy_group:
            if enemy.enchanted:
                enemy.enemy_move_right()
                collided_enemies = pygame.sprite.spritecollide(enemy, enemy_group, False)
                for target_enemy in collided_enemies:
                    if target_enemy != enemy:  # 确保不是与自己碰撞
                        enemy.remove_from_group()  # 移除发起碰撞的敌人
                        target_enemy.remove_from_group()  # 移除碰撞的目标敌人

    def game_state(self, enemy_handle):
        """
                判断游戏状态
                :param enemy_handle: Enemy的精灵组
                """
        # 检查是否所有敌人都被消灭了
        if len(enemy_handle.enemy_list) == 0:
            print("游戏胜利！")  # 测试用
            return 1
        # 检查是否过线
        for enemy in enemy_handle.enemy_list:
            if enemy.rect.x <= 300:  # 假设游戏区域的最左边的x坐标为400
                print("游戏失败！")  # 测试用
                # enemy_handle.clear_enemy()
                return 2
        return 0
