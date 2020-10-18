# git-owners

A simple utility to pretty print the list of files in a git repo and their owners.<br />
https://pypi.org/project/git-owners/

[![PyPI version](https://badge.fury.io/py/git-owners@2x.png)](https://badge.fury.io/py/git-owners)

## Installation

`python3 -m pip install git-owners` 

## Usage

<pre>
usage: git-owners [-h] 
    [-p PATH] 
    [-d DEPTH] 
    [-f {file,dir,mixed}] 
    [--as-list] [-s SINCE] 
    [--include-extensions INCLUDE_EXTENSIONS] 
    [--exclude-extensions EXCLUDE_EXTENSIONS] 
    [-o OUTPUT] 
    [--verbose] 
    repo

Print author owners statistics for a given git repo

positional arguments:
  repo                  Repository root

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Directory to process (Relative to repository root)
  -d DEPTH, --depth DEPTH
                        Maximum level of directory leaves to print out in the final tree (-1 to print all leaves)
  -f {file,dir,mixed}, --filter {file,dir,mixed}
                        Filter the output based on the value given. file: output files only (--as-list will be used in this case), dir: output directories only, mixed: output files and directories (default).
  --as-list             Print results as a list instead of a tree. If --filter is not specified, mixed will be used.
  -s SINCE, --since SINCE
                        Specifies the date range limit to use when executing git blame. date format is the same as used for git blame --since
  --include-extensions INCLUDE_EXTENSIONS
                        Comma separated extensions (ie. .py, .kt, .java). Specifies which file extensions to include while parsing the repository
  --exclude-extensions EXCLUDE_EXTENSIONS
                        Like for --include-extensions, but this will exclude the specified extensions. If specified, --include-extensions will be ignored
  -o OUTPUT, --output OUTPUT
                        Save Report to file instead of printing to stdout
  --verbose             Turn on logging
 </pre>
 
## Example

### Tree output

Consider the following input command:
 
`git-owners --include-extensions=.gradle,.java,.kt,.xml --output ~/Desktop/test-report.txt ~/Documents/git/sephiroth74/AndroidUIGestureRecognizer` 
 
Will generate the file `test-report.txt` with this content:
 
 <pre>
 Final Report for `~/Documents/git/sephiroth74/AndroidUIGestureRecognizer`
 
 Command line: `/usr/local/bin/git-owners --include-extensions=.gradle,.java,.kt --path uigesturerecognizer/src --output ~/Desktop/test-report.txt ~/Documents/git/sephiroth74/AndroidUIGestureRecognizer`
 
 
 Directory Structure Statistics:
 Directory/File                                                               Percent    Owner                            Lines    Total Lines    
 ---------------------------------------------------------------------------  ---------  -------------------------------  -------  -------------  
 src                                                                          93.9%      alessandro.crugnola@gmail.com    6410     6829           
 ├── androidTest                                                              100.0%     alessandro.crugnola@gmail.com    2753     2753           
 │   └── java                                                                 100.0%     alessandro.crugnola@gmail.com    2753     2753           
 │       └── it                                                               100.0%     alessandro.crugnola@gmail.com    2753     2753           
 │           └── sephiroth                                                    100.0%     alessandro.crugnola@gmail.com    2753     2753           
 │               └── android                                                  100.0%     alessandro.crugnola@gmail.com    2753     2753           
 │                   └── library                                              100.0%     alessandro.crugnola@gmail.com    2753     2753           
 │                       └── uigestures                                       100.0%     alessandro.crugnola@gmail.com    2753     2753           
 │                           ├── Interaction.kt                               100.0%     alessandro.crugnola@gmail.com    450      450            
 │                           ├── TestActivity.kt                              100.0%     alessandro.crugnola@gmail.com    78       78             
 │                           ├── TestBaseClass.kt                             100.0%     alessandro.crugnola@gmail.com    88       88             
 │                           ├── TestLongPressGesture.kt                      100.0%     alessandro.crugnola@gmail.com    430      430            
 │                           ├── TestPanGesture.kt                            100.0%     alessandro.crugnola@gmail.com    330      330            
 │                           ├── TestPinchGesture.kt                          100.0%     alessandro.crugnola@gmail.com    130      130            
 │                           ├── TestRotateGesture.kt                         100.0%     alessandro.crugnola@gmail.com    61       61             
 │                           ├── TestScreenEdgeGesture.kt                     100.0%     alessandro.crugnola@gmail.com    233      233            
 │                           ├── TestSwipeGesture.kt                          100.0%     alessandro.crugnola@gmail.com    223      223            
 │                           └── TestTapGesture.kt                            100.0%     alessandro.crugnola@gmail.com    730      730            
 ├── main                                                                     89.0%      alessandro.crugnola@gmail.com    3400     3819           
 │   └── java                                                                 89.0%      alessandro.crugnola@gmail.com    3400     3819           
 │       └── it                                                               89.0%      alessandro.crugnola@gmail.com    3400     3819           
 │           └── sephiroth                                                    89.0%      alessandro.crugnola@gmail.com    3400     3819           
 │               └── android                                                  89.0%      alessandro.crugnola@gmail.com    3400     3819           
 │                   └── library                                              89.0%      alessandro.crugnola@gmail.com    3400     3819           
 │                       └── uigestures                                       89.0%      alessandro.crugnola@gmail.com    3400     3819           
 │                           ├── Geometry.kt                                  100.0%     alessandro.crugnola@gmail.com    21       21             
 │                           ├── OnGestureRecognizerStateChangeListener.kt    100.0%     alessandro.crugnola@gmail.com    8        8              
 │                           ├── ScaleGestureDetector.kt                      63.1%      alessandro.crugnola@gmail.com    345      547            
 │                           ├── UIContinuousRecognizer.kt                    94.7%      alessandro.crugnola@gmail.com    18       19             
 │                           ├── UIDiscreteGestureRecognizer.kt               94.1%      alessandro.crugnola@gmail.com    16       17             
 │                           ├── UIGestureRecognizer.kt                       91.5%      alessandro.crugnola@gmail.com    346      378            
 │                           ├── UIGestureRecognizerDelegate.kt               71.9%      alessandro.crugnola@gmail.com    97       135            
 │                           ├── UILongPressGestureRecognizer.kt              97.1%      alessandro.crugnola@gmail.com    437      450            
 │                           ├── UIPanGestureRecognizer.kt                    89.8%      alessandro.crugnola@gmail.com    360      401            
 │                           ├── UIPinchGestureRecognizer.kt                  92.1%      alessandro.crugnola@gmail.com    234      254            
 │                           ├── UIRectEdge.kt                                100.0%     alessandro.crugnola@gmail.com    5        5              
 │                           ├── UIRotateGestureRecognizer.kt                 93.7%      alessandro.crugnola@gmail.com    328      350            
 │                           ├── UIScreenEdgePanGestureRecognizer.kt          93.3%      alessandro.crugnola@gmail.com    393      421            
 │                           ├── UISwipeGestureRecognizer.kt                  97.6%      alessandro.crugnola@gmail.com    439      450            
 │                           ├── UITapGestureRecognizer.kt                    97.2%      alessandro.crugnola@gmail.com    342      352            
 │                           └── View.kt                                      100.0%     alessandro.crugnola@gmail.com    11       11             
 └── test                                                                     100.0%     alessandro.crugnola@gmail.com    257      257            
     └── java                                                                 100.0%     alessandro.crugnola@gmail.com    257      257            
         └── it                                                               100.0%     alessandro.crugnola@gmail.com    257      257            
             └── sephiroth                                                    100.0%     alessandro.crugnola@gmail.com    257      257            
                 └── android                                                  100.0%     alessandro.crugnola@gmail.com    257      257            
                     └── library                                              100.0%     alessandro.crugnola@gmail.com    257      257            
                         └── uigestures                                       100.0%     alessandro.crugnola@gmail.com    257      257            
                             ├── TestBase.kt                                  100.0%     alessandro.crugnola@gmail.com    35       35             
                             ├── TestGeometry.kt                              100.0%     alessandro.crugnola@gmail.com    69       69             
                             ├── TestUIGestureRecognizerDelegate.kt           100.0%     alessandro.crugnola@gmail.com    81       81             
                             └── TestUITapGestureRecognizer.kt                100.0%     alessandro.crugnola@gmail.com    72       72             
 
 
 Accumulated Statistics:
 Percent    Author                           Lines    Total Lines
 ---------  -----------------------------  -------  -------------
 93.9%      alessandro.crugnola@gmail.com     6410           6829
 6.1%       crugnola@adobe.com                 419           6829
 
</pre>

### List output

Report can be printed as simple list

`git-owners --include-extensions=.gradle,.java,.kt --filter=file --output ~/Desktop/test-report.txt ~/Documents/git/sephiroth74/AndroidUIGestureRecognizer

<pre>
Final Report for `~/Documents/git/sephiroth74/AndroidUIGestureRecognizer`

Command line: `/usr/local/bin/git-owners --include-extensions=.gradle,.java,.kt --filter=file --output /Users/alessandro/Desktop/test-report.txt ~/Documents/git/sephiroth74/AndroidUIGestureRecognizer`


Directory Structure Statistics:
Directory/File                                                                                                          Perc      Owner                            Lines    Total Lines    
----------------------------------------------------------------------------------------------------------------------  --------  -------------------------------  -------  -------------  
app/build.gradle                                                                                                        50.9%     alessandro.crugnola@gmail.com    29       57             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/BaseTest.java                                            77.3%     crugnola@adobe.com               75       97             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/MainActivity.kt                                          100.0%    alessandro.crugnola@gmail.com    146      146            
app/src/main/java/it/sephiroth/android/library/uigestures/demo/MainApplication.java                                     86.7%     alessandro.crugnola@gmail.com    13       15             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/MotionView.kt                                            100.0%    alessandro.crugnola@gmail.com    183      183            
app/src/main/java/it/sephiroth/android/library/uigestures/demo/fragments/IRecognizerFragment.kt                         100.0%    alessandro.crugnola@gmail.com    23       23             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/fragments/UILongPressGestureRecognizerFragment.kt        100.0%    alessandro.crugnola@gmail.com    60       60             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/fragments/UIPanGestureRecognizerFragment.kt              100.0%    alessandro.crugnola@gmail.com    55       55             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/fragments/UIPinchGestureRecognizerFragment.kt            100.0%    alessandro.crugnola@gmail.com    41       41             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/fragments/UIRotateGestureRecognizerFragment.kt           100.0%    alessandro.crugnola@gmail.com    54       54             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/fragments/UIScreenEdgePanGestureRecognizerFragment.kt    100.0%    alessandro.crugnola@gmail.com    64       64             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/fragments/UISwipeGestureRecognizerFragment.kt            100.0%    alessandro.crugnola@gmail.com    68       68             
app/src/main/java/it/sephiroth/android/library/uigestures/demo/fragments/UITapGestureRecognizerFragment.kt              100.0%    alessandro.crugnola@gmail.com    51       51             
build.gradle                                                                                                            59.0%     crugnola@adobe.com               23       39             
settings.gradle                                                                                                         100.0%    alessandro.crugnola@gmail.com    2        2              
uigesturerecognizer/build.gradle                                                                                        75.7%     alessandro.crugnola@gmail.com    178      235            
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/Interaction.kt                         100.0%    alessandro.crugnola@gmail.com    450      450            
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/TestActivity.kt                        100.0%    alessandro.crugnola@gmail.com    78       78             
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/TestBaseClass.kt                       100.0%    alessandro.crugnola@gmail.com    88       88             
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/TestLongPressGesture.kt                100.0%    alessandro.crugnola@gmail.com    430      430            
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/TestPanGesture.kt                      100.0%    alessandro.crugnola@gmail.com    330      330            
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/TestPinchGesture.kt                    100.0%    alessandro.crugnola@gmail.com    130      130            
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/TestRotateGesture.kt                   100.0%    alessandro.crugnola@gmail.com    61       61             
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/TestScreenEdgeGesture.kt               100.0%    alessandro.crugnola@gmail.com    233      233            
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/TestSwipeGesture.kt                    100.0%    alessandro.crugnola@gmail.com    223      223            
uigesturerecognizer/src/androidTest/java/it/sephiroth/android/library/uigestures/TestTapGesture.kt                      100.0%    alessandro.crugnola@gmail.com    730      730            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/Geometry.kt                                   100.0%    alessandro.crugnola@gmail.com    21       21             
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/OnGestureRecognizerStateChangeListener.kt     100.0%    alessandro.crugnola@gmail.com    8        8              
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/ScaleGestureDetector.kt                       63.1%     alessandro.crugnola@gmail.com    345      547            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UIContinuousRecognizer.kt                     94.7%     alessandro.crugnola@gmail.com    18       19             
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UIDiscreteGestureRecognizer.kt                94.1%     alessandro.crugnola@gmail.com    16       17             
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UIGestureRecognizer.kt                        91.5%     alessandro.crugnola@gmail.com    346      378            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UIGestureRecognizerDelegate.kt                71.9%     alessandro.crugnola@gmail.com    97       135            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UILongPressGestureRecognizer.kt               97.1%     alessandro.crugnola@gmail.com    437      450            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UIPanGestureRecognizer.kt                     89.8%     alessandro.crugnola@gmail.com    360      401            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UIPinchGestureRecognizer.kt                   92.1%     alessandro.crugnola@gmail.com    234      254            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UIRectEdge.kt                                 100.0%    alessandro.crugnola@gmail.com    5        5              
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UIRotateGestureRecognizer.kt                  93.7%     alessandro.crugnola@gmail.com    328      350            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UIScreenEdgePanGestureRecognizer.kt           93.3%     alessandro.crugnola@gmail.com    393      421            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UISwipeGestureRecognizer.kt                   97.6%     alessandro.crugnola@gmail.com    439      450            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/UITapGestureRecognizer.kt                     97.2%     alessandro.crugnola@gmail.com    342      352            
uigesturerecognizer/src/main/java/it/sephiroth/android/library/uigestures/View.kt                                       100.0%    alessandro.crugnola@gmail.com    11       11             
uigesturerecognizer/src/test/java/it/sephiroth/android/library/uigestures/TestBase.kt                                   100.0%    alessandro.crugnola@gmail.com    35       35             
uigesturerecognizer/src/test/java/it/sephiroth/android/library/uigestures/TestGeometry.kt                               100.0%    alessandro.crugnola@gmail.com    69       69             
uigesturerecognizer/src/test/java/it/sephiroth/android/library/uigestures/TestUIGestureRecognizerDelegate.kt            100.0%    alessandro.crugnola@gmail.com    81       81             
uigesturerecognizer/src/test/java/it/sephiroth/android/library/uigestures/TestUITapGestureRecognizer.kt                 100.0%    alessandro.crugnola@gmail.com    72       72             


Accumulated Statistics:
Percent    Author                           Lines    Total Lines
---------  -----------------------------  -------  -------------
92.5%      alessandro.crugnola@gmail.com     7414           8019
7.5%       crugnola@adobe.com                 604           8019
0.0%       not.committed.yet                    1           8019
</pre>


## License

See the [MIT License](LICENSE)