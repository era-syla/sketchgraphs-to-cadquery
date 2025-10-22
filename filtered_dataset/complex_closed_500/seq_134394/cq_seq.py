import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.07523, 0.079).lineTo(0.08123, 0.07).lineTo(0.08123, 0.079).lineTo(0.07523, 0.079).close()
solid=wp_sketch0.add(loop0).extrude(0.0020142840613447057)
