"""Unit tests for the EmotionDetection package."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Validate the dominant emotion returned for representative statements."""

    def test_emotion_detector(self):
        """Confirm that all five expected dominant emotions are detected."""
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"],
            "joy"
        )
        self.assertEqual(
            emotion_detector("I am really mad about this")["dominant_emotion"],
            "anger"
        )
        self.assertEqual(
            emotion_detector(
                "I feel disgusted just hearing about this"
            )["dominant_emotion"],
            "disgust"
        )
        self.assertEqual(
            emotion_detector("I am so sad about this")["dominant_emotion"],
            "sadness"
        )
        self.assertEqual(
            emotion_detector(
                "I am really afraid that this will happen"
            )["dominant_emotion"],
            "fear"
        )


if __name__ == "__main__":
    unittest.main()
