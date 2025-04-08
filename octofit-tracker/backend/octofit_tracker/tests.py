from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="test@example.com", password="password123")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")

class TeamModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        self.team = Team.objects.create(name="Test Team")
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")
        self.assertIn(self.user, self.team.members.all())

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration=30, date="2025-04-08")

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name="Morning Run", description="A quick morning run", duration=30)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Morning Run")
        self.assertEqual(self.workout.duration, 30)