Mutation testing example with Cosmic Ray
========================================

Initially
[commit 4e786b8](https://github.com/atodorov/mutation-testing-example/commit/4e786b8afedb07a91bbc5c482e109bfe3a8957a7)
we think that our test is good but CR reports:

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


So a simple code mutation wasn't caught by the existing tests. So we go ahead and
add a second test in
[commit 14bec39](https://github.com/atodorov/mutation-testing-example/commit/14bec3935feaa76fb2061d23fc76157531856a30)
and re-run CR:

```
job ID 1:Outcome.KILLED:sandwich
command: cosmic-ray worker sandwich number_replacer 0 unittest -- tests/
Traceback (most recent call last):
  File "/home/atodorov/private/repos/github/mutation-testing-example/tests/test_burger.py", line 12, in test_default_burger_creation_and_check_default_values
    self.assertEqual(burger['ham'], 1)
AssertionError: 2 != 1

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
remained so we need to add a new test for it,
[commit 00e1f7e](https://github.com/atodorov/mutation-testing-example/commit/00e1f7e8fffd32b18bf173a1f89058b44ba1f92c).
After the second test is updated the results are:

```
job ID 1:Outcome.KILLED:sandwich
command: cosmic-ray worker sandwich number_replacer 0 unittest -- tests/
Traceback (most recent call last):
  File "/home/atodorov/private/repos/github/mutation-testing-example/tests/test_burger.py", line 12, in test_default_burger_creation_and_check_default_values
    self.assertEqual(burger['ham'], 1)
AssertionError: 2 != 1

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
Traceback (most recent call last):
  File "/home/atodorov/private/repos/github/mutation-testing-example/tests/test_burger.py", line 13, in test_default_burger_creation_and_check_default_values
    self.assertEqual(burger['eggs'], 0)
AssertionError: 1 != 0

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
