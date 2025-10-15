from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen, 'white', self.position, self.radius)
	def update(self, dt):
		self.position += self.velocity * dt
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		a_angle = self.velocity.rotate(random_angle)
		b_angle = self.velocity.rotate(-random_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		a_aster = Asteroid(self.position.x, self.position.y, new_radius)
		a_aster.velocity = a_angle * 1.2
		b_aster = Asteroid(self.position.x, self.position.y, new_radius)
		b_aster.velocity = b_angle * 1.2
