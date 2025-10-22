import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.33588, 0.0).lineTo(0.34748, 0.0).lineTo(-0.33588, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(1.1159888373008584)
