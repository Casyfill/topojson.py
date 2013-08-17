


class types:
	def Feature(self,feature):
		if feature.has_key('geometry'):
			self.geometry(feature['geometry'])
	def FeatureCollection(self,collection):
		for feature in collection['features']:
			self.Feature(feature)
	def GeometryCollection(self,collection):
		for geometry in collection['geometries']:
			self.geometry(geometry)
	def LineString(self,lineString):
		self.line(lineString['coordinates'])

	def MultiLineString(self,multiLineString):
		for coordinate in multiLineString['coordinates']:
			self.line(coordinate)
	def MultiPoint(self,multiPoint):
		for coordinate in multiPoint['coordinates']:
			self.point(coordinate);
	def MultiPolygon(self,multiPolygon):
		for coordinate in multiPolygon['coordinates']:
			self.polygon(coordinate);

	def Point(self,point):
		self.point(point['coordinates'])
	def Polygon(self,polygon):
		self.polygon(polygon['coordinates'])
	def object(self,object):
		if object == None:
			return None
		elif object['type']=='Feature' or object['type']=='FeatureCollection':
			return self[object.type](object)
		else:
			return self.geometry(object)
	def geometry(self,geometry):
		if(geometry != None and typeGeometries.has_key(geometry['type'])):
			return self.geometry['type'](geometry)
		else:
			return None
	def point(self):
		pass
	def line(self,coordinates):
		for coordinate in coordinates:
			self.point(coordinate)
	def polygon(self,coordinates):
		for coordinate in coordinates:
			self.line(coordinate)