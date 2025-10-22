import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0005, -0.03225).lineTo(-0.0005, -0.03225).lineTo(-0.0005, -0.01225).lineTo(0.0005, -0.01225).lineTo(0.0005, -0.03225).close()
solid=wp_sketch0.add(loop0).extrude(0.005555610885037492)
