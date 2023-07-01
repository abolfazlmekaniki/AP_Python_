CXX = g++
CXXFLAGS = -std=c++20 -Wall -c
LXXFLAGS = -std=c++20
OBJECTS = main.o CGaussSolver.o
TARGET = main


$(TARGET): $(OBJECTS)
	$(CXX) $(LXXFLAGS) $(OBJECTS) -o $(TARGET) -lgtest -lgtest_main -pthread
main.o: main.cpp 
	$(CXX) $(CXXFLAGS) main.cpp
CGaussSolver.o:CGaussSolver.cpp 
	$(CXX) $(CXXFLAGS) CGaussSolver.cpp
clean:
	rm -f $(TARGET) $(OBJECTS)