import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.13118, -0.08446).lineTo(-0.11882, -0.08446).lineTo(-0.11882, -0.09521).lineTo(0.13118, -0.09521).lineTo(0.13118, -0.08446).close()
solid=wp_sketch0.add(loop0).extrude(0.7023574407956863)
