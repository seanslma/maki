# other

C++ Core Guidelines\\
https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#es71-prefer-a-range-for-statement-to-a-for-statement-when-there-is-a-choice

C++ tips\\
https://abseil.io/tips/1

When add a new project, we need to set the Output Directory and the Intermediate Directory in Configuration Properties -> General

```cpp
// int to str
char strMonth[3];
sprintf_s(strMonth, "%02d", month);

// str to int dbl
int i = stoi(str);
double d = stod(str);

// str combination
std::stringstream ss;
ss.str("");
ss << folderin << strDay << "_" << strHour << "UT.txt";
string fileName = ss.str();

// progress report
std::cout << "Finished: " << i * 100 / (double)n << "%\r";
std::cout.flush();

// read file
ifstream inputfile(fileName);
if (!inputfile) {
  //File doesn't exist
  cout << "File '" << fileName + "' doesn't exist\n";
}
else {
  string line;
  while (getline(inputfile, line)) {
    stringstream lineStream(line);
    // Read a value one at a time from the line
    int val;
    while (lineStream >> val) {
        int x = val;
    }
}
inputfile.close();

// append to file
FILE *fp = fopen(fileName.c_str(), "ab");
stringstream ss;
ss.str("");
fwrite(ss.str().c_str(), 1, ss.str().length(), fp);
fclose(fp);

// get exe full path
char basePath[255] = "";
_fullpath(basePath, argv[0], sizeof(basePath));

string path_ = string(basePath);
int idx = path_.find_last_of("/\\");
cout << "exefolder: " << path_.substr(0, idx+1) << endl;
cout << "full path: " << basePath << endl;
```
