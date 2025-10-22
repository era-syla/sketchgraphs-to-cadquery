import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.48801, 0.18288).lineTo(-0.48801, 0.18288).lineTo(-0.48801, -0.18288).lineTo(0.48801, -0.18288).lineTo(0.48801, 0.18288).close()
solid=wp_sketch0.add(loop0).extrude(0.9481098280738016)
