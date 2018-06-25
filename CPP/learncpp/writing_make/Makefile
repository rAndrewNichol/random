# Makefile example

# Variables:
CXX := g++
CXXFLAGS := -Wall -g
IFLAG := -I ./headers/
H := ./headers/
O := ./objects/
P := ./programs/
#

# Targets:

run: $(O)main.o $(O)add.o
	$(CXX) $(CXXFLAGS) -o run $(O)main.o $(O)add.o

$(O)main.o: $(P)main.cpp $(H)add.h
	$(CXX) $(CXXFLAGS) $(IFLAG) -c $(P)main.cpp -o $(O)main.o 

$(O)add.o: $(P)add.cpp 
	$(CXX) $(CXXFLAGS) $(IFLAG) -c $(P)add.cpp -o $(O)add.o
# 
