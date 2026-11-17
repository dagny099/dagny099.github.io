#!/usr/bin/env python3
"""Tests for add-moment and the moments checks in validate.py.

Runs on copies of the real _listens files in a temp folder; touches nothing in the repo
and makes no network calls.  Usage: python3 -m unittest scripts/listens/test_moments.py
"""
import contextlib
import io
import shutil
import sys
import tempfile
import types
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import add_listen  # noqa: E402
import validate  # noqa: E402

REAL = HERE.parents[1] / "_listens"


class MomentsCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copytree(REAL, self.tmp / "_listens")
        self._listens = add_listen.LISTENS
        add_listen.LISTENS = self.tmp / "_listens"
        # A real listen that has no moments yet, so the assertions below start from zero.
        self.slug = sorted(p.stem for p in REAL.glob("*.md") if "moments" not in add_listen.front_matter(p))[0]
        self.fm = add_listen.front_matter(REAL / f"{self.slug}.md")
        self.pub = str(self.fm["published_on"])

    def tearDown(self):
        add_listen.LISTENS = self._listens
        shutil.rmtree(self.tmp)

    def add(self, at="1:00", shot_on=None, chapter=None, write=True, listen=None):
        args = types.SimpleNamespace(listen=listen or self.slug, at=at, shot_on=shot_on or self.pub,
                                     chapter=chapter, write=write)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            add_listen.cmd_add_moment(args)
        return add_listen.front_matter(self.tmp / "_listens" / f"{self.slug}.md")

    def errors(self, fm):
        found = []
        validate.check_moments(found, "x.md", fm)
        return found

    def test_rewriting_front_matter_changes_nothing_else(self):
        for path in REAL.glob("*.md"):
            _, head, _ = path.read_text().split("---\n", 2)
            self.assertEqual(add_listen.dump(add_listen.yaml.safe_load(head)), head, path.name)

    def test_dry_run_writes_nothing(self):
        before = (self.tmp / "_listens" / f"{self.slug}.md").read_text()
        self.add(write=False)
        self.assertEqual((self.tmp / "_listens" / f"{self.slug}.md").read_text(), before)

    def test_adds_one_moment_and_keeps_the_rest_of_the_file(self):
        fm = self.add(at="1:00", chapter="A chapter")
        self.assertEqual(fm["moments"], [{"at": "1:00", "shot_on": self.pub, "chapter": "A chapter"}])
        self.assertEqual(list(fm)[-1], "provenance")
        self.assertEqual({k: v for k, v in fm.items() if k != "moments"}, self.fm)
        self.assertEqual(self.errors(fm), [])

    def test_same_moment_twice_is_one_moment(self):
        self.add(at="1:00")
        self.add(at="1:00")
        fm = self.add(at="1:40")          # 40 seconds later, same day: the same burst
        self.assertEqual(len(fm["moments"]), 1)

    def test_a_later_position_or_another_day_is_a_new_moment_kept_in_order(self):
        self.add(at="5:00")
        self.add(at="1:00")
        later_day = str(add_listen.datetime.date.fromisoformat(self.pub) + add_listen.datetime.timedelta(days=3))
        fm = self.add(at="1:00", shot_on=later_day)
        self.assertEqual([m["at"] for m in fm["moments"]], ["1:00", "1:00", "5:00"])
        self.assertEqual(self.errors(fm), [])

    def test_refuses_impossible_moments(self):
        with self.assertRaises(SystemExit):
            self.add(at="1:00", shot_on="1999-01-01")            # before the episode existed
        with self.assertRaises(SystemExit):
            self.add(at="9:59:59")                               # past the end
        with self.assertRaises(SystemExit):
            self.add(at="25m53s")                                # not a clock
        with self.assertRaises(SystemExit):
            self.add(listen="no-such-episode")
        self.assertNotIn("moments", add_listen.front_matter(self.tmp / "_listens" / f"{self.slug}.md"))

    def test_validator_keeps_passage_text_out_of_the_public_file(self):
        fm = dict(self.fm, moments=[{"at": "1:00", "shot_on": self.pub, "passage": "words from a transcript"}])
        self.assertTrue(any("public" in e for e in self.errors(fm)))

    def test_validator_catches_bad_and_repeated_moments(self):
        bad = dict(self.fm, moments=[{"at": "soon", "shot_on": self.pub}])
        twice = dict(self.fm, moments=[{"at": "1:00", "shot_on": self.pub}, {"at": "01:00", "shot_on": self.pub}])
        early = dict(self.fm, moments=[{"at": "1:00", "shot_on": "1999-01-01"}])
        for fm in (bad, twice, early, dict(self.fm, moments="1:00")):
            self.assertEqual(len(self.errors(fm)), 1, fm["moments"])

    def test_files_without_moments_still_pass(self):
        self.assertEqual(self.errors(self.fm), [])


if __name__ == "__main__":
    unittest.main()
