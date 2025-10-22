import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.05949).lineTo(0.173, 0.05949).lineTo(0.225, 0.00749).lineTo(0.225, -0.02251).lineTo(0.0, -0.02251).lineTo(0.0, 0.0).lineTo(0.0, 0.05949).close()
solid=wp_sketch0.add(loop0).extrude(-0.5155287168713176)
