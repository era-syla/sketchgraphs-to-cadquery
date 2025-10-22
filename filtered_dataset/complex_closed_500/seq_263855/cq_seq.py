import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0237, -0.1496).lineTo(0.01178, -0.1496).lineTo(0.01178, -0.177).lineTo(0.0237, -0.177).lineTo(0.0237, -0.1496).close()
solid=wp_sketch0.add(loop0).extrude(0.016623057098980553)
