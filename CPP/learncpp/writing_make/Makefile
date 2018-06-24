# Makefile example

# Variables:
CXX := g++
CXXFLAGS := -Wall -g
H := ./headers/
O := ./objects/
C := ./programs/
#

# Targets:

run: $(O)main.o $(O)add.o
	$(CXX) $(CXXFLAGS) -o run $(O)main.o $(O)add.o

$(O)main.o: $(C)main.cpp $(H)add.h
	$(CXX) $(CXXFLAGS) -c main.cpp -o $(O)main.o

$(O)add.o: $(C)add.cpp $(H)add.h
	$(CXX) $(CXXFLAGS) -c add.cpp -o $(O)add.o
# 
