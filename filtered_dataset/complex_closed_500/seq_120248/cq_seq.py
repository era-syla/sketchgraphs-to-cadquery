import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.001, -0.004).lineTo(-0.001, -0.004).lineTo(-0.001, -0.002).lineTo(0.001, -0.002).lineTo(0.001, -0.004).close()
solid=wp_sketch0.add(loop0).extrude(-0.005709612370339823)
