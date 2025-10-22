import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.59588, 0.03175).lineTo(-0.57569, 0.03175).lineTo(-0.57569, -0.03175).lineTo(0.59588, -0.03175).lineTo(0.59588, 0.03175).close()
solid=wp_sketch0.add(loop0).extrude(-1.3712896838417643)
