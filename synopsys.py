import urllib.request
import json

class Graph:
    def __init__(self):
        self.graph = set()
    
    def addToGraph(self, coord):
        if coord not in self.graph:
            self.graph.add(coord)
    
    def checkGraph(self, coord):
        if coord not in self.graph:
            return True
        else:
            return False
class Tile:
    def __init__(self, coord, graph):
        self.coord = coord
        self.graph = graph
        self.neighbours = []
        self.win = False
        
    def setNeighbours(self):
        url = "http://188.166.28.247/villheik%40student.oulu.fi/challenges/2/?pos=" + self.coord + "&look="

        req = urllib.request.Request(url+"north")
        response = urllib.request.urlopen(req)
        north = json.loads(response.read())
        if (north["tile_type"] != "lava" and self.graph.checkGraph(north["pos"])):
            print("North: " + str(north))
            self.graph.addToGraph(north["pos"])
            self.neighbours.append(north["pos"])
            
            
        req = urllib.request.Request(url+"south")
        response = urllib.request.urlopen(req)
        south = json.loads(response.read())
        if (south["tile_type"] != "lava" and self.graph.checkGraph(south["pos"])):
            print("South: " + str(south))
            self.graph.addToGraph(south["pos"])
            self.neighbours.append(south["pos"])
            
        req = urllib.request.Request(url+"east")
        response = urllib.request.urlopen(req)
        east = json.loads(response.read())
        if (east["tile_type"] != "lava" and self.graph.checkGraph(east["pos"])):
            print("East: " + str(east))
            self.graph.addToGraph(east["pos"])
            self.neighbours.append(east["pos"])
            
        req = urllib.request.Request(url+"west")
        response = urllib.request.urlopen(req)
        west = json.loads(response.read())
        if (west["tile_type"] != "lava" and self.graph.checkGraph(west["pos"])):
            print("West:" + str(west))
            self.graph.addToGraph(west["pos"])
            self.neighbours.append(west["pos"])
            
        return self.neighbours


if __name__ == "__main__":
    graph = Graph()
    graph.addToGraph("a82b")
    startTile = Tile("a82b", graph)
    neighbour = startTile.setNeighbours()
    while neighbour:
        tile = Tile(neighbour.pop(0), graph)
        newNeighbours = tile.setNeighbours()
        neighbour.extend(newNeighbours)




