import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.027, -0.0568).lineTo(-0.001, -0.0568).lineTo(-0.001, -0.0555).lineTo(-0.027, -0.0555).lineTo(-0.027, -0.0568).close()
solid=wp_sketch0.add(loop0).extrude(0.031058726411362068)
