Mutation testing example with Cosmic Ray
========================================

Initially we think that our test is good but CR reports:

```
$ PYTHONPATH=. cosmic-ray run --baseline=10 burger.json sandwich -- tests/
$ cosmic-ray report burger.json 
job ID 1:Outcome.SURVIVED:sandwich
command: cosmic-ray worker sandwich number_replacer 0 unittest -- tests/
--- mutation diff ---
--- a/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
+++ b/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
@@ -7,6 +7,6 @@
 
 class Burger(FastFood):
 
-    def make_sandwich(self, ham=1, eggs=None, mayo=True):
+    def make_sandwich(self, ham=2, eggs=None, mayo=True):
         return {'type': 'burger', 'ham': ham, 'eggs': (eggs or 0), 'mayo': mayo}
 

job ID 2:Outcome.SURVIVED:sandwich
command: cosmic-ray worker sandwich number_replacer 1 unittest -- tests/
--- mutation diff ---
--- a/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
+++ b/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
@@ -8,5 +8,5 @@
 class Burger(FastFood):
 
     def make_sandwich(self, ham=1, eggs=None, mayo=True):
-        return {'type': 'burger', 'ham': ham, 'eggs': (eggs or 0), 'mayo': mayo}
+        return {'type': 'burger', 'ham': ham, 'eggs': (eggs or 1), 'mayo': mayo}
 

total jobs: 2
complete: 2 (100.00%)
survival rate: 100.00%
```


So a simple code mutation wasn't caought by the existing tests. So we go ahead and
add a second test and re-run CR:

```
$ cosmic-ray report burger.json 
job ID 1:Outcome.KILLED:sandwich
command: cosmic-ray worker sandwich number_replacer 0 unittest -- tests/
['test_default_burger_creation_and_check_default_values (test_burger.TestBurger)', 'Traceback (most recent call last):\n  File "/home/atodorov/private/repos/github/mutation-testing-example/tests/test_burger.py", line 12, in test_default_burger_creation_and_check_default_values\n    self.assertEqual(burger[\'ham\'], 1)\nAssertionError: 2 != 1\n']
--- mutation diff ---
--- a/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
+++ b/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
@@ -7,6 +7,6 @@
 
 class Burger(FastFood):
 
-    def make_sandwich(self, ham=1, eggs=None, mayo=True):
+    def make_sandwich(self, ham=2, eggs=None, mayo=True):
         return {'type': 'burger', 'ham': ham, 'eggs': (eggs or 0), 'mayo': mayo}
 

job ID 2:Outcome.SURVIVED:sandwich
command: cosmic-ray worker sandwich number_replacer 1 unittest -- tests/
--- mutation diff ---
--- a/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
+++ b/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
@@ -8,5 +8,5 @@
 class Burger(FastFood):
 
     def make_sandwich(self, ham=1, eggs=None, mayo=True):
-        return {'type': 'burger', 'ham': ham, 'eggs': (eggs or 0), 'mayo': mayo}
+        return {'type': 'burger', 'ham': ham, 'eggs': (eggs or 1), 'mayo': mayo}
 

total jobs: 2
complete: 2 (100.00%)
survival rate: 50.00%
```

We see that the first mutation was killed by the new test. However the second one
remained so we need to add a new test for it. After the second test is updated the
results are:

```
$ cosmic-ray report burger.json 
job ID 1:Outcome.KILLED:sandwich
command: cosmic-ray worker sandwich number_replacer 0 unittest -- tests/
['test_default_burger_creation_and_check_default_values (test_burger.TestBurger)', 'Traceback (most recent call last):\n  File "/home/atodorov/private/repos/github/mutation-testing-example/tests/test_burger.py", line 12, in test_default_burger_creation_and_check_default_values\n    self.assertEqual(burger[\'ham\'], 1)\nAssertionError: 2 != 1\n']
--- mutation diff ---
--- a/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
+++ b/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
@@ -7,6 +7,6 @@
 
 class Burger(FastFood):
 
-    def make_sandwich(self, ham=1, eggs=None, mayo=True):
+    def make_sandwich(self, ham=2, eggs=None, mayo=True):
         return {'type': 'burger', 'ham': ham, 'eggs': (eggs or 0), 'mayo': mayo}
 

job ID 2:Outcome.KILLED:sandwich
command: cosmic-ray worker sandwich number_replacer 1 unittest -- tests/
['test_default_burger_creation_and_check_default_values (test_burger.TestBurger)', 'Traceback (most recent call last):\n  File "/home/atodorov/private/repos/github/mutation-testing-example/tests/test_burger.py", line 13, in test_default_burger_creation_and_check_default_values\n    self.assertEqual(burger[\'eggs\'], 0)\nAssertionError: 1 != 0\n']
--- mutation diff ---
--- a/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
+++ b/home/atodorov/private/repos/github/mutation-testing-example/sandwich/__init__.py
@@ -8,5 +8,5 @@
 class Burger(FastFood):
 
     def make_sandwich(self, ham=1, eggs=None, mayo=True):
-        return {'type': 'burger', 'ham': ham, 'eggs': (eggs or 0), 'mayo': mayo}
+        return {'type': 'burger', 'ham': ham, 'eggs': (eggs or 1), 'mayo': mayo}
 

total jobs: 2
complete: 2 (100.00%)
survival rate: 0.00%
```



