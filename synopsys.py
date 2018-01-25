import urllib2
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
        self.setNeighbours()


    def setNeighbours(self):
        url = "http://188.166.28.247/villheik%40student.oulu.fi/challenges/2/?pos=" + self.coord + "&look="
        print url
        north = json.loads(urllib2.urlopen(url+"north").read())
        if (north["tile_type"] != "lava" and self.graph.checkGraph(north["tile_type"])):
            print "north: " + ''.join(self.neighbours)
            self.graph.addToGraph(north["tile_type"])
            self.neighbours.extend(Tile(north["pos"], self.graph))
            print "north: " + ''.join(self.neighbours)
            
            
        south = json.loads(urllib2.urlopen(url+"south").read())
        if (south["tile_type"] != "lava" and self.graph.checkGraph(south["tile_type"])):
            print "south: " + ''.join(self.neighbours)
            self.graph.addToGraph(south["tile_type"])
            self.neighbours.extend(Tile(south["pos"], self.graph))
            
            print south["tile_type"]

        east = json.loads(urllib2.urlopen(url+"east").read())
        if (east["tile_type"] != "lava" and self.graph.checkGraph(east["tile_type"])):
            print "east: " + ''.join(self.neighbours)
            self.graph.addToGraph(east["tile_type"])
            self.neighbours.extend(Tile(east["pos"], self.graph))
            
            print east["tile_type"]

        west = json.loads(urllib2.urlopen(url+"west").read())
        if (west["tile_type"] != "lava" and self.graph.checkGraph(west["tile_type"])):
            print "west: " + ''.join(self.neighbours)
            self.graph.addToGraph(west["tile_type"])
            self.neighbours.extend(Tile(west["pos"], self.graph))
            
            print west["tile_type"]

class SynopsysCrawler:
    def __init__(self, startTile):
       self.queue = [startTile]
       self.visited = set()
        
    def BFS(self):
        while self.queue:
            vertex = self.queue.pop(0)
            if vertex not in self.visited:
                self.visited.add(vertex)
                for neighbour in vertex.neighbours:
                    self.queue.extend(neighbour)
        return visited

if __name__ == "__main__":
    graph = Graph()
    graph.addToGraph("a82b")
    startTile = Tile("a82b", graph)
    crawler = SynopsysCrawler(startTile)




