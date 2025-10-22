import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.30056, -0.34118).lineTo(0.29944, -0.34118).lineTo(0.29944, 0.22882).threePointArc((0.27601, 0.28539), (0.21944, 0.30882)).lineTo(-0.22056, 0.30882).threePointArc((-0.27713, 0.28539), (-0.30056, 0.22882)).lineTo(-0.30056, -0.34118).close()
solid=wp_sketch0.add(loop0).extrude(0.5273101905250842)
